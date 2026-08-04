# Unit 3 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 2 – Gradient Descent

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what a **Gradient** is.
- Learn the intuition behind **Gradient Descent**.
- Understand why we move in the **negative gradient direction**.
- Learn the **weight update equation**.
- Understand the **Learning Rate**.
- Solve numerical examples.
- Understand how Gradient Descent minimizes the loss function.

---

# 1. What is Gradient Descent?

In the previous part, we learned that the optimizer's job is to reduce the loss by updating the weights and biases.

However, an important question still remains:

> **How does the optimizer know whether to increase or decrease a weight?**

The answer is **Gradient Descent**.

---

## Definition

Gradient Descent is an optimization algorithm that updates the model's **weights** and **biases** in the direction that **reduces the loss function the fastest**.

Its goal is

$$
\boxed{\text{Minimize the Loss Function}}
$$

---

# 2. What is a Gradient?

The word **Gradient** simply means

> **Slope**

Imagine standing on a hill.

```text
             ▲
            / \
           /   \
          /     \
         ●
```

- A steep hill has a **large gradient**.
- A flat surface has a **small gradient**.

In Deep Learning,

the gradient tells us

> **How much the loss changes when a weight changes slightly.**

For a single weight,

$$
\boxed{ \frac{\partial L}{\partial w} }
$$

where

- \(L\) = Loss
- \(w\) = Weight

This is called the **partial derivative of the loss with respect to the weight**.

---

# 3. Understanding the Gradient

Suppose

Current Weight

```text
w = 2
```

Gradient

```text
∂L/∂w = +5
```

This means

If the weight increases,

the loss increases rapidly.

---

Now suppose

```text
∂L/∂w = -4
```

This means

If the weight increases,

the loss decreases.

Therefore,

the **sign of the gradient** tells us the direction in which the loss changes.

---

# 4. Why Do We Move in the Negative Gradient Direction?

The gradient always points towards the direction of

> **Maximum Increase in the Loss**

However,

our goal is to **minimize** the loss.

Therefore,

we move in the opposite direction.

```text
Gradient

↑

Maximum Increase

↓

Negative Gradient

↓

Maximum Decrease
```

This is why the algorithm is called

**Gradient Descent**

because we are moving **downhill** on the loss surface.

---

# 5. Intuition Behind Gradient Descent

Imagine you are standing on the top of a mountain.

```text
        ▲ Peak
       / \
      /   \
     ●
```

Your goal is to reach the lowest point.

You cannot see the entire mountain.

So you

1. Check the slope.
2. Move a small step downhill.
3. Check the slope again.
4. Repeat.

Eventually,

you reach a point where the slope becomes almost zero.

That point is called the **Minimum**.

Gradient Descent works in exactly the same way.

---

# 6. Gradient Descent Update Equation

The most important equation in optimization is

$$
\boxed{ w_{\text{new}} = w_{\text{old}} - \eta \frac{\partial L}{\partial w} }
$$

where

- \(w_{\text{old}}\) = Current Weight
- \(w_{\text{new}}\) = Updated Weight
- \(\eta\) = Learning Rate
- \(\frac{\partial L}{\partial w}\) = Gradient

---

## Bias Update Equation

Similarly,

the bias is updated as

$$
\boxed{ b_{\text{new}} = b_{\text{old}} - \eta \frac{\partial L}{\partial b} }
$$

Both weights and biases are updated after every iteration.

---

# 7. Understanding the Weight Update Equation

Consider the equation

$$
w_{\text{new}} = w_{\text{old}} - \eta \frac{\partial L}{\partial w}
$$

Every term has a specific meaning.

| Symbol | Meaning |
|---------|----------|
| \(w_{\text{old}}\) | Current weight |
| \(\eta\) | Learning Rate |
| \(\frac{\partial L}{\partial w}\) | Gradient |
| \(w_{\text{new}}\) | Updated weight |

The gradient tells

- the direction of change,

while the learning rate determines

- how large the step should be.

---

# 8. What is the Learning Rate?

The Learning Rate controls

> **How much the weights should change during one update.**

It is represented by

$$
\boxed{\eta}
$$

Typical values

```text
0.1

0.01

0.001

0.0001
```

---

# 9. Large Learning Rate

Suppose the learning rate is very large.

```text
Loss

▲

      •

          •

              •

                  Minimum

↓

Large Jump

↓

Large Jump

↓

Overshoot
```

The optimizer may jump over the minimum repeatedly.

Learning becomes unstable.

---

# 10. Small Learning Rate

Suppose the learning rate is very small.

```text
•

↓

•

↓

•

↓

•

↓

Minimum
```

Learning becomes extremely slow.

The optimizer eventually reaches the minimum,

but requires many iterations.

---

# 11. Good Learning Rate

A properly selected learning rate allows smooth convergence.

```text
•

↓

•

↓

•

↓

Minimum
```

The optimizer reaches the minimum efficiently without overshooting.

---

# 12. Numerical Example

Suppose

Current Weight

$$
w=5
$$

Gradient

$$
\frac{\partial L}{\partial w}=2
$$

Learning Rate

$$
\eta=0.1
$$

Update

$$
w_{\text{new}} = 5 - 0.1\times2
$$

$$
= 5-0.2 = 4.8
$$

The weight has moved in the direction that reduces the loss.

---

# 13. Complete Training Cycle

During every training iteration,

the following steps occur.

```text
Initialize Weights

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss Value

↓

Backpropagation

↓

Compute Gradients

↓

Gradient Descent

↓

Update Weights

↓

Repeat
```

Over many iterations,

the loss gradually decreases.

---

# 14. When Does Gradient Descent Stop?

Training usually stops when one of the following conditions is met.

- The loss stops decreasing.
- The gradients become very close to zero.
- The maximum number of epochs is reached.
- Early Stopping is triggered because validation performance no longer improves.

---

# 15. Advantages of Gradient Descent

- Simple to understand.
- Easy to implement.
- Foundation of almost every modern optimizer.
- Works for both Machine Learning and Deep Learning.

---

# 16. Limitations of Gradient Descent

- Can be slow on very large datasets.
- Sensitive to the learning rate.
- May become trapped in local minima or saddle points.
- Basic Gradient Descent updates parameters only after processing the entire dataset.

These limitations motivate improved optimization algorithms such as

- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent
- Momentum
- RMSProp
- Adam

---

# 17. Real-Life Analogy

Imagine you are hiking in thick fog.

You cannot see the entire mountain.

Your goal is to reach the valley.

At every step,

you

1. Feel the slope beneath your feet.
2. Walk slightly downhill.
3. Feel the slope again.
4. Repeat.

Mapping this analogy to Deep Learning

| Real Life | Deep Learning |
|-----------|---------------|
| Mountain | Loss Surface |
| Height | Loss Value |
| Position | Current Weights |
| Valley | Minimum Loss |
| Walking Downhill | Gradient Descent |

---

# Interview Questions

## Q1. What is Gradient Descent?

**Answer**

Gradient Descent is an optimization algorithm that updates weights and biases to minimize the loss function.

---

## Q2. What is a Gradient?

**Answer**

A gradient is the slope (partial derivative) of the loss function with respect to a parameter.

It tells us how the loss changes when the parameter changes.

---

## Q3. Why do we move in the negative gradient direction?

**Answer**

Because the gradient points toward the direction of maximum increase in the loss.

The negative gradient points toward decreasing the loss.

---

## Q4. Write the Gradient Descent update equation.

$$
\boxed{ w_{\text{new}} = w_{\text{old}} - \eta \frac{\partial L}{\partial w} }
$$

---

## Q5. What is the Learning Rate?

**Answer**

The Learning Rate determines how large each weight update should be.

---

## Q6. What happens if the learning rate is too large?

**Answer**

The optimizer may overshoot the minimum,

making training unstable.

---

## Q7. What happens if the learning rate is too small?

**Answer**

Training becomes very slow because the optimizer takes extremely small steps.

---

# Summary

Gradient Descent is the fundamental optimization algorithm used in Machine Learning and Deep Learning.

It minimizes the loss function by repeatedly updating the model's weights and biases in the **negative gradient direction**.

The **gradient** indicates the direction in which the loss increases most rapidly, while the **learning rate** controls the size of each update.

Together, these concepts form the foundation of almost all modern optimization algorithms.

---

# Key Takeaways

✔ Gradient means **Slope**.

✔ Gradient tells how the loss changes with respect to a parameter.

✔ The optimizer always moves in the **negative gradient direction** to reduce the loss.

✔ Weight Update Equation

$$
w_{\text{new}} = w_{\text{old}} - \eta \frac{\partial L}{\partial w}
$$

✔ Bias Update Equation

$$
b_{\text{new}} = b_{\text{old}} - \eta \frac{\partial L}{\partial b}
$$

✔ The Learning Rate controls the step size.

✔ Large Learning Rate may overshoot the minimum.

✔ Small Learning Rate makes learning slow.

✔ Gradient Descent is the foundation of modern optimizers like SGD, Momentum, RMSProp, and Adam.
