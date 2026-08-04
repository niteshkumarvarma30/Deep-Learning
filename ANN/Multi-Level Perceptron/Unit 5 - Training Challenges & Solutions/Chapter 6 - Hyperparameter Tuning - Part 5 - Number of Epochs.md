# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 5 – Number of Epochs

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what an Epoch is.
- Differentiate between Epochs, Batches, and Iterations.
- Learn how the Number of Epochs affects training.
- Understand underfitting and overfitting with respect to epochs.
- Learn how to choose an appropriate number of epochs.

---

# 1. Introduction

When training a neural network,

the model repeatedly learns from the training dataset.

One complete pass through the entire dataset is called an

```text
Epoch
```

Training usually consists of multiple epochs.

---

# 2. What is an Epoch?

An Epoch is

> **One complete pass of the entire training dataset through the neural network.**

Suppose the dataset contains

```text
10,000 Samples
```

After the model processes all 10,000 samples once,

```text
Epoch 1

Completed
```

Processing all samples again gives

```text
Epoch 2
```

and so on.

---

# 3. Why Are Multiple Epochs Needed?

Initially,

the weights are randomly initialized.

```text
Random Weights

↓

Poor Predictions
```

After one epoch,

the model has learned only a little.

```text
Epoch 1

↓

Small Improvement
```

More epochs allow the model to gradually improve.

```text
Epoch 1

↓

Epoch 2

↓

Epoch 3

↓

...

↓

Better Model
```

---

# 4. Relationship Between Epoch, Batch, and Iteration

Suppose

```text
Dataset Size = 10,000

Batch Size = 100
```

Number of batches

```text
10,000 / 100

=

100 Batches
```

Each batch causes

```text
One Weight Update
```

Therefore,

```text
1 Epoch

=

100 Iterations
```

General formula

$$
\text{Iterations Per Epoch}
=
\frac{\text{Training Samples}}
{\text{Batch Size}}
$$

---

# 5. Example

Suppose

```text
Training Samples = 6,400

Batch Size = 64

Epochs = 20
```

Iterations per epoch

```text
6400 / 64

=

100
```

Total weight updates

```text
100 × 20

=

2000 Iterations
```

---

# 6. Too Few Epochs

Suppose

```text
Epochs = 2
```

Training stops before the model has learned enough.

Result

```text
High Training Loss

↓

High Validation Loss
```

This is called

```text
Underfitting
```

---

# 7. Too Many Epochs

Suppose

```text
Epochs = 500
```

Initially,

performance improves.

Later,

the model memorizes the training data.

Result

```text
Training Loss ↓

Validation Loss ↑
```

This leads to

```text
Overfitting
```

---

# 8. Appropriate Number of Epochs

A good number of epochs allows the model to

- Learn useful patterns
- Avoid memorization

Usually,

training is stopped automatically using

```text
Early Stopping
```

instead of choosing a fixed number of epochs.

---

# 9. Visual Comparison

## Too Few Epochs

```text
Training

↓

Stop Early

↓

Underfitting
```

---

## Appropriate Epochs

```text
Training

↓

Learn Patterns

↓

Good Generalization
```

---

## Too Many Epochs

```text
Training

↓

Memorization

↓

Overfitting
```

---

# 10. Epochs and Learning Curves

Typical behavior

```text
Training Loss

↓

↓

↓

↓

Validation Loss

↓

↓

Minimum

↑

↑
```

The best epoch is

```text
Lowest Validation Loss
```

This is exactly where Early Stopping terminates training.

---

# 11. Typical Number of Epochs

There is no universal best value.

Common ranges are

| Model Type | Typical Epochs |
|------------|---------------:|
| Small Neural Networks | 20–100 |
| CNNs | 30–200 |
| Transformers | 5–50 |
| Large Language Models | Thousands of optimization steps rather than fixed epochs |

The required number depends on

- Dataset size
- Model complexity
- Learning Rate
- Batch Size
- Optimizer

---

# 12. Real-Life Analogy

Imagine reading a textbook.

### One Reading

```text
Read Once

↓

Limited Understanding
```

---

### Multiple Readings

```text
Read

↓

Review

↓

Practice

↓

Better Understanding
```

---

### Too Many Readings

```text
Read

↓

Memorize Every Sentence

↓

Cannot Apply Concepts
```

The same happens with neural networks.

---

# 13. One Important Insight

Many beginners think

> **More epochs always produce better models.**

This is incorrect.

Too few epochs cause

```text
Underfitting
```

Too many epochs cause

```text
Overfitting
```

The objective is to stop training when the model achieves its best generalization performance.

---

# Visual Summary

```text
Dataset

↓

Epoch 1

↓

Epoch 2

↓

Epoch 3

↓

...

↓

Best Validation Performance

↓

Early Stop
```

---

# Difference Between Epoch, Batch, and Iteration

| Epoch | Batch | Iteration |
|--------|-------|-----------|
| One complete pass through the dataset | A subset of the dataset | One weight update after processing one batch |
| Contains many batches | Contains multiple samples | Happens once per batch |
| Controlled by Number of Epochs | Controlled by Batch Size | Depends on both Epochs and Batch Size |

---

# Interview Questions

## Q1. What is an Epoch?

**Answer**

An Epoch is one complete pass of the entire training dataset through the neural network.

---

## Q2. What is the relationship between Epochs and Iterations?

**Answer**

Each Epoch contains multiple Iterations.

The number of Iterations per Epoch equals

$$
\frac{\text{Training Samples}}{\text{Batch Size}}
$$

---

## Q3. What happens if the number of Epochs is too small?

**Answer**

The model underfits because it has not learned enough from the training data.

---

## Q4. What happens if the number of Epochs is too large?

**Answer**

The model may overfit by memorizing the training data instead of learning general patterns.

---

## Q5. How is the optimal number of Epochs usually determined?

**Answer**

Using Early Stopping, which monitors Validation Loss and stops training automatically when further improvement stops.

---

# Summary

An Epoch represents one complete pass through the training dataset.

Since models rarely learn everything in a single pass, multiple epochs are required.

Too few epochs lead to underfitting, while too many epochs can cause overfitting.

Modern Deep Learning systems often combine a maximum number of epochs with Early Stopping, allowing training to stop automatically when the model reaches its best validation performance.

---

# Key Takeaways

✔ One Epoch = One complete pass through the training dataset.

✔ Each Epoch consists of multiple batches.

✔ Each Batch produces one Iteration (weight update).

✔ Too few epochs cause underfitting.

✔ Too many epochs cause overfitting.

✔ Early Stopping helps determine the optimal number of training epochs automatically.

---

# Next Part

## **Part 6 – Number of Hidden Layers**

In the next chapter, we will study how the **depth of a neural network** affects learning, understand shallow vs deep networks, learn why deeper is not always better, and discover how to choose an appropriate number of hidden layers for different problems.
