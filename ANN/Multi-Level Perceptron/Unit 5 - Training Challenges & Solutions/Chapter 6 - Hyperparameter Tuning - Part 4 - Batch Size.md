# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 4 – Batch Size

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Batch Size is.
- Learn why datasets are divided into batches.
- Understand how Batch Size affects Gradient Descent.
- Learn the advantages and disadvantages of different Batch Sizes.
- Choose an appropriate Batch Size for Deep Learning models.

---

# 1. Introduction

Suppose you have a dataset containing

```text
60,000 Images
```

Should the neural network process

```text
All 60,000 Images

at once?
```

Usually,

the answer is **No.**

Instead,

the dataset is divided into

```text
Small Groups

↓

Called Batches
```

The number of samples in each batch is called the

> **Batch Size**

---

# 2. What is Batch Size?

Batch Size is

> **The number of training samples processed before the model updates its weights once.**

Example

Suppose

```text
Dataset Size = 10,000 Samples

Batch Size = 100
```

The dataset is divided into

```text
10,000 ÷ 100

=

100 Batches
```

The model processes

- Batch 1
- Update Weights

↓

- Batch 2
- Update Weights

↓

...

until all batches are completed.

---

# 3. Relationship with Gradient Descent

Recall the three Gradient Descent methods.

---

## Batch Gradient Descent

```text
Entire Dataset

↓

One Weight Update
```

Batch Size

```text
=

Entire Dataset
```

---

## Stochastic Gradient Descent (SGD)

```text
One Sample

↓

One Weight Update
```

Batch Size

```text
=

1
```

---

## Mini-Batch Gradient Descent

```text
Small Batch

↓

One Weight Update
```

Typical Batch Sizes

```text
16

32

64

128

256
```

Most Deep Learning models use **Mini-Batch Gradient Descent**.

---

# 4. Why Use Batches?

Processing an entire dataset at once may

- Require too much RAM
- Exceed GPU memory
- Slow down training

Instead,

Mini-Batches

- Reduce memory usage
- Speed up training
- Improve computational efficiency

---

# 5. Small Batch Size

Example

```text
Batch Size = 8
```

Advantages

- Lower memory usage
- More frequent weight updates
- Better generalization in many cases

Disadvantages

- Training is slower
- Noisier gradients
- Less efficient GPU utilization

---

# 6. Large Batch Size

Example

```text
Batch Size = 1024
```

Advantages

- Faster computation
- Better GPU utilization
- Stable gradient estimates

Disadvantages

- High memory consumption
- Fewer weight updates
- May reduce generalization

---

# 7. Visual Comparison

## Small Batch

```text
Batch

↓

Update

↓

Batch

↓

Update

↓

Batch

↓

Update
```

Many updates.

---

## Large Batch

```text
Large Batch

↓

Update

↓

Large Batch

↓

Update
```

Fewer updates.

---

# 8. Batch Size and Training Speed

Suppose

```text
Dataset = 6,400 Samples
```

---

### Batch Size = 32

```text
6400 / 32

=

200 Updates
```

---

### Batch Size = 64

```text
6400 / 64

=

100 Updates
```

---

### Batch Size = 128

```text
6400 / 128

=

50 Updates
```

Larger Batch Sizes require fewer weight updates per epoch.

---

# 9. Batch Size and Memory

Suppose one image occupies

```text
2 MB
```

---

Batch Size = 16

```text
16 × 2 MB

=

32 MB
```

---

Batch Size = 256

```text
256 × 2 MB

=

512 MB
```

Larger batches require significantly more memory.

---

# 10. Typical Batch Sizes

Common choices include

| Hardware | Typical Batch Size |
|-----------|-------------------:|
| CPU | 16–32 |
| Small GPU | 32–64 |
| Medium GPU | 64–128 |
| High-End GPU | 128–512 |

The optimal Batch Size depends on

- GPU memory
- Dataset size
- Model architecture
- Training objective

---

# 11. Real-Life Analogy

Imagine carrying books.

### Batch Size = 1

```text
One Book

↓

Walk

↓

Return

↓

Repeat
```

Many trips.

---

### Batch Size = 100

```text
Carry Many Books

↓

One Trip
```

Fewer trips,

but much heavier.

Batch Size determines how much work is done before returning.

---

# 12. One Important Insight

Many beginners think

> **Larger Batch Sizes always produce better models.**

This is incorrect.

Very large batches often train faster,

but they may produce models that generalize worse than models trained with moderate batch sizes.

The goal is to find a balance between

- Speed
- Memory usage
- Generalization

---

# Visual Summary

```text
Dataset

↓

Divide into Batches

↓

Process One Batch

↓

Compute Loss

↓

Backpropagation

↓

Update Weights

↓

Next Batch
```

---

# Comparison of Different Batch Sizes

| Small Batch Size | Large Batch Size |
|------------------|------------------|
| Lower memory usage | Higher memory usage |
| More weight updates | Fewer weight updates |
| Slower computation | Faster computation |
| Noisier gradients | Smoother gradients |
| Often better generalization | May reduce generalization |

---

# Interview Questions

## Q1. What is Batch Size?

**Answer**

Batch Size is the number of training samples processed before the model updates its weights once.

---

## Q2. What is the Batch Size in Stochastic Gradient Descent?

**Answer**

Batch Size = **1**.

---

## Q3. What is the Batch Size in Batch Gradient Descent?

**Answer**

The Batch Size equals the entire training dataset.

---

## Q4. Why is Mini-Batch Gradient Descent commonly used?

**Answer**

Because it balances computational efficiency, memory usage, and optimization stability better than Batch Gradient Descent or Stochastic Gradient Descent.

---

## Q5. Does increasing Batch Size always improve model performance?

**Answer**

No.

Larger Batch Sizes can speed up training but may require more memory and sometimes reduce generalization performance.

---

# Summary

Batch Size determines how many training samples are processed before a single weight update is performed.

Small Batch Sizes provide frequent updates and often improve generalization but require more computation.

Large Batch Sizes reduce the number of updates and improve computational efficiency but demand more memory and may reduce generalization.

Mini-Batch Gradient Descent, which uses moderate Batch Sizes such as 32, 64, or 128, is the most widely used approach in modern Deep Learning.

---

# Key Takeaways

✔ Batch Size determines the number of samples processed before one weight update.

✔ Batch Gradient Descent uses the entire dataset.

✔ SGD uses one sample at a time.

✔ Mini-Batch Gradient Descent is the industry standard.

✔ Small batches require less memory but more updates.

✔ Large batches are computationally efficient but consume more memory.

✔ Choosing the right Batch Size balances speed, memory usage, and model performance.

---

# Next Part

## **Part 5 – Number of Epochs**

In the next chapter, we will study the **Number of Epochs**, understand its relationship with Batch Size and iterations, learn how epochs affect learning and overfitting, and discover how to choose an appropriate number of training epochs.
