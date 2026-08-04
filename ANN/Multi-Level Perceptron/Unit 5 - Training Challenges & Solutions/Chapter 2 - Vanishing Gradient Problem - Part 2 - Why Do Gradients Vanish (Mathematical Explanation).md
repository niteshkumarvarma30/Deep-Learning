# Unit 5 – Training Challenges & Solutions

# Chapter 2 – Vanishing Gradient Problem

## Part 2 – Why Do Gradients Vanish? (Mathematical Explanation)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the mathematical cause of the Vanishing Gradient Problem.
- Learn how the Chain Rule causes gradients to shrink.
- Understand why repeated multiplication of small numbers leads to vanishing gradients.
- Learn why Sigmoid and Tanh activation functions contribute to this problem.
- Build the mathematical foundation for modern solutions such as ReLU and Batch Normalization.

---

# 1. Recap: Backpropagation Uses the Chain Rule

Recall the Backpropagation equation.

For a weight in an early layer,

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial a_n} \times \frac{\partial a_n}{\partial z_n} \times \frac{\partial z_n}{\partial a_{n-1}} \times \cdots \times \frac{\partial z_1}{\partial W}
$$

Notice something important.

The final gradient is obtained by **multiplying many local derivatives together**.

This multiplication is the key reason behind the Vanishing Gradient Problem.

---

# 2. What Happens When We Multiply Small Numbers?

Suppose every derivative equals

$$
0.5
$$

Now multiply them repeatedly.

```text
0.5

↓

0.5 × 0.5 = 0.25

↓

0.25 × 0.5 = 0.125

↓

0.125 × 0.5 = 0.0625

↓

0.0625 × 0.5 = 0.03125

↓

...
```

The more layers we have,

the smaller the gradient becomes.

---

# 3. Exponential Shrinking of Gradients

Suppose a neural network has

10 hidden layers.

If every derivative equals

$$
0.5
$$

then

$$
0.5^{10} = 0.000976
$$

Now suppose the network contains

50 hidden layers.

$$
0.5^{50} = 8.88\times10^{-16}
$$

This value is practically zero.

Therefore,

the gradient has vanished.

---

# 4. Why Does the Chain Rule Cause This?

The Chain Rule itself is mathematically correct.

The problem is **not** the Chain Rule.

The real issue is

> **Repeated multiplication of numbers smaller than 1.**

Every multiplication reduces the gradient.

As the number of layers increases,

the shrinking becomes exponential.

---

# 5. Role of the Sigmoid Activation Function

Recall the Sigmoid activation function.

$$
\sigma(z) = \frac{1}{1+e^{-z}}
$$

Its derivative is

$$
\sigma'(z) = \sigma(z)(1-\sigma(z))
$$

The maximum possible derivative is

$$
0.25
$$

Therefore,

```text
Sigmoid Derivative

≤ 0.25
```

Every hidden layer contributes a value less than or equal to **0.25**.

---

# 6. Example Using Sigmoid

Suppose

$$
\sigma'(z)=0.2
$$

for every hidden layer.

For a network with ten hidden layers,

the gradient becomes

$$
0.2^{10} = 1.024\times10^{-7}
$$

This value is almost zero.

Consequently,

the earliest layers receive almost no learning signal.

---

# 7. Role of the Tanh Activation Function

The Tanh activation function is

$$
\tanh(z)
$$

Its derivative is

$$
1-\tanh^2(z)
$$

Although Tanh generally performs better than Sigmoid,

its derivative is still usually less than 1.

Therefore,

repeated multiplication during Backpropagation still causes gradients to shrink,

especially in deep neural networks.

---

# 8. Visualizing Gradient Shrinking

Suppose the gradient initially equals

```text
1
```

Each layer multiplies it by

```text
0.5
```

The gradient evolves as

```text
1

↓

0.5

↓

0.25

↓

0.125

↓

0.0625

↓

0.03125

↓

...
```

Eventually,

the gradient becomes extremely small.

---

# 9. Why Earlier Layers Learn Slowly

Consider the following deep neural network.

```text
Output

↓

Layer 5

↓

Layer 4

↓

Layer 3

↓

Layer 2

↓

Layer 1
```

During Backpropagation,

Layer 5 multiplies the gradient once.

Layer 4 multiplies it twice.

Layer 3 multiplies it three times.

Layer 2 multiplies it four times.

Layer 1 multiplies it five times.

Therefore,

Layer 1 receives the smallest gradient.

This is why the earliest layers learn much more slowly than later layers.

---

# 10. Mathematical Summary

Suppose every derivative satisfies

$$
0<f_i'<1
$$

Then,

the overall gradient becomes

$$
\prod_{i=1}^{n}f_i'
$$

As the number of layers increases,

$$
\prod_{i=1}^{n}f_i' \rightarrow0
$$

This is the mathematical definition of the Vanishing Gradient Problem.

---

# 11. Why Is This Mainly a Deep Learning Problem?

Consider two neural networks.

## Shallow Neural Network

Two hidden layers.

$$
0.5^2 = 0.25
$$

The gradient is still large enough for learning.

---

## Deep Neural Network

One hundred hidden layers.

$$
0.5^{100} \approx 7.9\times10^{-31}
$$

The gradient is essentially zero.

This explains why deep neural networks suffer much more than shallow networks.

---

# 12. One Important Insight

Many beginners believe

> **Sigmoid itself causes the Vanishing Gradient Problem.**

This is only partially true.

The actual cause is

- repeated application of the Chain Rule,

combined with

- derivatives consistently smaller than 1.

Sigmoid makes the problem worse because its derivative is always at most **0.25**.

---

# Visual Summary

```text
Backpropagation

↓

Chain Rule

↓

Multiply Many Derivatives

↓

Each Derivative < 1

↓

Gradient Shrinks

↓

Gradient Approaches Zero

↓

Early Layers Stop Learning
```

---

# Difference Between Sigmoid and Tanh for Vanishing Gradients

| Sigmoid | Tanh |
|----------|------|
| Output range: (0,1) | Output range: (-1,1) |
| Maximum derivative = 0.25 | Maximum derivative = 1 |
| Strong Vanishing Gradient effect | Less severe but still affected |
| Not zero-centered | Zero-centered |
| Rarely used in hidden layers today | Occasionally used, but ReLU is preferred |

---

# Interview Questions

## Q1. What is the mathematical cause of the Vanishing Gradient Problem?

**Answer**

The repeated multiplication of derivatives smaller than 1 during Backpropagation causes gradients to decrease exponentially.

---

## Q2. Does the Chain Rule itself cause the problem?

**Answer**

No.

The Chain Rule is mathematically correct.

The problem arises because it repeatedly multiplies small derivatives together.

---

## Q3. Why does Sigmoid contribute to the Vanishing Gradient Problem?

**Answer**

Because the derivative of the Sigmoid function is always less than or equal to **0.25**, causing gradients to shrink after every layer.

---

## Q4. Why are the earliest layers affected the most?

**Answer**

Because gradients must pass through many layers before reaching them, resulting in repeated multiplication and significant shrinking.

---

## Q5. Why do shallow neural networks rarely suffer from this problem?

**Answer**

Because gradients pass through only a few layers, so there are far fewer multiplications of small derivatives.

---

# Summary

Backpropagation computes gradients using the Chain Rule, which multiplies local derivatives across multiple layers.

When these derivatives are consistently smaller than 1, the gradient decreases exponentially as it moves backward through the network.

Activation functions such as Sigmoid and Tanh contribute to this effect because their derivatives are generally less than 1.

As a result,

the earliest layers receive extremely small gradients and learn very slowly.

This mathematical behavior is the fundamental cause of the Vanishing Gradient Problem.

---

# Key Takeaways

✔ Backpropagation relies on the Chain Rule.

✔ The Chain Rule multiplies many local derivatives.

✔ Repeated multiplication of values smaller than 1 causes exponential shrinking.

✔ Sigmoid derivatives are always ≤ 0.25.

✔ Tanh derivatives are also generally less than 1.

✔ Earlier layers receive the smallest gradients.

✔ The Vanishing Gradient Problem is much more severe in deep neural networks.

---

## Next Part

**Part 3 – Effects of the Vanishing Gradient Problem**

In the next chapter, we will study how vanishing gradients affect neural network training in practice, including slow convergence, frozen early layers, reduced model accuracy, and why simply increasing the number of training epochs cannot solve the problem.
