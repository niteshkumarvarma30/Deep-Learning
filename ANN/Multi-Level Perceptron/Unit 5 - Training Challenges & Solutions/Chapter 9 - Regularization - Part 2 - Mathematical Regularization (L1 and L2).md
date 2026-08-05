# Unit 5 – Training Challenges & Solutions

# Chapter 9 – Regularization

## Part 2 – Mathematical Regularization (L1 and L2)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how L1 and L2 Regularization penalize large weights.
- Understand the mathematical formulas for L1 (Lasso) and L2 (Ridge) Regularization.
- Explain the difference in the effects of L1 vs L2 on the network's weights.

---

# 1. Introduction

A neural network memorizes training data by assigning extremely large values to certain weights. If a weight is massive, that specific feature dominates the network's decision, making the model highly sensitive to tiny changes (noise).

To prevent this, we modify the **Cost Function (Loss)**. We tell the network:
*"Your goal is to minimize the Error, BUT I will heavily penalize you if your weights get too big."*

This is the core concept of Mathematical Regularization.

---

# 2. L2 Regularization (Ridge Regression)

L2 Regularization is the most common form of mathematical regularization in deep learning (often called **Weight Decay**).

We add a penalty term to the original Loss function. The penalty is the **sum of the squared weights**.

## Mathematical Equation

$$
\text{Total Cost} = \text{Original Loss} + \frac{\lambda}{2m} \sum_{l=1}^{L} ||W^{[l]}||^2
$$

Where:
- \( \lambda \) (Lambda) is the Regularization Parameter (a hyperparameter you choose, e.g., 0.01).
- \( m \) is the number of training examples.
- \( ||W^{[l]}||^2 \) is the sum of the squares of all weights in the network.

## How it works

During Gradient Descent, the optimizer tries to minimize the Total Cost.
If the weights get too large, the penalty term gets huge. Therefore, Gradient Descent is forced to keep the weights as small as possible while still solving the problem.

Smaller weights mean the network relies on *all* features a little bit, rather than heavily relying on just a few features. This creates a much smoother, generalized model.

---

# 3. L1 Regularization (Lasso Regression)

L1 Regularization is similar, but instead of squaring the weights, we take the **absolute value** of the weights.

## Mathematical Equation

$$
\text{Total Cost} = \text{Original Loss} + \frac{\lambda}{m} \sum_{l=1}^{L} |W^{[l]}|
$$

## How it works (Sparsity)

Because of the geometry of absolute values vs squares, L1 Regularization tends to drive the weights of less important features to **exactly zero**.

If a weight becomes exactly zero, that feature is completely ignored by the neural network. Therefore, L1 Regularization acts as a built-in **Feature Selection** mechanism, making the network sparse.

---

# 4. L1 vs L2 Regularization

| Feature | L1 Regularization | L2 Regularization |
|---------|-------------------|-------------------|
| **Penalty Term** | Absolute value of weights (\( \|W\| \)) | Squared value of weights (\( W^2 \)) |
| **Effect on Weights** | Drives many weights to exactly 0 | Drives weights close to 0, but rarely exactly 0 |
| **Sparsity** | Creates a sparse model | Creates a dense model with small weights |
| **Use Case** | When you have thousands of features and want to ignore useless ones (Feature Selection) | Default choice for Deep Learning to prevent overfitting |

In Deep Learning, **L2 Regularization is used far more often** than L1, as maintaining all features with small weights usually leads to better performance than entirely zeroing them out.

---

# Interview Questions

## Q1. How does L2 Regularization (Weight Decay) prevent overfitting?

**Answer**

L2 Regularization adds a penalty term to the loss function proportional to the square of the network's weights. This forces the optimizer to keep the weights small during training. Smaller weights mean the model is less complex, smoother, and less sensitive to noisy data, which directly prevents overfitting.

---

## Q2. What is the primary difference between the effects of L1 and L2 regularization?

**Answer**

L1 Regularization drives the weights of less important features to exactly zero, resulting in a sparse network and performing automatic feature selection. L2 Regularization drives weights to become very small, but not zero, keeping all features slightly active.

---

# Summary

By mathematically penalizing large weights, L1 and L2 regularization prevent a neural network from becoming overly complex and memorizing training data. L2 (Weight Decay) is the standard mathematical regularization used in modern neural networks.

---

# Key Takeaways

✔ Regularization is added as a penalty to the Loss Function.
✔ L2 uses squared weights and keeps weights small (Weight Decay).
✔ L1 uses absolute weights and drives weights to exactly zero (Sparsity).
✔ \( \lambda \) (Lambda) controls how harsh the penalty is.
