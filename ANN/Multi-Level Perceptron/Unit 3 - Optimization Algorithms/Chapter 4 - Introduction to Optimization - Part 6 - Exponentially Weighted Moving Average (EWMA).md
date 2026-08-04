# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 6 – Exponentially Weighted Moving Average (EWMA)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what **Exponentially Weighted Moving Average (EWMA)** is.
- Learn why EWMA is important in Deep Learning.
- Understand how EWMA smooths noisy data.
- Learn the EWMA mathematical equation.
- Understand the role of **β (Beta)**.
- Learn why Momentum, RMSProp, and Adam all use EWMA.
- Build intuition for exponential weighting.

---

# 1. Why Do We Need EWMA?

During neural network training,

quantities like

- Loss
- Gradients
- Accuracy

often fluctuate significantly.

For example,

| Iteration | Loss |
|-----------|------|
| 1 | 8 |
| 2 | 3 |
| 3 | 10 |
| 4 | 4 |
| 5 | 9 |
| 6 | 2 |
| 7 | 11 |

The loss changes rapidly.

```text
8

↓

3

↓

10

↓

4

↓

9

↓

2

↓

11
```

It is difficult to understand the overall trend.

Instead,

we would like a smoother curve that represents the general direction of the values.

This is the purpose of **EWMA**.

---

# 2. What is EWMA?

## Definition

**Exponentially Weighted Moving Average (EWMA)** is a mathematical technique that computes a **smoothed average** of a sequence by giving

- **higher weight to recent observations**, and
- **lower weight to older observations**.

Unlike a simple average,

EWMA considers recent values to be more important.

---

# 3. Why is it Called "Exponentially Weighted"?

The contribution of older observations decreases exponentially.

For example,

```text
Most Recent Observation

↓

Weight = 1

Previous Observation

↓

Weight = β

Older Observation

↓

Weight = β²

Even Older Observation

↓

Weight = β³

...
```

As observations become older,

their contribution becomes smaller.

---

# 4. Simple Moving Average vs EWMA

## Simple Moving Average

Suppose the observations are

```text
10

20

30

40

50
```

The average is

$$
\frac{10+20+30+40+50}{5}=30
$$

Every observation contributes equally.

---

## Exponentially Weighted Moving Average

EWMA assigns

```text
50

↓

Highest Weight

40

↓

Second Highest

30

↓

Smaller Weight

20

↓

Even Smaller Weight

10

↓

Lowest Weight
```

Recent observations influence the average much more than older observations.

---

# 5. EWMA Formula

The recursive EWMA equation is

$$
\boxed{ V_t = \beta V_{t-1} + (1-\beta)x_t }
$$

where

| Symbol | Meaning |
|---------|----------|
| \(V_t\) | Current EWMA |
| \(V_{t-1}\) | Previous EWMA |
| \(x_t\) | Current Observation |
| \(\beta\) | Smoothing Factor |

This equation is one of the most important equations in optimization.

---

# 6. Understanding the Formula

The equation

$$
V_t = \beta V_{t-1} + (1-\beta)x_t
$$

has two parts.

---

## Part 1

$$
\beta V_{t-1}
$$

This represents

- previous information,
- historical memory.

---

## Part 2

$$
(1-\beta)x_t
$$

This represents

- the latest observation,
- new information.

---

Therefore,

EWMA combines

```text
Past Information

+

Present Information

↓

Smoothed Estimate
```

---

# 7. Understanding β (Beta)

The parameter

$$
\boxed{\beta}
$$

controls how much past information is remembered.

---

## Small β

Example

```text
β = 0.5
```

Characteristics

- Quickly forgets old values.
- Responds rapidly to changes.
- Less smoothing.

---

## Large β

Example

```text
β = 0.9
```

Characteristics

- Remembers past values longer.
- Produces smoother curves.
- Slower to react to sudden changes.

---

Typical values

```text
0.9

0.95

0.99
```

---

# 8. Numerical Example

Suppose

```text
β = 0.9
```

Initial EWMA

```text
V₀ = 0
```

Observations

```text
10

20

15

30
```

---

### Step 1

$$
V_1 = 0.9(0) + 0.1(10) = 1
$$

---

### Step 2

$$
V_2 = 0.9(1) + 0.1(20) = 2.9
$$

---

### Step 3

$$
V_3 = 0.9(2.9) + 0.1(15) = 4.11
$$

Notice

The EWMA changes gradually instead of jumping abruptly like the original observations.

---

# 9. Real-Life Analogy

Imagine predicting tomorrow's temperature.

Recent temperatures

```text
Today

↓

42°C

Yesterday

↓

41°C

2 Days Ago

↓

40°C
```

These are much more useful than temperatures from several months ago.

EWMA follows the same principle.

- Recent observations are more important.
- Older observations gradually lose influence.

---

# 10. Why is EWMA Important in Deep Learning?

EWMA itself is **not an optimizer**.

Instead,

it is a mathematical building block used by several optimization algorithms.

---

## Momentum

Uses

```text
EWMA of Gradients
```

---

## RMSProp

Uses

```text
EWMA of Squared Gradients
```

---

## Adam

Uses

```text
EWMA of Gradients

+

EWMA of Squared Gradients
```

Therefore,

understanding EWMA makes Momentum, RMSProp, and Adam much easier to understand.

---

# 11. Where is EWMA Used?

| Optimizer | Uses EWMA Of |
|-----------|--------------|
| Momentum | Gradients |
| RMSProp | Squared Gradients |
| Adam | Gradients + Squared Gradients |

---

# 12. Visualization

```text
Current Observation

↓

Combine With

↓

Previous EWMA

↓

New EWMA

↓

Next Observation

↓

Repeat
```

Every new EWMA carries information from all previous observations,

but recent observations contribute more.

---

# 13. Advantages of EWMA

- Smooths noisy data.
- Reduces fluctuations.
- Gives more importance to recent observations.
- Easy to compute recursively.
- Forms the foundation of modern optimization algorithms.

---

# 14. Limitations of EWMA

- The initial estimate may be biased toward zero.
- Choosing β is important.
- Not an optimizer by itself.

---

# Interview Questions

## Q1. What is EWMA?

**Answer**

EWMA is a smoothing technique that computes an exponentially weighted average of previous observations, assigning more weight to recent values.

---

## Q2. Why is EWMA used in Deep Learning?

**Answer**

It smooths noisy quantities such as gradients and forms the mathematical foundation of optimizers like Momentum, RMSProp, and Adam.

---

## Q3. What does β control?

**Answer**

β controls how much past information is retained.

---

## Q4. What happens when β is close to 1?

**Answer**

The average becomes smoother because older observations retain more influence.

---

## Q5. Is EWMA an optimizer?

**Answer**

No.

EWMA is a mathematical technique used inside optimization algorithms.

---

## Q6. Which optimizers use EWMA?

**Answer**

- Momentum
- RMSProp
- Adam

---

# Summary

Exponentially Weighted Moving Average (EWMA) is a smoothing technique that combines past and present observations by assigning exponentially decreasing weights to older values.

Instead of treating all observations equally,

EWMA emphasizes recent information while still retaining useful historical trends.

Although EWMA is **not an optimizer**, it is one of the most fundamental mathematical concepts in Deep Learning because it serves as the foundation for **Momentum**, **RMSProp**, and **Adam**.

---

# Key Takeaways

✔ EWMA stands for **Exponentially Weighted Moving Average**.

✔ EWMA smooths noisy sequences by giving greater importance to recent observations.

✔ EWMA Formula

$$
V_t = \beta V_{t-1} + (1-\beta)x_t
$$

✔ β controls the amount of historical memory.

✔ Small β reacts quickly to changes.

✔ Large β produces smoother estimates.

✔ EWMA is not an optimizer.

✔ Momentum uses **EWMA of Gradients**.

✔ RMSProp uses **EWMA of Squared Gradients**.

✔ Adam uses both **EWMA of Gradients** and **EWMA of Squared Gradients**.

✔ EWMA is one of the foundational mathematical ideas behind modern optimization algorithms.
