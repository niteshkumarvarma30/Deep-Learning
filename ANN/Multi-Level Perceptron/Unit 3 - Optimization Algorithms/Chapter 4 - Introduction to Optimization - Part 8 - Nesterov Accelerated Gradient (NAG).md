# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 8 – Nesterov Accelerated Gradient (NAG)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why NAG was introduced.
- Learn the limitations of Momentum.
- Understand the concept of **Look Ahead Optimization**.
- Learn how NAG improves Momentum.
- Understand the mathematical equations of NAG.
- Compare Momentum and NAG.
- Learn where NAG is useful.

---

# 1. Why Was NAG Introduced?

Previously, we studied **Momentum Optimizer**.

Momentum improves Gradient Descent by

- remembering previous updates,
- reducing oscillations,
- accelerating convergence.

However,

Momentum still has one limitation.

---

## Problem with Momentum

Momentum computes the gradient at the **current position**.

Suppose the optimizer is moving very fast.

It computes

```text
Current Position

↓

Gradient

↓

Move Forward
```

If the optimizer already has high velocity,

it may move too far and overshoot the minimum because it only checks the gradient where it currently is.

---

# 2. The Main Idea Behind NAG

NAG asks a simple question.

> **Instead of computing the gradient at the current position, why not first predict where Momentum will take us?**

This idea is called

## Look Ahead

Instead of

```text
Current Position

↓

Compute Gradient

↓

Move
```

NAG performs

```text
Current Position

↓

Look Ahead

↓

Compute Gradient

↓

Move
```

This small modification improves optimization significantly.

---

# 3. What is NAG?

## Definition

**Nesterov Accelerated Gradient (NAG)** is an optimization algorithm that improves Momentum by computing the gradient **after taking a predicted step** in the direction of the previous velocity.

Instead of reacting to the current position,

NAG reacts to the predicted future position.

---

# 4. Understanding the Look Ahead Idea

Suppose

Current Weight

```text
w
```

Current Velocity

```text
v
```

Momentum predicts that the next position will approximately be

$$
\boxed{ w+\beta v }
$$

Instead of computing the gradient at

$$
w
$$

NAG computes the gradient at

$$
\boxed{ w+\beta v }
$$

This predicted location is called the

**Look Ahead Position**.

---

# 5. Momentum vs NAG

## Momentum

```text
Current Position

↓

Compute Gradient

↓

Update Velocity

↓

Update Weight
```

---

## NAG

```text
Current Position

↓

Predict Future Position

↓

Compute Gradient

↓

Update Velocity

↓

Update Weight
```

NAG first predicts where it is going before deciding how to move.

---

# 6. Mathematical Formulation

Let

- \(w\) = Weight
- \(v\) = Velocity
- \(g\) = Gradient
- \(\eta\) = Learning Rate
- \(\beta\) = Momentum Coefficient

---

## Step 1 – Predict Future Position

$$
\boxed{ w+\beta v }
$$

---

## Step 2 – Compute Gradient

Instead of

$$
\nabla L(w)
$$

NAG computes

$$
\boxed{ g = \nabla L(w+\beta v) }
$$

Notice

The gradient is calculated at the predicted future position.

---

## Step 3 – Update Velocity

$$
\boxed{ v = \beta v - \eta g }
$$

---

## Step 4 – Update Weight

$$
\boxed{ w = w+v }
$$

---

# 7. Why is NAG Better than Momentum?

Suppose the optimizer is moving quickly toward the minimum.

### Momentum

```text
Current Position

↓

Move Quickly

↓

Overshoot
```

---

### NAG

```text
Current Position

↓

Look Ahead

↓

See Future Gradient

↓

Correct Direction

↓

Move
```

Because NAG checks the future position,

it reduces overshooting and improves convergence.

---

# 8. Real-Life Analogy

Imagine driving a car toward a traffic signal.

### Momentum Driver

Keeps driving based on the current road.

Only brakes after reaching the signal.

---

### NAG Driver

Looks ahead.

Sees the signal becoming red.

Starts braking before reaching it.

Therefore,

the journey becomes smoother and more controlled.

---

# 9. Advantages of NAG

## 1. Faster Convergence

NAG generally converges faster than Momentum.

---

## 2. Reduced Overshooting

The Look Ahead mechanism prevents excessively large updates.

---

## 3. Better Stability

Optimization becomes smoother near the minimum.

---

## 4. Improved Accuracy

Future information helps make better update decisions.

---

# 10. Limitations of NAG

- Slightly more complex than Momentum.
- Requires computing the gradient at the predicted position.
- Modern Deep Learning often prefers Adam because it also provides adaptive learning rates.

---

# 11. Gradient Descent vs Momentum vs NAG

| Feature | Gradient Descent | Momentum | NAG |
|----------|------------------|----------|-----|
| Uses Current Gradient | ✅ | ✅ | ❌ |
| Uses Previous Velocity | ❌ | ✅ | ✅ |
| Looks Ahead | ❌ | ❌ | ✅ |
| Faster than GD | ❌ | ✅ | ✅ |
| Reduces Overshooting | ❌ | Partial | Better |
| Uses Adaptive Learning Rate | ❌ | ❌ | ❌ |

---

# 12. Visualization

## Gradient Descent

```text
Current Position

↓

Gradient

↓

Move
```

---

## Momentum

```text
Current Position

↓

Gradient

↓

Velocity

↓

Move
```

---

## NAG

```text
Current Position

↓

Predict Future Position

↓

Compute Gradient

↓

Velocity

↓

Move
```

---

# 13. Where is NAG Used?

NAG can be used in

- Deep Neural Networks
- Computer Vision
- Speech Recognition
- Natural Language Processing

Although Adam is more popular today,

NAG remains an important algorithm because it represents the evolution of Momentum.

---

# Interview Questions

## Q1. What does NAG stand for?

**Answer**

Nesterov Accelerated Gradient.

---

## Q2. How is NAG different from Momentum?

**Answer**

Momentum computes the gradient at the current position, while NAG computes the gradient at a predicted future position.

---

## Q3. What is the Look Ahead concept?

**Answer**

NAG predicts where Momentum will move next and computes the gradient at that predicted position before updating the weights.

---

## Q4. Why is NAG faster than Momentum?

**Answer**

Because it anticipates future movement and adjusts the update before overshooting the minimum.

---

## Q5. Does NAG replace Momentum?

**Answer**

No.

NAG is an improved version of Momentum that introduces the Look Ahead mechanism while still using velocity.

---

# Summary

Nesterov Accelerated Gradient (NAG) improves the Momentum optimizer by introducing a **Look Ahead** strategy.

Instead of computing the gradient at the current position, NAG first predicts where the optimizer will move using the current velocity and then computes the gradient at that future position.

This allows NAG to anticipate changes in the loss surface, reduce overshooting, improve stability, and converge faster than standard Momentum.

Although modern deep learning often uses Adam, NAG remains an important milestone in the evolution of optimization algorithms.

---

# Key Takeaways

✔ NAG stands for **Nesterov Accelerated Gradient**.

✔ NAG is an improvement over Momentum.

✔ NAG introduces the **Look Ahead** concept.

✔ Instead of computing the gradient at the current position,

$$
\nabla L(w)
$$

NAG computes

$$
\nabla L(w+\beta v)
$$

✔ NAG still uses **Velocity**, just like Momentum.

✔ NAG reduces overshooting near the minimum.

✔ NAG generally converges faster and more smoothly than Momentum.

✔ NAG helped pave the way for more advanced optimizers such as Adam.
