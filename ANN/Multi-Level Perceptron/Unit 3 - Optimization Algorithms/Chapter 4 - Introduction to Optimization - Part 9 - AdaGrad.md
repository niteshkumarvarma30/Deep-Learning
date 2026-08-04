# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 9 – AdaGrad (Adaptive Gradient Algorithm)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why AdaGrad was introduced.
- Learn the limitations of Gradient Descent and Momentum.
- Understand the concept of an **Adaptive Learning Rate**.
- Learn how AdaGrad automatically adjusts the learning rate.
- Understand the mathematical equations of AdaGrad.
- Learn the advantages and limitations of AdaGrad.
- Understand why RMSProp was developed as an improvement over AdaGrad.

---

# 1. Why Was AdaGrad Introduced?

Previously, we studied

- Gradient Descent
- Momentum
- Nesterov Accelerated Gradient (NAG)

All of these optimizers use a **fixed learning rate**.

$$
\boxed{\eta}
$$

This means every parameter is updated using the same learning rate.

Suppose we have two weights.

```text
Weight W₁

Gradient = 120

Weight W₂

Gradient = 0.02
```

Using the same learning rate for both weights is not ideal.

- W₁ may take updates that are too large.
- W₂ may take updates that are too small.

We need an optimizer that automatically adjusts the learning rate for each parameter.

This idea led to **AdaGrad**.

---

# 2. What is AdaGrad?

## Definition

**AdaGrad (Adaptive Gradient Algorithm)** is an optimization algorithm that automatically adjusts the learning rate for each parameter based on the history of its gradients.

Instead of using one fixed learning rate,

AdaGrad assigns a different effective learning rate to every parameter.

---

# 3. The Main Idea Behind AdaGrad

AdaGrad follows a simple principle.

- Parameters with **large gradients** should receive **smaller future updates**.
- Parameters with **small gradients** should receive **larger future updates**.

This allows different parameters to learn at different speeds.

---

# 4. AdaGrad Introduces a New Variable

AdaGrad introduces

$$
\boxed{G}
$$

called the

**Accumulated Sum of Squared Gradients**.

Unlike RMSProp,

AdaGrad continuously accumulates squared gradients throughout training.

---

# 5. AdaGrad Update Equations

AdaGrad performs three main steps.

---

## Step 1 – Compute Gradient

$$
\boxed{ g = \frac{\partial L}{\partial w} }
$$

where

- \(g\) = Current Gradient

---

## Step 2 – Update the Accumulated Squared Gradient

$$
\boxed{ G = G + g^2 }
$$

where

- \(G\) = Sum of all previous squared gradients.

Notice

AdaGrad never removes old gradients.

The accumulated value keeps increasing.

---

## Step 3 – Update the Weight

$$
\boxed{ w_{new} = w_{old} - \frac{\eta} {\sqrt{G}+\epsilon} g }
$$

where

- \(w\) = Weight
- \(\eta\) = Initial Learning Rate
- \(G\) = Accumulated Squared Gradients
- \(\epsilon\) = Small Constant (typically \(10^{-8}\))

---

# 6. Why Does AdaGrad Work?

Suppose

A parameter repeatedly receives large gradients.

Then

```text
Large Gradient

↓

Large G

↓

Large √G

↓

Smaller Learning Rate

↓

Smaller Weight Update
```

---

Now suppose

A parameter receives small gradients.

Then

```text
Small Gradient

↓

Small G

↓

Small √G

↓

Larger Learning Rate

↓

Larger Weight Update
```

Thus,

AdaGrad automatically adjusts the learning rate for every parameter.

---

# 7. Numerical Example

Suppose

Learning Rate

```text
η = 0.01
```

Current Gradient

```text
g = 5
```

Current Accumulated Gradient

```text
G = 100
```

Weight update

$$
\Delta w = \frac{0.01} {\sqrt{100}} \times5 = 0.005
$$

Suppose after many iterations

```text
G = 10000
```

Then

$$
\Delta w = \frac{0.01} {100} \times5 = 0.0005
$$

Notice

As training continues,

the update becomes much smaller.

---

# 8. Real-Life Analogy

Imagine two students learning mathematics.

---

## Student A

Makes many mistakes.

The teacher slows down,

explains carefully,

and takes smaller steps.

---

## Student B

Makes very few mistakes.

The teacher progresses more quickly.

AdaGrad behaves similarly.

Each parameter learns at its own pace.

---

# 9. Advantages of AdaGrad

## 1. Adaptive Learning Rate

Each parameter receives its own learning rate.

---

## 2. Good for Sparse Data

AdaGrad performs well for datasets where many features occur infrequently.

Examples

- Text Classification
- Natural Language Processing
- Recommendation Systems

---

## 3. Less Manual Tuning

The optimizer automatically adjusts updates.

---

## 4. Simple to Implement

AdaGrad is mathematically straightforward.

---

# 10. Biggest Limitation of AdaGrad

AdaGrad keeps accumulating squared gradients.

$$
G = g_1^2 + g_2^2 + g_3^2 +\cdots
$$

Therefore,

\(G\) continuously increases.

```text
Training Progress

↓

G Increases

↓

√G Increases

↓

Effective Learning Rate Decreases

↓

Weight Updates Become Tiny
```

Eventually,

the learning rate becomes almost zero.

Training nearly stops.

This is called the

> **Learning Rate Decay Problem of AdaGrad**

---

# 11. Why Was RMSProp Invented?

Researchers observed AdaGrad's limitation.

Instead of storing

```text
All Previous Squared Gradients
```

RMSProp stores

```text
Exponentially Weighted Moving Average (EWMA)

of Squared Gradients
```

Older gradients gradually lose influence.

Therefore,

the learning rate does **not** shrink indefinitely.

---

# 12. AdaGrad vs RMSProp

| Feature | AdaGrad | RMSProp |
|----------|----------|----------|
| Adaptive Learning Rate | ✅ | ✅ |
| Stores Squared Gradients | ✅ | ✅ |
| Uses EWMA | ❌ | ✅ |
| Learning Rate Keeps Shrinking | ✅ | ❌ |
| Better for Long Training | ❌ | ✅ |
| Modern Usage | Limited | Common |

---

# 13. Visualization

```text
Gradient

↓

Square Gradient

↓

Accumulate Forever

↓

Adaptive Learning Rate

↓

Weight Update
```

Unlike RMSProp,

AdaGrad never forgets old gradients.

---

# 14. Evolution from AdaGrad to RMSProp

```text
Gradient Descent

↓

Fixed Learning Rate

↓

AdaGrad

↓

Adaptive Learning Rate

↓

Problem

Learning Rate → Almost Zero

↓

RMSProp

↓

Uses EWMA Instead of Full Accumulation

↓

Stable Learning Rate
```

---

# Interview Questions

## Q1. What does AdaGrad stand for?

**Answer**

Adaptive Gradient Algorithm.

---

## Q2. Why was AdaGrad introduced?

**Answer**

To automatically assign different learning rates to different parameters.

---

## Q3. What does AdaGrad store?

**Answer**

The accumulated sum of squared gradients.

---

## Q4. Why are gradients squared?

**Answer**

Squaring removes the sign and measures only the magnitude of the gradients.

---

## Q5. What is AdaGrad's biggest limitation?

**Answer**

The accumulated squared gradients keep increasing, causing the effective learning rate to become extremely small.

---

## Q6. Which optimizer solved AdaGrad's limitation?

**Answer**

RMSProp.

---

## Q7. Where is AdaGrad useful?

**Answer**

AdaGrad works well for sparse datasets such as text processing, recommendation systems, and natural language processing.

---

# Summary

AdaGrad (Adaptive Gradient Algorithm) was the first optimization algorithm to introduce the concept of **adaptive learning rates**.

Instead of using one fixed learning rate for all parameters, AdaGrad adjusts the learning rate individually based on the accumulated history of squared gradients.

This makes AdaGrad particularly effective for sparse datasets.

However, because it continuously accumulates squared gradients, the effective learning rate keeps decreasing during training and may eventually become too small.

This limitation led to the development of **RMSProp**, which replaces the accumulated sum with an **Exponentially Weighted Moving Average (EWMA)**.

---

# Key Takeaways

✔ AdaGrad stands for **Adaptive Gradient Algorithm**.

✔ AdaGrad automatically adjusts the learning rate for each parameter.

✔ AdaGrad introduces

$$
\boxed{G}
$$

which stores the accumulated sum of squared gradients.

✔ AdaGrad Update Equations

Gradient

$$
g=\frac{\partial L}{\partial w}
$$

Accumulated Gradient

$$
G=G+g^2
$$

Weight Update

$$
w_{new} = w_{old} - \frac{\eta} {\sqrt{G}+\epsilon} g
$$

✔ Parameters with large gradients receive smaller future updates.

✔ Parameters with small gradients receive relatively larger updates.

✔ AdaGrad is effective for sparse datasets.

✔ AdaGrad's main limitation is that its learning rate continually decreases.

✔ RMSProp was developed to solve AdaGrad's learning rate decay problem using **EWMA**.
