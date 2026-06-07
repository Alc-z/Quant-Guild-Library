# 控制变量法（Control Variates）用于方差缩减

> **主讲:** Roman Paolucci — Quant Guild
> **视频:** [Control Variates for Variance Reduction](https://www.youtube.com/watch?v=Iu_gCD74Y70&t=107s)
> **Notebook:** [GitHub](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/Control%20Variates%20for%20Variance%20Reduction.ipynb)

---

## 目录

1. [为什么需要方差缩减？](#1-为什么需要方差缩减)
2. [什么是控制变量？](#2-什么是控制变量)
3. [控制变量的数学原理](#3-控制变量的数学原理)
4. [最优系数的选择](#4-最优系数的选择)
5. [控制变量如何降低方差](#5-控制变量如何降低方差)
6. [实例：算术布朗运动下的欧式期权定价](#6-实例算术布朗运动下的欧式期权定价)
   - [模型设定](#61-模型设定)
   - [控制变量的选择](#62-控制变量的选择)
   - [Python 实现](#63-python-实现)
   - [结果分析](#64-结果分析)
7. [与前沿文献的联系](#7-与前沿文献的联系)
   - [粗糙波动率模型](#71-粗糙波动率模型)
   - [神经网络近似方法](#72-神经网络近似方法)
8. [总结](#8-总结)

---

## 1. 为什么需要方差缩减？

蒙特卡洛模拟是随机模型中估计量的核心技术。当我们通过模拟来估计某个参数 $\theta$（例如期权价格）时，我们关心估计的**精度**。估计量的标准误差与以下量成正比：

$$
\text{标准误差} \propto \frac{\sigma}{\sqrt{N}}
$$

其中 $\sigma$ 是模拟收益的标准差，$N$ 是模拟次数。

一个自然而然的问题出现了：*如果想要更窄的置信区间，为什么不直接增加 $N$——从 1,000 到 10,000 到 100,000 甚至一百万次模拟？*

答案是**计算成本**。对于许多实际模型，每条模拟路径的生成本身就非常昂贵。简单地增加 $N$ 可能不切实际，或者耗时过长。这就推动了**方差缩减技术**的发展——这些方法直接降低 $\sigma$，从而用更少的模拟就能达到相同的精度。

控制变量法（Control Variates）就是这样一种技术，也是理解方差缩减的一个很好的起点。

---

## 2. 什么是控制变量？

从高层次来看，控制变量利用了模拟过程中已有的**辅助信息**来改进目标量的估计。

考虑一个典型的期权定价蒙特卡洛模拟：

1. 选择一个标的资产价格的动态模型（如几何布朗运动、算术布朗运动、跳扩散模型、随机波动率模型等）。
2. 向前模拟大量价格路径至到期日。
3. 计算每条路径的收益，并贴现回当前时刻。
4. 对所有路径取平均，得到风险中性价格。

在生成这些价格路径的过程中，我们有大量**辅助信息**可用——每条路径上的平均价格、最低价格、最高价格等等。虽然这些量本身不是收益，但它们与收益高度相关，可以作为**控制变量**使用。

关键洞察：**控制变量本身不等于目标量，但它的*期望值*与目标量的期望值相等。** 这一特性使得我们可以利用辅助变量的信息来获得更精确的估计。

---

## 3. 控制变量的数学原理

控制变量法本质上是一个**线性回归**。设：

- $Y$ = 目标量（例如贴现后的期权收益）
- $X$ = 与 $Y$ 高度相关的辅助变量，且我们知道 $\mathbb{E}[X]$ 的闭式解
- $c$ = 一个常数系数

**控制变量估计量**定义为：

$$
Y_{CV} = Y - c\,(X - \mathbb{E}[X])
$$

为什么这是有效的？对两边取期望：

$$
\begin{aligned}
\mathbb{E}[Y_{CV}] &= \mathbb{E}[Y] - c\,\big(\mathbb{E}[X] - \mathbb{E}[X]\big) \\
&= \mathbb{E}[Y]
\end{aligned}
$$

$\mathbb{E}[X]$ 项恰好抵消。这意味着无论 $c$ 取何值，$Y_{CV}$ 都是 $\mathbb{E}[Y]$ 的**无偏估计量**——与原始量的期望完全相同。

系数 $c$ 是我们选择的一个常数。$\mathbb{E}[X]$ 是已知的（这一点至关重要——我们必须从模型中得到它的闭式表达式）。项 $(X - \mathbb{E}[X])$ 表示辅助变量与其已知均值的偏差，我们利用这个偏差来调整 $Y$。

---

## 4. 最优系数的选择

系数 $c$ 不是任意选取的——它通过**最小化估计量的方差**来确定。这是一个简单的优化问题。

我们要最小化 $\text{Var}(Y_{CV}) = \text{Var}\big(Y - c(X - \mathbb{E}[X])\big)$。

对 $c$ 求导并令其为零：

$$
\frac{d}{dc}\text{Var}(Y - cX) = -2\text{Cov}(Y, X) + 2c\,\text{Var}(X) = 0
$$

得到：

$$
c^* = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}
$$

这正是 $Y$ 对 $X$ 做普通线性回归的回归系数。

在实践中，我们事先并不知道 $\text{Cov}(Y, X)$ 和 $\text{Var}(X)$（如果知道的话，我们也就知道 $\mathbb{E}[Y]$ 了）。因此，我们用模拟样本对其进行估计：

$$
\hat{c} = \frac{\widehat{\text{Cov}}(Y, X)}{\widehat{\text{Var}}(X)}
$$

这是在**模拟之后**使用样本协方差和样本方差完成的。

---

## 5. 控制变量如何降低方差

对控制变量方程两边取方差：

$$
\begin{aligned}
\text{Var}(Y_{CV}) &= \text{Var}\big(Y - c\,(X - \mathbb{E}[X])\big) \\
&= \text{Var}(Y) + c^2\,\text{Var}(X) - 2c\,\text{Cov}(Y, X)
\end{aligned}
$$

代入最优 $c^* = \text{Cov}(Y, X) / \text{Var}(X)$：

$$
\begin{aligned}
\text{Var}(Y_{CV}) &= \text{Var}(Y) + \frac{\text{Cov}(Y, X)^2}{\text{Var}(X)} - 2\frac{\text{Cov}(Y, X)^2}{\text{Var}(X)} \\
&= \text{Var}(Y) - \frac{\text{Cov}(Y, X)^2}{\text{Var}(X)}
\end{aligned}
$$

由**相关系数**的定义 $\rho_{Y,X} = \dfrac{\text{Cov}(Y, X)}{\sqrt{\text{Var}(Y)\,\text{Var}(X)}}$，代入上式：

$$
\begin{aligned}
\text{Var}(Y_{CV}) &= \text{Var}(Y) - \frac{\rho_{Y,X}^2\,\text{Var}(Y)\,\text{Var}(X)}{\text{Var}(X)} \\
&= \text{Var}(Y)\,\big(1 - \rho_{Y,X}^2\big)
\end{aligned}
$$

这是一个强有力的结果：

| 相关系数 $\rho$ | 方差缩减比例 | 解读 |
|:---:|:---:|---|
| 0.0 | 0% | 无相关——无收益 |
| 0.5 | 25% | 中等相关——有用 |
| 0.7 | 49% | 高度相关——显著收益 |
| 0.9 | 81% | 极高相关——大幅缩减 |
| 1.0 | 100% | 完美相关——可直接知道 $\mathbb{E}[Y]$ |

$X$ 与 $Y$ 的相关性越高，方差缩减的效果越好。在 $\rho = 1$ 的极限情况下，我们将确切知道 $\mathbb{E}[Y]$（但那样我们就不需要模拟了）。

> **注意：** 这个框架可以自然扩展到多个控制变量，通过多元回归来实现：
>
> $$
> Y_{CV} = Y - c_1(X_1 - \mathbb{E}[X_1]) - c_2(X_2 - \mathbb{E}[X_2]) - \cdots
> $$

---

## 6. 实例：算术布朗运动下的欧式期权定价

### 6.1 模型设定

我们将控制变量法应用到一个具体的例子中：在**算术布朗运动（ABM）** 下对欧式看涨期权进行定价。

> **为什么用 ABM？** 这是一个精心设计的教学示例——ABM 有闭式解，实际上我们不需要模拟。但它提供了一个直观的环境，使控制变量的思想变得透明。理解之后，同样的原理可以应用于那些没有闭式解的更复杂模型。

**期权收益**（到期日 $T$）：

$$
C = \max(S_T - K, 0)
$$

**标的资产的 ABM 动态**：

$$
S_t = S_0 + \mu t + \sigma W_t
$$

其中：
- $S_0$ = 初始资产价格
- $K$ = 行权价
- $\mu$ = 漂移率（单位：价格/时间），控制价格的确定性趋势
- $\sigma$ = 波动率（单位：价格/$\sqrt{\text{时间}}$），控制随机波动幅度
- $W_t$ = 标准布朗运动，$W_t \sim N(0, t)$，是价格的随机驱动源

**公式解读：** ABM 将价格拆解为三个部分的叠加：
1. **$S_0$** — 起点价格
2. **$\mu t$** — 确定性漂移：每单位时间增长 $\mu$，经过时间 $t$ 后累积的趋势性变化
3. **$\sigma W_t$** — 随机波动：$W_t \sim N(0, t)$，故 $\sigma W_t \sim N(0, \sigma^2 t)$，不确定性的范围随 $\sqrt{t}$ 增长

这与几何布朗运动(GBM)不同。GBM 是乘法过程 $S_t = S_0 e^{\mu t + \sigma W_t}$，价格始终为正；而 ABM 是加法过程，价格可能为负。ABM 的优点是形式简单、闭式解易得，适合作为教学示例。在本例中参数设置使得价格为正的概率很高，不影响演示目的。

> **补充说明：** 在模拟代码中，$t$ 的单位是**交易日**（$T=252$），因此 $\mu = 0.1$ 表示每个交易日平均上涨 0.1 个单位。离散化实现时，每一时间步的增量为 $\Delta S = \mu \Delta t + \sigma \sqrt{\Delta t}\, \varepsilon$，其中 $\varepsilon \sim N(0,1)$。

### 6.2 控制变量的选择

我们需要一个辅助变量 $X$，满足：
1. 与收益 $C = \max(S_T - K, 0)$ 高度相关
2. 已知 $\mathbb{E}[X]$ 的闭式表达式

一个自然的选择是每条路径上模拟价格的**算术平均值**：

$$
X = \frac{1}{N} \sum_{i=1}^N S_{t_i}
$$

在 ABM 下，到期时平均价格的期望为：

$$
\mathbb{E}[X] = S_0 + \frac{\mu T}{2}
$$

这个值可以直接从模型动态中精确得到。沿路径的平均价格显然与路径终点 $S_T$ 相关，因此也与收益 $\max(S_T - K, 0)$ 相关。

> **一个重要说明：** 在这个例子中，如果我们知道 $\mathbb{E}[X]$，某种程度上我们其实已经知道了很多信息，所以这个例子有些冗余。但正是这种冗余让它成为了一个直观的教学工具——它清楚地展示了控制变量法的机制，尽管在这个特例中我们不一定需要模拟。

### 6.3 Python 实现

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 参数设置
S0 = 100           # 初始价格
K = 100            # 行权价
T = 252            # 到期时间（交易日）
mu = 0.1           # 漂移率
sigma = 0.3        # 波动率
n_simulations = 10000  # 模拟路径数
n_steps = 252      # 时间步数

# 模拟 ABM 路径
'''
离散化处理 T→dt，W→ delta_W
t = 0    → S_0
t = dt   → S_{dt}  = S_0 + μ·dt   + σ·W_{dt}
t = 2dt  → S_{2dt} = S_0 + μ·2dt  + σ·W_{2dt}

$W_0 = 0$
$W_{dt} = W_0 + \Delta W_1$（第一个增量）
$W_{2dt} = W_{dt} + \Delta W_2 = \Delta W_1 + \Delta W_2$

实现方式：
原先是S1 → S2 →  ... → St,串行计算
因为是Markov Chain，前后不影响，并行计算
固定偏移：(252,)
随机偏移：(10000, 252) →  cumsum →  取[:, -1], 一次性生成10000个paths，每个path有252天的值
'''
dt = T / n_steps
time_grid = np.linspace(0, T, n_steps)
brownian_increments = np.random.normal(0, np.sqrt(dt),
                                       size=(n_simulations, n_steps))
S_paths = S0 + mu * time_grid + sigma * np.cumsum(brownian_increments, axis=1)

# 到期日价格
S_T = S_paths[:, -1]

# 欧式看涨期权收益
payoffs = np.maximum(S_T - K, 0)

# --- 控制变量 ---
# 辅助变量：每条路径上价格的算术平均值
S_avg = S_paths.mean(axis=1)

# ABM 下的已知期望值 E(X)
expected_S_avg = S0 + mu * T / 2

# 从样本中估计最优系数 c
covariance = np.cov(payoffs, S_avg)[0, 1]
variance_x = np.var(S_avg)
c_optimal = covariance / variance_x

# 使用控制变量调整后的收益
adjusted_payoffs = payoffs - c_optimal * (S_avg - expected_S_avg)

# 蒙特卡洛估计
call_price = np.mean(payoffs)
adjusted_call_price = np.mean(adjusted_payoffs)

# 方差比较
variance_original = np.var(payoffs, ddof=1)
variance_adjusted = np.var(adjusted_payoffs, ddof=1)
variance_reduction = 100 * (1 - variance_adjusted / variance_original)

# 标准误差
se_original = np.std(payoffs, ddof=1) / np.sqrt(n_simulations)
se_adjusted = np.std(adjusted_payoffs, ddof=1) / np.sqrt(n_simulations)

# 置信区间（95%）
confidence_level = 0.95
z = norm.ppf(0.5 + confidence_level / 2)
ci_original = (call_price - z * se_original, call_price + z * se_original)
ci_adjusted = (adjusted_call_price - z * se_adjusted,
               adjusted_call_price + z * se_adjusted)

# 输出结果
print(f"原始期权价格估计:               {call_price:.4f}")
print(f"控制变量调整后价格:             {adjusted_call_price:.4f}")
print()
print(f"原始标准误差:                   {se_original:.4f}")
print(f"调整后标准误差:                 {se_adjusted:.4f}")
print()
print(f"方差缩减比例:                   {variance_reduction:.2f}%")
print(f"最优系数 c:                     {c_optimal:.4f}")

# 绘制直方图
plt.hist(payoffs, bins=50, alpha=0.5, label="原始收益")
plt.hist(adjusted_payoffs, bins=50, alpha=0.5, label="调整后收益（控制变量）")
plt.axvline(call_price, color='blue', linestyle='--', label="原始均值")
plt.axvline(adjusted_call_price, color='red', linestyle='--', label="调整后均值")
plt.title("使用与不使用控制变量的收益分布对比")
plt.xlabel("收益")
plt.ylabel("频数")
plt.legend()
plt.show()
```

### 6.4 结果分析

运行模拟将得到类似以下的输出：

```
原始期权价格估计:               25.1147
控制变量调整后价格:             25.0714

原始标准误差:                   0.5261
调整后标准误差:                 0.2675

方差缩减比例:                   74.15%
最优系数 c:                     1.0214
```

**关键观察：**

1. **期望相同，方差更低。** 原始估计和调整后估计的中心值大致相同（约 25.07–25.11），证实了无偏性。但调整后估计的分布要紧凑得多。

2. **约 75% 的方差缩减。** 标准误差从约 0.53 下降到约 0.27——大约减半。这意味着使用控制变量后，我们以相同的计算量达到了相当于不使用控制变量时 **4 倍模拟次数** 的精度。

3. **更窄的置信区间。** 在相同的计算成本下，我们得到了更窄的置信区间。

4. **直方图对比。** 在可视化时，原始收益分布（蓝色）较宽，而调整后的收益分布（橙色）更紧凑。两个分布的中心均值相同，但调整后的分布离散程度更小。

> **说明：** 这是一个教学示例。在 ABM 下，我们有期权价格的闭式解——实际上不需要模拟。其目的是在一个机制透明的环境中展示控制变量法的*工作原理*。真正的应用出现在没有闭式解且模拟成本高昂的情况下。

### 6.5 为什么例子不合适：

$S_T$ 在 ABM 下服从正态分布：
$$
S_T \sim N(m, v^2), \quad m = S_0 + \mu T, \quad v = \sigma\sqrt{T}
$$

看涨期权价格就是截断正态的期望：

$$
C = \mathbb{E}[\max(S_T - K, 0)] = \int_{K}^{\infty} (S - K) \cdot \frac{1}{v\sqrt{2\pi}} e^{-\frac{(s-m)^2}{2v^2}} ds
$$

做变量代换 $z = \frac{s - m}{v}$，令 $d = \frac{K - m}{v}$：

$$
\begin{aligned}
C &= \int_{d}^{\infty} (m + vz - K) \cdot \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz \\[4pt]
&= (m - K) \int_{d}^{\infty} \phi(z)\,dz \;+\; v \int_{d}^{\infty} z\,\phi(z)\,dz \\[4pt]
&= (m - K)\,\big(1 - \Phi(d)\big) \;+\; v\,\phi(d)
\end{aligned}
$$

其中 $\phi(z)$ 是标准正态 PDF（概率密度函数）(小写，值)，$\Phi(z)$ 是标准正态 CDF（累积分布函数）（大写，面积）。

利用性质 $\Phi(-d) = 1 - \Phi(d)$，令 $a = -d = \frac{m - K}{v}$，最终得到：

$$
\boxed{C = (m - K)\,\Phi(a) + v\,\phi(a)}
$$

其中：
$$
m = S_0 + \mu T,\quad v = \sigma\sqrt{T},\quad a = \frac{S_0 + \mu T - K}{\sigma\sqrt{T}}
$$

公式：“价内概率×价格“的结构。这就是Bachelier 模型（正态模型）的欧式看涨期权定价公式，常用于利率期权和期货期权定价。用你代码里的参数代进去可以算出精确价格，和蒙特卡洛的结果做对比。

---

## 7. 与前沿文献的联系

### 7.1 粗糙波动率模型

**粗糙波动率模型**（Rough Volatility Models，如 rough Bergomi 模型）近年受到广泛关注，因为它们能更好地刻画金融市场的某些典型特征，尤其是已实现波动率曲面。然而，它们引入了：

- **长期依赖性**——波动率过程具有长记忆性
- **非马尔可夫结构**——未来依赖于整个价格路径的历史
- **极高的计算成本**——每条路径的模拟都很昂贵

这就产生了一个直接的矛盾：更符合实际的模型也更难在实践中使用。当一家银行每天需要为数千个期权定价时，效率至关重要。一个精度较低但有闭式解的模型，往往胜过精度更高但需要数小时模拟的模型。

像控制变量这样的方差缩减技术有助于弥合这一差距。通过减少达到给定精度所需的路径数量，它们使计算成本高昂的模型变得更加可行。

### 7.2 神经网络近似方法

当前一个活跃的研究方向是利用**神经网络**来逼近复杂模型的定价函数。基本思路：

1. **生成训练集**：使用昂贵模型为多种参数组合模拟价格。
2. **训练神经网络**：学习从模型参数到期权价格的映射。
3. **使用训练好的网络**即时定价新期权——前向传播的计算成本几乎可以忽略不计。

由于神经网络本质上就是一个函数逼近器，它可以学习以下关系：
$$
f_\theta(\text{模型参数}) \approx \mathbb{E}^\mathbb{Q}[\text{收益}]
$$

这与方差缩减追求的是同一个目标——提高效率——只是从不同的角度入手。两种技术都旨在降低在复杂模型下获得精确价格的计算成本。

> 对于粗糙波动率模型等复杂模型，每一步的模拟都涉及整个路径的历史依赖。即使每条路径的模拟成本降低了，由于路径的分布范围广，我们仍然需要大量路径来获得稳定估计。这正是方差缩减技术的用武之地——通过利用模拟中已有的信息，在相同路径数下获得更精确的估计。

---

## 8. 总结

控制变量法为蒙特卡洛模拟中的方差缩减提供了一种强大而直观的方法：

| 概念 | 核心要点 |
|---------|-------------|
| **核心思想** | 利用模拟中的辅助信息改进目标量的估计 |
| **机制** | 线性回归：$Y_{CV} = Y - c(X - \mathbb{E}[X])$ |
| **无偏性** | 无论 $c$ 取何值，$\mathbb{E}[Y_{CV}] = \mathbb{E}[Y]$ |
| **最优系数** | $c^* = \text{Cov}(Y,X) / \text{Var}(X)$ |
| **方差缩减** | $\text{Var}(Y_{CV}) = \text{Var}(Y)(1 - \rho^2)$ |
| **关键要求** | 需要一个已知 $\mathbb{E}[X]$ 且与 $Y$ 高度相关的辅助变量 $X$ |

在金融领域，效率和复杂度之间始终存在一种反向关系：随着模型复杂度的增加，计算效率下降，反之亦然。简单的模型虽然可能精度略低，但如果有闭式解，其实际价值可能远高于一个虽更精确但无法高效计算的模型。方差缩减技术正是为了弥合这一鸿沟——让我们能够在不过度牺牲效率的前提下，使用更复杂的模型。

控制变量技术并不局限于金融领域——它适用于任何使用蒙特卡洛模拟且有辅助信息可用的场景。无论是定价奇异期权、估计风险度量，还是模拟物理系统，其原理都是一样的：**利用你已经知道的信息，来优化你正在估计的量。**

---

## 参考资料

- **Quant Guild 网站:** [https://quantguild.com](https://quantguild.com)
- **Discord 社区:** [https://discord.com/invite/MJ4FU2c6c3](https://discord.com/invite/MJ4FU2c6c3)
- **GitHub 仓库:** [https://github.com/romanmichaelpaolucci/Quant-Guild-Library](https://github.com/romanmichaelpaolucci/Quant-Guild-Library)
- **博客 / 文章:** [https://medium.com/quant-guild](https://medium.com/quant-guild)
- **Jupyter Notebook:** [Control Variates for Variance Reduction.ipynb](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/Control%20Variates%20for%20Variance%20Reduction.ipynb)
