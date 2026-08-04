# Unit 2 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 6 – Momentum Optimizer

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Momentum was introduced.
- Learn the limitations of Gradient Descent.
- Understand the concept of **Velocity**.
- Learn the Momentum update equations.
- Understand how Momentum accelerates learning.
- Learn why Momentum reduces oscillations.
- Understand the real-world intuition behind Momentum.

---

# 1. Why Was Momentum Introduced?

Previously, we studied

- Batch Gradient Descent (BGD)
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent (MBGD)

All of these optimizers update the weights using

$$
\boxed{ w_{new} = w_{old} - \eta \frac{\partial L}{\partial w} }
$$

Although this works,

Gradient Descent has two major limitations.

---

## Problem 1 – Slow Convergence

Imagine the optimizer moving toward the minimum.

```text
Start

↓

•

↓

•

↓

•

↓

Minimum
```

Each update is small.

Therefore,

reaching the minimum may require thousands of iterations.

---

## Problem 2 – Oscillations

Suppose the loss surface looks like a narrow valley.

```text
          /\

         /  \

        /    \

       /      \

      \/\/\/\/\/

        Minimum
```

Instead of moving smoothly,

the optimizer zig-zags.

```text
Left

↓

Right

↓

Left

↓

Right

↓

Minimum
```

This wastes time and slows convergence.

---

# 2. The Idea Behind Momentum

Imagine pushing a heavy ball.

Initially,

the ball moves slowly.

```text
Push

↓

○
```

After continuous pushing,

the ball gains speed.

```text
Push

↓

○────────►
```

Even if you stop pushing for a moment,

the ball continues moving because of its **momentum**.

Deep Learning uses exactly the same idea.

Instead of considering only the **current gradient**,

Momentum also remembers the **previous updates**.

---

# 3. What is Momentum?

## Definition

Momentum is an optimization technique that uses both

- the current gradient,
- and the previous update direction

to compute the next weight update.

Instead of forgetting previous movements,

Momentum remembers them.

---

# 4. What is Velocity?

Momentum introduces a new variable called

$$
\boxed{v}
$$

called the **Velocity**.

Velocity stores information about

- Previous Gradients
- Previous Directions
- Previous Weight Updates

You can think of velocity as the optimizer's **memory**.

---

# 5. Momentum Update Equations

Momentum uses two update equations.

---

## Step 1 – Update Velocity

$$
\boxed{ v = \beta v - \eta \frac{\partial L}{\partial w} }
$$

where

- \(v\) = Velocity
- \(\beta\) = Momentum Coefficient
- \(\eta\) = Learning Rate
- \(\frac{\partial L}{\partial w}\) = Gradient

---

## Step 2 – Update Weights

$$
\boxed{ w_{new} = w_{old} + v }
$$

Notice

Unlike ordinary Gradient Descent,

we do **not** directly subtract the gradient.

Instead,

we update the **velocity first**,

then use the velocity to update the weights.

---

# 6. What is β (Beta)?

The symbol

$$
\beta
$$

controls

> **How much of the previous velocity should be remembered.**

Typical values

```text
0.9

0.95

0.99
```

Most commonly,

```text
β = 0.9
```

Interpretation

- Small β → Less memory
- Large β → More memory

---

# 7. Understanding Velocity

Suppose

Previous Velocity

```text
2
```

Current Gradient

```text
-0.5
```

Momentum combines

```text
Previous Velocity

+

Current Gradient

↓

New Velocity
```

Instead of making completely independent updates,

Momentum smooths the movement.

---

# 8. Why Does Momentum Move Faster?

Without Momentum

```text
•

↓

•

↓

•

↓

Minimum
```

Every update starts from scratch.

---

With Momentum

```text
•

↓

────────►

────────►

────────►

Minimum
```

Previous movement helps the optimizer continue moving in the same direction.

Learning becomes much faster.

---

# 9. Why Does Momentum Reduce Oscillations?

Suppose the optimizer is moving inside a narrow valley.

Without Momentum

```text
←

→

←

→

←

→
```

The optimizer continuously bounces from one side to another.

---

With Momentum

The sideways movement is reduced,

while movement toward the minimum is accelerated.

```text
↓

↓

↓

↓

Minimum
```

This produces a much smoother optimization path.

---

# 10. Complete Training Workflow

```text
Mini-Batch

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Backpropagation

↓

Gradient

↓

Update Velocity

↓

Update Weights

↓

Next Mini-Batch
```

---

# 11. Real-Life Analogy

Imagine riding a bicycle.

Without Momentum,

you must keep pedaling continuously.

```text
Pedal

↓

Move

↓

Stop
```

---

With Momentum,

once the bicycle gains speed,

it continues moving for some distance even if you stop pedaling.

Similarly,

Momentum remembers previous movement and continues progressing toward the minimum.

---

# 12. Advantages of Momentum

## 1. Faster Convergence

The optimizer reaches the minimum more quickly.

---

## 2. Reduced Oscillations

Momentum smooths the optimization path.

---

## 3. Stable Updates

Updates become more consistent.

---

## 4. Better Performance

Momentum usually trains deep neural networks faster than plain Gradient Descent.

---

# 13. Disadvantages of Momentum

- Requires an additional hyperparameter (\(\beta\)).
- A very high Momentum value may overshoot the minimum.
- Still uses a fixed learning rate.

---

# 14. Gradient Descent vs Momentum

| Feature | Gradient Descent | Momentum |
|----------|------------------|----------|
| Uses Current Gradient | ✅ | ✅ |
| Uses Previous Updates | ❌ | ✅ |
| Uses Velocity | ❌ | ✅ |
| Faster Convergence | ❌ | ✅ |
| Reduces Oscillations | ❌ | ✅ |
| Memory of Previous Steps | ❌ | ✅ |

---

# 15. Visualization

## Gradient Descent

```text
Current Gradient

↓

Weight Update

↓

Next Step
```

Every update depends only on the current gradient.

---

## Momentum

```text
Previous Velocity

+

Current Gradient

↓

New Velocity

↓

Weight Update
```

Every update depends on both

- current information,
- previous movement.

---

# Interview Questions

## Q1. Why was Momentum introduced?

**Answer**

To accelerate convergence and reduce oscillations during optimization.

---

## Q2. What is Velocity?

**Answer**

Velocity is a variable that stores information from previous gradients and previous updates.

---

## Q3. What does β (Beta) control?

**Answer**

It controls how much of the previous velocity should be retained.

---

## Q4. What is the commonly used value of β?

**Answer**

$$
\beta = 0.9
$$

---

## Q5. Why is Momentum faster than Gradient Descent?

**Answer**

Because it remembers previous updates and continues moving in the same direction instead of starting every update from scratch.

---

## Q6. Why does Momentum reduce oscillations?

**Answer**

Because previous velocity smooths the optimization path and reduces unnecessary zig-zag movements.

---

# Summary

Momentum improves Gradient Descent by introducing a **Velocity** term that remembers previous updates.

Instead of updating the weights using only the current gradient,

Momentum combines

- previous velocity,
- current gradient,

to produce smoother and faster optimization.

As a result,

Momentum

- converges faster,
- reduces oscillations,
- and trains deep neural networks more efficiently than plain Gradient Descent.

---

# Key Takeaways

✔ Momentum improves ordinary Gradient Descent.

✔ Momentum introduces a new variable called **Velocity (v)**.

✔ Velocity stores information from previous updates.

✔ Momentum Update Equations

Velocity Update

$$
v = \beta v - \eta \frac{\partial L}{\partial w}
$$

Weight Update

$$
w_{new} = w_{old} + v
$$

✔ β controls how much previous velocity is remembered.

✔ Common value of β is **0.9**.

✔ Momentum accelerates convergence.

✔ Momentum reduces oscillations.

✔ Momentum serves as the foundation for more advanced optimizers such as **Adam**.
