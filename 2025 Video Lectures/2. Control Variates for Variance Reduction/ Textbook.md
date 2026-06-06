# Control Variates for Variance Reduction in Simulation

> **Lecture by:** Roman Paolucci — Quant Guild
> **Video:** [Control Variates for Variance Reduction](https://www.youtube.com/watch?v=Iu_gCD74Y70&t=107s)
> **Notebook:** [GitHub](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/Control%20Variates%20for%20Variance%20Reduction.ipynb)

---

## Table of Contents

1. [Why Variance Reduction?](#1-why-variance-reduction)
2. [What is a Control Variate?](#2-what-is-a-control-variate)
3. [The Mathematics of Control Variates](#3-the-mathematics-of-control-variates)
4. [Choosing the Optimal Coefficient c](#4-choosing-the-optimal-coefficient-c)
5. [How Control Variates Reduce Variance](#5-how-control-variates-reduce-variance)
6. [Toy Example: European Option Pricing under ABM](#6-toy-example-european-option-pricing-under-abm)
   - [Model Setup](#61-model-setup)
   - [The Control Variate for ABM](#62-the-control-variate-for-abm)
   - [Python Implementation](#63-python-implementation)
   - [Results and Interpretation](#64-results-and-interpretation)
7. [Connections to Current Literature](#7-connections-to-current-literature)
   - [Rough Volatility Models](#71-rough-volatility-models)
   - [Neural Network Approximations](#72-neural-network-approximations)
8. [Conclusion](#8-conclusion)

---

## 1. Why Variance Reduction?

Monte Carlo simulation is a cornerstone technique for estimating quantities in stochastic models. When we estimate some quantity $\theta$ (say, an option price) via simulation, we care about the **precision** of our estimate. The standard error of the estimator is proportional to:

$$
\text{Standard Error} \propto \frac{\sigma}{\sqrt{N}}
$$

where $\sigma$ is the standard deviation of the simulated payoffs and $N$ is the number of simulations.

A natural question arises: *If we want a tighter confidence interval, why not just increase $N$ — go from 1,000 to 10,000 to 100,000 or even a million simulations?*

The answer is **computational cost**. For many practical models, each individual simulation path is expensive to generate. Simply scaling up $N$ may be impractical or take far too long. This motivates the search for **variance reduction techniques** — methods that reduce $\sigma$ directly, so we achieve the same precision with fewer simulations.

Control variates are one such technique, and they provide an excellent starting point for understanding variance reduction more broadly.

---

## 2. What is a Control Variate?

At a high level, a control variate leverages **auxiliary information** already available within a simulation to improve the estimation of the quantity of interest.

Consider a typical Monte Carlo simulation for pricing an option:

1. Choose a model for the underlying asset dynamics (e.g., geometric Brownian motion, arithmetic Brownian motion, jump diffusion, stochastic volatility).
2. Simulate many price paths forward to maturity.
3. Compute the payoff for each path and discount back to the present.
4. Average over all paths to obtain the risk-neutral price.

In generating those price paths, we have a wealth of **auxiliary information** available — the average price along each path, the minimum price, the maximum price, and so on. While these quantities are not the payoff itself, they are highly correlated with it and can serve as **control variates**.

The key insight: **the control variate itself is not equal to the quantity of interest, but its *expectation* matches the expectation of the quantity of interest.** This subtle property allows us to use information from an auxiliary variable to produce a more precise estimate.

---

## 3. The Mathematics of Control Variates

The control variate technique takes the form of a **linear regression**. Let:

- $Y$ = the target quantity of interest (e.g., the discounted option payoff)
- $X$ = an auxiliary variable that is highly correlated with $Y$, and for which we know $\mathbb{E}[X]$ in closed form
- $c$ = a constant coefficient

The **control variate estimator** is defined as:

$$
Y_{CV} = Y - c\,(X - \mathbb{E}[X])
$$

Why is this valid? Taking expectations on both sides:

$$
\begin{aligned}
\mathbb{E}[Y_{CV}] &= \mathbb{E}[Y] - c\,\big(\mathbb{E}[X] - \mathbb{E}[X]\big) \\
&= \mathbb{E}[Y]
\end{aligned}
$$

The terms $\mathbb{E}[X]$ cancel exactly. This means $Y_{CV}$ is an **unbiased estimator** of $\mathbb{E}[Y]$ — the same expectation as the original quantity — regardless of the choice of $c$.

The coefficient $c$ is a constant we select. \mathbb{E}[X] is known (this is crucial — we must have a closed-form expression for it from our model). The term $(X - \mathbb{E}[X])$ represents the deviation of the auxiliary variable from its known mean, and we use this deviation to adjust $Y$.

---

## 4. Choosing the Optimal Coefficient $c$

The coefficient $c$ is not chosen arbitrarily — it is selected to **minimize the variance** of the estimator. This is a simple optimization problem.

We want to minimize $\text{Var}(Y_{CV}) = \text{Var}(Y - c(X - \mathbb{E}[X]))$.

Taking the derivative with respect to $c$ and setting it to zero:

$$
c^* = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}
$$

This is, unsurprisingly, the same coefficient as in an ordinary linear regression of $Y$ on $X$.

In practice, we do not know $\text{Cov}(Y, X)$ and $\text{Var}(X)$ a priori (if we did, we would already know $\mathbb{E}[Y]$). Instead, we estimate them from our simulated sample:

$$
\hat{c} = \frac{\widehat{\text{Cov}}(Y, X)}{\widehat{\text{Var}}(X)}
$$

This is done **after simulation** using the sample covariance and sample variance.

---

## 5. How Control Variates Reduce Variance

Taking the variance of both sides of the control variate equation:

$$
\begin{aligned}
\text{Var}(Y_{CV}) &= \text{Var}\big(Y - c\,(X - \mathbb{E}[X])\big) \\
&= \text{Var}(Y) + c^2\,\text{Var}(X) - 2c\,\text{Cov}(Y, X)
\end{aligned}
$$

Substituting the optimal $c^* = \text{Cov}(Y, X) / \text{Var}(X)$:

$$
\begin{aligned}
\text{Var}(Y_{CV}) &= \text{Var}(Y) + \frac{\text{Cov}(Y, X)^2}{\text{Var}(X)} - 2\frac{\text{Cov}(Y, X)^2}{\text{Var}(X)} \\
&= \text{Var}(Y) - \frac{\text{Cov}(Y, X)^2}{\text{Var}(X)}
\end{aligned}
$$

This can be rewritten in terms of the **correlation** $\rho_{Y,X}$:

$$
\text{Var}(Y_{CV}) = \text{Var}(Y)\,\big(1 - \rho_{Y,X}^2\big)
$$

This is a powerful result:

| Correlation $\rho$ | Variance Reduction | Interpretation |
|:---:|:---:|---|
| 0.0 | 0% | No correlation — no benefit |
| 0.5 | 25% | Moderate correlation — useful |
| 0.7 | 49% | High correlation — significant benefit |
| 0.9 | 81% | Very high correlation — dramatic reduction |
| 1.0 | 100% | Perfect correlation — would know $\mathbb{E}[Y]$ exactly |

The more correlated $X$ is with $Y$, the greater the variance reduction. In the limiting case of $\rho = 1$, we would know $\mathbb{E}[Y]$ exactly (but then we wouldn't need simulation at all).

> **Note:** This framework extends naturally to multiple control variates via multiple regression:
>
> $$
> Y_{CV} = Y - c_1(X_1 - \mathbb{E}[X_1]) - c_2(X_2 - \mathbb{E}[X_2]) - \cdots
> $$

---

## 6. Toy Example: European Option Pricing under ABM

### 6.1 Model Setup

We now apply control variates to a concrete example: pricing a European call option under **Arithmetic Brownian Motion (ABM)**.

> **Why ABM?** This is intentionally a toy example — ABM has a closed-form solution, so we don't actually need simulation. But it provides an intuitive setting where the control variate idea is transparent. Once understood, the same principle applies to more complex models where closed-form solutions are unavailable.

**Option payoff** (at maturity $T$):

$$
C = \max(S_T - K, 0)
$$

**ABM dynamics** for the underlying asset:

$$
S_t = S_0 + \mu t + \sigma W_t
$$

where:
- $S_0$ = initial asset price
- $\mu$ = drift
- $\sigma$ = volatility
- $W_t$ = standard Brownian motion

### 6.2 The Control Variate for ABM

We need an auxiliary variable $X$ that:
1. Is highly correlated with the payoff $C = \max(S_T - K, 0)$
2. Has a known expectation $\mathbb{E}[X]$ in closed form

A natural choice is the **arithmetic average of the simulated prices** along each path:

$$
X = \frac{1}{N} \sum_{i=1}^N S_{t_i}
$$

Under ABM, the expected average price at maturity is:

$$
\mathbb{E}[X] = S_0 + \frac{\mu T}{2}
$$

This is known exactly from the model dynamics. The average price along a path is clearly correlated with where the path ends ($S_T$), and therefore with the payoff $\max(S_T - K, 0)$.

### 6.3 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
S0 = 100           # Initial price
K = 100            # Strike price
T = 252            # Time to maturity (trading days)
mu = 0.1           # Drift
sigma = 0.3        # Volatility
n_simulations = 10000  # Number of simulation paths
n_steps = 252      # Time steps

# Simulating ABM paths
dt = T / n_steps
time_grid = np.linspace(0, T, n_steps)
brownian_increments = np.random.normal(0, np.sqrt(dt),
                                       size=(n_simulations, n_steps))
S_paths = S0 + mu * time_grid + sigma * np.cumsum(brownian_increments, axis=1)

# Final prices at maturity
S_T = S_paths[:, -1]

# European Call Payoff
payoffs = np.maximum(S_T - K, 0)

# --- Control Variate ---
# Auxiliary variable: arithmetic average of prices along each path
S_avg = S_paths.mean(axis=1)

# Known expectation under ABM
expected_S_avg = S0 + mu * T / 2

# Estimate optimal coefficient c from sample
covariance = np.cov(payoffs, S_avg)[0, 1]
variance_x = np.var(S_avg)
c_optimal = covariance / variance_x

# Adjusted payoffs using control variate
adjusted_payoffs = payoffs - c_optimal * (S_avg - expected_S_avg)

# Monte Carlo estimates
call_price = np.mean(payoffs)
adjusted_call_price = np.mean(adjusted_payoffs)

# Variance comparison
variance_original = np.var(payoffs, ddof=1)
variance_adjusted = np.var(adjusted_payoffs, ddof=1)
variance_reduction = 100 * (1 - variance_adjusted / variance_original)

# Standard errors
se_original = np.std(payoffs, ddof=1) / np.sqrt(n_simulations)
se_adjusted = np.std(adjusted_payoffs, ddof=1) / np.sqrt(n_simulations)

# Confidence intervals (95%)
confidence_level = 0.95
z = norm.ppf(0.5 + confidence_level / 2)
ci_original = (call_price - z * se_original, call_price + z * se_original)
ci_adjusted = (adjusted_call_price - z * se_adjusted,
               adjusted_call_price + z * se_adjusted)

# Print results
print(f"Original Call Price Estimate:         {call_price:.4f}")
print(f"Adjusted Call Price (Control Variate): {adjusted_call_price:.4f}")
print()
print(f"Standard Error (Original):            {se_original:.4f}")
print(f"Standard Error (Adjusted):            {se_adjusted:.4f}")
print()
print(f"Variance Reduction:                   {variance_reduction:.2f}%")
print(f"Optimal c:                            {c_optimal:.4f}")
```

### 6.4 Results and Interpretation

Running the simulation produces output similar to:

```
Original Call Price Estimate:         25.1147
Adjusted Call Price (Control Variate): 25.0714

Standard Error (Original):            0.5261
Standard Error (Adjusted):            0.2675

Variance Reduction:                   74.15%
Optimal c:                             1.0214
```

**Key observations:**

1. **Same expectation, lower variance.** Both the original and adjusted estimates center on approximately the same value (~25.07–25.11), confirming unbiasedness. But the adjusted estimate has a much tighter distribution.

2. **~75% variance reduction.** The standard error dropped from ~0.53 to ~0.27 — roughly half. This means we achieved the same precision with the control variate as we would have by running **4× as many simulations** without it.

3. **Tighter confidence intervals.** For the same computational cost, we obtain a narrower confidence interval around our price estimate.

4. **The orange vs. blue histogram.** When visualized, the original payoff distribution (blue) is wide, while the adjusted payoff distribution (orange) is tighter. Both distributions center on the same mean, but the adjusted one has less spread.

![Payoffs histogram showing original vs. adjusted distributions](https://raw.githubusercontent.com/romanmichaelpaolucci/Quant-Guild-Library/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/figures/payoffs_histogram.png)

> **Caveat:** This example is intentionally a toy. Under ABM, we have a closed-form solution for the option price — we don't need simulation at all. The purpose is to illustrate *how* control variates work in a setting where the mechanics are transparent. Real applications arise when closed-form solutions are unavailable and simulation is expensive.

---

## 7. Connections to Current Literature

### 7.1 Rough Volatility Models

**Rough volatility models** (e.g., the rough Bergomi model) have gained significant attention because they better characterize certain stylized facts of financial markets, particularly the realized volatility surface. However, they introduce:

- **Long-range dependency** in the volatility process
- **Non-Markovian structure** — the future depends on the entire price path
- **Extreme computational cost** — each path simulation is expensive

This creates a direct tension: a model that is more realistic is also harder to use in practice. When a bank needs to price thousands of options daily, efficiency is paramount. A less accurate model with a closed-form solution often beats a more accurate one that takes hours to simulate.

Variance reduction techniques like control variates help bridge this gap. By reducing the number of paths needed for a given precision level, they make computationally expensive models more tractable.

### 7.2 Neural Network Approximations

An active stream of current research focuses on using **neural networks** to approximate pricing functionals for complex models. The idea:

1. **Generate a training set** by simulating prices for many parameter combinations using the expensive model.
2. **Train a neural network** to learn the mapping from model parameters to option prices.
3. **Use the trained network** to price new options instantly — a forward pass through the network costs essentially nothing compared to a full simulation.

Since a neural network is, at its core, just a function approximator, it can learn the relationship:
$$
f_\theta(\text{model parameters}) \approx \mathbb{E}^\mathbb{Q}[\text{payoff}]
$$

This is the same efficiency goal as variance reduction — just approached from a different angle. Both techniques aim to reduce the computational cost of obtaining accurate prices under complex models.

---

## 8. Conclusion

Control variates provide a powerful and intuitive method for variance reduction in Monte Carlo simulation:

| Concept | Key Takeaway |
|---------|-------------|
| **Core idea** | Use auxiliary information from within a simulation to improve estimation |
| **Mechanism** | Linear regression: $Y_{CV} = Y - c(X - \mathbb{E}[X])$ |
| **Unbiasedness** | $\mathbb{E}[Y_{CV}] = \mathbb{E}[Y]$ regardless of $c$ |
| **Optimal c** | $c^* = \text{Cov}(Y,X) / \text{Var}(X)$ |
| **Variance reduction** | $\text{Var}(Y_{CV}) = \text{Var}(Y)(1 - \rho^2)$ |
| **Key requirement** | Need an auxiliary variable $X$ with known $\mathbb{E}[X]$ and high correlation with $Y$ |

The control variate technique is not limited to finance — it applies anywhere Monte Carlo simulation is used and auxiliary information is available. Whether pricing exotic options, estimating risk measures, or simulating physical systems, the principle is the same: **use what you already know to sharpen what you estimate.**

---

## References and Resources

- **Quant Guild Website:** [https://quantguild.com](https://quantguild.com)
- **Discord Community:** [https://discord.com/invite/MJ4FU2c6c3](https://discord.com/invite/MJ4FU2c6c3)
- **GitHub Repository:** [https://github.com/romanmichaelpaolucci/Quant-Guild-Library](https://github.com/romanmichaelpaolucci/Quant-Guild-Library)
- **Blog / Articles:** [https://medium.com/quant-guild](https://medium.com/quant-guild)
- **Jupyter Notebook:** [Control Variates for Variance Reduction.ipynb](https://github.com/romanmichaelpaolucci/Quant-Guild-Library/blob/main/2025%20Video%20Lectures/2.%20Control%20Variates%20for%20Variance%20Reduction/Control%20Variates%20for%20Variance%20Reduction.ipynb)
