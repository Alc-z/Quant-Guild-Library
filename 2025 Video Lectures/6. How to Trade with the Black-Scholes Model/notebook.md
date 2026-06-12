# How to Trade Options with the Black-Scholes Model

> 一份结合教学视频字幕与代码实践的综合教材
>
> 基于 Roman Paolucci (Quant Guild) 的教学视频《How to Trade Options with the Black-Scholes Model》
> 以及配套 Jupyter Notebook 代码示例

---

## 目录

1. [模型辅助决策：Black-Scholes 的正确用法](#1-模型辅助决策black-scholes-的正确用法)
2. [数学模型基础](#2-数学模型基础)
3. [相对定价：化苹果为苹果](#3-相对定价化苹果为苹果)
4. [隐含波动率：统一的定价标尺](#4-隐含波动率统一的定价标尺)
5. [Delta：最被误解的希腊字母](#5-delta最被误解的希腊字母)
6. [实盘市场中的相对定价](#6-实盘市场中的相对定价)
7. [实盘中的 Delta 应用](#7-实盘中的-delta-应用)
8. [利用模型进行交易：计算交易优势 (Edge)](#8-利用模型进行交易计算交易优势-edge)
9. [模拟权益曲线：在模型假设下评估策略](#9-模拟权益曲线在模型假设下评估策略)
10. [模型定价的固有问题与局限性](#10-模型定价的固有问题与局限性)
11. [总结与关键要点](#11-总结与关键要点)

---

## 1. 模型辅助决策：Black-Scholes 的正确用法

### 1.1 核心理念

**交易的本质是关于 positioning（仓位管理）和 survival（生存），而非预测。**

- 市场中没有水晶球（crystal ball），不存在价格预测
- Black-Scholes 模型不是一个预测模型，它无法告诉你未来股价会涨还是会跌
- 模型的真正用途是作为 **决策过滤器（filter for decision-making）**，帮助交易者在不确定性中做出相对理性的判断

### 1.2 常见的误解

很多人批评 Black-Scholes 模型"没用"，因为它什么也预测不了。这种批评本身没有错——模型确实不用于预测。但它的价值在于：

> **"It is a model used to explain and understand, effectively as a filter for decision-making, relative pricing, and probability based on what the market is currently thinking."**

也就是说，Black-Scholes 模型帮助我们理解市场当前在"想什么"，提供一个将不同合约放在同一尺度下比较的框架。

### 1.3 理论与实践之间的桥梁

本教材将完成以下目标：

1. **课堂理论** — 理解模型的数学基础以及它在现实中为何看似失效
2. **实盘市场** — 借助 Interactive Brokers 的 Trader Workstation，观察真实的期权合约，理解理论如何应用于实践

---

## 2. 数学模型基础

### 2.1 Black-Scholes 方程

Black-Scholes 模型的核心假设是标的资产价格遵循 **几何布朗运动 (Geometric Brownian Motion)**：

$$\frac{dS_t}{S_t} = \mu dt + \sigma dW_t$$

其中：
- $S_t$ — 标的资产在时间 $t$ 的价格
- $\mu$ — 漂移率（预期收益率）
- $\sigma$ — 波动率
- $dW_t$ — 维纳过程（布朗运动）

### 2.2 Black-Scholes 欧式看涨期权定价公式

在上述假设下，求解 Black-Scholes 偏微分方程得到欧式看涨期权的封闭解：

$$C = S_t \Phi(d_1) - Ke^{-rt} \Phi(d_2)$$

其中 $\Phi(x)$ 是标准正态分布的累积分布函数：

$$\Phi(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}} e^{\frac{-s^2}{2}} ds$$

中间变量 $d_1$ 和 $d_2$ 定义为：

$$d_1 = \frac{\ln\left(\frac{S_t}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)t}{\sigma \sqrt{t}}$$

$$d_2 = d_1 - \sigma \sqrt{t}$$

#### 公式参数的详细解释

| 参数 | 名称 | 含义与说明 |
|------|------|-----------|
| $C$ | **看涨期权价格** (Call Price) | 公式的输出结果，表示欧式看涨期权在当前时刻的理论公允价值 |
| $S_t$ | **标的资产现价** (Spot Price) | 当前时刻标的资产（如股票）的市场价格 |
| $K$ | **行权价** (Strike Price) | 期权合约约定的未来买入标的资产的价格。期权是否实值取决于 $S_t$ 与 $K$ 的对比：$S_t > K$ 为实值 (ITM)，$S_t \approx K$ 为平值 (ATM)，$S_t < K$ 为虚值 (OTM) |
| $r$ | **无风险利率** (Risk-free Rate) | 通常使用同期限国债收益率，用于对未来现金流进行折现 |
| $\sigma$ | **波动率** (Volatility) | 标的资产年化收益率的标准差，衡量价格的不确定性 |
| $t$ | **剩余到期时间** (Time to Maturity) | 以年为单位，如 15 天 = $15/252$ |

#### 公式的结构含义

Black-Scholes 公式可以理解为：

> **看涨期权价格 = 预期收到标的资产的现值 — 预期支付行权价的现值**

具体拆解为两个部分：

**第一部分（被减数）：$S_t \Phi(d_1)$**

- 含义：**期权被行权时，预期收到的标的资产的当前价值**
- $S_t$ 是标的资产当前价格
- $\Phi(d_1)$ 是一个概率权重，它不仅包含行权的概率，还**根据股价水平进行了调整**——因为当期权实值时，股价越高，收到的资产价值也越大
- 因此这一项可以理解为：在风险中性世界里，**"行权发生时，以股价为权重的条件期望"的现值**

**第二部分（减数）：$Ke^{-rt} \Phi(d_2)$**

- 含义：**期权被行权时，预期支付的行权价的当前价值**
- $Ke^{-rt}$ 是行权价 $K$ 按无风险利率折现到当前的价值（即行权价的现值）
- $\Phi(d_2)$ 是**风险中性下的行权概率**（即期权到期实值的概率），在风险中性测度下 $P(S_T > K) = \Phi(d_2)$
- 因此这一项可以理解为：**"行权时需支付的行权价 × 行权概率"的现值**

**两者之差**即为：你预期会获得的资产的价值，减去你为获得它而必须支付的成本，得到的是这张期权合约在当前时点的合理价值。

#### 直觉理解

- 如果你持有一张看涨期权，你有**权利**在到期时以 $K$ 的价格买入标的资产
- 只有当到期股价 $S_T > K$ 时你才会行权（否则放弃）
- 公式中 $S_t \Phi(d_1)$ 衡量的是 **"你将会收到的东西的期望价值"**
- $Ke^{-rt} \Phi(d_2)$ 衡量的是 **"你将要付出的东西的期望价值"**
- 二者的差就是这张期权的公允价值

> 这种 "期望价值之差" 的视角，是所有风险中性定价的核心思想。

### 2.3 Python 实现

Black-Scholes 模型的代码实现非常简洁，使用 `scipy.stats.norm` 计算累积正态分布：

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, sigma, r, t):
    """
    计算欧式看涨期权的 Black-Scholes 理论价格
    
    参数:
        S     — 当前标的资产价格 (spot price)
        K     — 行权价 (strike price)
        sigma — 波动率 (volatility)
        r     — 无风险利率 (risk-free rate)
        t     — 到期时间（年化）(time to maturity)
    """
    d1 = (np.log(S/K) + (r + ((sigma**2)/2))*t) / (sigma * np.sqrt(t))
    d2 = d1 - (sigma * np.sqrt(t))
    C = S * norm.cdf(d1) - K * np.exp(-r*t) * norm.cdf(d2)
    return C

# 示例：平价期权 (at-the-money) 定价
# S=100, K=100, sigma=30%, r=5%, t=1年
print("Call Price:", black_scholes_call(100, 100, .3, .05, 1))
```

输出：
```
Call Price: 14.231254785985819
```

> 即：在给定参数下，一张行权价为 100、剩余期限 1 年的平值看涨期权，理论价格为约 14.23 美元。

---

## 3. 相对定价：化苹果为苹果

### 3.1 问题的提出

假设市场上有两个平值（at-the-money）看涨期权：

| 合约 | 标的现价 | 到期时间 | 价格 |
|------|---------|---------|------|
| Google 平值看涨 | ~$340 | 15 天 | $11 |
| Nvidia 平值看涨 | ~$214 | 15 天 | $11 |

**问题：哪个更贵？**

如果只看价格，两个都是 $11，似乎一样贵。但这显然不合理——Google 和 Nvidia 是两家完全不同的公司，股价规模（spot size）不同，波动特征也不同。这就是典型的 **apples to oranges（苹果与橘子）** 问题。

### 3.2 模型提供的解决方案

Black-Scholes 模型提供了一个 **反向转换** 的思路：

> 市场价格 → 通过模型反推 → **隐含波动率 (Implied Volatility)**

尽管市场并不真正遵循几何布朗运动，但 Black-Scholes 模型作为一个 **标准化的转换函数**，可以将不同标的、不同行权价的期权价格统一转换为波动率这一标尺，从而实现在同一维度上的比较。

### 3.3 核心认识

在这个例子中：
- Google 平值期权的 **隐含波动率较低**
- Nvidia 平值期权的 **隐含波动率较高**

这意味着市场预期 Nvidia 在未来 15 天内会有更大的价格波动（更高不确定性），因此 Nvidia 的合约 **相对更贵**——尽管它们的名义价格相同。

> 如果没有模型，你在交易终端上光看价格，根本无法获取这一层面的信息。

---

## 4. 隐含波动率：统一的定价标尺

### 4.1 IV 的本质

隐含波动率 (Implied Volatility, IV) 是市场对**未来波动性**的当前定价，它反映的是：

> **此时此刻** 市场参与者对这只股票未来价格波动幅度的集体预期

关键点：隐含波动率 **不** 是一个稳定的预测值，它随时可能变化。

### 4.2 IV 的动态特性

- Nvidia 某天从 208 涨到 218，又跌回 208-213，隐含波动率会随价格大幅波动
- 所有合约每秒钟都在重新定价（repricing）
- 这是对模型最大的误解来源——误以为模型有某种预测能力

> **"No. It is telling you what is going on in the market right now."**

隐含波动率告诉你的是 **市场现在正在发生什么**，而不是一小时、一天或一周之后会发生什么。

---

## 5. Delta：最被误解的希腊字母

### 5.1 Delta 的理论定义

在 Black-Scholes 框架下，看涨期权的 Delta 定义为：

$$\Delta_{call} = \frac{\partial C}{\partial S} = \Phi(d_1)$$

从数学上看，Delta 等于 $\Phi(d_1)$——标准正态累积分布函数在 $d_1$ 处的值。这个值被**粗略地**解释为期权实值（in-the-money）到期的概率。

### 5.2 课堂模拟：Delta 作为概率的局限

以下代码模拟了在几何布朗运动假设下，一个 15 天期平值 Nvidia 看涨期权的到期收益：

```python
import matplotlib.pyplot as plt
import qfin as qf

# 按照几何布朗运动模拟标的价格路径
path = qf.simulations.GeometricBrownianMotion(100, 0.05, .3, 1/252, 1)

# 绘制价格路径与行权价
plt.title("Terminal Value of an Option Contract")
plt.hlines(100, 0, 252, label='Strike', color='orange')
plt.plot(path.simulated_path, label='Price Path', color='white')
if max(path.simulated_path[-1] - 100, 0) == 0:
    plt.vlines(252, path.simulated_path[-1], 100, color='red', label="P/L")
else:
    plt.vlines(252, 100, path.simulated_path[-1], color='green', label="P/L")
plt.style.use('dark_background')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

# 打印权利金与盈亏
print("Premium at t=0:", black_scholes_call(100, 100, .3, .05, 1))
print("P/L:", max(path.simulated_path[-1] - 100, 0) - black_scholes_call(100, 100, .3, .05, 1))
```

模拟显示：
- 初始 Delta 为 0.53（平值期权）
- 随着模拟路径数量增加，实值到期的比例趋向于 53%（大数定律）
- 但这是 **在模型假设下** 的渐进收敛，在现实市场中毫无意义

### 5.3 现实中 Delta 为什么不是概率

现实市场与模拟世界的关键区别：

| 课堂模拟 | 现实市场 |
|---------|---------|
| 参数固定不变 | 波动率、价格不断变化 |
| 大数定律成立 | 市场不具备平稳性（non-stationary） |
| 路径独立生成 | 价格存在跳跃和趋势 |
| 概率是稳定的 | Delta 每秒钟都在重新定价 |

**真实案例**：
- 你买入一个 Delta = 0.30 的看涨期权（理论上 30% 概率实值到期）
- 如果标的股价在未来几小时内暴跌 3%
- 这个 Delta 会迅速降到 0.10 甚至更低
- 到期的实值概率随之大幅下降

> **"The probabilities are amorphous."** —— 概率是"无定形"的，时刻都在变化。

### 5.4 Delta 的正确用法

Delta 的本质是一个 **对冲比率 (hedge ratio)**——它告诉你在 Black-Scholes 框架下，为了对冲期权价格的小幅变动需要持有多少标的资产。

在交易实践中，Delta 更重要的用途是作为一个 **相对度量工具 (relative measure)**：

- 不同行权价的合约之间的 Delta 值提供了一个一致的比较标准
- 与名义价格不同，Delta 在不同的标的上具有可比性
- 帮助你理解在当前市场条件下，某个行权价相对于平值合约的"位置"

---

## 6. 实盘市场中的相对定价

### 6.1 在 Trader Workstation 中观察期权链

打开 Interactive Brokers 的 Trader Workstation：

1. 在搜索栏中输入标的代码（如 GOOG 或 NVDA）
2. 选择期权合约（Option Trader）
3. 选择特定的到期日

### 6.2 比较不同标的的期权价格

**Google 期权链观察**：
- 选择约 16 天到期的平值看涨期权
- 行权价 345，价格约 $11.45（即每份合约 $1,145）

**Nvidia 期权链观察**：
- 相同到期日，平值看涨期权
- 价格约 $6.90-$7.00（即每份合约 $690-$700）

**哪个更贵？**

如果只看名义价格，Google 更贵。但在期权链的右上角，我们可以看到 **平值隐含波动率 (ATM IV)**：
- Google: ~40.8%
- Nvidia: ~40.3%

以波动率为标尺，Google 的合约 **相对更贵**——市场对 Google 未来波动的定价略高于 Nvidia。

### 6.3 关键认识

> 隐含波动率是动态的——如果价格跳空上涨或下跌，波动率会随之调整。原来更贵的可能变便宜，更便宜的也可能变贵。

这就是模型的**相对度量**本质——它为你提供一个当下决策的参考基准，而不是永恒不变的真理。

---

## 7. 实盘中的 Delta 应用

### 7.1 Delta 作为相对位置的度量

Delta 不仅可以理解为"概率"，更重要的是它在实盘中提供了一种 **相对位置度量**：

假设我们用 30 Delta 的看涨期权作为一个交易标的：

**Nvidia（现价约 $210）**：
- 30 Delta 看涨期权的行权价约在 $222.5（高出当前价格约 $12.5）

**Google（现价约 $346）**：
- 30 Delta 看涨期权的行权价约在 $365（高出当前价格约 $20）

> 同样是 30 Delta，Nvidia 只需要向上 12.5 个点，Google 需要向上 20 个点。

这说明什么？**不同的标的，同样的 Delta 对应着不同的价格区间**。Delta 提供了一个标准化后的比较维度。

### 7.2 实践中的用法

- 你不需要关注期权的名义价格，因为价格本身在不同标的之间不可比
- 使用 Delta 来定位你想要的合约——比如始终交易 30 Delta 的合约
- 通过 Delta 保持策略在不同标的和不同时间上的一致性

---

## 8. 利用模型进行交易：计算交易优势 (Edge)

### 8.1 策略思路

设 $T$ 为一个交易策略，当模型理论价格与做市商报价之间出现理论差异时，买入或卖出期权：

$$\mathbb{E}[T] > 0 \implies \text{Positive P/L Over Time}$$

即：如果期望收益为正，长期执行该策略应能获得正收益。

### 8.2 计算交易 Edge

```python
print("Call Price:", black_scholes_call(100, 100, .3, .05, 1))
print("Market Maker Quote:", "13.43 @ 14.10")
print("Trade Edge:", black_scholes_call(100, 100, .3, .05, 1) - 14.10)
```

输出：
```
Call Price: 14.231254785985819
Market Maker Quote: 13.43 @ 14.10
Trade Edge: 0.13125478598581886
```

在此示例中：
- 模型理论价格：**$14.23**
- 做市商卖价：**$14.10**
- 交易优势 (Edge)：**$0.13**（理论值高于报价）

这意味着按照模型假设，以 $14.10 买入该合约具有正期望收益。

### 8.3 在模型动态下验证 Edge

通过蒙特卡洛模拟验证该策略的期望收益：

```python
premium = 14.10 * 100
pls = []

for i in range(100000):
    path = qf.simulations.GeometricBrownianMotion(100, 0.05, .3, 1/252, 1)
    pls.append(max(path.simulated_path[-1] - 100, 0)*100 - premium)

np.mean(pls)
```

输出：
```
np.float64(87.82994266388759)
```

这意味着在模型假设（GBM）下，每张合约（100股）的期望盈利约为 $87.83。模拟次数越多，结果越趋于稳定（大数定律）。

---

## 9. 模拟权益曲线：在模型假设下评估策略

### 9.1 模拟不同市场条件下的策略表现

以下代码模拟了在 **负漂移率**（$\mu = -50\%$）的市场条件下，持续执行该 Edge 策略的权益曲线：

```python
premium = 14.10 * 100
pls = []

for i in range(100000):
    # 注意：此处 mu = -0.5，表示标的整体趋势下跌
    path = qf.simulations.GeometricBrownianMotion(100, -.5, .3, 1/252, 1)
    pls.append(max(path.simulated_path[-1] - 100, 0)*100 - premium)

plt.title("Trading this Edge Over Time")
plt.plot(np.cumsum(pls), label="Account Equity")
plt.style.use('dark_background')
plt.xlabel('Option Trade')
plt.ylabel('Portfolio Value')
plt.legend()
plt.show()
```

### 9.2 关于权益曲线的重要提醒

> **在复杂、非平稳的现实市场中，这种固定的参数假设几乎必定失效。**

权益曲线在模拟中看起来平滑上升，是因为我们假设：
1. 波动率 $\sigma$ 固定为 30%
2. 漂移率 $\mu$ 固定不变
3. 无跳跃风险（jump risk）
4. 动力学完美符合 GBM

这些都是模型世界中的理想假设，现实市场远为复杂。

---

## 10. 模型定价的固有问题与局限性

Black-Scholes 模型虽有用，但存在显著的固有问题：

### 10.1 参数非平稳性 (Non-stationarity)

> 市场的参数在时间上不是稳定的——今天估计的波动率明天可能完全无效。

- 波动率会随市场情绪、新闻事件、宏观经济变化而剧烈波动
- 历史波动率不能保证未来的波动特征
- 模型假设了恒定的参数，这在现实中不成立

### 10.2 波动率不是常数

- 现实中存在 **波动率微笑 (volatility smile)** 和 **波动率期限结构 (term structure)**
- 不同行权价、不同期限的隐含波动率各不相同
- 模型假设恒定波动率，忽略了波动率的聚集效应（volatility clustering）

### 10.3 没有跳跃 (No Jumps)

- 几何布朗运动的路径是连续的
- 现实市场中存在大量的 **价格跳跃（jumps）**——财报发布、突发事件等
- 跳跃风险无法在 Black-Scholes 框架中对冲

### 10.4 其他问题

- **厚尾分布**：实际收益率分布比正态分布具有更厚的尾部
- **流动性风险**：某些合约可能流动性不足，导致实际成交价偏离理论值
- **交易成本**：频繁对冲会产生显著的交易成本

---

## 11. 总结与关键要点

### 11.1 你必须记住的核心观点

1. **模型不是水晶球** — Black-Scholes 不预测价格，它只是一个 **决策辅助工具**

2. **隐含波动率是相对定价的关键** — 它把不同标的、不同行权价的期权价格转化为统一的比较标尺，使 "苹果与橘子" 变得可比

3. **Delta 是对冲比率，不是概率** — 在现实中，Delta 代表的"到期实值概率"每秒钟都在变化。它是用来做 **相对定位** 的，不是用来做概率预测的

4. **一切都是相对的** — 价格本身在不同标的上不可比，但 Delta 和隐含波动率提供了一致的比较框架

5. **模型是过滤器** — 在不确定性的海洋中，模型帮你过滤出当下的相对信息，辅助你的 **主观或系统化决策**

### 11.2 交易的终极本质

> **"This is poker at best."** —— 交易充其量就是玩扑克。

即使有 Black-Scholes 这样的工具，你玩的依然是一个不完全信息的博弈。模型让你从"盲目下注"变成"有信息依据地决策"，但并不能消除不确定性本身。

### 11.3 All Models Are Wrong, Some Are Useful

> 没有这个模型，你可以抱怨市场不遵循几何布朗运动、模型没有预测能力、Delta 对冲不完美……是的，这些我们都知道。
>
> 但 **没有这个模型，你没有任何具体的相对决策基础**。
>
> *"Without this model, you do not have any relative basis, any concrete relative basis for your decision-making."*

这就是 Black-Scholes 模型在交易中的真正价值。

---

## 附录：代码与资源

### 完整代码文件

本教材所有代码来自配套的 [Black-ScholesTrading.ipynb](Black-ScholesTrading.ipynb) 教学笔记。

### 需要安装的依赖

```bash
pip install numpy scipy matplotlib
```

另外需要 Quant Guild 的自定义库 `qfin`（用于几何布朗运动模拟），可从以下资源获取：

- **Quant Guild Library**: https://github.com/romanmichaelpaolucci/Quant-Guild-Library
- **Quant Guild 官网**: https://quantguild.com
- **高斯菜谱 (The Gaussian Cookbook)**: https://gaussiancookbook.com

### 参考视频

- 原始教学视频: [How to Trade Options with the Black-Scholes Model](https://www.youtube.com/watch?v=1OByexsEJXc)
- 如何交易 Covered Call: [How to Trade the Covered Call](https://youtu.be/iPsPRQlDeTA)
- 如何阅读期权链: [How to Read Options Chains](https://youtu.be/RrRbz6oXwxE)

---

> *"Trading is about positioning and survival. There is no crystal ball."*
