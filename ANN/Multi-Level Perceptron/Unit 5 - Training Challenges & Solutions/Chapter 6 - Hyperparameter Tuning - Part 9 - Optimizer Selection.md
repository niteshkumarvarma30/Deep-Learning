# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 9 – Optimizer Selection

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what an optimizer is.
- Learn how optimizers update neural network parameters.
- Compare the major optimization algorithms.
- Learn which optimizers are commonly used in practice.
- Understand how to choose the appropriate optimizer for different tasks.

---

# 1. Introduction

Training a neural network involves minimizing a loss function.

This is done by repeatedly updating the model's parameters.

The component responsible for these updates is called the

```text
Optimizer
```

Without an optimizer,

the neural network cannot learn.

---

# 2. What is an Optimizer?

An optimizer is

> **An algorithm that updates the weights and biases of a neural network to minimize the loss function.**

The optimizer uses

- Gradient Descent
- Gradients from Backpropagation
- Learning Rate

to determine how the parameters should change.

---

# 3. Role of an Optimizer

The training process follows

```text
Forward Propagation

↓

Compute Loss

↓

Backpropagation

↓

Compute Gradients

↓

Optimizer Updates Weights

↓

Next Iteration
```

The optimizer is responsible for the final step.

---

# 4. Why Do We Need Different Optimizers?

Different optimization algorithms

- Converge at different speeds.
- Handle noisy gradients differently.
- Require different amounts of memory.
- Perform differently on different datasets.

There is no single optimizer that is best for every problem.

---

# 5. Common Optimizers

Modern Deep Learning commonly uses

| Optimizer | Main Idea |
|-----------|-----------|
| SGD | Basic Gradient Descent |
| Momentum | Adds previous velocity |
| Nesterov (NAG) | Looks ahead before updating |
| AdaGrad | Adaptive learning rate |
| RMSProp | Adaptive learning rate with moving average |
| Adam | Momentum + RMSProp |
| AdamW | Adam with proper weight decay |

---

# 6. SGD (Stochastic Gradient Descent)

Update Rule

$$
W
=
W
-
\eta
\frac{\partial L}{\partial W}
$$

Advantages

- Simple
- Low memory usage
- Easy to understand

Disadvantages

- Slow convergence
- Can oscillate
- Sensitive to Learning Rate

Typical use

Small models and educational examples.

---

# 7. Momentum

Momentum remembers previous updates.

Instead of moving only according to the current gradient,

it also considers previous movement.

Advantages

- Faster convergence
- Reduced oscillation
- Better optimization

Typical use

Deep neural networks before Adam became popular.

---

# 8. Nesterov Accelerated Gradient (NAG)

NAG improves Momentum by

```text
Look Ahead

↓

Compute Gradient

↓

Update
```

Advantages

- Better convergence
- More accurate updates
- Less overshooting

Typical use

Deep optimization tasks.

---

# 9. AdaGrad

AdaGrad adapts the Learning Rate for each parameter individually.

Frequently updated parameters receive

```text
Smaller Learning Rate
```

Rarely updated parameters receive

```text
Larger Learning Rate
```

Advantages

- Good for sparse data
- Automatic learning rate adaptation

Disadvantages

- Learning Rate eventually becomes too small.

---

# 10. RMSProp

RMSProp improves AdaGrad.

Instead of continuously decreasing the Learning Rate,

it maintains a moving average of squared gradients.

Advantages

- Stable optimization
- Faster convergence
- Suitable for recurrent neural networks

Typical use

RNNs and sequence models.

---

# 11. Adam

Adam combines

```text
Momentum

+

RMSProp
```

Advantages

- Fast convergence
- Adaptive Learning Rates
- Stable optimization
- Minimal tuning required

Typical use

- CNNs
- RNNs
- Transformers
- Most Deep Learning applications

Adam is the default optimizer for many projects.

---

# 12. AdamW

AdamW is an improved version of Adam.

Instead of mixing

```text
Weight Decay

↓

Gradient Update
```

AdamW separates them.

Advantages

- Better regularization
- Better generalization
- Improved performance

Typical use

Modern Transformer models such as

- BERT
- GPT
- Llama
- Vision Transformers

---

# 13. How to Choose an Optimizer?

General recommendations

| Problem Type | Recommended Optimizer |
|--------------|----------------------|
| Beginner Projects | Adam |
| CNNs | Adam |
| RNNs | Adam or RMSProp |
| Transformers | AdamW |
| Research Experiments | SGD + Momentum |
| Large Language Models | AdamW |

These are common starting points,

not strict rules.

---

# 14. Real-Life Analogy

Imagine driving to a destination.

### SGD

```text
Drive

↓

Check Map

↓

Correct Direction
```

---

### Momentum

```text
Keep Previous Speed

↓

Move Faster
```

---

### Adam

```text
Remember Previous Direction

+

Adjust Speed Automatically

↓

Fast Navigation
```

Each optimizer uses a different strategy to reach the destination efficiently.

---

# 15. One Important Insight

Many beginners think

> **Adam is always the best optimizer.**

This is incorrect.

Adam performs extremely well for many tasks,

but some applications,

especially image classification,

may achieve better final accuracy using

```text
SGD + Momentum
```

The optimal optimizer depends on

- Dataset
- Model architecture
- Training objective

---

# Visual Summary

```text
Forward Propagation

↓

Loss

↓

Backpropagation

↓

Gradients

↓

Optimizer

↓

Update Weights

↓

Repeat
```

---

# Comparison of Optimizers

| Optimizer | Main Strength | Main Limitation |
|-----------|---------------|-----------------|
| SGD | Simple | Slow convergence |
| Momentum | Faster than SGD | Requires tuning |
| NAG | Better Momentum | Slightly more computation |
| AdaGrad | Adaptive learning rates | Learning rate becomes too small |
| RMSProp | Stable adaptive updates | Less common than Adam |
| Adam | Fast and stable | Sometimes poorer generalization than SGD |
| AdamW | Better regularization | Slightly more computation |

---

# Interview Questions

## Q1. What is an optimizer?

**Answer**

An optimizer is an algorithm that updates the model's parameters to minimize the loss function using gradients computed during Backpropagation.

---

## Q2. Which optimizer is most commonly used in Deep Learning?

**Answer**

Adam is one of the most widely used optimizers because it combines fast convergence with adaptive learning rates.

---

## Q3. What is the difference between Adam and AdamW?

**Answer**

AdamW separates Weight Decay from the gradient update, leading to better regularization and often better generalization.

---

## Q4. Which optimizer is commonly used for Transformer models?

**Answer**

AdamW is commonly used for modern Transformer architectures such as BERT, GPT, and Llama.

---

## Q5. Is there a universally best optimizer?

**Answer**

No.

The best optimizer depends on the dataset, model architecture, computational resources, and training objective.

---

# Summary

An optimizer determines how a neural network updates its parameters during training.

Different optimizers use different strategies to improve convergence, stability, and generalization.

While Adam is the default choice for many Deep Learning applications, AdamW is widely used for modern Transformer models, and SGD with Momentum remains competitive for certain computer vision tasks.

Choosing the right optimizer is therefore an important hyperparameter tuning decision.

---

# Key Takeaways

✔ Optimizers update model parameters using gradients.

✔ SGD is the simplest optimization algorithm.

✔ Momentum accelerates convergence.

✔ NAG improves Momentum by looking ahead.

✔ AdaGrad and RMSProp use adaptive learning rates.

✔ Adam combines Momentum and RMSProp.

✔ AdamW is the preferred optimizer for many modern Transformer models.

✔ The optimal optimizer depends on the problem being solved.

---

# Next Part

## **Part 10 – Grid Search**

In the next chapter, we will begin **Hyperparameter Optimization Techniques** by studying **Grid Search**, learn how it systematically tests different hyperparameter combinations, understand its advantages and limitations, and compare it with **Random Search** and **Bayesian Optimization**.
