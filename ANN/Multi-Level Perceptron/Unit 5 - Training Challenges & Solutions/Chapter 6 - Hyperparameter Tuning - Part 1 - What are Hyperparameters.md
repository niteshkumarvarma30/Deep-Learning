# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 1 – What are Hyperparameters?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Hyperparameters are.
- Differentiate between Parameters and Hyperparameters.
- Learn why Hyperparameter Tuning is necessary.
- Understand how Hyperparameters influence model performance.
- Build the foundation for advanced Hyperparameter Tuning techniques.

---

# 1. Introduction

When training a neural network,

there are two different types of values involved.

```text
Parameters

Hyperparameters
```

Many beginners confuse these two concepts.

Understanding the difference is essential because

- **Parameters** are learned automatically.
- **Hyperparameters** are chosen by the developer before training.

---

# 2. What are Parameters?

Parameters are

> **Values that the neural network learns automatically during training.**

Examples include

- Weights
- Biases

Example

```text
Input

↓

Weight = 0.72

↓

Neuron

↓

Bias = -0.14

↓

Output
```

These values are updated during training using

- Forward Propagation
- Backpropagation
- Gradient Descent

The developer does **not** manually assign their final values.

---

# 3. What are Hyperparameters?

Hyperparameters are

> **Settings chosen before training begins that control how the model learns.**

Unlike parameters,

they are **not learned automatically**.

The developer (or an automated tuning algorithm) selects them before training starts.

Examples include

- Learning Rate
- Batch Size
- Number of Epochs
- Number of Hidden Layers
- Number of Neurons
- Optimizer
- Activation Function
- Dropout Rate
- Weight Decay (L2 Regularization)

---

# 4. Why Are They Called Hyperparameters?

The prefix

```text
Hyper
```

means

> **Above** or **outside**.

Parameters belong **inside** the neural network and are learned.

Hyperparameters exist **outside** the learning process and determine **how learning occurs**.

---

# 5. Example

Suppose we build a neural network.

Before training,

we choose

```text
Learning Rate = 0.001

Batch Size = 32

Epochs = 100

Optimizer = Adam

Hidden Layers = 3
```

These values remain fixed throughout training (unless deliberately modified by methods such as Learning Rate Scheduling).

Meanwhile,

the model automatically learns

```text
Weight 1

Weight 2

...

Bias 1

Bias 2
```

---

# 6. Why Are Hyperparameters Important?

Two identical neural networks

can produce completely different results

simply because they use different hyperparameters.

Example

## Model A

```text
Learning Rate = 1
```

Training may diverge.

---

## Model B

```text
Learning Rate = 0.001
```

Training converges successfully.

The architecture is identical,

but performance is completely different.

---

# 7. Common Hyperparameters

Some of the most important hyperparameters are

| Hyperparameter | Purpose |
|---------------|---------|
| Learning Rate | Controls the step size during optimization |
| Batch Size | Number of training samples processed before updating weights |
| Number of Epochs | Number of complete passes through the training dataset |
| Hidden Layers | Controls network depth |
| Number of Neurons | Controls model capacity |
| Activation Function | Determines neuron output behavior |
| Optimizer | Controls how weights are updated |
| Dropout Rate | Helps reduce overfitting |
| Weight Decay (L2) | Controls regularization strength |

---

# 8. Why Can't the Model Learn Hyperparameters?

The learning algorithm updates only

```text
Weights

Biases
```

Hyperparameters define **how** learning itself occurs.

For example,

Gradient Descent uses the Learning Rate,

but it does **not** automatically determine the best Learning Rate.

That decision must be made

- By the developer, or
- By a Hyperparameter Tuning algorithm.

---

# 9. Real-Life Analogy

Imagine baking a cake.

Before baking,

you decide

```text
Temperature

Baking Time

Oven Mode
```

These are selected **before** the cake is baked.

They are like **Hyperparameters**.

During baking,

the cake rises naturally.

This is similar to the neural network automatically learning its

```text
Weights

Biases
```

You control the recipe,

not every air bubble inside the cake.

---

# 10. One Important Insight

Many beginners think

> **Hyperparameters are learned during Backpropagation.**

This is incorrect.

Backpropagation updates only

- Weights
- Biases

Hyperparameters are chosen **before training** and remain fixed unless explicitly changed.

---

# Visual Summary

```text
Before Training

↓

Choose Hyperparameters

↓

Start Training

↓

Learn Parameters

↓

Finished Model
```

---

# Difference Between Parameters and Hyperparameters

| Parameters | Hyperparameters |
|------------|-----------------|
| Learned automatically | Chosen before training |
| Updated during Backpropagation | Not updated during Backpropagation |
| Include weights and biases | Include Learning Rate, Batch Size, Epochs, etc. |
| Change during training | Usually remain fixed during training |
| Define the learned model | Control how the model learns |

---

# Interview Questions

## Q1. What are Hyperparameters?

**Answer**

Hyperparameters are settings chosen before training that control how a Machine Learning or Deep Learning model learns.

---

## Q2. What is the difference between Parameters and Hyperparameters?

**Answer**

Parameters (weights and biases) are learned automatically during training, whereas Hyperparameters are chosen before training and control the learning process.

---

## Q3. Give three examples of Hyperparameters.

**Answer**

- Learning Rate
- Batch Size
- Number of Epochs

Other examples include the Optimizer, Number of Hidden Layers, and Dropout Rate.

---

## Q4. Are Hyperparameters updated during Backpropagation?

**Answer**

No.

Backpropagation updates only the model parameters (weights and biases), not the hyperparameters.

---

## Q5. Why are Hyperparameters important?

**Answer**

Because they strongly influence training speed, convergence, model performance, computational cost, and generalization.

---

# Summary

Hyperparameters are configuration settings selected before training begins that determine how a neural network learns.

Unlike parameters, which are automatically learned through Backpropagation, hyperparameters remain under the control of the developer or an automated tuning algorithm.

Selecting appropriate hyperparameters is critical because they directly affect convergence speed, training stability, computational efficiency, and final model performance.

---

# Key Takeaways

✔ Hyperparameters are chosen before training.

✔ Parameters are learned during training.

✔ Hyperparameters control the learning process.

✔ Backpropagation updates only weights and biases.

✔ Good Hyperparameter selection can dramatically improve model performance.

---

# Next Part

## **Part 2 – Parameters vs Hyperparameters (Detailed Comparison)**

In the next chapter, we will perform a detailed comparison between **Parameters** and **Hyperparameters**, understand their roles throughout the training pipeline, and answer one of the most common interview questions in Machine Learning and Deep Learning.
