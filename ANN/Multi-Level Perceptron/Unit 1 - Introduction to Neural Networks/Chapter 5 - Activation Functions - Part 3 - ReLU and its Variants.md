# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 3 – ReLU and its Variants

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the Rectified Linear Unit (ReLU) activation function.
- Explain why ReLU is the default choice for hidden layers in modern deep learning.
- Identify the mathematical definition and graph of ReLU.
- Explore variants of ReLU such as Leaky ReLU, Parametric ReLU (PReLU), ELU, and SELU.

---

# 1. Introduction

As neural networks became deeper, the Vanishing Gradient problem caused by Sigmoid and Tanh made training almost impossible.

Researchers needed an activation function that:
1. Did not saturate in the positive direction (no flat curves for positive numbers).
2. Was computationally cheap.

This led to the adoption of **ReLU (Rectified Linear Unit)**, which is now the most widely used activation function in the world.

---

# 2. ReLU (Rectified Linear Unit)

ReLU is incredibly simple. If the input is positive, it returns the input. If the input is negative, it returns zero.

## Mathematical Equation

$$

f(z) = \max(0, z)

$$

## Graph

```text
       │      /
       │    /
       │  /
 0.0 ──┼───────────
       │
      -∞      0       +∞
```

## Advantages of ReLU

1. **No Vanishing Gradient (for positive $ z $):** In the positive region, the derivative is always exactly 1. It never flattens out, meaning gradients do not vanish.
2. **Extremely Fast Computation:** There are no expensive exponential functions to calculate. It just involves a simple `if` condition or `max(0, z)` operation.
3. **Sparse Activation:** Because all negative inputs are output as exactly 0, only a subset of neurons in the network is activated at any given time. This sparsity makes the network highly efficient and acts as a mild regularizer.

## Disadvantages of ReLU

- **The Dying ReLU Problem:** This is its biggest flaw. If a large gradient updates a weight in such a way that the neuron always outputs a negative $ z $, the ReLU will output 0. Its gradient will also be 0. The neuron is essentially "dead" and will never update again.

*(We will cover the Dying ReLU problem in detail in Part 4).*

---

# 3. Variants of ReLU

To fix the "Dying ReLU" problem, researchers developed several modified versions of ReLU.

---

## 3.1 Leaky ReLU

Instead of making the output exactly zero for negative inputs, Leaky ReLU allows a very small, non-zero gradient to "leak" through.

### Mathematical Equation

$$

f(z) = \begin{cases} z, & \text{if } z \ge 0 \\ 0.01z, & \text{if } z < 0 \end{cases}

$$

### How it solves Dying ReLU
Because the slope for negative values is `0.01` instead of `0`, the gradient is never exactly zero. This allows "dead" neurons a chance to recover and start learning again.

---

## 3.2 Parametric ReLU (PReLU)

In Leaky ReLU, the slope for negative values is fixed at `0.01`. In PReLU, this slope becomes a learnable parameter.

### Mathematical Equation

$$

f(z) = \begin{cases} z, & \text{if } z \ge 0 \\ \alpha z, & \text{if } z < 0 \end{cases}

$$

Here, $ \alpha $ (alpha) is not a fixed number. The neural network learns the best value for $ \alpha $ during Backpropagation via Gradient Descent.

---

## 3.3 Exponential Linear Unit (ELU)

ELU modifies the negative part of the curve to be a smooth exponential curve instead of a straight line. This makes the function closer to zero-centered and smoother than Leaky ReLU.

### Mathematical Equation

$$

f(z) = \begin{cases} z, & \text{if } z \ge 0 \\ \alpha(e^z - 1), & \text{if } z < 0 \end{cases}

$$

### Advantages
- Smooth curve (differentiable everywhere, unlike ReLU which has a sharp corner at z=0).
- Faster convergence than ReLU in some deep networks.

### Disadvantages
- Computationally expensive due to the exponential function $ e^z $.

---

## 3.4 Scaled Exponential Linear Unit (SELU)

SELU is an advanced variant of ELU. When used with a specific type of weight initialization (LeCun Normal initialization), SELU has a magical property: it induces **self-normalizing** neural networks.

This means that the output of every hidden layer automatically maintains a mean of 0 and a variance of 1, eliminating the need for Batch Normalization.

---

# Interview Questions

## Q1. Why is ReLU preferred over Sigmoid in deep neural networks?

**Answer**

ReLU is preferred because it solves the Vanishing Gradient problem for positive inputs (its derivative is always 1) and is extremely computationally efficient (no exponential operations). This allows deep networks to train much faster and more reliably.

---

## Q2. What is Leaky ReLU, and why was it introduced?

**Answer**

Leaky ReLU is a variant of ReLU that returns a very small gradient (e.g., 0.01z) for negative inputs instead of returning 0. It was introduced to solve the Dying ReLU problem, ensuring that neurons receiving negative inputs can still update their weights and recover.

---

# Summary

ReLU revolutionized Deep Learning by providing a fast, non-saturating activation function that mitigated the Vanishing Gradient problem. While its main flaw is the Dying ReLU problem, simple variants like Leaky ReLU and PReLU successfully address it by allowing a small gradient flow for negative inputs.

---

# Key Takeaways

✔ ReLU is defined as $ \max(0, z) $.
✔ ReLU is the default choice for hidden layers.
✔ It is computationally cheap and induces sparse activations.
✔ Leaky ReLU prevents the Dying ReLU problem by allowing a small negative slope.
✔ PReLU allows the network to learn the negative slope dynamically.

---

## Next Part

**Part 4 – The Dying ReLU Problem**

In the next part, we will take a deep dive into the Dying ReLU problem, understanding exactly why it happens and how it affects the training of a neural network.
