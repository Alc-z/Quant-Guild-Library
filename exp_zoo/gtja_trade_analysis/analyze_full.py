#!/usr/bin/env python3
"""
GTJA 2020-2026 对账单完整分析
================================
复现课程 "Analyzing Trading Strategy Performance Over Time"

步骤:
  1. 加载数据, 过滤交易类型 (A股 + ETF/LOF + 港股通)
  2. FIFO 买卖匹配, 计算每轮完整交易 P&L（含佣金税费）
  3. 绘制权益曲线 + 滚动胜率双轴图
  4. 移动平均平滑胜率, 识别趋势
  5. 拟合 Ornstein-Uhlenbeck 均值回复过程
  6. 应用课程决策判断框架
"""

import csv, os, sys, warnings
from collections import defaultdict, deque
from datetime import datetime, timedelta
from copy import deepcopy

import numpy as np

warnings.filterwarnings('ignore')

# ── 导入 openpyxl ─────────────────────────────────────────────
try:
    import openpyxl
except ImportError:
    print("❌ 需要 openpyxl: pip3 install openpyxl")
    sys.exit(1)

# ── 导入 matplotlib ───────────────────────────────────────────
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.ticker import FuncFormatter
except ImportError:
    print("❌ 需要 matplotlib: pip3 install matplotlib")
    sys.exit(1)

# ── 导入 scipy (可选 ─ OU 拟合用) ──────────────────────────────
try:
    from scipy.optimize import minimize
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    print("⚠ scipy 未安装, 跳过 OU 拟合")

# ═══════════════════════════════════════════════════════════════
# 全局配置
# ═══════════════════════════════════════════════════════════════
EXCEL_PATH = '/Users/wangzhiwei/py_projects/Quant-Guild-Library/exp_zoo/gtja_trade_analysis/2020-2026-对账单.xlsx'
OUTPUT_DIR = '/Users/wangzhiwei/py_projects/Quant-Guild-Library/exp_zoo/gtja_trade_analysis'

# 要包含的买入交易类型
BUY_TYPES = {
    '证券买入',
    '上海A股普通股票竞价买入', '深圳A股普通股票竞价买入', '深圳A股创业板股票竞价买入',
    '上海跨境ETF竞价买入', '深圳跨境ETF竞价买入',
    '上海跨市场股票ETF竞价买入', '深圳跨市场股票ETF竞价买入',
    '上海单市场股票ETF竞价买入', '深圳LOF基金竞价买入',
    '沪港通港股买入交收',
}

# 要包含的卖出交易类型
SELL_TYPES = {
    '证券卖出',
    '上海A股普通股票竞价卖出', '深圳A股普通股票竞价卖出', '深圳A股创业板股票竞价卖出',
    '上海跨境ETF竞价卖出', '深圳跨境ETF竞价卖出',
    '上海跨市场股票ETF竞价卖出', '深圳跨市场股票ETF竞价卖出',
    '上海单市场股票ETF竞价卖出', '深圳LOF基金竞价卖出',
    '沪港通港股卖出交收',
}

# 成交类（金额=0，忽略）
TRADE_ONLY_TYPES = {
    '沪港通港股买入成交', '沪港通港股卖出成交',
}

# 股票风格对应的颜色 (用于图例)
EXCHANGE_COLORS = {
    'SH': '#E74C3C',  # 上海
    'SZ': '#3498DB',  # 深圳
    'HK': '#2ECC71',  # 港股通
    'ETF': '#9B59B6', # ETF
}


# ═══════════════════════════════════════════════════════════════
# 1. 数据加载与分类
# ═══════════════════════════════════════════════════════════════
print("=" * 70)
print("📂 加载数据...")
print("=" * 70)

wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
ws = wb['合并对账单']

all_rows = []
for row in ws.iter_rows(min_row=2, values_only=True):
    all_rows.append(row)
print(f"  总记录数: {len(all_rows)}")

def parse_date(d):
    """安全解析日期"""
    if d is None:
        return None
    d_str = str(d).strip()
    if len(d_str) == 8 and d_str.isdigit():
        return datetime.strptime(d_str, '%Y%m%d')
    if isinstance(d, datetime):
        return d
    return d


def detect_exchange(code, category):
    """检测交易所"""
    code_str = str(code).strip()
    if '沪港通' in str(category) or '港股' in str(category):
        return 'HK'
    if code_str.startswith('6') or code_str.startswith('9'):
        return 'SH'
    if code_str.startswith(('0', '3')):
        return 'SZ'
    # ETF 代码
    if code_str.startswith(('51', '16', '15')):
        return 'ETF'
    return 'SZ'  # 默认


# 解析并分类
parsed = []
stats = defaultdict(int)
# 记录全部现金余额事件 (用于权益曲线)
balance_events = []

for r in all_rows:
    date_settle, date_order, contract, account, holder_code, code, name, category, qty, price, amount, balance, currency, remark = r

    if category is None or code is None:
        # 记录余额事件（银行转证券/利息等）
        if category and balance is not None and date_settle:
            balance_events.append((parse_date(date_settle), balance, category, amount or 0))
        continue

    # 判断交易方向
    direction = None
    if category in BUY_TYPES:
        direction = 'buy'
        stats['buy'] += 1
    elif category in SELL_TYPES:
        direction = 'sell'
        stats['sell'] += 1
    elif category in TRADE_ONLY_TYPES:
        stats['trade_only'] += 1
        continue  # 跳过成交记录（金额为0）
    else:
        stats['other'] += 1
        # 记录非买卖的余额事件
        if balance is not None and date_settle:
            balance_events.append((parse_date(date_settle), balance, category, amount or 0))
        continue

    dt = parse_date(date_settle)
    qty_val = int(qty) if qty else 0
    price_val = float(price) if price else 0
    amount_val = float(amount) if amount else 0
    balance_val = float(balance) if balance else 0

    # 检测交易所
    exchange = detect_exchange(code, category)

    parsed.append({
        'date': dt,
        'date_str': date_settle,
        'code': str(code).strip(),
        'name': str(name).strip() if name else '',
        'category': category,
        'direction': direction,
        'qty': qty_val,
        'price': price_val,
        'amount': amount_val,   # 含费用的净额: 买入为负, 卖出为正
        'balance': balance_val,
        'exchange': exchange,
    })

    # 记录余额事件
    balance_events.append((dt, balance_val, category, amount_val))


print(f"  ├ 买入记录: {stats['buy']}")
print(f"  ├ 卖出记录: {stats['sell']}")
print(f"  ├ 成交记录(跳过): {stats['trade_only']}")
print(f"  └ 其他记录: {stats['other']}")

# 按日期排序
parsed.sort(key=lambda x: x['date'])

# 统计涉及的证券
securities = set((p['code'], p['name']) for p in parsed)
print(f"\n  涉及证券: {len(securities)} 只")

# 交易所分布
exch_counts = defaultdict(int)
for p in parsed:
    exch_counts[p['exchange']] += 1
for ex, cnt in sorted(exch_counts.items()):
    print(f"  {EXCHANGE_COLORS.get(ex, '#666')} {ex}: {cnt} 条")

# 时间范围
dates = [p['date'] for p in parsed if p['date']]
print(f"  时间范围: {min(dates).strftime('%Y/%m/%d')} ~ {max(dates).strftime('%Y/%m/%d')}")

# ═══════════════════════════════════════════════════════════════
# 2. FIFO 买卖匹配
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("🔄 FIFO 买卖匹配...")
print("=" * 70)

inventory = {}  # code -> deque of buy lots
trades = []     # 完整的 round-trip trades
pre_existing = defaultdict(int)  # code -> estimated initial position

for p in parsed:
    code = p['code']

    if code not in inventory:
        inventory[code] = deque()

    if p['direction'] == 'buy':
        # 买入 → 加入 FIFO 队列
        lot = {
            'buy_date': p['date'],
            'code': code,
            'name': p['name'],
            'qty': p['qty'],
            'total_cost': abs(p['amount']),  # 买入总成本（正数）
            'price': p['price'],
            'exchange': p['exchange'],
        }
        inventory[code].append(lot)

    elif p['direction'] == 'sell':
        sell_qty = p['qty']
        sell_proceeds = p['amount']  # 卖出净收入（正数，已扣费）
        remaining = sell_qty
        matched_lots = []
        total_cost = 0
        matched_qty = 0

        # FIFO 从最老的开始匹配
        while remaining > 0 and inventory[code]:
            lot = inventory[code][0]
            use_qty = min(lot['qty'], remaining)
            cost_share = lot['total_cost'] * (use_qty / lot['qty'])

            matched_lots.append({
                'buy_date': lot['buy_date'],
                'qty': use_qty,
                'cost': cost_share,
                'buy_price': lot['price'],
            })
            total_cost += cost_share
            matched_qty += use_qty
            remaining -= use_qty

            if use_qty >= lot['qty']:
                inventory[code].popleft()
            else:
                lot['qty'] -= use_qty
                lot['total_cost'] -= cost_share

        # 库存不够的部分来自期初持仓
        from_pre = remaining > 0
        if from_pre:
            pre_existing[code] += remaining

        # 分配卖出收入
        if matched_qty > 0:
            allocated_proceeds = sell_proceeds * (matched_qty / sell_qty)
            pnl = allocated_proceeds - total_cost
        else:
            allocated_proceeds = 0
            pnl = 0

        trades.append({
            'sell_date': p['date'],
            'code': code,
            'name': p['name'],
            'sell_price': p['price'],
            'sell_qty': sell_qty,
            'matched_qty': matched_qty,
            'sell_proceeds': allocated_proceeds,
            'buy_lots': matched_lots,
            'total_cost': total_cost,
            'pnl': round(pnl, 2),
            'from_pre_existing': from_pre,
            'exchange': p['exchange'],
        })

# 过滤出完整匹配的交易（不含期初持仓部分）
clean_trades = [t for t in trades if not t['from_pre_existing'] and abs(t['pnl']) > 0.01]

print(f"\n  总交易轮次: {len(trades)}")
print(f"  完整匹配交易(可用于胜率分析): {len(clean_trades)}")
print(f"  部分匹配(期初持仓): {len(trades) - len(clean_trades)}")

if pre_existing:
    print(f"  涉及的期初持仓标的: {len(pre_existing)}")

# 检查是否有未匹配的持仓
open_positions = {code: sum(lot['qty'] for lot in lots) for code, lots in inventory.items() if lots}
if open_positions:
    print(f"  期末持仓标的: {len(open_positions)} 只")
    for code, qty in sorted(open_positions.items(), key=lambda x: -x[1])[:10]:
        name = inventory[code][0]['name']
        print(f"    {code} {name}: {qty} 股")

# ═══════════════════════════════════════════════════════════════
# 3. 基础统计 & Edge 计算
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("📊 Edge 计算")
print("=" * 70)

if clean_trades:
    clean_trades.sort(key=lambda x: x['sell_date'])
    wins = [t for t in clean_trades if t['pnl'] > 0]
    losses = [t for t in clean_trades if t['pnl'] < 0]
    n_wins = len(wins)
    n_losses = len(losses)
    total_trades = len(clean_trades)

    p_win = n_wins / total_trades
    avg_win = np.mean([t['pnl'] for t in wins]) if n_wins > 0 else 0
    avg_loss = np.mean([t['pnl'] for t in losses]) if n_losses > 0 else 0
    edge = p_win * avg_win + (1 - p_win) * avg_loss

    # 盈亏比
    win_loss_ratio = abs(avg_win / avg_loss) if avg_loss != 0 else float('inf')

    print(f"\n  完整交易: {total_trades} 笔")
    print(f"  盈利: {n_wins} 笔 ({p_win*100:.1f}%)")
    print(f"  亏损: {n_losses} 笔 ({(1-p_win)*100:.1f}%)")
    print(f"  平均盈利: ¥{avg_win:>10.2f}")
    print(f"  平均亏损: ¥{avg_loss:>10.2f}")
    print(f"  盈亏比:   {win_loss_ratio:>10.2f}")
    print(f"  总盈亏:   ¥{sum(t['pnl'] for t in clean_trades):>10.2f}")
    print(f"  Edge/笔:  ¥{edge:>10.2f}  {'✅' if edge > 0 else '⚠️' if edge < 0 else '➡️'}")

    # 按年份统计
    print(f"\n  按年份统计:")
    by_year = defaultdict(list)
    for t in clean_trades:
        y = t['sell_date'].year
        by_year[y].append(t)

    years_sorted = sorted(by_year.keys())
    for y in years_sorted:
        yr_trades = by_year[y]
        yr_wins = sum(1 for t in yr_trades if t['pnl'] > 0)
        yr_pnl = sum(t['pnl'] for t in yr_trades)
        print(f"    {y}: {len(yr_trades):3d} 笔, {yr_wins:3d} 胜, "
              f"胜率 {yr_wins/len(yr_trades)*100:5.1f}%, "
              f"总P&L ¥{yr_pnl:+8.2f}")

    # 按交易所统计
    print(f"\n  按交易所统计:")
    by_exch = defaultdict(list)
    for t in clean_trades:
        by_exch[t.get('exchange', 'UNK')].append(t)
    for ex, trs in sorted(by_exch.items()):
        ex_wins = sum(1 for t in trs if t['pnl'] > 0)
        ex_pnl = sum(t['pnl'] for t in trs)
        print(f"    {ex}: {len(trs):3d} 笔, {ex_wins:3d} 胜, "
              f"胜率 {ex_wins/len(trs)*100:5.1f}%, "
              f"总P&L ¥{ex_pnl:+8.2f}")

else:
    print("  ⚠ 没有完整匹配的交易")
    p_win = avg_win = avg_loss = edge = 0
    n_wins = n_losses = 0

# ═══════════════════════════════════════════════════════════════
# 4. 权益曲线构建
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("📈 构建权益曲线...")
print("=" * 70)

# 从第一笔余额记录获取初始现金余额
balance_events.sort(key=lambda x: x[0])
initial_cash = balance_events[0][1] if balance_events else 0
print(f"  初始现金余额: ¥{initial_cash:>10.2f}")

# 统计银转证/证转银净额
net_deposit = sum(amt for _, _, cat, amt in balance_events if '银转证' in str(cat) or '银行转证券' in str(cat))
net_withdraw = sum(amt for _, _, cat, amt in balance_events if '证转银' in str(cat) or '证券转银行' in str(cat))
print(f"  银转证总额: ¥{net_deposit:>10,.2f}")
print(f"  证转银总额: ¥{net_withdraw:>10,.2f}")

# ⚠ 不能用现金余额做权益曲线，因为存提款金额(¥423,909)远大于交易P&L(¥86,468)
#    正确方法: 初始余额 + 累计交易P&L = 真实交易权益曲线

# 累计交易 P&L 曲线（仅含完整匹配的交易）
if clean_trades:
    trade_dates = [t['sell_date'] for t in clean_trades]
    trade_pnl_cum = np.cumsum([t['pnl'] for t in clean_trades])
    # 交易权益曲线 = 初始现金余额 + 累计P&L
    trade_equity = [initial_cash] + [initial_cash + p for p in trade_pnl_cum]
    trade_eq_dates = [trade_dates[0]] + trade_dates  # 折线从首笔交易开始
    final_equity = trade_equity[-1]
    total_pnl = trade_pnl_cum[-1]
    total_return_pct = total_pnl / initial_cash * 100 if initial_cash > 0 else 0
    print(f"  交易权益终值: ¥{final_equity:>10.2f}")
    print(f"  交易累计P&L:  ¥{total_pnl:>10,.2f}")
    print(f"  收益率:       {total_return_pct:>+8.2f}%")
else:
    trade_eq_dates, trade_equity = [], []
    initial_cash = 0
    total_pnl = 0
    final_equity = 0
    total_return_pct = 0

# ═══════════════════════════════════════════════════════════════
# 5. 滚动胜率计算
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("🎯 计算滚动胜率...")
print("=" * 70)

def rolling_win_rate(trades_list, windows=[10, 20, 50]):
    """
    计算多个窗口的滚动胜率
    返回 {window: (dates, rates)}
    """
    result = {}
    for w in windows:
        rates = []
        dates = []
        for i in range(len(trades_list)):
            start = max(0, i - w + 1)
            window = trades_list[start:i+1]
            wr = sum(1 for t in window if t['pnl'] > 0) / len(window)
            rates.append(wr)
            dates.append(trades_list[i]['sell_date'])
        result[w] = (dates, rates)
    return result

if clean_trades:
    # 使用 [10, 20, 50, 100] 窗口
    wr_data = rolling_win_rate(clean_trades, [10, 20, 50, 100])

    for w in [10, 20, 50]:
        dates_w, rates_w = wr_data[w]
        if rates_w:
            print(f"  滚动{w}笔: 首段均值={np.mean(rates_w[:min(5,len(rates_w))]):.3f}  "
                  f"末段均值={np.mean(rates_w[-min(5,len(rates_w)):]):.3f}  "
                  f"整体均值={np.mean(rates_w):.3f}")

    # 对20期胜率做移动平均平滑
    rates_20 = np.array(wr_data[20][1])
    ma3 = np.convolve(rates_20, np.ones(3)/3, mode='valid')
    ma5 = np.convolve(rates_20, np.ones(5)/5, mode='valid')
    ma10 = np.convolve(rates_20, np.ones(10)/10, mode='valid')

    smooth_dates_3 = wr_data[20][0][1:-1]
    smooth_dates_5 = wr_data[20][0][2:-2]
    smooth_dates_10 = wr_data[20][0][4:-5]

    print(f"\n  平滑后胜率趋势 (MA5):")
    print(f"    前半段: {np.mean(ma5[:len(ma5)//2])*100:.1f}%")
    print(f"    后半段: {np.mean(ma5[len(ma5)//2:])*100:.1f}%")
else:
    wr_data = {}
    ma3 = ma5 = ma10 = np.array([])
    smooth_dates_3 = smooth_dates_5 = smooth_dates_10 = []

# ═══════════════════════════════════════════════════════════════
# 6. OU 过程拟合 (均值回复)
# 使用对数似然的OU公式，拟合参数 θ (回复速度), μ (长期均值), σ (波动率)
# 初始化参数后，通过数值优化最小化负对数似然，得到最佳拟合参数，即结果包括长期均值 μ 和半衰期（由 θ 计算）。如果 μ > 0.5，说明策略长期为正 Edge；半衰期则表示胜率偏离均值后回复的速度。
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("📐 拟合 Ornstein-Uhlenbeck 过程...")
print("=" * 70)

ou_params = None

if HAS_SCIPY and len(ma5) > 20:
    def ou_log_likelihood(params, data, dt=1.0/252):
        """OU 过程对数似然

        $$\mathcal{L} = \sum_{t} \left[ -\frac{1}{2}\ln(2\pi\sigma^2 dt) - \frac{(X_{t+1} - X_t - \theta(\mu-X_t)dt)^2}{2\sigma^2 dt} \right]$$

        return ll: log likelihood
        """
        theta, mu, sigma = params
        if sigma <= 0 or theta <= 0:
            return 1e10
        n = len(data)
        ll = 0
        for i in range(1, n):
            prev = data[i-1]
            curr = data[i]
            mean = prev + theta * (mu - prev) * dt
            var = sigma**2 * dt
            if var <= 0:
                return 1e10
            ll += -0.5 * np.log(2 * np.pi * var) - (curr - mean)**2 / (2 * var)
        return -ll

    data_ou = ma5  # Use MA5 smoothed win rate
    data_ou = np.clip(data_ou, 0.01, 0.99)  # prevent boundary issues

    try:
        mu_init = np.mean(data_ou)
        theta_init = 0.5
        sigma_init = np.std(np.diff(data_ou)) * np.sqrt(252)

        result = minimize(
            lambda p: ou_log_likelihood(p, data_ou),
            [theta_init, mu_init, sigma_init],  # 传入初始参数
            bounds=[(1e-4, 10), (0.01, 0.99), (1e-4, 0.5)], # 参数边界，约束条件
            method='L-BFGS-B'
        )

        if result.success:
            theta_fit, mu_fit, sigma_fit = result.x
            ou_params = {
                'theta': theta_fit,   # 回复速度
                'mu': mu_fit,         # 长期均值
                'sigma': sigma_fit,   # 波动率
                'half_life': np.log(2) / theta_fit if theta_fit > 0 else float('inf'),
            }
            print(f"  θ (回复速度)   = {theta_fit:.4f}")
            print(f"  μ (长期均值)   = {mu_fit:.4f} ({mu_fit*100:.1f}%)")
            print(f"  σ (波动率)     = {sigma_fit:.4f}")
            print(f"  半衰期        = {ou_params['half_life']:.1f} 笔交易")
            print(f"  正Edge (μ>0.5): {'✅ 是' if mu_fit > 0.5 else '⚠️ 否'}")
        else:
            print(f"  ⚠ OU 拟合未收敛: {result.message}")
    except Exception as e:
        print(f"  ⚠ OU 拟合出错: {e}")
else:
    if not HAS_SCIPY:
        print("  ⚠ 跳过 (需 scipy)")
    else:
        print("  ⚠ 跳过 (数据不足, 需要 >20 个平滑数据点)")

# ═══════════════════════════════════════════════════════════════
# 7. 趋势判定
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("🔍 趋势判定")
print("=" * 70)

if len(ma5) >= 10:
    first_half = np.mean(ma5[:len(ma5)//2])
    second_half = np.mean(ma5[len(ma5)//2:])
    change = second_half - first_half

    if change > 0.03:
        trend = "📈 上升"
        trend_detail = "胜率呈现上升趋势，Edge 可能在增强"
    elif change < -0.03:
        trend = "📉 下降"
        trend_detail = "⚠ 胜率呈现下降趋势，关注 Edge 衰减"
    else:
        trend = "➡️ 稳定"
        trend_detail = "胜率总体稳定"

    # 检查最近的趋势
    recent_10 = np.mean(ma5[-10:]) if len(ma5) >= 10 else np.mean(ma5)
    prior_10 = np.mean(ma5[-20:-10]) if len(ma5) >= 20 else np.mean(ma5[:len(ma5)//2])

    print(f"  整体趋势: {trend}")
    print(f"  前半段均值: {first_half*100:.1f}%")
    print(f"  后半段均值: {second_half*100:.1f}%")
    print(f"  变化: {change*100:+.1f}%")
    print(f"  近期(后10笔)均值: {recent_10*100:.1f}%")
    print(f"  中期(前10笔)均值: {prior_10*100:.1f}%")

    recent_change = recent_10 - prior_10
    if recent_change > 0.02:
        print(f"  近期趋势: 📈 胜率近期上升中")
    elif recent_change < -0.02:
        print(f"  近期趋势: 📉 胜率近期下降中")
    else:
        print(f"  近期趋势: ➡️ 胜率近期稳定")
else:
    first_half = second_half = 0
    change = 0
    trend = "数据不足"
    trend_detail = ""

# OU 校验
if ou_params:
    print(f"\n  OU 长期均值 {ou_params['mu']*100:.1f}% — "
          f"{'正 Edge 策略 ✅' if ou_params['mu'] > 0.5 else '长期为负 Edge ⚠️'}")
    print(f"  半衰期 {ou_params['half_life']:.0f} 笔: "
          f"胜率偏离后约需 {ou_params['half_life']:.0f} 笔交易回复到均值")

# ═══════════════════════════════════════════════════════════════
# 8. 应用决策框架
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("📋 课程决策框架")
print("=" * 70)

# 基于以下判断:
# - 整体胜率趋势: 前半 vs 后半
# - 近期趋势: 近10笔 vs 前10笔
# - OU 长期均值: 是否 > 0.5

state = []
if clean_trades:
    if change < -0.03:
        state.append(("胜率持续下降", "停止交易"))
    elif recent_change < -0.02:
        state.append(("胜率暂时低迷但均值回复", "持有观察或减少仓位"))
    if ou_params and ou_params['mu'] > 0.5:
        state.append(("胜率稳定在正 Edge (OU长期均值)", "继续交易"))
    elif ou_params and ou_params['mu'] <= 0.5:
        state.append(("OU 长期均值 < 50%", "需谨慎评估"))
    if recent_change > 0.02:
        state.append(("胜率从低点回复到正 Edge", "可以考虑重新入场"))
    if p_win >= 0.50 and edge > 0:
        state.append(("胜率稳定在正 Edge", "继续交易"))

print(f"{'状态':<40} {'行动':<20}")
print(f"{'-'*60}")
for s, a in state:
    print(f"{s:<40} {a:<20}")

print(f"\n  综合判定:")
if edge > 0 and p_win >= 0.50:
    print(f"    ✅ 策略总体为正 Edge — 继续交易, 持续监控")
elif edge > 0 and p_win < 0.50:
    print(f"    ⚠️ Edge 为正但胜率低于50% — 靠盈亏比支撑, 减少仓位")
elif edge < 0 and recent_change > 0.02:
    print(f"    🔄 Edge 目前为负, 但近期胜率在回升 — 持有观察")
elif edge < 0:
    print(f"    ❌ Edge 为负 — 建议停止交易或大幅减仓")
else:
    print(f"    ⚖️ 难以判定 — 数据不足")

# ═══════════════════════════════════════════════════════════════
# 9. 可视化
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("🖼️ 生成图表...")
print("=" * 70)

plt.rcParams['font.sans-serif'] = ['PingFang HK', 'STHeiti', 'Songti SC', 'SimHei', 'Apple LiGothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150

# ─── 图1: 权益曲线 + 滚动胜率 双轴图 ──────────────────────
print("  图1: 权益曲线 + 滚动胜率...")
fig, ax1 = plt.subplots(figsize=(16, 7))

# 主轴: 交易权益曲线 (初始余额 + 累计交易P&L, 排除存提款干扰)
if trade_eq_dates and trade_equity:
    ax1.plot(trade_eq_dates, trade_equity, 'g-', linewidth=2.5, alpha=0.9,
             label=f'交易权益曲线 (初始¥{initial_cash:.0f}+累计P&L) 终¥{final_equity:.0f}')
    # 标注关键日期
    for label_dt, label_txt, y_offset in [
        (datetime(2020,7,1), '初始¥20,000', 0.05),
        (datetime(2022,1,1), '2022亏损期', -0.08),
        (datetime(2024,1,1), '2024盈利爆发', 0.08),
    ]:
        idx = np.searchsorted(trade_eq_dates, label_dt)
        if 0 < idx < len(trade_equity):
            y_val = trade_equity[idx]
            ax1.annotate(label_txt, xy=(label_dt, y_val),
                        fontsize=9, fontweight='bold', color='darkgreen',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

ax1.axhline(y=initial_cash, color='gray', linestyle='--', alpha=0.5, linewidth=1,
            label=f'初始余额 ¥{initial_cash:.0f}')
ax1.set_xlabel('日期')
ax1.set_ylabel('账户权益 (¥)', color='g')
ax1.tick_params(axis='y', labelcolor='g')

# 在图上注明银转证干扰
ax1.text(0.98, 0.95,
         f'⚠ 现金余额含银转证¥{net_deposit:.0f},不可直接用于分析\n  此处曲线=初始¥{initial_cash:.0f}+累计P&L¥{total_pnl:+.0f}',
         transform=ax1.transAxes, fontsize=8, ha='right', va='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

# 双轴: 胜率
ax2 = ax1.twinx()
colors_wr = ['#3498DB', '#E74C3C', '#9B59B6', '#F39C12']
labels_wr = ['滚动10笔', '滚动20笔', '滚动50笔', '滚动100笔']
wr_windows = [10, 20, 50, 100]

for w, c, l in zip(wr_windows, colors_wr, labels_wr):
    if w in wr_data and wr_data[w][1]:
        ax2.plot(wr_data[w][0], [v*100 for v in wr_data[w][1]],
                 color=c, linewidth=1, alpha=0.6, label=l)

# 平滑线
if len(ma5) > 0 and len(smooth_dates_5) > 0:
    ax2.plot(smooth_dates_5, ma5 * 100, 'r--', linewidth=2,
             label=f'MA平滑(5) 末={ma5[-1]*100:.1f}%')

ax2.axhline(y=50, color='orange', linestyle=':', alpha=0.7, linewidth=1.5, label='50% 基准线')
if ou_params and ou_params['mu']:
    ax2.axhline(y=ou_params['mu']*100, color='purple', linestyle='--', alpha=0.5,
                linewidth=1, label=f"OU长期均值 {ou_params['mu']*100:.1f}%")

ax2.set_ylabel('胜率 (%)', color='b')
ax2.set_ylim(0, 105)

# 日期格式
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_major_locator(mdates.YearLocator())
plt.xticks(rotation=45)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8, ncol=2)

plt.title('GTJA 2020-2026 对账单 — 权益曲线与滚动胜率', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'full_fig1_equity_winrate.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"    ✓ 保存: full_fig1_equity_winrate.png")

# ─── 图2: P&L 分析 + 年度胜率 ──────────────────────────────
print("  图2: P&L 与年度分析...")
if clean_trades:
    fig = plt.figure(figsize=(16, 12))

    # 2a: P&L 柱状图
    ax1 = plt.subplot(2, 2, (1, 2))
    colors_bar = ['g' if t['pnl'] > 0 else 'r' for t in clean_trades]
    x = np.arange(len(clean_trades))
    ax1.bar(x, [t['pnl'] for t in clean_trades], color=colors_bar, alpha=0.7, edgecolor='black', linewidth=0.3)
    ax1.axhline(y=0, color='black', linewidth=0.8)
    ax1.axhline(y=avg_win, color='g', linestyle='--', alpha=0.6, label=f'平均盈利 ¥{avg_win:.0f}')
    ax1.axhline(y=avg_loss, color='r', linestyle='--', alpha=0.6, label=f'平均亏损 ¥{avg_loss:.0f}')

    # 累积曲线
    ax1_t = ax1.twinx()
    cum_pnl = np.cumsum([t['pnl'] for t in clean_trades])
    ax1_t.plot(x, cum_pnl, 'b-', linewidth=2, label=f'累计P&L ¥{cum_pnl[-1]:.0f}')
    ax1_t.legend(loc='upper right', fontsize=9)

    ax1.set_xlabel('交易序号')
    ax1.set_ylabel('P&L (¥)')
    ax1.set_title('每笔交易 P&L 与累计收益', fontsize=12)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(alpha=0.3)

    # 2b: 年度胜率
    ax2 = plt.subplot(2, 2, 3)
    years = sorted(by_year.keys())
    year_win_rates = [sum(1 for t in by_year[y] if t['pnl'] > 0) / len(by_year[y]) * 100 for y in years]
    year_counts = [len(by_year[y]) for y in years]

    bars2 = ax2.bar(years, year_win_rates, color=['#3498DB' if wr >= 50 else '#E74C3C' for wr in year_win_rates],
                    alpha=0.8, edgecolor='black', linewidth=0.5)
    ax2.axhline(y=50, color='orange', linestyle=':', alpha=0.7, linewidth=1.5)
    ax2.set_ylabel('胜率 (%)')
    ax2.set_xlabel('年份')
    ax2.set_title('年度胜率', fontsize=12)
    ax2.grid(axis='y', alpha=0.3)

    for i, (bar, ct) in enumerate(zip(bars2, year_counts)):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{year_win_rates[i]:.0f}%\n({ct}笔)', ha='center', fontsize=9)

    # 2c: 交易所分布
    ax3 = plt.subplot(2, 2, 4)
    ex_names = list(by_exch.keys())
    ex_win_rates = [sum(1 for t in by_exch[ex] if t['pnl'] > 0) / len(by_exch[ex]) * 100 if by_exch[ex] else 0
                    for ex in ex_names]
    ex_colors = [EXCHANGE_COLORS.get(ex, '#666') for ex in ex_names]
    ex_counts = [len(by_exch[ex]) for ex in ex_names]

    bars3 = ax3.barh(ex_names, ex_win_rates, color=ex_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    ax3.axvline(x=50, color='orange', linestyle=':', alpha=0.7, linewidth=1.5)
    ax3.set_xlabel('胜率 (%)')
    ax3.set_title('按交易所胜率', fontsize=12)
    ax3.grid(axis='x', alpha=0.3)

    for bar, ct, wr in zip(bars3, ex_counts, ex_win_rates):
        ax3.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                 f'{wr:.0f}% ({ct}笔)', va='center', fontsize=9)

    plt.suptitle('GTJA 2020-2026 — P&L 与胜率分析', fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(os.path.join(OUTPUT_DIR, 'full_fig2_pnl_analysis.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"    ✓ 保存: full_fig2_pnl_analysis.png")

# ─── 图3: 胜率时间演变（核心图）──────────────────────────────
print("  图3: 胜率时间演变...")
if clean_trades and len(ma5) > 0:
    fig, ax = plt.subplots(figsize=(16, 7))

    # 绘制滚动20笔胜率
    dates20, rates20 = wr_data[20]
    ax.plot(dates20, [r*100 for r in rates20], 'b-', linewidth=1.2, alpha=0.5, label='滚动20笔胜率')

    # MA 平滑线
    ax.plot(smooth_dates_5, ma5 * 100, 'r-', linewidth=2.5, label='MA平滑(5期)')
    if len(ma10) > 0 and len(smooth_dates_10) > 0:
        ax.plot(smooth_dates_10, ma10 * 100, 'orange', linewidth=2, alpha=0.8, label='MA平滑(10期)')

    # 填充正/负 Edge 区域
    if len(smooth_dates_5) > 0:
        ax.fill_between(smooth_dates_5, ma5 * 100, 50,
                         where=(ma5 * 100 >= 50), color='g', alpha=0.08, label='正Edge区域')
        ax.fill_between(smooth_dates_5, ma5 * 100, 50,
                         where=(ma5 * 100 < 50), color='r', alpha=0.08, label='负Edge区域')

    ax.axhline(y=50, color='orange', linestyle=':', linewidth=2, alpha=0.8)
    ax.axhline(y=p_win * 100, color='purple', linestyle='--', linewidth=1.5, alpha=0.6,
               label=f'整体胜率 {p_win*100:.1f}%')

    if ou_params:
        ax.axhline(y=ou_params['mu']*100, color='darkgreen', linestyle='-.', linewidth=1.5,
                   alpha=0.6, label=f"OU长期均值 {ou_params['mu']*100:.1f}%")

    ax.set_xlabel('交易时间')
    ax.set_ylabel('胜率 (%)')
    ax.set_title('核心分析：胜率的时间演变 — 是否出现 Edge 衰减？', fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(alpha=0.3)

    # 时间刻度
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    plt.xticks(rotation=45)

    # 判断文本框
    judgement_parts = [
        f"分析判断:",
        f"  整体胜率: {p_win*100:.1f}% ({n_wins}胜/{n_losses}负)",
        f"  Edge/笔: ¥{edge:.2f}",
        f"  前半MA: {first_half*100:.1f}% → 后半MA: {second_half*100:.1f}%",
    ]
    if ou_params:
        judgement_parts.append(f"  OU长期均值: {ou_params['mu']*100:.1f}% (半衰期{ou_params['half_life']:.0f}笔)")

    if edge > 0 and p_win > 0.5:
        judgement_parts.append(f"  ✅ 正 Edge 策略")
    elif edge < 0:
        judgement_parts.append(f"  ⚠️ 负 Edge — 建议关注")
    elif recent_change > 0.02:
        judgement_parts.append(f"  🔄 近期回升中")

    ax.text(0.01, 0.01, '\n'.join(judgement_parts), transform=ax.transAxes, fontsize=9.5,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9),
            verticalalignment='bottom', fontfamily='monospace')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'full_fig3_winrate_evolution.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"    ✓ 保存: full_fig3_winrate_evolution.png")

# ─── 图4: OU 过程模拟图 ─────────────────────────────────────
print("  图4: OU 模拟与未来路径...")
if ou_params and len(ma5) > 20:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 左: OU 拟合 vs 实际胜率
    ax1.plot(smooth_dates_5, ma5 * 100, 'b-', linewidth=1.5, alpha=0.7, label='实际胜率 (MA5)')
    ax1.axhline(y=ou_params['mu']*100, color='r', linestyle='--', linewidth=2,
                label=f"OU μ = {ou_params['mu']*100:.1f}%")
    # ±σ 区间
    std_est = ou_params['sigma'] / np.sqrt(2 * ou_params['theta']) * 100
    ax1.fill_between(smooth_dates_5,
                     (ou_params['mu'] - std_est/100) * 100,
                     (ou_params['mu'] + std_est/100) * 100,
                     color='red', alpha=0.1, label=f'±1σ 区间 ({std_est:.1f}%)')
    ax1.axhline(y=50, color='orange', linestyle=':', alpha=0.5)
    ax1.set_ylabel('胜率 (%)')
    ax1.set_xlabel('交易时间')
    ax1.set_title(f'OU 过程拟合\nθ={ou_params["theta"]:.3f} 半衰期={ou_params["half_life"]:.0f}笔')
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    plt.sca(ax1)
    plt.xticks(rotation=45)

    # 右: 模拟未来路径
    np.random.seed(42)
    n_future = 200
    n_paths = 50

    last_val = ma5[-1]
    theta, mu, sigma = ou_params['theta'], ou_params['mu'], ou_params['sigma']
    dt_ou = 1.0

    future_paths = []
    for _ in range(n_paths):
        path = [last_val]
        for _ in range(n_future):
            prev = path[-1]
            dv = theta * (mu - prev) * dt_ou + sigma * np.sqrt(dt_ou) * np.random.randn()
            next_val = min(max(prev + dv, 0.01), 0.99)
            path.append(next_val)
        future_paths.append(path)

    future_x = np.arange(len(smooth_dates_5), len(smooth_dates_5) + n_future + 1)

    for path in future_paths:
        ax2.plot(future_x, [v*100 for v in path], 'b-', alpha=0.08, linewidth=0.5)
    ax2.plot(future_x, [np.median([p[i] for p in future_paths])*100 for i in range(n_future+1)],
             'r-', linewidth=2, label='中位数路径')
    ax2.axhline(y=mu*100, color='green', linestyle='--', linewidth=1.5, label=f'长期均值 {mu*100:.1f}%')
    ax2.axhline(y=50, color='orange', linestyle=':', alpha=0.7)

    # 标记当前最后观测值
    ax2.axvline(x=len(smooth_dates_5)-1, color='gray', linestyle='--', alpha=0.5)
    ax2.text(len(smooth_dates_5)-1, ax2.get_ylim()[1]*0.95, '← 当前',
             ha='right', fontsize=9, color='gray')

    ax2.set_xlabel('交易序号')
    ax2.set_ylabel('胜率 (%)')
    ax2.set_title(f'OU 模拟未来 {n_future} 笔交易\n({n_paths} 条路径模拟)')
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3)

    plt.suptitle('Ornstein-Uhlenbeck 均值回复过程分析', fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(OUTPUT_DIR, 'full_fig4_ou_analysis.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"    ✓ 保存: full_fig4_ou_analysis.png")

# ═══════════════════════════════════════════════════════════════
# 10. 总结
# ══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("📋 分析总结")
print("=" * 70)

print(f"""
  数据周期:  {min(dates).strftime('%Y/%m/%d')} ~ {max(dates).strftime('%Y/%m/%d')}
  完整轮次:  {len(clean_trades)} 笔
  胜率:      {p_win*100:.1f}% ({n_wins}胜/{n_losses}负)
  平均盈利:  ¥{avg_win:.2f}
  平均亏损:  ¥{avg_loss:.2f}
  Edge(期望): ¥{edge:.2f}

  交易权益曲线: ¥{initial_cash:.0f} → ¥{final_equity:.0f} ({total_return_pct:+.2f}%)
  累计交易P&L: ¥{total_pnl:+,.0f} (银转证¥{net_deposit:+,.0f}已排除)

  趋势判定:  {trend_detail}
  {'✅ OU正Edge(长期胜率>50%)' if ou_params and ou_params['mu'] > 0.5 else '⚠️ OU长期胜率偏低' if ou_params else 'OU未拟合'}

  课程决策:
""")

print(f"{'状态':<42} {'行动':<22}")
print(f"{'-'*64}")
for s, a in state:
    print(f"{s:<42} {a:<22}")

print(f"\n  综合建议: ", end='')
if edge > 0 and p_win >= 0.50:
    print("继续交易, 持续监控滚动胜率变化")
elif edge > 0 and p_win < 0.50:
    print("减少仓位, 监控胜率能否回升到50%以上")
elif edge < 0 and recent_change > 0.02:
    print("持有观察, 近期胜率有回升迹象")
elif edge < 0:
    print("⚠️ Edge为负 — 建议停止交易或大幅减仓")
else:
    print("数据不足以判断")

print(f"\n  图表输出目录: {OUTPUT_DIR}")
print("=" * 70)
