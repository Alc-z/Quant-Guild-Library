# Delta Hedging and Black-Scholes Prices

> 本教材基于 Roman Paolucci 的教学视频 [Delta Hedging and Black-Scholes Prices](https://www.youtube.com/watch?v=jDoLost28tE) 及配套 Jupyter Notebook 整理而成。

---

## 1. 概述

Black-Scholes 模型的推导核心是**连续时间 Delta 对冲**。其思想是：持有一个由股票和期权组成的投资组合，通过持有特定数量的股票，使得投资组合的瞬时变化是**风险中性**的——即消除组合中的随机性。由于组合无风险，其收益率必须等于无风险利率，由此建立了 Black-Scholes 方程，其解即为 Black-Scholes 模型。

然而，在现实中我们无法连续地对冲一个投资组合（交易成本过高）。本教材将探讨：

- Delta 的定义与直觉
- 离散时间（每日）Delta 对冲的实现
- 蒙特卡洛模拟与 P&L 分布
- 对冲频率趋近连续时，P&L 如何收敛到 Black-Scholes 模型价格
- 如何利用对波动率的观点进行交易

---

## 2. Black-Scholes 模型回顾

Black-Scholes 模型是一个为欧式期权定价的数学框架。它假设标的资产的价格遵循**几何布朗运动（GBM）**，具有恒定的漂移率和波动率。

### 2.1 Black-Scholes 公式（欧式看涨期权）

$$
C(S, t) = S N(d_1) - Ke^{-r(T-t)} N(d_2)
$$

其中：

| 符号 | 含义 |
|------|------|
| $S$ | 当前股票价格 |
| $K$ | 行权价 |
| $T$ | 到期时间（年） |
| $r$ | 无风险利率 |
| $\sigma$ | 波动率 |
| $N(\cdot)$ | 标准正态分布的累积分布函数 (CDF) |
| $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma \sqrt{T-t}}$ |
| $d_2 = d_1 - \sigma \sqrt{T-t}$ |

### 2.2 Python 实现

```python
import numpy as np
import scipy.stats as si
import matplotlib.pyplot as plt

def black_scholes_call(S, K, T, r, sigma):
    """计算欧式看涨期权的价格和 Delta"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    delta = si.norm.cdf(d1)  # 看涨期权的 Delta
    return call_price, delta
```

---

## 3. 什么是 Delta？

### 3.1 定义

**Delta（$\Delta$）** 是期权价格对标的资产价格的一阶敏感度：

$$
\Delta = \frac{\partial C}{\partial S}
$$

通俗地说：**当标的资产价格变动 1 单位时期权价格大约变动多少**。Delta 是期权价格关于股票价格变化的线性近似。

### 3.2 Delta 的两种解读

1. **价格敏感度**：如果某期权 Delta = 0.6，股票价格从 $100 涨到 $101，期权价格预计上涨约 $0.60。
2. **到期实值概率的近似**：Delta 也常被用作期权到期时处于实值状态（In-the-Money）的概率近似。

### 3.3 Delta 与参数的关系

```python
import ipywidgets as widgets
from ipywidgets import interactive

def update(K=100, T=1, r=0.05, sigma=0.2):
    S_range = np.linspace(50, 150, 100)
    prices = []
    deltas = []
    
    for s in S_range:
        price, delta = black_scholes_call(s, K, T, r, sigma)
        prices.append(price)
        deltas.append(delta)
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    ax1.plot(S_range, prices, 'b-', label='Option Price')
    ax2.plot(S_range, deltas, 'r-', label='Delta')
    
    ax1.set_xlabel('Stock Price (S)')
    ax1.set_ylabel('Option Price', color='b')
    ax2.set_ylabel('Delta', color='r')
    
    ax1.tick_params(axis='y', colors='b')
    ax2.tick_params(axis='y', colors='r')
    
    plt.title('Black-Scholes Option Pricing & Delta')
    plt.show()

interactive_plot = interactive(update, 
                               K=widgets.FloatSlider(min=50, max=150, step=1, value=100, description='K'),
                               T=widgets.FloatSlider(min=0.1, max=5, step=0.1, value=1, description='T'),
                               r=widgets.FloatSlider(min=0, max=0.2, step=0.01, value=0.05, description='r'),
                               sigma=widgets.FloatSlider(min=0.05, max=1, step=0.05, value=0.2, description='sigma'))
interactive_plot
```

**观察：**
- 当剩余时间很长时，Delta 曲线平滑，平值（ATM）附近 Delta 约 0.5
- 当临近到期时，Delta 曲线趋近于一个阶跃函数（hockey stick 形状）
- 在行权价附近，Delta 变化最剧烈——这也是不确定性最大的区域

---

## 4. 几何布朗运动 (Geometric Brownian Motion)

Black-Scholes 模型假设股票价格遵循几何布朗运动：

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

其中：
- $\mu$ = 漂移率（预期收益率）
- $\sigma$ = 波动率
- $dW_t$ = 维纳过程（布朗运动）

### 4.1 GBM 模拟函数

```python
def simulate_gbm(S0, mu, sigma, T, dt=1/252):
    """
    模拟几何布朗运动价格路径
    
    参数:
        S0: 初始价格
        mu: 漂移率
        sigma: 波动率
        T: 时间跨度（年）
        dt: 时间步长（默认 1/252，即每日）
    """
    n_steps = int(T / dt)
    t = np.linspace(0, T, n_steps)
    W = np.random.standard_normal(size=n_steps)
    W = np.cumsum(W) * np.sqrt(dt)  # 维纳过程
    S_t = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)
    return S_t, t
```

### 4.2 示例路径

```python
S0, K, T, r, sigma, mu = 100, 100, 1, 0.05, 0.2, 0.08

S_t, t = simulate_gbm(S0, mu, sigma, T)

plt.figure(figsize=(10, 5))
plt.plot(t, S_t, label="Stock Price (GBM)")
plt.title("Stock Price Path")
plt.xlabel("Time (Years)")
plt.ylabel("Stock Price")
plt.legend()
plt.show()
```

每次运行都会得到一条不同的路径——这正是 GBM 的随机性体现。

---

## 5. Delta 对冲策略

### 5.1 核心思想

假设我们**卖出一份欧式看涨期权**（Short Call）：

- 卖出看涨期权 → Delta 为负（期权价格上涨对我们不利）
- 为对冲风险，我们买入 $\Delta$ 份股票
- 当股票上涨时，股票端盈利弥补期权端的亏损
- 当股票下跌时，股票端亏损被期权端的盈利抵消

**关键问题**：期权价格和 Delta 都是非线性函数。当股价偏离初始对冲点时，线性近似的误差会越来越大。因此我们必须**不断重新平衡（rebalance）** 对冲头寸。

> 这正是一开始提到的 Black-Scholes 方程推导中"连续时间对冲"的核心论证。

### 5.2 离散时间 Delta 对冲模拟

```python
def delta_hedge_simulation(S0, K, T, r, sigma, mu, dt=1/252):
    """
    模拟卖出看涨期权的 Delta 对冲策略
    
    策略步骤：
    1. 按 Black-Scholes 价格卖出一份欧式看涨期权
    2. 买入 Delta 份股票进行对冲
    3. 在期权存续期内每日重新平衡
    4. 到期时计算最终 P&L
    """
    # 生成 GBM 路径
    S_t, t = simulate_gbm(S0, mu, sigma, T, dt)
    
    # 计算初始期权价格和 Delta
    call_price, delta = black_scholes_call(S0, K, T, r, sigma)
    
    # 初始现金头寸：收到期权费 - 买入股票的成本
    initial_cash = call_price - delta * S0
    portfolio_value = initial_cash
    deltas = [delta]
    
    # 逐日重新平衡
    for i in range(1, len(S_t)):
        tau = T - i * dt  # 剩余时间
        call_price, delta = black_scholes_call(S_t[i], K, tau, r, sigma)
        deltas.append(delta)
        
        # 投资组合价值 = 股票头寸 + 现金头寸（按无风险利率增值）
        portfolio_value = delta * S_t[i] + initial_cash * np.exp(r * i * dt)

    # 最终 P&L = 组合价值 - 期权到期支付（卖出看涨期权的义务）
    final_pnl = portfolio_value - max(S_t[-1] - K, 0)
    return S_t, final_pnl, deltas, t
```

### 5.3 单次模拟示例

```python
S0, K, T, r, sigma, mu = 100, 100, 1, 0.05, 0.2, 0.08

call_price, delta = black_scholes_call(S0, K, T, r, sigma)
print(f'Option Price: {call_price:.2f} | Initial Delta: {delta:.2%}')

S_t, final_pnl, deltas, t = delta_hedge_simulation(S0, K, T, r, sigma, mu)

plt.figure(figsize=(10, 5))
plt.plot(t, S_t, label="Stock Price (GBM)")
plt.axhline(K, color='r', linestyle="--", label="Strike Price")
plt.title("Stock Price Path and Delta Hedging")
plt.xlabel("Time (Years)")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

print(f"Final P&L from Delta Hedging: {final_pnl:.2f}")
```

**输出示例：**
```
Option Price: 10.45 | Initial Delta: 64.00%
Final P&L from Delta Hedging: 44.05
```

每次运行结果不同——有时正、有时负。这正是离散对冲的不完美性导致的结果。

---

## 6. 蒙特卡洛模拟分析

### 6.1 多次模拟的 P&L 分布

```python
n_simulations = 1000
pnl_results = []

for _ in range(n_simulations):
    _, final_pnl, _, _ = delta_hedge_simulation(S0, K, T, r, sigma, mu)
    pnl_results.append(final_pnl)

plt.figure(figsize=(10, 5))
plt.hist(pnl_results, bins=30, alpha=0.75, color="blue", edgecolor="black")
plt.axvline(np.mean(pnl_results), color='r', linestyle="--", 
            label=f"Mean P/L: {np.mean(pnl_results):.2f}")
plt.title("Distribution of P&L from (Daily) Delta Hedging")
plt.xlabel("Final P&L")
plt.ylabel("Frequency")
plt.legend()
plt.show()

print(f"Average P&L over {n_simulations} simulations: {np.mean(pnl_results):.2f}")
```

**核心发现**：每日对冲时，平均 P&L 接近 Black-Scholes 模型价格（10.45），但并不完全相等。

### 6.2 收敛到理论价格

Black 和 Scholes (1973) 论文的核心论证指出：**当对冲频率趋近连续时，对冲的期望 P&L 将收敛到 Black-Scholes 模型价格**。

```python
def delta_hedge_simulation_hf(S0, K, T, r, sigma, mu, dt=1/1000):
    """更精细的时间步长（接近连续对冲）"""
    S_t, t = simulate_gbm(S0, mu, sigma, T, dt)
    
    call_price, delta = black_scholes_call(S0, K, T, r, sigma)
    initial_cash = call_price - delta * S0
    portfolio_value = initial_cash
    
    for i in range(1, len(S_t)):
        tau = T - i * dt
        call_price, delta = black_scholes_call(S_t[i], K, tau, r, sigma)
        portfolio_value = delta * S_t[i] + initial_cash * np.exp(r * i * dt)

    final_pnl = portfolio_value - max(S_t[-1] - K, 0)
    return S_t, final_pnl, deltas, t

# 更高频率对冲
n_simulations = 100
pnl_results_hf = []

for _ in range(n_simulations):
    _, final_pnl, _, _ = delta_hedge_simulation_hf(S0, K, T, r, sigma, mu, dt=1/1000)
    pnl_results_hf.append(final_pnl)

print(f"Average P&L (high freq): {np.mean(pnl_results_hf):.2f}")
print(f"Theoretical BS Price: {black_scholes_call(S0, K, T, r, sigma)[0]:.2f}")
```

**结果**：随着对冲频率提高（`dt` 减小），平均 P&L 越来越接近 Black-Scholes 模型的理论价格。

### 6.3 直觉理解

- **连续时间 Delta 对冲** → 组合完全无风险 → 只能赚取无风险利率 → P&L = 期权费
- **离散时间对冲** → 存在"对冲误差"（gamma 风险）→ P&L 围绕理论价格波动
- 对冲频率越高，方差越小，均值越接近理论价格

**一句话总结**：进行 Delta 对冲的期望 P&L 就是收取的期权费本身。我们并不能通过单纯的对冲获得超额收益。

---

## 7. 实际交易应用：基于波动率观点的套利

### 7.1 核心思想

虽然单纯的对冲只能赚取期权费，但如果我们对模型参数（尤其是波动率）有自己的观点，就可以利用 Delta 对冲构建**统计套利**策略。

**具体做法**：

1. **市场隐含波动率**：假设 Nvidia 目前交易在 40% 隐含波动率
2. **我们的观点**：预期未来实现的波动率将显著低于 40%（例如 10-20%）
3. **策略**：按市场隐含波动率（40%）定价卖出期权，但实际的股价路径按我们预期的波动率（10%）生成

```python
def delta_hedge_simulation_with_vol_view(S0, K, T, r, sigma_market, mu, 
                                          vol_realized, dt=1/500):
    """
    基于波动率观点的 Delta 对冲模拟
    
    参数:
        sigma_market: 市场隐含波动率（用于定价）
        vol_realized: 我们预期的实际波动率（用于路径生成）
    """
    # 按市场隐含波动率定价（收取期权费）
    call_price, delta = black_scholes_call(S0, K, T, r, sigma_market)
    
    # 按我们预期的实际波动率生成路径
    S_t, t = simulate_gbm(S0, mu, vol_realized, T, dt)
    
    # 初始头寸
    initial_cash = call_price - delta * S0
    portfolio_value = initial_cash
    
    # 逐日重新平衡
    for i in range(1, len(S_t)):
        tau = T - i * dt
        call_price, delta = black_scholes_call(S_t[i], K, tau, r, sigma_market)
        portfolio_value = delta * S_t[i] + initial_cash * np.exp(r * i * dt)

    final_pnl = portfolio_value - max(S_t[-1] - K, 0)
    return S_t, final_pnl, deltas, t
```

### 7.2 模拟验证

```python
n_simulations = 1000
pnl_results_vol = []

for _ in range(n_simulations):
    _, final_pnl, _, _ = delta_hedge_simulation_with_vol_view(
        S0=100, K=100, T=1, r=0.05, 
        sigma_market=0.40,   # 市场隐含波动率 40%
        mu=0.08, 
        vol_realized=0.10   # 实际实现波动率 10%
    )
    pnl_results_vol.append(final_pnl)

plt.figure(figsize=(10, 5))
plt.hist(pnl_results_vol, bins=30, alpha=0.75, color="green", edgecolor="black")
plt.axvline(np.mean(pnl_results_vol), color='r', linestyle="--",
            label=f"Mean P/L: {np.mean(pnl_results_vol):.2f}")
plt.title("P&L Distribution: Selling Options Priced at 40% IV, Realizing 10% RV")
plt.xlabel("Final P&L")
plt.ylabel("Frequency")
plt.legend()
plt.show()

print(f"Average P&L: {np.mean(pnl_results_vol):.2f}")
```

### 7.3 实证结论

当实际实现的波动率低于市场隐含波动率时，Delta 对冲策略的平均 P&L 显著高于期权费本身。这意味着：

> 我们以高于实际价值的价格**卖出**期权，通过对冲锁定利润。

反过来，如果我们认为波动率会被低估，可以**买入**期权并进行 Delta 对冲。

**波动率风险溢价（Volatility Risk Premium）**：
- 大量学术论文（包括 AQR 的早期研究）证明市场上存在 volatility risk premium
- 隐含波动率通常系统性高于已实现波动率
- 这意味着卖出波动率并 Delta 对冲是一种统计上有正期望值的策略

---

## 8. 关键要点总结

| 概念 | 要点 |
|------|------|
| **Delta** | 期权价格对标的资产价格的一阶敏感度，也近似到期实值概率 |
| **Delta 对冲** | 通过持有 $\Delta$ 份标的资产来抵消期权的价格波动 |
| **重新平衡** | 由于 Delta 非线性变化，需要持续调整头寸 |
| **收敛性** | 对冲频率趋近连续时，期望 P&L 收敛到 Black-Scholes 理论价格 |
| **离散对冲** | 产生 gamma 风险，P&L 有分布，频率越高方差越小 |
| **统计套利** | 对波动率等参数有观点时，可通过 Delta 对冲实现正期望收益 |
| **波动率风险溢价** | IV > RV 是市场常态，相关策略具有正期望值 |

### 交易策略的核心洞见

只要你认为价格路径的实现参数集与市场定价所用的参数集不同，就可以通过 Delta 对冲来利用这种观点：

- **认为波动率偏高** → 卖出期权 + Delta 对冲
- **认为波动率偏低** → 买入期权 + Delta 对冲
- 长期执行这类策略，累积的期望 P&L 将为正是

---

## 9. 延伸阅读

- [Black-Scholes 方程推导视频](https://www.youtube.com/watch?v=2iClLEfXuqA)
- [Black-Scholes 方程推导文章](https://medium.com/swlh/deriving-the-black-scholes-model-5e518c65d0bc)
- [市场隐含波动率视频](https://www.youtube.com/watch?v=VzieTIsBaHM)
- [Quant Guild GitHub](https://github.com/Quant-Guild)
- [Quant Guild Medium Blog](https://medium.com/quant-guild)

---

*本教材由 Roman Paolucci 的视频讲座及配套 Jupyter Notebook 整理而成。*
