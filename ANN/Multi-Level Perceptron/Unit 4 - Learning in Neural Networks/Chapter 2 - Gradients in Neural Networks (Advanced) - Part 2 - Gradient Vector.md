# Unit 4 – Learning in Neural Networks

# Chapter 2 – Gradients in Neural Networks (Advanced)

## Part 2 – Gradient Vector

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a Gradient Vector is.
- Learn why a single derivative is not enough for neural networks.
- Understand the **∇ (Nabla)** notation.
- Learn how multiple partial derivatives combine into a vector.
- Understand why optimization algorithms update all parameters simultaneously.

---

# 1. Recap

In the previous chapter, we learned that neural networks use **partial derivatives** because the loss depends on many parameters.

Suppose the loss function is

$$
L=L(W_1,W_2,b)
$$

Backpropagation computes

$$
\frac{\partial L}{\partial W_1}
$$

$$
\frac{\partial L}{\partial W_2}
$$

$$
\frac{\partial L}{\partial b}
$$

These are three different partial derivatives.

Now ask yourself

> **How do we represent all these derivatives together?**

Instead of storing them separately,

we combine them into a single mathematical object called the **Gradient Vector**.

---

# 2. Why Do We Need a Gradient Vector?

Imagine a neural network with

```text
1 Weight
```

Only one derivative is needed.

Now imagine

```text
100 Weights
```

Now we need

```text
100 Partial Derivatives
```

Now imagine a deep neural network with

```text
10 Million Parameters
```

Backpropagation computes

```text
10 Million Partial Derivatives
```

Writing them individually is impractical.

Instead,

we store all of them together in one vector.

---

# 3. What is a Vector?

Before understanding the Gradient Vector,

let us recall what a vector is.

A vector is simply an ordered collection of numbers.

Example

$$
\begin{bmatrix} 2\\ 5\\ 7 \end{bmatrix}
$$

Instead of storing three separate values,

the vector stores them together.

Similarly,

the Gradient Vector stores all gradients together.

---

# 4. Definition of Gradient Vector

Suppose

$$
L=L(W_1,W_2,b)
$$

The Gradient Vector is

$$
\boxed{ \nabla L = \begin{bmatrix} \frac{\partial L}{\partial W_1}\\[6pt] \frac{\partial L}{\partial W_2}\\[6pt] \frac{\partial L}{\partial b} \end{bmatrix} }
$$

Instead of writing three separate partial derivatives,

we write one vector.

Every element of this vector corresponds to one trainable parameter.

---

# 5. The Nabla Symbol (∇)

The symbol

$$
\boxed{\nabla}
$$

is called

- **Nabla**
- **Del Operator**

When applied to a function,

it means

> **Compute all partial derivatives of the function.**

Example

$$
\nabla L
$$

means

Compute the gradient of the loss with respect to all trainable parameters.

---

# 6. A Numerical Example

Suppose

$$
L = W_1^2 + 2W_2^2 + b^2
$$

Compute the partial derivatives.

---

## Step 1

With respect to \(W_1\)

$$
\frac{\partial L}{\partial W_1} = 2W_1
$$

---

## Step 2

With respect to \(W_2\)

$$
\frac{\partial L}{\partial W_2} = 4W_2
$$

---

## Step 3

With respect to \(b\)

$$
\frac{\partial L}{\partial b} = 2b
$$

---

Now combine them.

$$
\boxed{ \nabla L = \begin{bmatrix} 2W_1\\[6pt] 4W_2\\[6pt] 2b \end{bmatrix} }
$$

This is the Gradient Vector.

---

# 7. Interpretation of the Gradient Vector

Each element represents the sensitivity of the loss to one parameter.

```text
Gradient Vector

↓

∂L/∂W₁

↓

∂L/∂W₂

↓

∂L/∂b
```

Each value answers

> **How much will the loss change if this particular parameter changes?**

---

# 8. Why Is It Called a Vector?

A vector has two important properties.

- Magnitude
- Direction

Suppose

$$
\nabla L = \begin{bmatrix} 3\\ 4 \end{bmatrix}
$$

This vector points in the direction of the **greatest increase** of the loss.

Since our objective is to minimize the loss,

we move in the opposite direction.

This is why Gradient Descent updates the parameters using

$$
-\nabla L
$$

instead of

$$
+\nabla L
$$

---

# 9. Gradient Descent Using the Gradient Vector

For a single parameter,

Gradient Descent is

$$
w = w - \eta \frac{dL}{dw}
$$

For multiple parameters,

we use the Gradient Vector.

$$
\boxed{ \theta = \theta - \eta \nabla L }
$$

where

$$
\theta = \begin{bmatrix} W_1\\ W_2\\ b \end{bmatrix}
$$

Notice

All parameters are updated **simultaneously**.

---

# 10. Real-Life Analogy

Imagine using a GPS.

Instead of saying

```text
Walk North
```

or

```text
Walk East
```

the GPS combines both directions.

```text
Walk

20 m North

+

10 m East
```

This combined instruction is a vector.

Similarly,

the Gradient Vector tells the optimizer

how every parameter should move together.

---

# 11. Gradient Vector in Neural Networks

A modern neural network may contain

```text
Millions of Weights

+

Millions of Biases
```

Backpropagation computes

one partial derivative for every parameter.

These derivatives are collected into one Gradient Vector.

The optimizer then updates all parameters simultaneously.

---

# 12. Gradient vs Gradient Vector

Many beginners confuse these two terms.

---

## Gradient

Often refers to

one partial derivative.

Example

$$
\frac{\partial L}{\partial W}
$$

---

## Gradient Vector

Contains

all partial derivatives.

Example

$$
\nabla L = \begin{bmatrix} \frac{\partial L}{\partial W_1}\\ \frac{\partial L}{\partial W_2}\\ \frac{\partial L}{\partial b} \end{bmatrix}
$$

In Deep Learning,

when people say

> "Compute the gradient"

they usually mean

> **Compute the Gradient Vector.**

---

# 13. Why Is the Gradient Vector Important?

Without the Gradient Vector,

the optimizer would need to update millions of parameters individually.

Instead,

the Gradient Vector allows

- efficient computation,
- compact storage,
- simultaneous parameter updates.

This makes training modern neural networks practical.

---

# 14. Relationship Between Partial Derivatives and the Gradient Vector

```text
Loss Function

↓

Compute

∂L/∂W₁

↓

Compute

∂L/∂W₂

↓

Compute

∂L/∂b

↓

Combine

↓

Gradient Vector (∇L)

↓

Optimizer

↓

Update Parameters
```

Notice

The Gradient Vector is simply a collection of all partial derivatives.

---

# One Important Insight

Think of the Gradient Vector as a report card.

Instead of showing only one subject,

it reports the performance of every subject.

```text
Mathematics

Physics

Chemistry

English
```

Similarly,

the Gradient Vector reports the gradient of every trainable parameter in one mathematical object.

---

# Difference Between Partial Derivative and Gradient Vector

| Partial Derivative | Gradient Vector |
|--------------------|-----------------|
| One derivative | Collection of all derivatives |
| Measures one parameter | Represents all parameters |
| Symbol: ∂ | Symbol: ∇ |
| Scalar value | Vector |
| Example: ∂L/∂W₁ | Example: ∇L |

---

# Interview Questions

## Q1. What is a Gradient Vector?

**Answer**

A Gradient Vector is a vector containing the partial derivatives of the loss with respect to every trainable parameter.

---

## Q2. What does the symbol ∇ represent?

**Answer**

The Nabla operator, which computes all partial derivatives of a function.

---

## Q3. Why do optimization algorithms use the Gradient Vector?

**Answer**

Because neural networks contain many parameters, and the Gradient Vector allows all parameters to be updated simultaneously.

---

## Q4. Why does Gradient Descent move in the negative gradient direction?

**Answer**

Because the Gradient Vector points toward the direction of maximum increase of the loss. Moving in the opposite direction decreases the loss.

---

## Q5. What is the difference between a partial derivative and a Gradient Vector?

**Answer**

A partial derivative measures the effect of one parameter, while the Gradient Vector combines the partial derivatives of all trainable parameters into one vector.

---

# Summary

Neural networks contain many trainable parameters, so Backpropagation computes a partial derivative for each one.

These individual derivatives are combined into a **Gradient Vector**, represented by the **Nabla (∇)** operator.

The Gradient Vector points in the direction of the greatest increase of the loss.

Optimization algorithms such as Gradient Descent update all parameters simultaneously by moving in the opposite direction of the Gradient Vector, thereby reducing the loss.

---

# Key Takeaways

✔ A Gradient Vector is a collection of all partial derivatives.

✔ The symbol **∇** is called the Nabla operator.

✔ Every trainable parameter contributes one element to the Gradient Vector.

✔ The Gradient Vector points toward the direction of maximum increase of the loss.

✔ Optimization algorithms move in the opposite direction to minimize the loss.

✔ The Gradient Vector enables simultaneous updates of all parameters in a neural network.

---

## Next Part

**Part 3 – Jacobian Matrix**

In the next chapter, we will study the **Jacobian Matrix**, which generalizes gradients for functions with multiple inputs and multiple outputs and plays an important role in vector-valued functions and automatic differentiation.
