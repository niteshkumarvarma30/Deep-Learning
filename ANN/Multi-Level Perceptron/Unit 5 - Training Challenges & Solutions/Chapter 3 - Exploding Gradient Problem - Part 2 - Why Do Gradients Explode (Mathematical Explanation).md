# Unit 5 – Training Challenges & Solutions

# Chapter 3 – Exploding Gradient Problem

## Part 2 – Why Do Gradients Explode? (Mathematical Explanation)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the mathematical cause of the Exploding Gradient Problem.
- Learn how the Chain Rule can amplify gradients.
- Understand why repeated multiplication of numbers greater than 1 causes exponential growth.
- Learn the role of weight matrices in exploding gradients.
- Build the mathematical foundation for Gradient Clipping and other stabilization techniques.

---

# 1. Recap: Backpropagation Uses the Chain Rule

Recall the gradient computation.

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial a_n} \times \frac{\partial a_n}{\partial z_n} \times \frac{\partial z_n}{\partial a_{n-1}} \times \cdots \times \frac{\partial z_1}{\partial W}
$$

Notice something important.

The final gradient is obtained by **multiplying many local derivatives together**.

Previously,

the derivatives were **smaller than 1**, causing gradients to vanish.

Now,

suppose the derivatives become **greater than 1**.

---

# 2. What Happens When We Multiply Large Numbers?

Suppose every derivative equals

$$
2
$$

Now multiply them repeatedly.

```text
2

↓

2 × 2 = 4

↓

4 × 2 = 8

↓

8 × 2 = 16

↓

16 × 2 = 32

↓

...
```

Instead of shrinking,

the gradient grows rapidly.

---

# 3. Exponential Growth of Gradients

Suppose a neural network contains

10 hidden layers.

If every derivative equals

$$
2
$$

then

$$
2^{10} = 1024
$$

Now consider

50 hidden layers.

$$
2^{50} = 1.1259\times10^{15}
$$

The gradient becomes astronomically large.

This is the **Exploding Gradient Problem**.

---

# 4. Why Does the Chain Rule Cause This?

The Chain Rule itself is mathematically correct.

The real issue is

> **Repeated multiplication of numbers greater than 1.**

Every multiplication amplifies the gradient.

As the number of layers increases,

the growth becomes exponential.

---

# 5. Role of Weight Matrices

During Backpropagation,

the error term (delta) for a hidden layer is

$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(Z^{[l]})
$$

Notice that

every hidden layer multiplies the gradient by the weight matrix.

If the weights become very large,

the gradient also becomes larger.

Example

```text
Gradient = 2

↓

Weight = 5

↓

New Gradient = 10

↓

Weight = 5

↓

New Gradient = 50

↓

Weight = 5

↓

New Gradient = 250
```

The gradient keeps increasing after every layer.

---

# 6. Large Initial Weights

Suppose

all weights are initialized as

```text
W = 10
```

Then

```text
Input

↓

Large Activations

↓

Large Gradients

↓

Even Larger Weight Updates

↓

Training Instability
```

This explains why proper weight initialization is extremely important.

---

# 7. Role of Activation Functions

Unlike the Vanishing Gradient Problem,

activation functions are usually **not the primary cause** of exploding gradients.

Instead,

exploding gradients are commonly caused by

- Large weight values
- Repeated matrix multiplications
- Deep network architectures

Activation functions may contribute,

but large weights are generally the dominant factor.

---

# 8. Visualizing Gradient Growth

Suppose the initial gradient equals

```text
1
```

Each layer multiplies it by

```text
2
```

The gradient evolves as

```text
1

↓

2

↓

4

↓

8

↓

16

↓

32

↓

64

↓

...
```

The growth is exponential.

---

# 9. Why Deep Networks Are More Vulnerable

Consider two neural networks.

## Shallow Neural Network

Two hidden layers.

$$
2^2=4
$$

The gradient remains manageable.

---

## Deep Neural Network

Fifty hidden layers.

$$
2^{50} = 1.1259\times10^{15}
$$

The gradient becomes enormous.

This explains why deep neural networks are much more susceptible to exploding gradients.

---

# 10. Mathematical Summary

Suppose every derivative satisfies

$$
f_i' > 1
$$

Then,

the total gradient becomes

$$
\prod_{i=1}^{n} f_i'
$$

As the number of layers increases,

$$
\prod_{i=1}^{n} f_i' \rightarrow \infty
$$

This is the mathematical definition of the **Exploding Gradient Problem**.

---

# 11. Relationship Between Vanishing and Exploding Gradients

Both problems originate from the same mathematical principle.

| Derivative Value | Result |
|------------------|--------|
| Less than 1 | Gradient shrinks (Vanishing Gradient) |
| Equal to 1 | Stable Gradient Flow |
| Greater than 1 | Gradient grows (Exploding Gradient) |

The only difference is whether repeated multiplication decreases or increases the gradient.

---

# 12. One Important Insight

Many beginners think

> **Exploding gradients occur because activation functions are bad.**

This is generally incorrect.

The primary cause is

- repeated multiplication through the Chain Rule,
- combined with large weights or large derivatives.

The mathematics is exactly the opposite of the Vanishing Gradient Problem.

---

# Visual Summary

```text
Backpropagation

↓

Chain Rule

↓

Multiply Many Derivatives

↓

Each Derivative > 1

↓

Gradient Grows Exponentially

↓

Huge Weight Updates

↓

Unstable Training
```

---

# Difference Between Vanishing and Exploding Gradients

| Vanishing Gradient | Exploding Gradient |
|--------------------|-------------------|
| Derivatives < 1 | Derivatives > 1 |
| Gradient decreases exponentially | Gradient increases exponentially |
| Tiny weight updates | Huge weight updates |
| Slow learning | Unstable learning |
| Early layers stop learning | Parameters diverge |
| Loss decreases slowly | Loss oscillates or becomes NaN |

---

# Interview Questions

## Q1. What is the mathematical cause of the Exploding Gradient Problem?

**Answer**

Repeated multiplication of derivatives greater than 1 during Backpropagation causes gradients to increase exponentially.

---

## Q2. Does the Chain Rule itself cause exploding gradients?

**Answer**

No.

The Chain Rule is mathematically correct.

The problem arises because repeated multiplication amplifies large derivatives.

---

## Q3. Why can large weight values cause exploding gradients?

**Answer**

Large weights amplify gradients during Backpropagation, causing them to grow larger after every layer.

---

## Q4. Why are deep neural networks more vulnerable?

**Answer**

Because gradients pass through many layers, resulting in repeated multiplication and exponential growth.

---

## Q5. How is the Exploding Gradient Problem related to the Vanishing Gradient Problem?

**Answer**

Both arise from repeated multiplication during the Chain Rule.

- Derivatives smaller than 1 produce vanishing gradients.
- Derivatives greater than 1 produce exploding gradients.

---

# Summary

Backpropagation computes gradients using the Chain Rule, which multiplies local derivatives across multiple layers.

When these derivatives or weight matrices have values greater than 1, the gradient grows exponentially as it propagates backward.

This produces extremely large parameter updates, unstable optimization, oscillating loss values, and sometimes numerical overflow.

Understanding this mathematical behavior explains why proper initialization, controlled learning rates, and Gradient Clipping are essential for stable deep neural network training.

---

# Key Takeaways

✔ Backpropagation relies on the Chain Rule.

✔ Repeated multiplication of values greater than 1 causes exponential gradient growth.

✔ Large weight matrices amplify gradients.

✔ Deep neural networks are more susceptible to exploding gradients.

✔ Stable training requires controlling gradient magnitude.

---

## Next Part

**Part 3 – Effects of the Exploding Gradient Problem**

In the next chapter, we will study the practical consequences of exploding gradients, including unstable optimization, oscillating loss, parameter divergence, numerical overflow, and why training may suddenly produce **NaN (Not a Number)** values.
