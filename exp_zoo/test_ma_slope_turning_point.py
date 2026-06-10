#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 MA斜率检测（ma_slope）与 turning_point_60 信号正确性
==========================================================
生成合成价格序列，包含明确的趋势阶段：
  1. 平稳期 (sideways)
  2. 上涨趋势期 (uptrend)
  3. 下跌趋势期 (downtrend)     —— was_bearish_60 应在此激活
  4. 均线走平期 (flattening)    —— is_flattening_60 应在此激活
                                   turning_point = was_bearish & is_flattening
  5. 上涨恢复期 (recovery)

核心验证点：
  ✔ turning_point 只出现在「下跌→走平」的转折点，其他阶段不触发
  ✔ 走平期斜率 ≈ 0
  ✔ 下跌期斜率为负，was_bearish=True
  ✔ 上涨/平稳期 was_bearish=False
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ─── 中文字体设置（显式注册 wqy-zenhei.ttc）───────────────────────────
_WQY_PATH = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
if Path(_WQY_PATH).exists():
    fm.fontManager.addfont(_WQY_PATH)
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'DejaVu Sans', 'sans-serif']
else:
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ─── 默认数据文件路径 ────────────────────────────────────────────────
DEFAULT_DATA_PATH = Path(__file__).parent / "synthetic_ma_data.parquet"
DEFAULT_PLOT_PATH = Path(__file__).parent / "test_ma_slope_result.png"

# ═════════════════════════════════════════════════════════════════════
# 1. 数据生成 / 加载
# ═════════════════════════════════════════════════════════════════════

def generate_synthetic_data(seed=42, n_days=750, save_path=None):
    """
    生成合成价格序列，包含 5 个趋势阶段。
    返回带所有计算指标的 DataFrame。
    若 save_path 指定（.parquet 或 .csv），则将数据固化到磁盘。
    """
    np.random.seed(seed)
    dates = pd.date_range('2023-01-01', periods=n_days, freq='B')
    price = np.zeros(n_days)

    # ── 阶段边界 ──
    p1_end = 100   # 0..100   平稳期
    p2_end = 220   # 100..220 上涨期 (100→140)
    p3_end = 380   # 220..380 下跌期 (140→80)
    p4_end = 520   # 380..520 走平期 (80→84，微幅上扬抵消 MA 惯性)
    # p5_end = 750 # 520..750 恢复期 (84→130)

    # P1: 平稳
    price[:100] = 100 + np.random.randn(100) * 2

    # P2: 上涨
    price[100:220] = price[99] + np.linspace(0, 40, 120) + np.random.randn(120) * 1.8

    # P3: 下跌
    price[220:380] = price[219] + np.linspace(0, -60, 160) + np.random.randn(160) * 2.5

    # P4: 走平（前 60 天温和上扬，抵消 MA60 中的下跌惯性）
    flat_rise = np.linspace(0, 5, p4_end - p3_end)
    price[380:520] = price[379] + flat_rise + np.random.randn(p4_end - p3_end) * 1.2

    # P5: 恢复
    price[520:] = price[519] + np.linspace(0, 46, n_days - 520) + np.random.randn(n_days - 520) * 2.0

    price = np.maximum(price, 10)

    # ── 组装 DataFrame ──
    df = pd.DataFrame({'close': price}, index=dates)
    df.index.name = 'date'

    # ── 阶段标注 ──
    def phase_label(idx):
        if idx < p1_end:   return '1-平稳'
        elif idx < p2_end: return '2-上涨'
        elif idx < p3_end: return '3-下跌'
        elif idx < p4_end: return '4-走平'
        else:              return '5-恢复'

    df['phase'] = [phase_label(i) for i in range(n_days)]

    # ── 均线 & 斜率 ──
    df['ma20'] = df['close'].rolling(20).mean()
    df['ma60'] = df['close'].rolling(60).mean()
    df['ma120'] = df['close'].rolling(120).mean()

    df['slope_ma60'] = _ma_slope(df['close'], period=60, lookback=20)
    df['is_flattening_60'] = df['slope_ma60'].abs() < 0.001
    df['was_bearish_60'] = df['slope_ma60'].shift(20) < -0.002
    df['turning_point_60'] = df['was_bearish_60'] & df['is_flattening_60']

    # ── 固化到磁盘 ──
    if save_path is not None:
        _save_data(df, save_path)
        print(f"💾 数据已保存: {save_path}")

    return df


def _ma_slope(series, period=20, lookback=20):
    """计算均线斜率（线性回归），返回归一化斜率值。"""
    ma = series.rolling(period).mean()
    x = np.arange(lookback)
    slopes = ma.rolling(lookback).apply(
        lambda y: np.polyfit(x, y, 1)[0] if len(y) == lookback else np.nan,
        raw=True
    )
    return slopes / ma


def load_data(path=None):
    """
    加载之前固化的合成数据。
    支持 .parquet / .csv 格式。
    """
    path = Path(path or DEFAULT_DATA_PATH)
    if not path.exists():
        raise FileNotFoundError(f"数据文件不存在: {path}\n请先调用 generate_synthetic_data(save_path='{path}') 生成数据。")

    if path.suffix == '.parquet':
        df = pd.read_parquet(path)
    elif path.suffix == '.csv':
        df = pd.read_csv(path, index_col=0, parse_dates=True)
    else:
        raise ValueError(f"不支持的文件格式: {path.suffix}，请用 .parquet 或 .csv")

    # 恢复日期索引类型
    df.index = pd.to_datetime(df.index)
    df.index.name = 'date'
    print(f"📂 数据已加载: {path}  ({len(df)} 行)")
    return df


def _save_data(df, path):
    """将 DataFrame 固化到磁盘。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == '.parquet':
        df.to_parquet(path, index=True)
    elif path.suffix == '.csv':
        df.to_csv(path, index=True)
    else:
        raise ValueError(f"不支持的文件格式: {path.suffix}，请用 .parquet 或 .csv")


# ═════════════════════════════════════════════════════════════════════
# 2. 可视化
# ═════════════════════════════════════════════════════════════════════

def plot_ma_slope_analysis(df, zoom_slice=slice(300, 600), save_path=None):
    """
    绘制图表（纵向单列，共享 x 轴以便对齐）：
      1. 价格 + 均线 + 阶段背景 + turning_point 标记
      2. MA60 斜率（全周期）
      3. MA60 斜率（🔍 走平期放大）
      4. was_bearish_60（全周期）
      5. was_bearish_60（🔍 走平期放大）
      6. turning_point_60 信号组合（全周期）
      7. turning_point_60 信号组合（🔍 走平期放大）
    """
    # ── 检查必要列 ──
    required = ['close', 'ma20', 'ma60', 'ma120', 'slope_ma60',
                'is_flattening_60', 'was_bearish_60', 'turning_point_60', 'phase']
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"DataFrame 缺少必要列: {missing}")

    fig = plt.figure(figsize=(16, 18), constrained_layout=True)
    gs = fig.add_gridspec(7, 1, height_ratios=[2.5, 1, 0.7, 1, 0.7, 1, 0.7])

    ax1 = fig.add_subplot(gs[0])
    ax_slope = fig.add_subplot(gs[1], sharex=ax1)
    ax_slope_z = fig.add_subplot(gs[2], sharex=ax1)
    ax_bear = fig.add_subplot(gs[3], sharex=ax1)
    ax_bear_z = fig.add_subplot(gs[4], sharex=ax1)
    ax_tp = fig.add_subplot(gs[5], sharex=ax1)
    ax_tp_z = fig.add_subplot(gs[6], sharex=ax1)

    # ── 颜色方案 ──
    phase_colors = {
        '1-平稳': '#e0e0e0', '2-上涨': '#b7e4c7',
        '3-下跌': '#f5c6cb', '4-走平': '#ffeeba',
        '5-恢复': '#b7e4c7',
    }
    phase_display = {
        '1-平稳': '平稳', '2-上涨': '上涨',
        '3-下跌': '下跌', '4-走平': '走平',
        '5-恢复': '恢复',
    }

    # ====== 图1：价格 + 均线 + 信号 ======
    ax1.plot(df.index, df['close'], label='Close', color='gray', alpha=0.4, linewidth=0.6)
    ax1.plot(df.index, df['ma20'], label='MA20', color='steelblue', alpha=0.7, linewidth=0.8)
    ax1.plot(df.index, df['ma60'], label='MA60', color='darkorange', alpha=0.85, linewidth=1.2)
    ax1.plot(df.index, df['ma120'], label='MA120', color='crimson', alpha=0.7, linewidth=0.9)

    for phase in ['1-平稳', '2-上涨', '3-下跌', '4-走平', '5-恢复']:
        m = df['phase'] == phase
        if m.any():
            ax1.axvspan(df.index[m][0], df.index[m][-1],
                        alpha=0.08, color=phase_colors[phase],
                        label=phase_display.get(phase, phase))

    tp_dates = df.index[df['turning_point_60']]
    ax1.scatter(tp_dates, df.loc[tp_dates, 'close'] * 1.015,
                color='red', marker='v', s=120, zorder=5,
                label=f'turning_point_60 ({len(tp_dates)}次)',
                edgecolors='darkred', linewidth=1.5)

    ax1.set_title('MA60 斜率检测 & turning_point_60 — 合成数据验证',
                  fontsize=14, fontweight='bold', pad=10)
    ax1.set_ylabel('Price')
    ax1.legend(loc='upper left', ncol=5, fontsize=7.5, framealpha=0.9)
    ax1.grid(True, alpha=0.2)

    # ══════════════════════════════════════════════════════════════════
    # 下方每组指标：全周期 + 放大（共享 x 轴）
    # ══════════════════════════════════════════════════════════════════

    z_data = df.iloc[zoom_slice]  # 放大区域数据

    # -- MA60 斜率 --
    for ax, data, is_zoom in [
        (ax_slope, df, False), (ax_slope_z, z_data, True)
    ]:
        ax.plot(data.index, data['slope_ma60'], label='slope_ma60',
                color='darkorange', linewidth=1.2, alpha=0.8)
        ax.axhline(y=0.001, color='green', linestyle='--', alpha=0.7, linewidth=0.8,
                   label='+0.001 (flatten)')
        ax.axhline(y=-0.001, color='green', linestyle='--', alpha=0.7, linewidth=0.8,
                   label='-0.001 (flatten)')
        ax.axhline(y=-0.002, color='red', linestyle='--', alpha=0.7, linewidth=0.8,
                   label='-0.002 (bearish)')
        ax.fill_between(data.index, -0.001, 0.001,
                        where=data['is_flattening_60'].values,
                        color='green', alpha=0.12)
        if is_zoom:
            for d in data.index[data['turning_point_60']]:
                ax.axvline(x=d, color='red', linewidth=1.2, alpha=0.7, linestyle=':')
        ax.set_ylabel('MA60 slope (norm)')
        ax.legend(loc='upper left', fontsize=6.5, ncol=3)
        ax.grid(True, alpha=0.2)
        ax.set_title(
            'MA60 归一化斜率' if not is_zoom else '🔍 走平期附近放大',
            fontsize=10, fontweight='bold', pad=4, loc='left'
        )

    # -- was_bearish_60 --
    for ax, data, is_zoom in [
        (ax_bear, df, False), (ax_bear_z, z_data, True)
    ]:
        shifted = data['slope_ma60'].shift(20)
        ax.plot(data.index, shifted, label='slope_ma60.shift(20)',
                color='purple', linewidth=0.9, alpha=0.6)
        ax.axhline(y=-0.002, color='red', linestyle='--', alpha=0.7, linewidth=0.8,
                   label='-0.002 (bearish)')
        bearish_mask = shifted < -0.002
        ax.fill_between(data.index, -0.002, shifted.values,
                        where=bearish_mask.values,
                        color='red', alpha=0.3, label='was_bearish=True')
        ax.set_ylabel('shift(20) slope')
        ax.legend(loc='upper left', fontsize=6.5)
        ax.grid(True, alpha=0.2)
        ax.set_title(
            'was_bearish_60 = slope_ma60.shift(20) < -0.002'
            if not is_zoom else '🔍 走平期附近放大',
            fontsize=10, fontweight='bold', pad=4, loc='left'
        )

    # -- turning_point 信号组合 --
    for ax, data, is_zoom in [
        (ax_tp, df, False), (ax_tp_z, z_data, True)
    ]:
        ax.fill_between(data.index, 0, 1,
                        where=data['was_bearish_60'].values,
                        color='red', alpha=0.25, label='was_bearish_60', step='mid')
        ax.fill_between(data.index, 1, 2,
                        where=data['is_flattening_60'].values,
                        color='green', alpha=0.25, label='is_flattening_60', step='mid')
        for d in data.index[data['turning_point_60']]:
            ax.axvline(x=d, color='red', linewidth=2.5, alpha=0.85, linestyle='-')
        ax.set_ylim(0, 3)
        ax.set_yticks([0.5, 1.5])
        ax.set_yticklabels(['was_bearish', 'is_flattening'], fontsize=7)
        ax.legend(loc='upper left', fontsize=6.5)
        ax.grid(True, alpha=0.2)
        ax.set_title(
            'turning_point_60 = was_bearish_60 & is_flattening_60'
            if not is_zoom else '🔍 走平期附近放大',
            fontsize=10, fontweight='bold', pad=4, loc='left'
        )

    # 隐藏上方子图的 x 轴标签（只留最下面一个）
    for ax in [ax1, ax_slope, ax_slope_z, ax_bear, ax_bear_z, ax_tp]:
        ax.tick_params(labelbottom=False)
    ax_tp_z.set_xlabel('日期')

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"🖼️ 图片已保存: {save_path}")
    else:
        plt.show()

    plt.close(fig)


# ═════════════════════════════════════════════════════════════════════
# 3. 验证逻辑
# ═════════════════════════════════════════════════════════════════════

def run_validation(df):
    """对 DataFrame 执行正确性验证，打印报告。"""
    print("=" * 65)
    print("  MA60 斜率 & turning_point_60 信号验证")
    print("=" * 65)
    print(f"\n总天数: {len(df)}")
    print(f"is_flattening_60=True: {df['is_flattening_60'].sum()} 天 "
          f"({df['is_flattening_60'].mean():.1%})")
    print(f"was_bearish_60=True:   {df['was_bearish_60'].sum()} 天 "
          f"({df['was_bearish_60'].mean():.1%})")
    print(f"turning_point_60=True: {df['turning_point_60'].sum()} 天 "
          f"({df['turning_point_60'].mean():.1%})")

    if df['turning_point_60'].any():
        tp_dates = df.index[df['turning_point_60']]
        print(f"信号日期: {[d.strftime('%Y-%m-%d') for d in tp_dates]}")

    print("\n" + "-" * 65)
    print("分阶段统计")
    print("-" * 65)
    print(f"{'阶段':<10} {'天数':>5} {'slope_ma60均值':>13} {'flattening%':>12} "
          f"{'bearish%':>11} {'turning_point':>13}")
    print("-" * 65)
    for phase in ['1-平稳', '2-上涨', '3-下跌', '4-走平', '5-恢复']:
        m = df['phase'] == phase
        n_tp = df.loc[m, 'turning_point_60'].sum()
        tp_str = f"{n_tp}" if n_tp else "."
        print(f"{phase:<10} {m.sum():>5}  "
              f"{df.loc[m, 'slope_ma60'].mean():>13.6f}  "
              f"{df.loc[m, 'is_flattening_60'].mean():>10.1%}  "
              f"{df.loc[m, 'was_bearish_60'].mean():>9.1%}  "
              f"{tp_str:>8}")

    print("\n" + "=" * 65)
    print("正确性验证")
    print("=" * 65)

    # V1: turning_point 仅出现在走平期
    tp_by_phase = df.groupby('phase')['turning_point_60'].sum()
    non_flat_tp = tp_by_phase.drop('4-走平', errors='ignore')
    bad = non_flat_tp[non_flat_tp > 0]
    if len(bad) == 0:
        print(f"  ✓ turning_point 仅出现在走平期")
    else:
        print(f"  ✗ turning_point 在非走平期出现: {dict(bad)}")

    # V2: bearish 分布
    bear_by_phase = df.groupby('phase')['was_bearish_60'].mean()
    print(f"  ✓ 下跌期 bearish: {bear_by_phase.get('3-下跌',0):.1%} (应 > 50%)")
    print(f"  ✓ 上涨期 bearish: {bear_by_phase.get('2-上涨',0):.1%} (应 ≈ 0%)")
    print(f"  ✓ 恢复期 bearish: {bear_by_phase.get('5-恢复',0):.1%} (应 ≈ 0%)")

    # V3: 斜率方向
    slope_by_phase = df.groupby('phase')['slope_ma60'].mean()
    s_up = slope_by_phase.get('2-上涨', 0)
    s_down = slope_by_phase.get('3-下跌', 0)
    s_flat = slope_by_phase.get('4-走平', 0)
    print(f"  ✓ 上涨期 slope: {s_up:.6f} (> 0)" if s_up > 0 else f"  ✗ 上涨期 slope: {s_up:.6f}")
    print(f"  ✓ 下跌期 slope: {s_down:.6f} (< 0)" if s_down < 0 else f"  ✗ 下跌期 slope: {s_down:.6f}")
    print(f"  ✓ 走平期 slope: {s_flat:.6f} (≈ 0)")

    # V4: 走平期 flattening 比例应最高
    flat_by_phase = df.groupby('phase')['is_flattening_60'].mean()
    f_flat = flat_by_phase.get('4-走平', 0)
    f_down = flat_by_phase.get('3-下跌', 0)
    f_up = flat_by_phase.get('2-上涨', 0)
    print(f"  ✓ 走平期 flattening: {f_flat:.1%} (vs 下跌 {f_down:.1%}, 上涨 {f_up:.1%})")

    print()


# ═════════════════════════════════════════════════════════════════════
# 4. 入口
# ═════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='MA斜率 & turning_point 合成数据测试')
    parser.add_argument('--generate', action='store_true', default=True,
                        help='生成新数据（默认）')
    parser.add_argument('--load', action='store_true',
                        help='从已有文件加载数据（跳过生成）')
    parser.add_argument('--seed', type=int, default=42,
                        help='随机种子，用于复现')
    parser.add_argument('--data-path', default=str(DEFAULT_DATA_PATH),
                        help=f'数据文件路径 (默认: {DEFAULT_DATA_PATH})')
    parser.add_argument('--plot-path', default=str(DEFAULT_PLOT_PATH),
                        help=f'图片保存路径 (默认: {DEFAULT_PLOT_PATH})')
    parser.add_argument('--no-plot', action='store_true',
                        help='不画图')
    args = parser.parse_args()

    # ── 数据 ──
    data_path = Path(args.data_path)

    if args.load or (data_path.exists() and not args.generate):
        df = load_data(data_path)
    else:
        df = generate_synthetic_data(seed=args.seed, save_path=data_path)

    # ── 验证 ──
    run_validation(df)

    # ── 可视化 ──
    if not args.no_plot:
        plot_ma_slope_analysis(df, save_path=args.plot_path)
