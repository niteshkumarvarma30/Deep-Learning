# Unit 4 – Learning in Neural Networks

# Chapter 3 – Backpropagation in Multi-Layer Neural Networks

## Part 1 – Why Do We Need Backpropagation for Multi-Layer Networks?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why single-neuron Backpropagation is not sufficient for deep neural networks.
- Learn why multi-layer neural networks require a specialized learning algorithm.
- Understand how prediction errors propagate through hidden layers.
- Learn the role of the Chain Rule in multi-layer neural networks.
- Prepare for the mathematical derivation of Backpropagation.

---

# 1. Recap: Backpropagation for a Single Neuron

Previously, we studied Backpropagation for a neural network containing only one neuron.

The network looked like

```text
Input (x)

↓

Weight (w)

↓

Bias (b)

↓

Weighted Sum (z)

↓

Sigmoid Activation

↓

Prediction (ŷ)

↓

Loss
```

The gradient with respect to the weight was

$$
\frac{\partial L}{\partial w}
$$

Using the Chain Rule,

we computed

$$
\boxed{ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z} \times \frac{\partial z}{\partial w} }
$$

Since there was only one weight,

the computation was relatively simple.

---

# 2. The Problem with Multi-Layer Neural Networks

Now consider a neural network containing a hidden layer.

```text
Input

↓

Hidden Layer

↓

Output Layer

↓

Loss
```

Suppose the network contains two sets of weights.

```text
Input

↓

Weight W₁

↓

Hidden Neuron

↓

Weight W₂

↓

Output Neuron

↓

Loss
```

Now ask

> **How does the loss change when \(W_1\) changes?**

Unlike the previous example,

\(W_1\) does **not** directly affect the loss.

Instead,

it affects the hidden neuron,

which affects the output neuron,

which finally affects the loss.

The dependency becomes much longer.

---

# 3. Why Can't We Differentiate Directly?

Suppose

$$
L=f(a_2)
$$

where

$$
a_2=f(z_2)
$$

and

$$
z_2=f(a_1)
$$

and

$$
a_1=f(z_1)
$$

and

$$
z_1=f(W_1)
$$

Notice

The loss depends on \(W_1\) through several intermediate variables.

```text
W₁

↓

z₁

↓

a₁

↓

z₂

↓

a₂

↓

Loss
```

Because of these dependencies,

we cannot differentiate the loss with respect to \(W_1\) directly.

Instead,

we must move through each intermediate variable one step at a time.

---

# 4. The Dependency Chain

Every variable depends on the previous one.

```text
Weight W₁

↓

Weighted Sum z₁

↓

Hidden Activation a₁

↓

Weighted Sum z₂

↓

Output Activation a₂

↓

Loss
```

To compute

$$
\frac{\partial L}{\partial W_1}
$$

we must compute the derivative of every intermediate step.

---

# 5. The Chain Rule Solves the Problem

The Chain Rule allows us to connect all intermediate derivatives.

$$
\boxed{ \frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial a_2} \times \frac{\partial a_2}{\partial z_2} \times \frac{\partial z_2}{\partial a_1} \times \frac{\partial a_1}{\partial z_1} \times \frac{\partial z_1}{\partial W_1} }
$$

Instead of computing one complicated derivative,

we compute several simple local derivatives and multiply them together.

This is the fundamental idea behind Backpropagation.

---

# 6. What Happens in a Deep Neural Network?

Now imagine a deeper neural network.

```text
Input

↓

Layer 1

↓

Layer 2

↓

Layer 3

↓

Layer 4

↓

Output Layer

↓

Loss
```

Suppose we want

$$
\frac{\partial L}{\partial W_1}
$$

The gradient must pass through

- Output Layer
- Layer 4
- Layer 3
- Layer 2
- Layer 1

before reaching \(W_1\).

This backward movement of gradients gives the algorithm its name.

> **Backpropagation**

---

# 7. Why Is Backpropagation Efficient?

Imagine computing the derivative for every weight independently.

A neural network with

```text
10 Million Parameters
```

would require an enormous amount of repeated computation.

Backpropagation avoids this problem.

Each layer computes its local derivatives only once,

then passes the necessary information backward.

Intermediate results are reused,

making the algorithm highly efficient.

---

# 8. Error Propagation

Forward Propagation computes

```text
Input

↓

Prediction
```

Backpropagation computes

```text
Loss

↓

Output Layer Error

↓

Hidden Layer Error

↓

Earlier Hidden Layers

↓

Input Layer
```

Each hidden layer receives an error signal from the layer after it.

This error signal is then used to compute gradients for that layer's weights and biases.

---

# 9. Real-Life Analogy

Imagine a factory.

```text
Raw Material

↓

Machine A

↓

Machine B

↓

Machine C

↓

Finished Product
```

Suppose the finished product is defective.

To identify the cause,

the engineer investigates in reverse order.

```text
Finished Product

↓

Machine C

↓

Machine B

↓

Machine A
```

Each machine contributes to the final defect.

Similarly,

each neural network layer contributes to the final prediction error.

Backpropagation traces the error backward to determine how each layer contributed.

---

# 10. Complete Training Pipeline

The complete learning process becomes

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

Backpropagation

↓

Layer-wise Gradients

↓

Optimizer

↓

Updated Parameters

↓

Repeat
```

Notice

Backpropagation computes gradients **layer by layer**.

The optimizer then updates all trainable parameters.

---

# 11. One Important Insight

Many beginners believe

> **Backpropagation for deep neural networks is completely different from Backpropagation for a single neuron.**

This is not true.

The mathematics remains exactly the same.

The only difference is that the Chain Rule is applied repeatedly across many layers.

In other words,

a deep neural network is simply many single-neuron computations connected together.

---

# Visual Summary

```text
Single Neuron

↓

Simple Chain Rule

↓

One Weight Gradient
```

```text
Multi-Layer Neural Network

↓

Repeated Chain Rule

↓

Gradients for Every Layer
```

---

# Difference Between Single-Layer and Multi-Layer Backpropagation

| Single Neuron | Multi-Layer Neural Network |
|---------------|----------------------------|
| One weight | Many weights |
| One application of the Chain Rule | Repeated applications of the Chain Rule |
| Direct dependency | Multiple intermediate dependencies |
| Simple gradient computation | Layer-wise gradient computation |
| Suitable for simple models | Suitable for deep neural networks |

---

# Interview Questions

## Q1. Why can't we compute \(\frac{\partial L}{\partial W_1}\) directly in a deep neural network?

**Answer**

Because the loss depends on \(W_1\) through many intermediate variables such as weighted sums and activations. The Chain Rule must be applied to connect these dependencies.

---

## Q2. Why is Backpropagation necessary for multi-layer neural networks?

**Answer**

Backpropagation efficiently computes gradients for every weight and bias by propagating the error backward through all hidden layers using the Chain Rule.

---

## Q3. Why is Backpropagation computationally efficient?

**Answer**

Because it reuses intermediate derivatives instead of recomputing them for every parameter, avoiding redundant calculations.

---

## Q4. What travels backward during Backpropagation?

**Answer**

The error signal (gradients) travels backward from the output layer to the input layer.

---

## Q5. Is the mathematics of Backpropagation different for deep neural networks?

**Answer**

No.

The same Chain Rule is used.

The only difference is that it is applied repeatedly across multiple layers.

---

# Summary

Single-neuron Backpropagation is straightforward because the loss depends directly on one weight.

In multi-layer neural networks,

the loss depends on each weight indirectly through many intermediate variables.

The Chain Rule connects these dependencies by multiplying local derivatives together.

Backpropagation efficiently applies the Chain Rule layer by layer, propagating the error backward through the network and computing gradients for every trainable parameter.

This makes it possible to train deep neural networks containing millions of weights.

---

# Key Takeaways

✔ Multi-layer neural networks contain many intermediate computations.

✔ The loss depends indirectly on earlier-layer weights.

✔ Direct differentiation is not possible.

✔ The Chain Rule connects all intermediate dependencies.

✔ Backpropagation computes gradients layer by layer.

✔ Intermediate derivatives are reused, making Backpropagation computationally efficient.

✔ Deep neural network Backpropagation is simply repeated application of the Chain Rule.

---

## Next Part

**Part 2 – Mathematical Derivation of Backpropagation for a Two-Layer Neural Network**

In the next chapter, we will derive the complete Backpropagation equations for a two-layer neural network, introduce the **δ (delta) error term**, compute gradients for the output layer first, and then propagate those errors backward to the hidden layer. This derivation forms the mathematical foundation of modern deep learning frameworks such as PyTorch and TensorFlow.
