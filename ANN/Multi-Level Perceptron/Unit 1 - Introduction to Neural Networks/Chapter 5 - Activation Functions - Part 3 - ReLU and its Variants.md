# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 3 – ReLU and Its Variants

---

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the Rectified Linear Unit (ReLU) activation function.
- Explain why ReLU is the default choice for hidden layers in modern deep learning.
- Understand the mathematical definition and graph of ReLU.
- Explore variants of ReLU, such as Leaky ReLU, Parametric ReLU (PReLU), ELU, and SELU.

---

## 1. Introduction

As neural networks became deeper, the Vanishing Gradient problem caused by Sigmoid and Tanh made training increasingly difficult.

Researchers needed an activation function that:

1. Did not saturate in the positive direction (no flat curves for positive inputs).
2. Was computationally inexpensive.

This led to the adoption of **ReLU (Rectified Linear Unit)**, which is now one of the most widely used activation functions in deep learning.

---

## 2. ReLU (Rectified Linear Unit)

ReLU is a simple activation function:

- If the input is positive, it returns the input itself.
- If the input is negative or zero, it returns zero.

### Mathematical Equation

$$
f(z) = \max(0, z)
$$

### Derivative of ReLU

The derivative of ReLU is:

$$
f'(z) =
\begin{cases}
1, & z > 0 \\
0, & z < 0
\end{cases}
$$

At $z = 0$, ReLU is not differentiable. In practice, deep learning frameworks define a subgradient at this point, commonly choosing zero.

### Graph

```text
       f(z)
        |
        |          /
        |        /
        |      /
        |    /
        |  /
--------+---------------- z
        0
```

### Advantages of ReLU

1. **Reduced Vanishing Gradient Problem:** In the positive region, the derivative is exactly 1. Unlike Sigmoid and Tanh, ReLU does not saturate for positive inputs, allowing gradients to flow more effectively through deep networks.

2. **Extremely Fast Computation:** ReLU does not require expensive exponential calculations. It involves a simple maximum operation:

   ```python
   output = max(0, z)
   ```

3. **Sparse Activation:** Negative inputs produce exactly zero. Therefore, only a subset of neurons is active for a given input. This sparsity can improve computational efficiency and act as a mild regularizer.

### Disadvantages of ReLU

- **The Dying ReLU Problem:** This is ReLU's biggest limitation. If weight updates cause a neuron to consistently receive negative inputs, it will always output zero. Its gradient will also be zero, preventing the neuron from updating its weights through that activation.

  The neuron may become permanently inactive during training.

*We will cover the Dying ReLU problem in detail in Part 4.*

---

## 3. Variants of ReLU

To address the limitations of standard ReLU, researchers developed several modified activation functions.

### 3.1 Leaky ReLU

Instead of making the output exactly zero for negative inputs, Leaky ReLU allows a small, non-zero gradient to pass through.

#### Mathematical Equation

$$
f(z) =
\begin{cases}
z, & z \geq 0 \\
0.01z, & z < 0
\end{cases}
$$

#### How Does It Address the Dying ReLU Problem?

In standard ReLU, the gradient for negative inputs is zero.

In Leaky ReLU, the slope for negative inputs is `0.01` instead of `0`.

This allows gradients to flow even when the input is negative, giving inactive neurons an opportunity to recover and continue learning.

---

### 3.2 Parametric ReLU (PReLU)

In Leaky ReLU, the slope for negative inputs is fixed at `0.01`.

In Parametric ReLU (PReLU), this slope becomes a learnable parameter.

#### Mathematical Equation

$$
f(z) =
\begin{cases}
z, & z \geq 0 \\
\alpha z, & z < 0
\end{cases}
$$

Here, $\alpha$ (alpha) is a learnable parameter rather than a fixed constant.

The neural network learns the appropriate value of $\alpha$ during training through Backpropagation and Gradient Descent.

#### Key Difference Between Leaky ReLU and PReLU

| Feature | Leaky ReLU | PReLU |
|---|---|---|
| Negative slope | Fixed (e.g., 0.01) | Learnable parameter |
| Parameter learning | No | Yes |
| Flexibility | Lower | Higher |
| Main purpose | Allow negative gradient flow | Learn the optimal negative slope |

---

### 3.3 Exponential Linear Unit (ELU)

ELU modifies the negative part of the activation curve using an exponential function instead of a straight line.

This allows negative inputs to produce smooth, negative outputs that approach a finite value.

#### Mathematical Equation

$$
f(z) =
\begin{cases}
z, & z \geq 0 \\
\alpha(e^z - 1), & z < 0
\end{cases}
$$

Here, $\alpha$ controls the saturation value for negative inputs.

#### Advantages

- **Smooth Curve:** ELU is differentiable everywhere, unlike standard ReLU, which has a sharp corner at $z = 0$.
- **Negative Outputs:** It allows negative values, which can help keep activations closer to zero-centered.
- **Potentially Faster Convergence:** ELU can converge faster than ReLU in some deep neural network architectures.

#### Disadvantages

- **Computationally Expensive:** ELU requires an exponential calculation for negative inputs, making it more computationally expensive than ReLU.

---

### 3.4 Scaled Exponential Linear Unit (SELU)

SELU is an advanced variant of ELU designed to support self-normalizing neural networks.

When used with an appropriate network architecture and specific weight initialization, such as **LeCun Normal initialization**, SELU can help maintain the mean and variance of activations across layers.

The goal is to maintain:

$$
\mu \approx 0
$$

$$
\sigma^2 \approx 1
$$

This property is known as **self-normalization**.

It can reduce the need for Batch Normalization in suitable network architectures.

---

## 4. Comparison of ReLU Variants

| Activation Function | Positive Input | Negative Input | Main Characteristic |
|---|---|---|---|
| ReLU | $z$ | $0$ | Simple and computationally efficient |
| Leaky ReLU | $z$ | $0.01z$ | Allows a small negative gradient |
| PReLU | $z$ | $\alpha z$ | Learns the negative slope |
| ELU | $z$ | $\alpha(e^z - 1)$ | Smooth negative exponential curve |
| SELU | Scaled $z$ | Scaled ELU | Supports self-normalizing networks |

---

## 5. Interview Questions

### Q1. Why is ReLU preferred over Sigmoid in deep neural networks?

**Answer:**

ReLU is preferred because it reduces the Vanishing Gradient problem for positive inputs. Its derivative is exactly 1 in the positive region, allowing gradients to flow more effectively through deep networks.

It is also computationally efficient because it does not require exponential operations like Sigmoid.

These properties often make deep networks faster and easier to train.

### Q2. What is Leaky ReLU, and why was it introduced?

**Answer:**

Leaky ReLU is a variant of ReLU that allows a small, non-zero output for negative inputs instead of returning zero.

For example:

$$
f(z) =
\begin{cases}
z, & z \geq 0 \\
0.01z, & z < 0
\end{cases}
$$

It was introduced to address the Dying ReLU problem by allowing gradients to flow even when the input is negative.

### Q3. What is the difference between Leaky ReLU and PReLU?

**Answer:**

The main difference is how they handle the negative slope.

- **Leaky ReLU:** Uses a fixed negative slope, such as `0.01`.
- **PReLU:** Uses a learnable negative slope that the network updates during training.

### Q4. What is the main advantage of SELU?

**Answer:**

SELU supports self-normalizing neural networks. Under suitable conditions, it helps maintain the mean and variance of activations across layers, potentially reducing the need for Batch Normalization.

---

## 6. Summary

ReLU revolutionized deep learning by providing a computationally efficient, non-saturating activation function for positive inputs.

Its main limitation is the Dying ReLU problem, where neurons can become permanently inactive because their gradients become zero.

Several variants were developed to address this limitation:

- **Leaky ReLU:** Allows a small negative slope.
- **PReLU:** Learns the negative slope during training.
- **ELU:** Uses an exponential function for negative inputs.
- **SELU:** Supports self-normalizing neural networks under suitable conditions.

---

## 7. Key Takeaways

- ReLU is defined as $f(z) = \max(0, z)$.
- ReLU is a common default choice for hidden layers in deep neural networks.
- It is computationally inexpensive and produces sparse activations.
- ReLU has a zero gradient for negative inputs, which can cause the Dying ReLU problem.
- Leaky ReLU addresses this issue by allowing a small negative slope.
- PReLU makes the negative slope a learnable parameter.
- ELU uses an exponential function for negative inputs.
- SELU supports self-normalizing neural networks under appropriate conditions.

---

## Next Part

**Part 4 – The Dying ReLU Problem**

In the next part, we will take a deeper look at the Dying ReLU problem, understand exactly why it happens, and explore how it affects the training of neural networks.
