# Unit 5 – Training Challenges & Solutions

# Chapter 3 – Exploding Gradient Problem

## Part 1 – What is the Exploding Gradient Problem?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what the Exploding Gradient Problem is.
- Learn why it occurs during Backpropagation.
- Understand how extremely large gradients affect training.
- Learn why this problem is dangerous for deep neural networks.
- Build the intuition needed for the mathematical explanation in the next chapter.

---

# 1. Introduction

Recall the Gradient Descent update equation.

$$
W = W - \eta \frac{\partial L}{\partial W}
$$

The gradient determines how much the weights change.

Previously, we studied the Vanishing Gradient Problem.

```text
Very Small Gradient

↓

Tiny Weight Update

↓

Slow Learning
```

Now consider the opposite.

```text
Very Large Gradient

↓

Huge Weight Update

↓

Unstable Learning
```

This phenomenon is called the **Exploding Gradient Problem**.

---

# 2. What Does "Exploding" Mean?

The word **exploding** means

```text
Growing Larger

↓

Larger

↓

Much Larger

↓

Extremely Large
```

Therefore,

an exploding gradient is

> **A gradient that becomes extremely large during Backpropagation.**

---

# 3. Where Does It Occur?

Like the Vanishing Gradient Problem,

the Exploding Gradient Problem also occurs during

```text
Forward Propagation

❌ No

↓

Backpropagation

✅ Yes
```

During Backpropagation,

gradients travel from the output layer toward the input layer.

Sometimes,

instead of becoming smaller,

they become larger after every layer.

---

# 4. Visual Example

Suppose the gradient starts as

```text
1
```

After every layer,

it grows.

```text
1

↓

2

↓

5

↓

20

↓

100

↓

1000
```

Eventually,

the gradient becomes extremely large.

---

# 5. Why Is This a Problem?

Recall the Gradient Descent update equation.

Suppose

$$
\frac{\partial L}{\partial W} = 5000
$$

Then

```text
Old Weight

↓

0.50

↓

New Weight

↓

-499.50
```

The weight changes dramatically in a single update.

Instead of gradually approaching the minimum,

the optimizer jumps far away from it.

---

# 6. Effect on Training

Normally,

weights should change smoothly.

```text
0.50

↓

0.49

↓

0.48

↓

0.47
```

With exploding gradients,

the updates become unstable.

```text
0.50

↓

-120

↓

3500

↓

-90000
```

The optimizer oscillates instead of converging.

---

# 7. What Happens to the Loss?

Normally,

the loss decreases gradually.

```text
Epoch

↓

Lower Loss

↓

Better Model
```

With exploding gradients,

the loss becomes unstable.

```text
Epoch 1

Loss = 1.20

↓

Epoch 2

Loss = 35

↓

Epoch 3

Loss = 5000

↓

Epoch 4

Loss = NaN
```

Training completely fails.

---

# 8. What Is NaN?

Sometimes,

weights become so large that the computer can no longer represent them correctly.

This produces

```text
NaN

=

Not a Number
```

When NaN values appear,

the neural network cannot continue training correctly.

---

# 9. Which Networks Are Most Affected?

The Exploding Gradient Problem mainly affects

- Very Deep Feedforward Neural Networks
- Recurrent Neural Networks (RNNs)
- Networks with poor weight initialization
- Models trained using excessively large learning rates

Shallow networks are much less likely to experience this problem.

---

# 10. Real-Life Analogy

Imagine driving a car toward a parking space.

## Normal Driving

```text
Move Slowly

↓

Adjust Steering

↓

Park Successfully
```

---

## Exploding Gradient

```text
Accelerate Hard

↓

Overshoot

↓

Reverse Fast

↓

Overshoot Again

↓

Never Park
```

The optimizer behaves similarly.

Instead of approaching the minimum,

it keeps jumping past it.

---

# 11. Why Didn't We Observe This Earlier?

In previous chapters,

we worked with

- Small neural networks
- Carefully selected weights
- Simple numerical examples

These conditions rarely produce exploding gradients.

However,

modern deep neural networks contain many layers,

and repeated multiplication during Backpropagation can sometimes make gradients grow exponentially.

---

# 12. One Important Insight

Many beginners believe

> **Large gradients mean faster learning.**

This is incorrect.

Large gradients do **not** improve learning.

Instead,

they produce

- Extremely large parameter updates
- Oscillating optimization
- Numerical overflow
- Training failure

Stable gradients—not large gradients—lead to successful learning.

---

# Visual Summary

```text
Loss

↓

Backpropagation

↓

Very Large Gradient

↓

Huge Weight Update

↓

Unstable Optimization

↓

Training Failure
```

---

# Difference Between Vanishing and Exploding Gradients

| Vanishing Gradient | Exploding Gradient |
|--------------------|-------------------|
| Gradient becomes very small | Gradient becomes very large |
| Weight updates become tiny | Weight updates become huge |
| Learning becomes slow | Learning becomes unstable |
| Early layers stop learning | Parameters oscillate wildly |
| Loss decreases slowly | Loss increases or becomes NaN |

---

# Interview Questions

## Q1. What is the Exploding Gradient Problem?

**Answer**

The Exploding Gradient Problem occurs when gradients become extremely large during Backpropagation, causing excessively large weight updates and unstable training.

---

## Q2. During which stage of training does it occur?

**Answer**

It occurs during **Backpropagation**, when gradients propagate from the output layer toward the input layer.

---

## Q3. Why are very large gradients harmful?

**Answer**

Because they produce huge weight updates that prevent the optimizer from converging smoothly.

---

## Q4. What is a common symptom of exploding gradients?

**Answer**

The training loss becomes unstable, oscillates significantly, or eventually becomes **NaN (Not a Number)**.

---

## Q5. Which types of neural networks are especially vulnerable?

**Answer**

Very deep neural networks and recurrent neural networks (RNNs) are especially susceptible to exploding gradients.

---

# Summary

The Exploding Gradient Problem occurs when gradients become excessively large during Backpropagation.

These large gradients produce huge parameter updates, causing unstable optimization, oscillating loss values, and sometimes numerical overflow resulting in NaN values.

Unlike the Vanishing Gradient Problem, where learning becomes too slow, exploding gradients make learning unstable and prevent the optimizer from converging.

Modern Deep Learning addresses this issue using techniques such as Gradient Clipping, better weight initialization, Batch Normalization, and carefully selected learning rates.

---

# Key Takeaways

✔ The Exploding Gradient Problem is the opposite of the Vanishing Gradient Problem.

✔ It occurs during Backpropagation.

✔ Extremely large gradients produce huge weight updates.

✔ Training becomes unstable and may diverge.

✔ Loss values may oscillate or become NaN.

✔ Stable gradients are essential for successful neural network training.

✔ Specialized techniques are required to control exploding gradients.

---

## Next Part

**Part 2 – Why Do Gradients Explode? (Mathematical Explanation)**

In the next chapter, we will derive the Exploding Gradient Problem mathematically using the **Chain Rule**, understand why repeated multiplication of derivatives greater than 1 causes gradients to grow exponentially, and learn why this results in unstable neural network training.
