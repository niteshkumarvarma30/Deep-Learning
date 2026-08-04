# Unit 4 – Learning in Neural Networks

# Chapter 1 – Introduction to Learning in Neural Networks

## Part 5 – Complete Numerical Example of Backpropagation

---

# Learning Objectives

After completing this chapter, you will be able to:

- Perform one complete Forward Propagation manually.
- Compute the prediction error using a Loss Function.
- Construct the Computational Graph.
- Apply the Chain Rule step by step.
- Compute gradients manually.
- Update weights using Gradient Descent.
- Understand the complete learning cycle of an Artificial Neural Network.

---

# 1. The Neural Network

To understand Backpropagation clearly, we will use the simplest possible neural network.

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

This network contains

- One input
- One weight
- One bias
- One output neuron

Although real neural networks are much larger, the learning process is exactly the same.

---

# 2. Given Values

Suppose

### Input

```text
x = 2
```

### Weight

```text
w = 1
```

### Bias

```text
b = 0
```

### Actual Output

```text
y = 1
```

### Learning Rate

```text
η = 0.1
```

---

# 3. Step 1 – Forward Propagation

First compute the weighted sum.

$$
z=wx+b
$$

Substitute the values.

$$
z=(1)(2)+0
$$

$$
z=2
$$

---

Now apply the Sigmoid Activation Function.

$$
\hat y = \frac{1}{1+e^{-z}}
$$

Substituting

$$
\hat y = \frac{1}{1+e^{-2}}
$$

$$
\hat y = 0.8808
$$

Therefore,

```text
Prediction (ŷ)

↓

0.8808
```

---

# 4. Step 2 – Compute the Loss

For simplicity,

we use the **Mean Squared Error (MSE)**.

$$
L = \frac12 (y-\hat y)^2
$$

Substitute

$$
L = \frac12 (1-0.8808)^2
$$

$$
L = 0.0071
$$

The loss is small,

but not zero.

Therefore,

the network still needs to learn.

---

# 5. Build the Computational Graph

Instead of treating everything as one large equation,

we divide it into small operations.

```text
Input x

↓

Multiply by Weight

↓

Add Bias

↓

Weighted Sum (z)

↓

Sigmoid

↓

Prediction (ŷ)

↓

Loss
```

Each node performs one simple mathematical operation.

During Backpropagation,

we compute the derivative at every node.

---

# 6. Goal of Backpropagation

The objective is to compute

$$
\frac{\partial L}{\partial w}
$$

This derivative answers the question

> **How does the loss change if the weight changes slightly?**

---

# 7. Apply the Chain Rule

Notice that

the loss depends on the weight through several intermediate variables.

```text
Weight

↓

Weighted Sum

↓

Prediction

↓

Loss
```

Therefore,

we cannot differentiate directly.

Instead,

we apply the Chain Rule.

$$
\boxed{ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat y} \times \frac{\partial \hat y}{\partial z} \times \frac{\partial z}{\partial w} }
$$

The overall gradient is obtained by multiplying three smaller derivatives.

---

# 8. Compute Each Local Derivative

## Step 1 – Derivative of the Loss

The loss function is

$$
L = \frac12 (y-\hat y)^2
$$

Differentiate with respect to the prediction.

$$
\frac{\partial L} {\partial \hat y} = \hat y-y
$$

Substitute

$$
0.8808-1 = -0.1192
$$

Therefore,

$$
\boxed{ \frac{\partial L} {\partial \hat y} = -0.1192 }
$$

---

## Step 2 – Derivative of the Sigmoid Function

The Sigmoid function is

$$
\hat y = \sigma(z)
$$

Its derivative is

$$
\frac{\partial\hat y} {\partial z} = \hat y(1-\hat y)
$$

Substitute

$$
0.8808(1-0.8808) = 0.1050
$$

Therefore,

$$
\boxed{ \frac{\partial\hat y} {\partial z} = 0.1050 }
$$

---

## Step 3 – Derivative of the Weighted Sum

The weighted sum is

$$
z=wx+b
$$

Differentiate with respect to the weight.

$$
\frac{\partial z} {\partial w} = x
$$

Since

```text
x = 2
```

we obtain

$$
\boxed{ \frac{\partial z} {\partial w} = 2 }
$$

---

# 9. Compute the Gradient

Now multiply the local derivatives.

$$
\frac{\partial L} {\partial w} = (-0.1192) \times 0.1050 \times 2
$$

$$
= -0.0250
$$

Therefore,

$$
\boxed{ \frac{\partial L} {\partial w} = -0.025 }
$$

This is the gradient computed by Backpropagation.

---

# 10. Interpret the Gradient

The gradient is

```text
−0.025
```

### Negative Sign

The negative sign indicates that

increasing the weight will reduce the loss.

---

### Magnitude

The magnitude is small.

Therefore,

only a small update is required.

---

# 11. Update the Weight

Gradient Descent updates the weight using

$$
w_{new} = w_{old} - \eta \frac{\partial L} {\partial w}
$$

Substitute

$$
= 1 - 0.1(-0.025)
$$

$$
= 1.0025
$$

Therefore,

```text
Old Weight

↓

1.0000

↓

New Weight

↓

1.0025
```

The weight has moved in the direction that reduces the loss.

---

# 12. Repeat the Learning Cycle

Training does not stop after one update.

The network repeats the same steps.

```text
Updated Weight

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

Weight Update

↓

Repeat
```

After many iterations,

the loss gradually decreases,

and the predictions become more accurate.

---

# 13. Complete Neural Network Learning Pipeline

The complete learning process is

```text
Training Sample

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss

↓

Computational Graph

↓

Chain Rule

↓

Gradient

↓

Optimizer

↓

Weight Update

↓

Repeat
```

This entire process happens for every mini-batch during training.

---

# 14. Why This Example is Important

Although we used only

- one input,
- one weight,
- one bias,

every deep neural network follows exactly the same procedure.

The only difference is that large networks perform these computations for

- thousands of neurons,
- millions of weights,
- multiple hidden layers.

The mathematics remains the same.

---

# 15. Key Insight

Backpropagation does not invent a new mathematical formula.

It simply applies the **Chain Rule** repeatedly on a **Computational Graph**.

This is why Backpropagation is often described as

> **The efficient application of the Chain Rule on a Computational Graph.**

---

# Interview Questions

## Q1. What is the purpose of Backpropagation?

**Answer**

Backpropagation computes the gradients of the loss with respect to every weight and bias in the neural network.

---

## Q2. Why do we use the Chain Rule?

**Answer**

Because the loss depends on the weights through several intermediate computations.

The Chain Rule allows us to compute the overall derivative by multiplying local derivatives.

---

## Q3. What is the first derivative computed during Backpropagation?

**Answer**

The derivative of the loss with respect to the prediction.

$$
\frac{\partial L}{\partial \hat y}
$$

---

## Q4. Does Backpropagation update the weights?

**Answer**

No.

Backpropagation computes the gradients.

The optimizer uses those gradients to update the weights.

---

## Q5. Why do we build a Computational Graph?

**Answer**

A Computational Graph breaks a complex computation into smaller operations, making Forward Propagation and Backpropagation easier to perform.

---

# Summary

This chapter demonstrated one complete learning iteration of a neural network.

Starting from the input,

we performed Forward Propagation to compute the prediction,

used the Loss Function to measure the prediction error,

constructed a Computational Graph,

applied the Chain Rule to compute gradients,

and finally updated the weight using Gradient Descent.

This process forms the foundation of training every Artificial Neural Network, regardless of its size or complexity.

---

# Key Takeaways

✔ Forward Propagation computes the prediction.

✔ The Loss Function measures prediction error.

✔ The Computational Graph represents the computation as simple operations.

✔ The Chain Rule computes the overall gradient by multiplying local derivatives.

✔ Backpropagation computes gradients for every parameter.

✔ The Optimizer updates the weights using those gradients.

✔ Neural networks learn by repeating this process until the loss is minimized.

---

## Next Part

**Chapter 2 – Gradient**

**Part 1 – What is a Gradient? (Advanced Mathematical Perspective)**

In the next chapter, we will study gradients more formally, including **partial derivatives**, **gradient vectors**, and how gradients are represented mathematically for neural networks containing multiple parameters.
