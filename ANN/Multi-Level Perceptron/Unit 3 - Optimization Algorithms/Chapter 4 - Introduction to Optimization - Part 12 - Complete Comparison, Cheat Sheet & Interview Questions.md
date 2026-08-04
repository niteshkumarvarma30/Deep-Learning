# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 12 – Complete Comparison, Cheat Sheet & Interview Questions

---

# Learning Objectives

After completing this chapter, you will be able to:

- Compare all optimization algorithms.
- Understand when to use each optimizer.
- Learn the complete evolution of optimization algorithms.
- Revise all important mathematical formulas.
- Prepare for interviews and examinations.

---

# 1. Evolution of Optimization Algorithms

Optimization algorithms were developed to solve the limitations of previous algorithms.

```text
Gradient Descent

↓

Batch Gradient Descent

↓

Stochastic Gradient Descent (SGD)

↓

Mini-Batch Gradient Descent

↓

Exponentially Weighted Moving Average (EWMA)

↓

Momentum

↓

Nesterov Accelerated Gradient (NAG)

↓

AdaGrad

↓

RMSProp

↓

Adam
```

Each optimizer improves one or more weaknesses of earlier algorithms.

---

# 2. Why Was Each Optimizer Introduced?

| Optimizer | Why Was It Introduced? |
|------------|------------------------|
| Gradient Descent | Basic optimization algorithm |
| Batch GD | Uses the entire dataset for stable updates |
| SGD | Faster updates than Batch GD |
| Mini-Batch GD | Balance between Batch GD and SGD |
| EWMA | Smooth noisy values using exponential averaging |
| Momentum | Speed up convergence and reduce oscillations |
| NAG | Improve Momentum by looking ahead before computing gradients |
| AdaGrad | Introduce adaptive learning rates |
| RMSProp | Fix AdaGrad's continuously shrinking learning rate |
| Adam | Combine Momentum and RMSProp |

---

# 3. Dataset Usage

| Optimizer | Data Used Per Update |
|------------|----------------------|
| Batch GD | Entire Dataset |
| SGD | One Sample |
| Mini-Batch GD | Small Batch |

Example

Dataset

```text
1000 Samples
```

| Algorithm | Batch Size | Updates per Epoch |
|------------|-----------:|------------------:|
| Batch GD | 1000 | 1 |
| SGD | 1 | 1000 |
| Mini-Batch GD | 100 | 10 |

---

# 4. Memory Comparison

| Optimizer | Extra Memory Required |
|------------|----------------------|
| Gradient Descent | None |
| Momentum | Velocity (v) |
| NAG | Velocity (v) |
| AdaGrad | Accumulated Squared Gradients (G) |
| RMSProp | EWMA of Squared Gradients (s) |
| Adam | First Moment (m) + Second Moment (v) |

---

# 5. Speed Comparison

```text
Slowest

↓

Batch GD

↓

Gradient Descent

↓

Mini-Batch GD

↓

Momentum

↓

NAG

↓

AdaGrad

↓

RMSProp

↓

Adam

↓

Fastest
```

---

# 6. Formula Cheat Sheet

## Gradient Descent

$$
w_{new} = w_{old} - \eta \frac{\partial L}{\partial w}
$$

---

## Momentum

Velocity

$$
v = \beta v - \eta \frac{\partial L}{\partial w}
$$

Weight Update

$$
w = w+v
$$

---

## NAG

Look Ahead

$$
w+\beta v
$$

Velocity

$$
v = \beta v - \eta \nabla L(w+\beta v)
$$

Weight Update

$$
w=w+v
$$

---

## AdaGrad

Accumulated Gradient

$$
G=G+g^2
$$

Weight Update

$$
w = w - \frac{\eta} {\sqrt{G}+\epsilon} g
$$

---

## RMSProp

Running Average

$$
s = \beta s + (1-\beta)g^2
$$

Weight Update

$$
w = w - \frac{\eta} {\sqrt{s}+\epsilon} g
$$

---

## Adam

First Moment

$$
m = \beta_1m + (1-\beta_1)g
$$

Second Moment

$$
v = \beta_2v + (1-\beta_2)g^2
$$

Bias Correction

$$
\hat m = \frac{m}{1-\beta_1^t}
$$

$$
\hat v = \frac{v}{1-\beta_2^t}
$$

Weight Update

$$
w = w - \eta \frac{\hat m} {\sqrt{\hat v}+\epsilon}
$$

---

# 7. Default Hyperparameters

| Parameter | Typical Value |
|------------|--------------:|
| Learning Rate (η) | 0.001 |
| Momentum β | 0.9 |
| Adam β₁ | 0.9 |
| Adam β₂ | 0.999 |
| ε | 10⁻⁸ |

---

# 8. Comparison of Optimizers

| Feature | GD | Momentum | NAG | AdaGrad | RMSProp | Adam |
|----------|:--:|:--------:|:---:|:--------:|:--------:|:----:|
| Uses Current Gradient | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Uses Previous Updates | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Adaptive Learning Rate | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Uses EWMA | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Bias Correction | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Fast Convergence | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Modern Usage | Limited | Moderate | Moderate | Rare | Common | Very Common |

---

# 9. Evolution of Ideas

```text
Gradient Descent

↓

Fixed Learning Rate

↓

Momentum

↓

Remember Previous Updates

↓

NAG

↓

Look Ahead

↓

AdaGrad

↓

Adaptive Learning Rate

↓

RMSProp

↓

Adaptive Learning Rate

+

EWMA

↓

Adam

↓

Momentum

+

Adaptive Learning Rate

+

Bias Correction
```

---

# 10. Which Optimizer Stores What?

| Optimizer | Stored Quantity |
|------------|-----------------|
| Gradient Descent | Nothing |
| Momentum | Velocity |
| NAG | Velocity |
| AdaGrad | Sum of Squared Gradients |
| RMSProp | EWMA of Squared Gradients |
| Adam | First Moment + Second Moment |

---

# 11. Which Optimizer Should You Use?

| Application | Recommended Optimizer |
|--------------|-----------------------|
| Beginner Projects | Adam |
| Deep Neural Networks | Adam |
| CNNs | Adam |
| Transformers | AdamW |
| Sparse Data | AdaGrad |
| Computer Vision Research | SGD + Momentum |
| General Purpose | Adam |

---

# 12. Complete Neural Network Training Pipeline

```text
Training Dataset

↓

Mini-Batch

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss

↓

Backpropagation

↓

Gradients

↓

Optimizer

↓

Weight Update

↓

Repeat Until Convergence
```

---

# Interview Questions

## Q1. Which optimizer is the most commonly used today?

**Answer**

Adam.

---

## Q2. Which optimizer first introduced adaptive learning rates?

**Answer**

AdaGrad.

---

## Q3. Why was RMSProp developed?

**Answer**

To solve AdaGrad's continuously decreasing learning rate problem by using EWMA instead of accumulating all squared gradients.

---

## Q4. How does NAG improve Momentum?

**Answer**

NAG computes the gradient at a predicted future position instead of the current position.

---

## Q5. Which optimizer combines Momentum and RMSProp?

**Answer**

Adam.

---

## Q6. Which optimizer uses Bias Correction?

**Answer**

Adam.

---

## Q7. What is EWMA used for?

**Answer**

EWMA smooths noisy values and is used in Momentum, RMSProp, and Adam.

---

# Chapter Summary

In this chapter, we studied the complete evolution of optimization algorithms used to train neural networks.

We began with **Gradient Descent** and learned its three variants:

- Batch Gradient Descent
- Stochastic Gradient Descent
- Mini-Batch Gradient Descent

We then introduced **EWMA**, the mathematical foundation used by several advanced optimizers.

Building on this, we studied:

- **Momentum**, which remembers previous updates.
- **NAG**, which improves Momentum using a Look Ahead strategy.
- **AdaGrad**, which introduced adaptive learning rates.
- **RMSProp**, which solved AdaGrad's learning rate decay problem using EWMA.
- **Adam**, which combines Momentum, RMSProp, and Bias Correction into one optimizer.

Together, these algorithms represent the progression from simple optimization methods to the sophisticated optimizers used in modern Deep Learning.

---

# Key Takeaways

✔ Gradient Descent is the foundation of optimization.

✔ Batch GD uses the entire dataset.

✔ SGD updates after every sample.

✔ Mini-Batch GD balances speed and stability.

✔ EWMA smooths noisy values.

✔ Momentum introduces velocity.

✔ NAG introduces the Look Ahead concept.

✔ AdaGrad introduces adaptive learning rates.

✔ RMSProp improves AdaGrad using EWMA.

✔ Adam combines Momentum, RMSProp, and Bias Correction.

✔ Adam is the most widely used optimizer in modern Deep Learning.
