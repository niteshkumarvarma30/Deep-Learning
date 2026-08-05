# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 2 – Sigmoid and Tanh

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the mathematical equation and graph of the Sigmoid function.
- Explain the advantages and severe disadvantages of the Sigmoid function.
- Understand the mathematical equation and graph of the Tanh function.
- Compare Sigmoid and Tanh functions.
- Explain why these functions are rarely used in hidden layers of deep neural networks today.

---

# 1. Introduction

In the early days of neural networks, the Step Function was used. However, it was not differentiable, which prevented the network from learning using Backpropagation.

To fix this, researchers needed a function that:
1. Was non-linear.
2. Was smooth and differentiable everywhere.
3. Could squash real numbers into a small, defined range (like probability).

This led to the widespread adoption of the **Sigmoid** activation function.

---

# 2. Sigmoid Activation Function

The Sigmoid function, also known as the Logistic function, takes any real number and squashes it into a range between `0` and `1`.

## Mathematical Equation

$$

\sigma(z) = \frac{1}{1 + e^{-z}}

$$

## Graph

```text
 1.0 ┼───────────────       (z is large positive)
     │            .
 0.5 ┼───── .
     │   .
 0.0 ┼───────────────       (z is large negative)
    -∞       0       +∞
```

If $ z $ is a large positive number, the output is close to 1.
If $ z $ is a large negative number, the output is close to 0.

## Advantages of Sigmoid

- **Smooth Gradient:** It is differentiable everywhere.
- **Probability Output:** Because the output is between 0 and 1, it is perfectly suited for the output layer of binary classification models.

## Disadvantages of Sigmoid

Despite its early popularity, Sigmoid is rarely used in hidden layers today due to three major problems:

1.  **Vanishing Gradients:** Look at the graph. When $ z $ is very large (e.g., +10) or very small (e.g., -10), the curve becomes flat. In these flat regions, the derivative (gradient) is almost zero. During Backpropagation, these near-zero gradients multiply, causing the network to stop learning entirely.
2.  **Not Zero-Centered:** The outputs are always positive (between 0 and 1). This forces the gradients during backpropagation to move in a zig-zag, inefficient path, slowing down training.
3.  **Computationally Expensive:** Computing the exponential function $ e^{-z} $ is relatively slow for computers when done millions of times.

---

# 3. Tanh (Hyperbolic Tangent) Activation Function

To solve the "not zero-centered" problem of the Sigmoid function, researchers proposed the **Tanh** function.

Tanh is mathematically a shifted and stretched version of the Sigmoid function. It squashes real numbers into a range between `-1` and `1`.

## Mathematical Equation

$$

\tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}

$$

## Graph

```text
  1.0 ┼───────────────       (z is large positive)
      │            .
  0.0 ┼───── . ────────
      │   .
 -1.0 ┼───────────────       (z is large negative)
     -∞       0       +∞
```

## Advantages of Tanh over Sigmoid

- **Zero-Centered:** Because the output ranges from -1 to 1, the mean of the activations is closer to zero. This makes optimization significantly faster compared to Sigmoid.

In practice, if you must choose between Sigmoid and Tanh for a hidden layer, **Tanh is always strictly preferred over Sigmoid.**

## Disadvantages of Tanh

- **Vanishing Gradients:** Just like Sigmoid, Tanh saturates (flattens out) for large positive or negative values of $ z $. Thus, deep networks using Tanh still suffer heavily from the Vanishing Gradient problem.
- **Computationally Expensive:** It still requires calculating exponentials.

---

# Interview Questions

## Q1. Why is Sigmoid primarily used in the output layer and not in hidden layers?

**Answer**

Sigmoid is used in the output layer for binary classification because it maps raw scores into probabilities between 0 and 1. It is not used in hidden layers because it suffers from the Vanishing Gradient problem and its outputs are not zero-centered, which severely slows down training in deep networks.

---

## Q2. How is Tanh better than Sigmoid?

**Answer**

Tanh is zero-centered (outputs range from -1 to 1), whereas Sigmoid is not (outputs range from 0 to 1). Zero-centered activations result in better gradient flow and faster convergence during optimization.

---

## Q3. What is the Vanishing Gradient problem in the context of Sigmoid/Tanh?

**Answer**

For both Sigmoid and Tanh, when the input $ z $ becomes very large (positive or negative), the activation function reaches its limits (saturates) and the curve becomes perfectly flat. The derivative (slope) at these flat regions is almost zero. During Backpropagation, these zero gradients stop the weights from updating, stalling the learning process.

---

# Summary

Sigmoid and Tanh were the default activation functions in early neural networks. While Sigmoid is still essential for binary classification output layers, both functions suffer from the Vanishing Gradient problem, making them unsuitable for the hidden layers of modern deep neural networks.

---

# Key Takeaways

✔ Sigmoid outputs range from 0 to 1.
✔ Tanh outputs range from -1 to 1.
✔ Tanh is zero-centered and generally outperforms Sigmoid in hidden layers.
✔ Both functions suffer from the Vanishing Gradient problem because they saturate at their extremes.
✔ Exponentials make them computationally expensive.

---

## Next Part

**Part 3 – ReLU and its Variants**

To solve the Vanishing Gradient problem and the computational inefficiency of Sigmoid and Tanh, researchers developed a surprisingly simple function that changed Deep Learning forever: ReLU.
