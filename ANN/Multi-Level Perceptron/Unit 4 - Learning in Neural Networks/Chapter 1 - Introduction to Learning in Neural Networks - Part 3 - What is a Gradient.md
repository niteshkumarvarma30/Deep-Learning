# Unit 4 – Learning in Neural Networks

# Chapter 1 – Introduction to Learning in Neural Networks

## Part 3 – What is a Gradient?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a gradient is.
- Learn why gradients are important in neural networks.
- Understand the relationship between gradients and derivatives.
- Learn how gradients tell the optimizer **which direction** and **how much** to update the weights.
- Build intuition before studying the mathematical derivation of Backpropagation.

---

# 1. What is a Gradient?

Imagine you are standing on a hill.

Your goal is to reach the lowest point of the hill.

Two questions immediately arise:

1. Which direction should you move?
2. How steep is the hill?

These are exactly the two questions that a **gradient** answers in machine learning.

A gradient tells us

- **which direction** a function changes most rapidly, and
- **how quickly** it changes.

In neural networks, the function is usually the **Loss Function**.

---

# 2. Why Do Neural Networks Need Gradients?

Suppose a neural network has completed Forward Propagation.

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss = 8.5
```

The loss is high.

This means the prediction is poor.

Now we want to improve the model.

Questions arise:

- Should the weights increase?
- Should the weights decrease?
- Which weights should change?
- By how much?

The neural network cannot answer these questions by looking only at the loss value.

It needs additional information.

This information is called the **Gradient**.

---

# 3. A Simple Mathematical Example

Suppose the loss depends on only one weight.

$$
L(w)=w^2
$$

where

- \(w\) = Weight
- \(L(w)\) = Loss

Now calculate the loss for different weights.

| Weight (\(w\)) | Loss (\(L(w)\)) |
|---------------:|----------------:|
| -3 | 9 |
| -2 | 4 |
| -1 | 1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |

The graph looks like

```text
Loss

^

|        •

|      •   •

|    •       •

|  •           •

|________________________> Weight
```

The minimum loss occurs at

```text
w = 0
```

---

# 4. What Happens if the Weight Changes?

Suppose

```text
Weight = 3
```

Loss

```text
9
```

Now decrease the weight slightly.

```text
Weight = 2.9
```

The loss decreases.

Decrease it again.

```text
Weight = 2.8
```

The loss decreases further.

This tells us

> Moving toward the left reduces the loss.

But how does the neural network know this?

Because of the **Gradient**.

---

# 5. The Gradient is the Slope

In calculus,

the gradient is simply the **derivative** of a function.

For a single variable,

$$
\boxed{\text{Gradient} = \frac{dL}{dw}}
$$

This derivative measures

> **How much the loss changes when the weight changes slightly.**

---

# 6. Interpreting the Gradient

Suppose

$$
\frac{dL}{dw}=5
$$

This means

A small increase in the weight causes the loss to increase rapidly.

---

Now suppose

$$
\frac{dL}{dw}=-5
$$

This means

Increasing the weight causes the loss to decrease.

---

Suppose

$$
\frac{dL}{dw}=0
$$

This means

The slope is flat.

The weight may already be at a minimum (or another stationary point).

---

# 7. Understanding the Sign of the Gradient

The sign of the gradient tells us the direction.

---

## Positive Gradient

```text
Gradient > 0
```

As the weight increases,

the loss increases.

To reduce the loss,

the optimizer should decrease the weight.

---

## Negative Gradient

```text
Gradient < 0
```

As the weight increases,

the loss decreases.

To reduce the loss,

the optimizer should increase the weight.

---

## Zero Gradient

```text
Gradient = 0
```

The loss is not changing at that point.

This often indicates a stationary point.

---

# 8. Understanding the Magnitude of the Gradient

The magnitude tells us how steep the loss surface is.

---

## Small Gradient

```text
Gradient = 0.02
```

The loss changes slowly.

Only a small adjustment is required.

---

## Large Gradient

```text
Gradient = 25
```

The loss changes rapidly.

A larger correction is required.

---

# 9. Real-Life Analogy

Imagine riding a bicycle down a hill.

If the hill is very steep,

your speed increases rapidly.

If the road is almost flat,

your speed changes very little.

The steepness of the hill is analogous to the **Gradient**.

```text
Steep Hill

↓

Large Gradient

↓

Large Weight Update
```

```text
Flat Hill

↓

Small Gradient

↓

Small Weight Update
```

---

# 10. Gradients in Neural Networks

A neural network contains many parameters.

Example

```text
Input

↓

Weight W₁

↓

Hidden Layer

↓

Weight W₂

↓

Output Layer
```

Backpropagation computes

$$
\frac{\partial L}{\partial W_1}
$$

and

$$
\frac{\partial L}{\partial W_2}
$$

Each gradient tells us

> **How sensitive the loss is to that particular weight.**

---

# 11. Why Do We Use Partial Derivatives?

A neural network has many parameters.

The loss depends on all of them.

For example,

$$
L=L(W_1,W_2,b_1,b_2)
$$

Therefore,

we compute

$$
\frac{\partial L}{\partial W_1}
$$

$$
\frac{\partial L}{\partial W_2}
$$

$$
\frac{\partial L}{\partial b_1}
$$

$$
\frac{\partial L}{\partial b_2}
$$

Each partial derivative measures

> **How the loss changes when only one parameter changes while all others remain fixed.**

---

# 12. Why Are Gradients So Important?

Without gradients,

the optimizer does not know

- which direction to move,
- how much to move.

Gradients provide both pieces of information.

The optimizer simply follows the gradient information to reduce the loss.

---

# 13. Complete Learning Pipeline

The complete learning process now becomes

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss

↓

Gradient

↓

Optimizer

↓

Updated Weights

↓

Repeat
```

Later,

we will learn that **Backpropagation is the algorithm that computes these gradients efficiently.**

---

# 14. Gradient vs Backpropagation

Many books state

> "Backpropagation computes gradients."

This is correct.

However,

it is important to distinguish the two concepts.

### Gradient

The mathematical quantity.

```text
Derivative

↓

Result
```

---

### Backpropagation

The algorithm used to compute gradients efficiently.

```text
Loss

↓

Backward Pass

↓

Gradients
```

Therefore,

```text
Gradient

↓

The Result

Backpropagation

↓

The Process That Computes It
```

---

# Interview Questions

## Q1. What is a gradient?

**Answer**

A gradient is the derivative (or partial derivative) of the loss function with respect to a parameter. It indicates the direction and rate at which the loss changes.

---

## Q2. Why are gradients important?

**Answer**

Gradients tell the optimizer how each parameter should be updated to reduce the loss.

---

## Q3. What does a positive gradient indicate?

**Answer**

A positive gradient means the loss increases as the parameter increases. To reduce the loss, the parameter should be decreased.

---

## Q4. What does a negative gradient indicate?

**Answer**

A negative gradient means the loss decreases as the parameter increases. To reduce the loss, the parameter should be increased.

---

## Q5. What is the difference between a gradient and Backpropagation?

**Answer**

A gradient is the mathematical quantity (the derivative), whereas Backpropagation is the algorithm used to compute gradients efficiently for all parameters in the neural network.

---

# Summary

A **gradient** measures how the loss changes when a parameter changes.

It provides two essential pieces of information:

- **Direction** in which the parameter should move.
- **Magnitude** of the required update.

Gradients are the mathematical foundation of neural network learning.

Backpropagation computes these gradients, and the optimizer uses them to update the weights.

Without gradients, a neural network would have no systematic way to improve its predictions.

---

# Key Takeaways

✔ A gradient is the derivative of the loss with respect to a parameter.

✔ Gradients indicate both the **direction** and **magnitude** of parameter updates.

✔ Positive gradients suggest decreasing the parameter.

✔ Negative gradients suggest increasing the parameter.

✔ The magnitude of the gradient reflects the steepness of the loss surface.

✔ Neural networks use **partial derivatives** because the loss depends on many parameters.

✔ Backpropagation computes gradients.

✔ Optimizers use gradients to update weights and minimize the loss.

---

## Next Part

**Part 4 – Computational Graph and the Chain Rule**

In the next chapter, we will study the **Computational Graph** and the **Chain Rule**, which form the mathematical foundation of Backpropagation and enable efficient gradient computation across deep neural networks.
