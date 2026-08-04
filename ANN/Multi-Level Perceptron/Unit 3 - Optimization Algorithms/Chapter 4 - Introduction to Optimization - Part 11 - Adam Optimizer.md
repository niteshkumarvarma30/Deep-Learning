# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 11 – Adam Optimizer (Adaptive Moment Estimation)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Adam was introduced.
- Learn how Adam combines **Momentum** and **RMSProp**.
- Understand the concepts of **First Moment** and **Second Moment**.
- Learn the Adam update equations.
- Understand **Bias Correction**.
- Learn why Adam is the default optimizer in modern Deep Learning.
- Understand Adam's advantages and limitations.

---

# 1. Why Was Adam Introduced?

Previously, we studied two advanced optimizers.

## Momentum

Momentum

- remembers previous gradients,
- accelerates optimization,
- reduces oscillations.

However,

Momentum **does not adapt the learning rate**.

---

## RMSProp

RMSProp

- adapts the learning rate,
- adjusts updates for each parameter individually.

However,

RMSProp **does not remember previous directions**.

---

Researchers asked

> **Why not combine both Momentum and RMSProp into one optimizer?**

The answer is

# Adam Optimizer

Adam combines

```text
Momentum

+

RMSProp

↓

Adam
```

Thus,

Adam inherits the strengths of both algorithms.

---

# 2. What Does Adam Mean?

Adam stands for

> **Adaptive Moment Estimation**

The name can be understood as follows.

### Adaptive

The learning rate automatically adjusts for every parameter.

---

### Moment

Adam estimates statistical moments of the gradients.

There are two moments.

- First Moment
- Second Moment

---

### Estimation

These moments are estimated during training.

---

# 3. The Main Idea Behind Adam

Adam keeps track of two quantities.

## First Moment

Stores

```text
Average Gradient
```

This idea comes from **Momentum**.

---

## Second Moment

Stores

```text
Average Squared Gradient
```

This idea comes from **RMSProp**.

---

Therefore,

Adam remembers both

- the direction of movement,
- the magnitude of recent gradients.

---

# 4. Variables Used in Adam

Adam introduces two variables.

---

## First Moment

$$
\boxed{m}
$$

Stores

- Average Gradient
- Optimizer Momentum

---

## Second Moment

$$
\boxed{v}
$$

Stores

- Average Squared Gradient
- Adaptive Learning Rate Information

---

# 5. Adam Update Equations

Adam performs several steps.

---

## Step 1 – Compute Gradient

$$
\boxed{ g = \frac{\partial L}{\partial w} }
$$

where

- \(g\) = Current Gradient

---

## Step 2 – Update First Moment

$$
\boxed{ m = \beta_1m + (1-\beta_1)g }
$$

where

- \(m\) = First Moment
- \(\beta_1\) = Momentum Decay Rate

---

## Step 3 – Update Second Moment

$$
\boxed{ v = \beta_2v + (1-\beta_2)g^2 }
$$

where

- \(v\) = Second Moment
- \(\beta_2\) = RMSProp Decay Rate

Notice

The gradient is squared,

just like RMSProp.

---

# 6. Why is Bias Correction Needed?

Initially,

both

```text
m = 0

v = 0
```

During the first few iterations,

their values become biased toward zero.

This causes

- inaccurate first moment,
- inaccurate second moment,
- incorrect weight updates.

Adam corrects this using **Bias Correction**.

---

# 7. Bias-Corrected First Moment

The corrected first moment is

$$
\boxed{ \hat m = \frac{m} {1-\beta_1^t} }
$$

where

- \(t\) = Current Iteration Number

This removes the bias from the first moment estimate.

---

# 8. Bias-Corrected Second Moment

Similarly,

$$
\boxed{ \hat v = \frac{v} {1-\beta_2^t} }
$$

This removes the bias from the second moment estimate.

---

# 9. Final Weight Update Equation

After bias correction,

Adam updates the weights using

$$
\boxed{ w_{new} = w_{old} - \eta \frac{\hat m} {\sqrt{\hat v}+\epsilon} }
$$

where

- \(\eta\) = Learning Rate
- \(\hat m\) = Bias-Corrected First Moment
- \(\hat v\) = Bias-Corrected Second Moment
- \(\epsilon\) = Small Constant

Notice

The numerator comes from **Momentum**.

The denominator comes from **RMSProp**.

---

# 10. Typical Hyperparameters

Most Deep Learning libraries use the following default values.

---

Learning Rate

```text
η = 0.001
```

---

First Moment Decay

```text
β₁ = 0.9
```

---

Second Moment Decay

```text
β₂ = 0.999
```

---

Small Constant

```text
ε = 10⁻⁸
```

These values work well for most applications.

---

# 11. Complete Workflow

```text
Mini-Batch

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Backpropagation

↓

Gradient

↓

Update First Moment (m)

↓

Update Second Moment (v)

↓

Bias Correction

↓

Adaptive Learning Rate

↓

Update Weights

↓

Next Mini-Batch
```

---

# 12. Real-Life Analogy

Imagine driving a smart car.

The car

- remembers its previous speed,
- automatically adjusts its speed according to road conditions.

Similarly,

Adam

- remembers previous gradients (Momentum),
- adapts learning rates (RMSProp).

This produces smoother and faster optimization.

---

# 13. Advantages of Adam

## 1. Fast Convergence

Adam usually reaches good solutions quickly.

---

## 2. Adaptive Learning Rate

Every parameter receives its own effective learning rate.

---

## 3. Uses Momentum

Previous gradients accelerate optimization.

---

## 4. Reduced Oscillations

Momentum smooths the optimization path.

---

## 5. Minimal Hyperparameter Tuning

Default settings often work well.

---

## 6. Excellent for Deep Learning

Widely used for

- CNNs
- RNNs
- LSTMs
- Transformers
- Large Language Models

---

# 14. Disadvantages of Adam

- More memory is required because Adam stores two additional variables (\(m\) and \(v\)).
- Computationally more expensive than SGD.
- Sometimes generalizes slightly worse than SGD with Momentum on certain vision tasks.

---

# 15. Momentum vs RMSProp vs Adam

| Feature | Momentum | RMSProp | Adam |
|----------|----------|----------|------|
| Uses Previous Gradients | ✅ | ❌ | ✅ |
| Adaptive Learning Rate | ❌ | ✅ | ✅ |
| Stores First Moment | ✅ | ❌ | ✅ |
| Stores Second Moment | ❌ | ✅ | ✅ |
| Bias Correction | ❌ | ❌ | ✅ |
| Fast Convergence | ✅ | ✅ | ✅ |
| Widely Used Today | ❌ | ❌ | ✅ |

---

# 16. Which Optimizer Should You Use?

General recommendations.

| Scenario | Recommended Optimizer |
|-----------|-----------------------|
| Beginner Projects | Adam |
| CNNs | Adam |
| NLP | Adam |
| Transformers | AdamW |
| Research Baselines | Adam |
| Some Computer Vision Tasks | SGD + Momentum |

---

# 17. Complete Adam Pipeline

```text
Initialize Weights

↓

Forward Propagation

↓

Prediction

↓

Loss

↓

Backpropagation

↓

Gradient

↓

Compute First Moment (m)

↓

Compute Second Moment (v)

↓

Bias Correction

↓

Adaptive Learning Rate

↓

Update Weights

↓

Repeat
```

---

# Interview Questions

## Q1. What does Adam stand for?

**Answer**

Adaptive Moment Estimation.

---

## Q2. Which two optimizers are combined in Adam?

**Answer**

Momentum and RMSProp.

---

## Q3. What is the First Moment?

**Answer**

The exponentially weighted moving average of gradients.

---

## Q4. What is the Second Moment?

**Answer**

The exponentially weighted moving average of squared gradients.

---

## Q5. Why is Bias Correction required?

**Answer**

Because the first and second moment estimates start from zero and are biased during the initial iterations. Bias correction removes this bias.

---

## Q6. What are the default values of β₁ and β₂?

**Answer**

- β₁ = 0.9
- β₂ = 0.999

---

## Q7. Why is Adam so popular?

**Answer**

Because it combines the advantages of Momentum and RMSProp, converges quickly, adapts the learning rate automatically, and usually works well with default hyperparameters.

---

# Summary

Adam (Adaptive Moment Estimation) is one of the most widely used optimization algorithms in modern Deep Learning.

It combines

- **Momentum**, which remembers previous gradients and accelerates optimization,
- **RMSProp**, which adapts the learning rate for each parameter.

Adam also introduces **Bias Correction** to improve the accuracy of its estimates during the early stages of training.

Because of its fast convergence, adaptive learning rates, and minimal tuning requirements, Adam has become the default optimizer in frameworks such as TensorFlow and PyTorch.

---

# Key Takeaways

✔ Adam stands for **Adaptive Moment Estimation**.

✔ Adam combines **Momentum** and **RMSProp**.

✔ Adam maintains two moving averages:

- First Moment (\(m\))
- Second Moment (\(v\))

✔ Adam performs Bias Correction using

$$
\hat m=\frac{m}{1-\beta_1^t}
$$

and

$$
\hat v=\frac{v}{1-\beta_2^t}
$$

✔ Final Weight Update

$$
w_{new} = w_{old} - \eta \frac{\hat m} {\sqrt{\hat v}+\epsilon}
$$

✔ Default Hyperparameters

- Learning Rate = 0.001
- β₁ = 0.9
- β₂ = 0.999
- ε = 10⁻⁸

✔ Adam converges quickly, adapts learning rates automatically, reduces oscillations, and is the most commonly used optimizer in modern Deep Learning.
