# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 3 – Learning Rate (The Most Important Hyperparameter)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what the Learning Rate is.
- Learn why it is the most important hyperparameter.
- Understand its role in Gradient Descent.
- Learn what happens when the Learning Rate is too small or too large.
- Understand how to choose an appropriate Learning Rate.

---

# 1. Introduction

Recall the Gradient Descent update equation.

$$
W_{new}
=
W_{old}
-
\eta
\frac{\partial L}{\partial W}
$$

where

- $$W$$ = Weight
- $$L$$ = Loss Function
- $$\frac{\partial L}{\partial W}$$ = Gradient
- $$\eta$$ (eta) = **Learning Rate**

The Learning Rate controls

> **How large each weight update should be during training.**

---

# 2. What is Learning Rate?

The Learning Rate is

> **A hyperparameter that determines the size of each optimization step during Gradient Descent.**

Imagine walking toward the bottom of a valley.

The Learning Rate determines

```text
Small Step

or

Large Step
```

taken at every iteration.

---

# 3. Where is Learning Rate Used?

During every optimization step,

Gradient Descent computes

```text
Gradient

↓

Learning Rate

↓

Weight Update
```

Mathematically

$$
\text{Weight Update}
=
\eta
\times
\text{Gradient}
$$

The Learning Rate scales the gradient before updating the weights.

---

# 4. Small Learning Rate

Suppose

```text
Learning Rate = 0.00001
```

The optimizer takes extremely small steps.

```text
Start

↓

.

↓

.

↓

.

↓

.

↓

Minimum
```

Advantages

- Stable training
- Less chance of overshooting

Disadvantages

- Very slow convergence
- Requires many epochs
- Higher computational cost

---

# 5. Large Learning Rate

Suppose

```text
Learning Rate = 5
```

The optimizer takes huge steps.

```text
Start

↓

>>>>>>>>>

<<<<<<<<<<

>>>>>>>>>

<<<<<<<<<<
```

Instead of reaching the minimum,

it repeatedly jumps across it.

This is called

```text
Overshooting
```

Training may never converge.

---

# 6. Good Learning Rate

A suitable Learning Rate takes balanced steps.

```text
Start

↓

↓

↓

↓

Minimum
```

Advantages

- Fast convergence
- Stable optimization
- Efficient training

This is the goal of Hyperparameter Tuning.

---

# 7. Visual Comparison

## Learning Rate Too Small

```text
Start

↓

.

↓

.

↓

.

↓

Minimum

Very Slow
```

---

## Good Learning Rate

```text
Start

↓

↓

↓

↓

Minimum

Fast
```

---

## Learning Rate Too Large

```text
Start

↓

>>>>>>>>>

<<<<<<<<<<

>>>>>>>>>

Never Converges
```

---

# 8. Effect on the Loss Curve

### Small Learning Rate

```text
Loss

↓

↓

↓

↓

Very Slow
```

The loss decreases gradually.

---

### Good Learning Rate

```text
Loss

↓

↓

↓

Rapid Convergence
```

The loss decreases quickly and smoothly.

---

### Large Learning Rate

```text
Loss

↓

↑

↓

↑

↓

↑
```

The loss oscillates or even increases.

Training becomes unstable.

---

# 9. Typical Learning Rate Values

Common starting values are

| Optimizer | Typical Learning Rate |
|-----------|----------------------:|
| SGD | 0.1, 0.01 |
| Momentum | 0.01 |
| RMSProp | 0.001 |
| Adam | 0.001 |
| AdamW | 0.001 |

These are starting points,

not universal rules.

The optimal value depends on the

- Dataset
- Model architecture
- Optimizer

---

# 10. Real-Life Analogy

Imagine climbing down a mountain.

### Small Steps

```text
Tiny Steps

↓

Safe

↓

Very Slow
```

---

### Large Steps

```text
Huge Steps

↓

Jump Over the Path

↓

May Fall
```

---

### Medium Steps

```text
Balanced Steps

↓

Safe

↓

Fast
```

The Learning Rate controls your step size in exactly the same way.

---

# 11. Why Is Learning Rate So Important?

A poor Learning Rate can

- Prevent convergence
- Increase training time
- Cause unstable optimization
- Produce poor accuracy

A good Learning Rate can

- Speed up convergence
- Improve optimization
- Reduce computational cost
- Produce better models

---

# 12. One Important Insight

Many beginners think

> **A larger Learning Rate always makes training faster.**

This is incorrect.

A very large Learning Rate may prevent convergence entirely because the optimizer repeatedly overshoots the minimum.

The objective is

> **Not the largest Learning Rate, but the largest stable Learning Rate.**

---

# Visual Summary

```text
Learning Rate

↓

Controls Step Size

↓

Small

↓

Slow Learning

OR

↓

Large

↓

Overshooting

OR

↓

Balanced

↓

Fast Stable Convergence
```

---

# Comparison of Different Learning Rates

| Small Learning Rate | Good Learning Rate | Large Learning Rate |
|----------------------|-------------------|---------------------|
| Very slow training | Fast convergence | Unstable training |
| Many epochs required | Efficient optimization | Overshooting |
| Stable | Stable | Oscillation or divergence |
| High computation time | Balanced | May never converge |

---

# Interview Questions

## Q1. What is the Learning Rate?

**Answer**

The Learning Rate is a hyperparameter that determines the size of each weight update during Gradient Descent.

---

## Q2. What happens if the Learning Rate is too small?

**Answer**

Training becomes very slow because the optimizer takes tiny steps toward the minimum.

---

## Q3. What happens if the Learning Rate is too large?

**Answer**

The optimizer overshoots the minimum, causing oscillation or divergence instead of convergence.

---

## Q4. Why is the Learning Rate considered the most important hyperparameter?

**Answer**

Because it directly controls optimization speed, convergence stability, and final model performance.

---

## Q5. Is there one best Learning Rate for every model?

**Answer**

No.

The optimal Learning Rate depends on the dataset, model architecture, optimizer, and training objective.

---

# Summary

The Learning Rate is the most influential hyperparameter in Deep Learning.

It controls the magnitude of each weight update during optimization.

A very small Learning Rate leads to slow convergence, while a very large Learning Rate can cause overshooting and unstable training.

Choosing an appropriate Learning Rate allows the optimizer to converge efficiently and improves overall model performance.

---

# Key Takeaways

✔ Learning Rate controls the step size in Gradient Descent.

✔ Small Learning Rates produce slow but stable training.

✔ Large Learning Rates may cause overshooting and divergence.

✔ A balanced Learning Rate enables fast and stable convergence.

✔ The Learning Rate is one of the most important hyperparameters in Deep Learning.

---

# Next Part

## **Part 4 – Batch Size**

In the next chapter, we will study **Batch Size**, understand how data is divided into batches, learn the difference between **Batch Gradient Descent**, **Stochastic Gradient Descent**, and **Mini-Batch Gradient Descent**, and explore how Batch Size affects training speed, memory usage, convergence, and model generalization.
