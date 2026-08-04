# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 10 – RMSProp (Root Mean Square Propagation)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why RMSProp was introduced.
- Learn the limitations of Gradient Descent and Momentum.
- Understand the concept of an **Adaptive Learning Rate**.
- Learn the RMSProp update equations.
- Understand the moving average of squared gradients.
- Learn why RMSProp works well for deep neural networks.
- Understand the real-world intuition behind RMSProp.

---

# 1. Why Was RMSProp Introduced?

Previously, we studied

- Gradient Descent
- Momentum

Momentum improves learning by

- remembering previous updates,
- reducing oscillations,
- accelerating convergence.

However,

Momentum still has one important limitation.

---

## Problem – Fixed Learning Rate

Momentum still uses

$$
\boxed{\eta}
$$

which is the **same learning rate for every weight**.

Suppose

```text
Weight 1

Gradient = 100

Weight 2

Gradient = 0.05
```

Using the same learning rate for both weights is not ideal.

- Weight 1 may receive updates that are too large.
- Weight 2 may receive updates that are too small.

We need an optimizer that automatically adjusts the learning rate for each parameter.

This idea is called an

> **Adaptive Learning Rate**

---

# 2. What is an Adaptive Learning Rate?

Instead of using one learning rate for all parameters,

RMSProp gives **each weight its own effective learning rate**.

Therefore,

- Large gradients → Smaller updates
- Small gradients → Larger updates

This allows every parameter to learn at an appropriate speed.

---

# 3. What is RMSProp?

## Definition

RMSProp (Root Mean Square Propagation) is an optimization algorithm that **adapts the learning rate for each parameter** by maintaining an exponentially weighted moving average of the **squared gradients**.

Instead of treating every parameter equally,

RMSProp adjusts each update according to the recent gradient history of that parameter.

---

# 4. The Main Idea

Suppose

```text
Weight A

Large Gradients
```

RMSProp says

```text
Reduce the learning rate.
```

---

Suppose

```text
Weight B

Small Gradients
```

RMSProp says

```text
Increase the effective learning rate.
```

Thus,

parameters with unstable gradients receive smaller updates,

while parameters with stable or small gradients receive relatively larger updates.

---

# 5. RMSProp Introduces a New Variable

RMSProp introduces

$$
\boxed{s}
$$

called the

**Running Average of Squared Gradients**.

This variable stores information about

- recent gradient magnitudes,
- average squared gradients.

Notice

It remembers the **size** of gradients,

not their direction.

---

# 6. RMSProp Update Equations

RMSProp performs two updates.

---

## Step 1 – Update Running Average

$$
\boxed{ s = \beta s + (1-\beta) \left( \frac{\partial L}{\partial w} \right)^2 }
$$

where

- \(s\) = Running Average of Squared Gradients
- \(\beta\) = Decay Rate
- \(\frac{\partial L}{\partial w}\) = Current Gradient

Notice

The gradient is squared.

---

## Why Square the Gradient?

Suppose

Gradient

```text
-5
```

Squared Gradient

```text
25
```

Similarly,

```text
Gradient = +5

↓

Squared Gradient = 25
```

Therefore,

squaring

- removes the sign,
- measures only the magnitude,
- emphasizes larger gradients.

---

## Step 2 – Update Weights

$$
\boxed{ w_{new} = w_{old} - \frac{\eta} {\sqrt{s}+\epsilon} \frac{\partial L}{\partial w} }
$$

where

- \(\eta\) = Learning Rate
- \(\sqrt{s}\) = Root Mean Square of Recent Gradients
- \(\epsilon\) = Small Constant

---

# 7. Why Divide by \(\sqrt{s}\)?

Suppose

Recent gradients have been very large.

Then

```text
Large Gradient

↓

Large s

↓

Large √s

↓

Smaller Update
```

---

Now suppose

Recent gradients have been very small.

Then

```text
Small Gradient

↓

Small s

↓

Small √s

↓

Larger Update
```

This is the adaptive learning rate mechanism.

---

# 8. What is ε (Epsilon)?

The symbol

$$
\boxed{\epsilon}
$$

is a very small positive number.

Typical value

```text
10^-8
```

Purpose

To prevent division by zero.

Suppose

$$
s=0
$$

Then

$$
\frac{\eta}{\sqrt{s}} = \frac{\eta}{0}
$$

which is undefined.

Adding ε ensures

$$
\sqrt{s}+\epsilon>0
$$

always.

---

# 9. Complete Workflow

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

Update Running Average (s)

↓

Compute Adaptive Learning Rate

↓

Update Weights

↓

Next Mini-Batch
```

---

# 10. Real-Life Analogy

Imagine driving a car.

### Smooth Road

You drive faster.

---

### Rough Road

You automatically reduce your speed.

---

Similarly,

RMSProp behaves as follows.

Large gradients

↓

Drive slowly

↓

Small updates

---

Small gradients

↓

Drive faster

↓

Larger updates

Thus,

the optimizer automatically adjusts its speed according to the terrain.

---

# 11. Advantages of RMSProp

## 1. Adaptive Learning Rate

Each parameter receives an appropriate update size.

---

## 2. Faster Convergence

Especially effective for deep neural networks.

---

## 3. Reduced Oscillations

Large gradients are automatically dampened.

---

## 4. Better Stability

Training becomes smoother than ordinary Gradient Descent.

---

## 5. Suitable for Non-Stationary Problems

RMSProp continuously adapts during training.

---

# 12. Disadvantages of RMSProp

- More complex than Gradient Descent.
- Requires additional hyperparameters.
- Does not include Momentum by itself.
- Adam generally performs better because it combines Momentum and RMSProp.

---

# 13. Gradient Descent vs Momentum vs RMSProp

| Feature | Gradient Descent | Momentum | RMSProp |
|----------|------------------|----------|----------|
| Uses Current Gradient | ✅ | ✅ | ✅ |
| Uses Previous Updates | ❌ | ✅ | ❌ |
| Uses Velocity | ❌ | ✅ | ❌ |
| Stores Squared Gradients | ❌ | ❌ | ✅ |
| Adaptive Learning Rate | ❌ | ❌ | ✅ |
| Reduces Oscillations | ❌ | ✅ | ✅ |
| Faster Convergence | ❌ | ✅ | ✅ |

---

# 14. Why Was Adam Created?

Momentum remembers

```text
Previous Updates
```

RMSProp remembers

```text
Squared Gradients
```

Researchers realized

> Why not combine both?

The result is

**Adam Optimizer**

which combines

- Momentum
- RMSProp

into one optimizer.

---

# Interview Questions

## Q1. Why was RMSProp introduced?

**Answer**

To provide an adaptive learning rate for each parameter instead of using one fixed learning rate.

---

## Q2. What does RMSProp store?

**Answer**

An exponentially weighted moving average of squared gradients.

---

## Q3. Why are gradients squared?

**Answer**

Squaring removes the sign and measures only the magnitude of the gradients.

---

## Q4. Why do we divide by \(\sqrt{s}\)?

**Answer**

To reduce updates for parameters with large gradients and allow relatively larger updates for parameters with small gradients.

---

## Q5. What is the purpose of ε?

**Answer**

To prevent division by zero during weight updates.

---

## Q6. What is the typical value of ε?

**Answer**

$$
\boxed{10^{-8}}
$$

---

# Summary

RMSProp improves optimization by introducing an **adaptive learning rate** for each parameter.

Instead of updating every weight with the same learning rate,

RMSProp adjusts the update size according to the recent history of squared gradients.

Parameters with consistently large gradients receive smaller updates,

while parameters with smaller gradients receive relatively larger updates.

This leads to faster, more stable convergence and makes RMSProp well suited for deep neural networks.

---

# Key Takeaways

✔ RMSProp stands for **Root Mean Square Propagation**.

✔ RMSProp introduces the variable

$$
\boxed{s}
$$

which stores the exponentially weighted moving average of squared gradients.

✔ RMSProp automatically adjusts the learning rate for each parameter.

✔ Large gradients receive smaller updates.

✔ Small gradients receive larger updates.

✔ The update equations are

Running Average

$$
s = \beta s + (1-\beta) \left( \frac{\partial L}{\partial w} \right)^2
$$

Weight Update

$$
w_{new} = w_{old} - \frac{\eta} {\sqrt{s}+\epsilon} \frac{\partial L}{\partial w}
$$

✔ ε prevents division by zero.

✔ RMSProp converges faster and more smoothly than ordinary Gradient Descent.

✔ RMSProp is one of the two main components used to build the **Adam Optimizer**.
