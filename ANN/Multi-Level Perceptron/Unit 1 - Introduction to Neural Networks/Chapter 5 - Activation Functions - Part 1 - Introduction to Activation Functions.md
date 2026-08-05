# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 1 – Introduction to Activation Functions

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what an activation function is in a neural network.
- Explain why activation functions are necessary.
- Understand the concept of non-linearity and its importance.
- Compare linear and non-linear transformations.
- Build the foundation for learning specific activation functions in the next parts.

---

# 1. Introduction

In Chapter 1, we learned the components of an Artificial Neuron (Perceptron).

We saw that the neuron calculates a **weighted sum** and adds a **bias**:

$$

z = x_1w_1 + x_2w_2 + \dots + x_nw_n + b

$$

This sum $ z $ can be any real number: very large positive, very large negative, or zero.

By itself, this raw number doesn't tell us much. It is simply a linear combination of the inputs.

To make this number useful, we pass it through an **Activation Function**.

```text
Inputs & Weights
      │
      ▼
Weighted Sum (z)
      │
      ▼
Activation Function f(z)
      │
      ▼
Neuron Output (a)
```

---

# 2. What is an Activation Function?

An activation function is a mathematical equation attached to each neuron.

It decides whether a neuron should be "activated" or "ignored".

It determines the output of a neural network model, its accuracy, and the computational efficiency of training.

Without it, the neural network is essentially just a linear regression model.

---

# 3. Why Do We Need Activation Functions?

The most critical role of an activation function is to introduce **Non-Linearity**.

## The Problem with Linear Functions

If we do not use an activation function (or use a purely linear one like $ f(z) = z $), the neural network will behave like a single layer network, no matter how many layers it has.

Suppose we have two hidden layers with linear activations.

Layer 1 computes:

$$

h_1 = W_1x + b_1

$$

Layer 2 computes:

$$

h_2 = W_2h_1 + b_2

$$

Substitute $ h_1 $ into the second equation:

$$

h_2 = W_2(W_1x + b_1) + b_2

$$

$$
h_2 = (W_2W_1)x + (W_2b_1 + b_2)

$$

Notice that $ W_2W_1 $ is just another weight matrix, and $ W_2b_1 + b_2 $ is just another bias.

This means:

```text
Linear Layer + Linear Layer = Single Linear Layer
```

If we only use linear functions, a 100-layer neural network is no more powerful than a 1-layer neural network!

## The Power of Non-Linearity

Real-world problems are highly complex.
- Predicting housing prices based on multiple varying factors.
- Recognizing faces in an image.
- Translating languages.

These problems require **Non-Linear Decision Boundaries**.

An activation function allows the network to learn and represent these complex curves and patterns.

```text
Complex Data
      │
      ▼
Non-Linear Activation
      │
      ▼
Network Learns Complex Patterns
```

---

# 4. Desirable Properties of Activation Functions

Not all mathematical functions are good activation functions. A good activation function should be:

1.  **Differentiable:** It must have a derivative because we use Backpropagation and Gradient Descent to train the network.
2.  **Computationally Efficient:** It should be fast to calculate, as it will be executed millions of times.
3.  **Zero-Centered (Ideally):** Helps the gradients to not shift in a single direction, making optimization faster.
4.  **Non-Saturating:** It should not cause gradients to become zero (which leads to the Vanishing Gradient problem).

---

# Interview Questions

## Q1. What happens if we don't use an activation function in a neural network?

**Answer**

If we do not use an activation function, the neural network simply performs linear transformations. No matter how deep the network is, it will behave exactly like a single-layer linear regression model and will fail to learn complex, non-linear patterns.

---

## Q2. Why must activation functions be differentiable?

**Answer**

Neural networks learn by updating their weights using Gradient Descent and Backpropagation. These algorithms require calculating the derivative (gradient) of the error with respect to the weights. If the activation function is not differentiable, we cannot compute these gradients, and the network cannot learn.

---

# Summary

An activation function is the mathematical "gate" that determines the output of a neuron. Its primary purpose is to introduce non-linearity into the network, allowing the model to learn complex relationships in the data. Without non-linear activation functions, deep learning would not exist.

---

# Key Takeaways

✔ An activation function processes the weighted sum to produce the neuron's final output.
✔ The most important role of an activation function is introducing non-linearity.
✔ Multiple linear layers mathematically collapse into a single linear layer.
✔ Activation functions must be differentiable to allow Backpropagation.

---

## Next Part

**Part 2 – Sigmoid and Tanh**

In the next part, we will look at the earliest and most famous non-linear activation functions: Sigmoid and Tanh, understand their math, and explore their critical limitations.
