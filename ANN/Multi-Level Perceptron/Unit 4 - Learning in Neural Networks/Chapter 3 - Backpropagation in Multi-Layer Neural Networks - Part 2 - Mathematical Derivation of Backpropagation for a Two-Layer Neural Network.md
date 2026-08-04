# Unit 4 – Learning in Neural Networks

# Chapter 3 – Backpropagation in Multi-Layer Neural Networks

## Part 2 – Mathematical Derivation of Backpropagation for a Two-Layer Neural Network

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the mathematical notation used in Backpropagation.
- Derive the Backpropagation equations for a two-layer neural network.
- Learn the meaning of the **δ (delta) error term**.
- Compute gradients for the output layer.
- Understand how errors propagate backward to hidden layers.

---

# 1. Our Neural Network

Consider the simplest multi-layer neural network.

```text
Input (x)

↓

Hidden Layer

↓

Output Layer

↓

Loss
```

Suppose the network consists of

```text
Input

↓

(W₁, b₁)

↓

Weighted Sum (z₁)

↓

Activation

↓

Hidden Output (a₁)

↓

(W₂, b₂)

↓

Weighted Sum (z₂)

↓

Activation

↓

Prediction (ŷ)

↓

Loss
```

where

- \(W_1, b_1\) are the hidden-layer parameters.
- \(W_2, b_2\) are the output-layer parameters.

Our goal is to compute

$$
\frac{\partial L}{\partial W_2}
$$

and

$$
\frac{\partial L}{\partial W_1}
$$

so that Gradient Descent can update the weights.

---

# 2. Forward Propagation Equations

The hidden layer computes

## Step 1 – Weighted Sum

$$
z_1=W_1x+b_1
$$

---

## Step 2 – Activation

$$
a_1=f(z_1)
$$

where \(f\) is an activation function such as Sigmoid, Tanh, or ReLU.

---

The output layer computes

## Step 3 – Weighted Sum

$$
z_2=W_2a_1+b_2
$$

---

## Step 4 – Output Activation

$$
\hat y=f(z_2)
$$

---

## Step 5 – Loss

$$
L=L(y,\hat y)
$$

This completes the **Forward Propagation**.

---

# 3. Goal of Backpropagation

After computing the prediction,

suppose the loss is large.

The objective is to determine

> **How should every weight change to reduce the loss?**

We therefore compute

```text
∂L/∂W₂

↓

Output Layer Gradient
```

and

```text
∂L/∂W₁

↓

Hidden Layer Gradient
```

These gradients tell the optimizer how each weight should be updated.

---

# 4. Computing the Output Layer Gradient

We first compute

$$
\frac{\partial L}{\partial W_2}
$$

Observe the dependency chain.

```text
W₂

↓

z₂

↓

ŷ

↓

Loss
```

Applying the Chain Rule,

$$
\boxed{ \frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z_2} \times \frac{\partial z_2}{\partial W_2} }
$$

This equation computes the gradient of the output-layer weights.

---

# 5. Introducing the Delta (δ) Error Term

Notice that the expression

$$
\frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z_2}
$$

appears repeatedly.

Instead of writing it every time,

we define

$$
\boxed{ \delta_2 = \frac{\partial L}{\partial z_2} }
$$

This quantity is called the

> **Output Layer Delta (Error Term)**

Using the Chain Rule,

$$
\delta_2 = \frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z_2}
$$

The gradient equation becomes much simpler.

$$
\boxed{ \frac{\partial L}{\partial W_2} = \delta_2a_1 }
$$

---

# 6. Why Introduce the Delta Term?

Without introducing δ,

the equations become lengthy.

For example,

without δ,

$$
\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z_2} \times a_1
$$

With δ,

$$
\frac{\partial L}{\partial W_2} = \delta_2a_1
$$

The notation is shorter,

cleaner,

and easier to extend to deeper neural networks.

---

# 7. Backpropagation to the Hidden Layer

Now consider the hidden-layer weights.

The dependency chain is

```text
W₁

↓

z₁

↓

a₁

↓

z₂

↓

ŷ

↓

Loss
```

Applying the Chain Rule,

$$
\boxed{ \frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial z_2} \times \frac{\partial z_2}{\partial a_1} \times \frac{\partial a_1}{\partial z_1} \times \frac{\partial z_1}{\partial W_1} }
$$

Notice

The gradient must pass through the output layer before reaching the hidden layer.

---

# 8. Hidden Layer Delta

Again,

instead of repeatedly writing the long Chain Rule expression,

we define another delta term.

$$
\boxed{ \delta_1 = \frac{\partial L}{\partial z_1} }
$$

Using the Chain Rule,

$$
\boxed{ \delta_1 = (W_2^T\delta_2) \odot f'(z_1) }
$$

where

- \(W_2^T\) is the transpose of the output-layer weight matrix.
- \(f'(z_1)\) is the derivative of the hidden-layer activation function.
- \(\odot\) denotes element-wise (Hadamard) multiplication.

This equation propagates the output-layer error backward into the hidden layer.

---

# 9. Hidden Layer Weight Gradient

Once the hidden-layer delta has been computed,

the hidden-layer weight gradient is

$$
\boxed{ \frac{\partial L}{\partial W_1} = \delta_1x }
$$

Thus,

the hidden-layer gradient depends on

- the hidden-layer error,
- and the input to that layer.

---

# 10. Complete Backpropagation Equations

For a two-layer neural network,

the complete Backpropagation equations are

## Output Layer

$$
\boxed{ \delta_2 = \frac{\partial L}{\partial z_2} }
$$

$$
\boxed{ \frac{\partial L}{\partial W_2} = \delta_2a_1 }
$$

---

## Hidden Layer

$$
\boxed{ \delta_1 = (W_2^T\delta_2) \odot f'(z_1) }
$$

$$
\boxed{ \frac{\partial L}{\partial W_1} = \delta_1x }
$$

These four equations form the mathematical foundation of Backpropagation.

---

# 11. Visual Summary

## Forward Pass

```text
Input (x)

↓

z₁

↓

a₁

↓

z₂

↓

Prediction (ŷ)

↓

Loss
```

---

## Backward Pass

```text
Loss

↓

δ₂

↓

δ₁

↓

Weight Gradients

↓

Optimizer

↓

Updated Weights
```

The forward pass computes predictions.

The backward pass computes gradients.

---

# 12. Why This Derivation is Important

Every modern Deep Learning framework follows the same procedure.

```text
Forward Propagation

↓

Prediction

↓

Loss

↓

Output Delta

↓

Hidden Delta

↓

Weight Gradients

↓

Optimizer

↓

Weight Update
```

Whether using

- PyTorch,
- TensorFlow,
- JAX,

or another framework,

the underlying mathematics remains the same.

---

# 13. One Important Insight

Many beginners think

> **Backpropagation directly computes the gradients.**

In reality,

Backpropagation proceeds in two stages.

### Stage 1

Compute the **delta (error term)** for every layer.

### Stage 2

Use the delta values to compute the gradients of the weights and biases.

The delta carries the error information backward through the network.

---

# Difference Between Gradient and Delta

| Gradient | Delta |
|----------|--------|
| Derivative of the loss with respect to a weight or bias | Derivative of the loss with respect to the weighted sum \(z\) |
| Used to update parameters | Used to propagate error backward |
| Example: \(\frac{\partial L}{\partial W}\) | Example: \(\delta=\frac{\partial L}{\partial z}\) |
| Consumed by the optimizer | Used during Backpropagation |

---

# Interview Questions

## Q1. What is the delta (δ) term?

**Answer**

The delta term is the error signal of a layer. Mathematically, it is the derivative of the loss with respect to the weighted sum \(z\) of that layer.

---

## Q2. Why do we introduce the delta term?

**Answer**

It simplifies the Backpropagation equations by grouping repeated derivative expressions into a single variable.

---

## Q3. How is the hidden-layer delta computed?

**Answer**

The hidden-layer delta is computed by multiplying the output-layer delta by the transpose of the next layer's weight matrix and the derivative of the hidden-layer activation function.

$$
\delta_1=(W_2^T\delta_2)\odot f'(z_1)
$$

---

## Q4. What is the purpose of Backpropagation?

**Answer**

Backpropagation computes the gradients of the loss with respect to every trainable parameter so that the optimizer can update the weights and biases.

---

## Q5. Why is the Chain Rule essential in Backpropagation?

**Answer**

Because the loss depends on earlier-layer weights through many intermediate variables. The Chain Rule connects these dependencies by multiplying local derivatives.

---

# Summary

In a multi-layer neural network,

the loss depends indirectly on the weights of earlier layers.

Backpropagation applies the Chain Rule to compute gradients efficiently.

To simplify the equations,

the **delta (δ) error term** is introduced.

The output-layer delta is computed first,

then propagated backward to compute the hidden-layer delta.

Finally,

these delta values are used to calculate the gradients of the weights.

This derivation forms the mathematical foundation of modern Deep Learning training algorithms.

---

# Key Takeaways

✔ Forward Propagation computes predictions.

✔ Backpropagation computes gradients.

✔ The delta term represents the error at a layer.

✔ The output-layer delta is computed first.

✔ Hidden-layer deltas are computed by propagating errors backward.

✔ Weight gradients are calculated using the corresponding delta values.

✔ Every modern Deep Learning framework implements these same mathematical equations.

---

## Next Part

**Part 3 – Complete Numerical Example of Multi-Layer Backpropagation**

In the next chapter, we will perform a complete numerical example using actual values to manually compute:

- Forward Propagation
- Loss
- Output-layer delta
- Hidden-layer delta
- Weight gradients
- Bias gradients
- Weight updates

This example will demonstrate exactly how Backpropagation trains a neural network step by step.
