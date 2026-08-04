# Unit 5 – Training Challenges & Solutions

# Chapter 3 – Exploding Gradient Problem

## Part 3 – Effects of the Exploding Gradient Problem

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how exploding gradients affect neural network training.
- Learn why optimization becomes unstable.
- Understand why weights diverge instead of converging.
- Recognize the symptoms of exploding gradients during model training.
- Learn why training may suddenly fail with NaN values.

---

# 1. Introduction

Recall the Gradient Descent update equation.

$$
W = W - \eta \frac{\partial L}{\partial W}
$$

The gradient determines the size of the weight update.

When gradients become extremely large,

the weight updates also become extremely large.

Instead of moving toward the minimum,

the optimizer becomes unstable.

---

# 2. Effect 1 – Huge Weight Updates

Normally,

weights change gradually.

```text
0.50

↓

0.49

↓

0.48

↓

0.47
```

This allows the optimizer to approach the minimum smoothly.

With exploding gradients,

suppose

$$
\frac{\partial L}{\partial W}=5000
$$

The update becomes

```text
Old Weight

↓

0.50

↓

New Weight

↓

-499.50
```

The parameter jumps a huge distance in a single iteration.

---

# 3. Effect 2 – Optimizer Overshoots the Minimum

Normally,

Gradient Descent moves toward the minimum.

```text
Current Position

↓

Small Step

↓

Minimum
```

With exploding gradients,

the update becomes too large.

```text
Current Position

↓

Huge Step

↓

Overshoot Minimum

↓

Another Huge Step

↓

Overshoot Again
```

Instead of converging,

the optimizer keeps jumping across the minimum.

---

# 4. Effect 3 – Oscillating Loss

A healthy training process looks like

```text
Epoch

↓

Loss

↓

Lower Loss

↓

Better Model
```

With exploding gradients,

the loss oscillates dramatically.

```text
Epoch 1

Loss = 1.2

↓

Epoch 2

Loss = 15

↓

Epoch 3

Loss = 2

↓

Epoch 4

Loss = 80

↓

Epoch 5

Loss = 5

↓

Epoch 6

Loss = 500
```

Instead of decreasing,

the loss fluctuates wildly.

---

# 5. Effect 4 – Divergence

Sometimes,

the optimizer moves farther away from the optimum after every update.

```text
Minimum

↓

Closer

↓

Farther

↓

Much Farther

↓

Very Far Away
```

The model never converges.

This behavior is called **divergence**.

---

# 6. Effect 5 – Numerical Overflow

Large gradients produce very large weights.

Eventually,

the numbers become too large for the computer.

Example

```text
100

↓

10,000

↓

10⁸

↓

10¹⁶

↓

10³⁰

↓

Overflow
```

The floating-point representation can no longer store these values accurately.

---

# 7. Effect 6 – NaN Values

After numerical overflow,

the training process may produce

```text
NaN

=

Not a Number
```

Examples include

```text
Loss = NaN

Weight = NaN

Gradient = NaN
```

Once NaN values appear,

the model can no longer continue training correctly.

---

# 8. Effect 7 – Training Completely Fails

A typical training log might look like

```text
Epoch 1

Loss = 2.1

↓

Epoch 2

Loss = 1.4

↓

Epoch 3

Loss = 0.9

↓

Epoch 4

Loss = 75

↓

Epoch 5

Loss = 3200

↓

Epoch 6

Loss = NaN
```

Training suddenly collapses.

---

# 9. Symptoms You Can Observe

When training a model,

exploding gradients often produce these symptoms.

- Loss suddenly increases.
- Loss oscillates dramatically.
- Parameters become extremely large.
- Gradients become extremely large.
- NaN values appear.
- Training crashes or diverges.

---

# 10. Real-Life Analogy

Imagine trying to adjust the temperature of a shower.

## Normal Adjustment

```text
Cold

↓

Small Adjustment

↓

Comfortable Temperature
```

---

## Exploding Gradient

```text
Cold

↓

Maximum Hot

↓

Maximum Cold

↓

Maximum Hot

↓

Never Stable
```

Instead of making small corrections,

you keep making huge adjustments.

The optimizer behaves in the same way.

---

# 11. Why This Is Dangerous

Exploding gradients are particularly dangerous because

- Training may appear normal initially.
- The loss suddenly becomes unstable.
- Parameters grow uncontrollably.
- Numerical overflow occurs.
- Training completely fails.

Unlike the Vanishing Gradient Problem,

which slows learning,

the Exploding Gradient Problem can terminate training entirely.

---

# 12. One Important Insight

Many beginners believe

> **A rapidly changing loss means the model is learning quickly.**

This is incorrect.

Healthy training should exhibit

- Smooth convergence
- Stable loss reduction
- Controlled parameter updates

Large oscillations usually indicate unstable optimization rather than better learning.

---

# Visual Summary

```text
Exploding Gradient

↓

Huge Gradients

↓

Huge Weight Updates

↓

Overshooting

↓

Oscillating Loss

↓

Numerical Overflow

↓

NaN Values

↓

Training Failure
```

---

# Difference Between Normal Training and Exploding Gradients

| Normal Training | Exploding Gradient |
|-----------------|-------------------|
| Moderate gradients | Extremely large gradients |
| Small weight updates | Huge weight updates |
| Smooth convergence | Overshooting |
| Loss decreases steadily | Loss oscillates |
| Stable optimization | Unstable optimization |
| Successful training | Training failure |

---

# Interview Questions

## Q1. What is the first practical effect of exploding gradients?

**Answer**

Exploding gradients produce extremely large weight updates.

---

## Q2. Why does the optimizer overshoot the minimum?

**Answer**

Because very large gradients produce excessively large parameter updates, causing the optimizer to jump past the optimum.

---

## Q3. What is divergence?

**Answer**

Divergence occurs when the optimizer moves farther away from the minimum instead of converging toward it.

---

## Q4. Why do NaN values appear?

**Answer**

Very large gradients and weights can cause numerical overflow, resulting in invalid floating-point values such as NaN.

---

## Q5. What symptoms indicate exploding gradients?

**Answer**

- Oscillating loss
- Rapidly increasing loss
- Extremely large gradients
- Very large parameter values
- NaN values
- Training failure

---

# Summary

The Exploding Gradient Problem causes gradients to become extremely large during Backpropagation.

These large gradients produce huge weight updates, causing the optimizer to overshoot the optimum, oscillate, and eventually diverge.

As the weights continue growing, numerical overflow may occur, producing NaN values and causing training to fail completely.

Recognizing these symptoms is essential for diagnosing unstable neural network training.

---

# Key Takeaways

✔ Exploding gradients produce huge weight updates.

✔ Large updates cause the optimizer to overshoot the minimum.

✔ Loss values oscillate instead of decreasing smoothly.

✔ Numerical overflow may produce NaN values.

✔ Training can diverge and fail completely.

✔ Stable optimization requires controlling gradient magnitude.

---

## Next Part

**Part 4 – Solutions to the Exploding Gradient Problem**

In the next chapter, we will study the major techniques used to control exploding gradients, including:

- Gradient Clipping
- Proper Weight Initialization
- Batch Normalization
- Learning Rate Reduction
- Adaptive Optimizers (Adam, RMSProp)

and understand how these methods stabilize deep neural network training.
