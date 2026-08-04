# Unit 2 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 5 – Mini-Batch Gradient Descent (MBGD)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Mini-Batch Gradient Descent (MBGD) is.
- Learn why MBGD was introduced.
- Understand the concept of Batch Size.
- Learn how MBGD combines the advantages of Batch Gradient Descent and Stochastic Gradient Descent.
- Understand the complete Mini-Batch Gradient Descent algorithm.
- Learn why almost every Deep Learning framework uses Mini-Batch Gradient Descent.

---

# 1. Why Was Mini-Batch Gradient Descent Introduced?

Previously, we studied two optimization methods.

## Batch Gradient Descent (BGD)

Uses

```text
Entire Dataset

↓

One Weight Update
```

Problems

- Slow
- High Memory Usage
- Only one update per epoch

---

## Stochastic Gradient Descent (SGD)

Uses

```text
One Sample

↓

One Weight Update
```

Problems

- Noisy updates
- Unstable loss curve
- Oscillations during training

---

Neither method is ideal.

We need an optimizer that is

- Faster than Batch Gradient Descent.
- More stable than Stochastic Gradient Descent.

The solution is

**Mini-Batch Gradient Descent (MBGD).**

---

# 2. What is Mini-Batch Gradient Descent?

## Definition

Mini-Batch Gradient Descent is an optimization algorithm that divides the training dataset into **small batches** and updates the model parameters after processing each batch.

Instead of using

- the entire dataset,
- or a single sample,

it uses

```text
Small Batch of Samples
```

---

# 3. What is Batch Size?

A **Batch Size** is the number of training samples processed before updating the weights.

---

## Example

Suppose

```text
Training Dataset

↓

1000 Samples
```

Choose

```text
Batch Size = 100
```

The dataset becomes

```text
Batch 1

100 Samples

↓

Update

Batch 2

100 Samples

↓

Update

...

Batch 10

100 Samples

↓

Update
```

Therefore,

there are

```text
10 Weight Updates
```

during one epoch.

---

# 4. Working of Mini-Batch Gradient Descent

Suppose

Dataset

```text
1000 Samples
```

Batch Size

```text
100
```

The algorithm performs the following steps.

---

## Step 1

Initialize random weights.

---

## Step 2

Divide the dataset into mini-batches.

```text
100

100

100

...

100
```

---

## Step 3

Select the first mini-batch.

---

## Step 4

Perform Forward Propagation.

---

## Step 5

Compute predictions.

---

## Step 6

Calculate the loss.

---

## Step 7

Perform Backpropagation.

---

## Step 8

Compute the average gradient for the current mini-batch.

---

## Step 9

Update the weights.

---

## Step 10

Move to the next mini-batch.

Repeat until every mini-batch has been processed.

This completes one epoch.

---

# 5. Complete Workflow

```text
Mini-Batch

↓

Forward Propagation

↓

Prediction

↓

Loss

↓

Backpropagation

↓

Average Gradient

↓

Update Weights

↓

Next Mini-Batch
```

---

# 6. Mathematical Representation

Suppose

Batch Size

$$
B
$$

The average gradient is

$$
\boxed{ \frac1B \sum_{i=1}^{B} \frac{\partial L_i}{\partial w} }
$$

The weight update equation becomes

$$
\boxed{ w_{new} = w_{old} - \eta \left( \frac1B \sum_{i=1}^{B} \frac{\partial L_i}{\partial w} \right) }
$$

Similarly,

the bias update equation is

$$
\boxed{ b_{new} = b_{old} - \eta \left( \frac1B \sum_{i=1}^{B} \frac{\partial L_i}{\partial b} \right) }
$$

Notice

The average gradient is computed only over the **current mini-batch**, not the entire dataset.

---

# 7. Example

Suppose

Dataset

```text
1000 Samples
```

Batch Size

```text
100
```

Training proceeds as

```text
Batch 1

100 Samples

↓

Update

↓

Batch 2

100 Samples

↓

Update

↓

...

↓

Batch 10

100 Samples

↓

Update
```

Therefore,

one epoch contains

```text
10 Weight Updates
```

---

# 8. Number of Updates Per Epoch

The number of updates is

$$
\boxed{ \text{Updates per Epoch} = \frac{\text{Dataset Size}} {\text{Batch Size}} }
$$

---

## Example 1

Dataset

```text
1000 Samples
```

Batch Size

```text
100
```

Updates

$$
\frac{1000}{100}=10
$$

---

## Example 2

Dataset

```text
60000 Samples
```

Batch Size

```text
128
```

Updates

$$
\frac{60000}{128} \approx469
$$

---

# 9. Common Batch Sizes

Frequently used batch sizes are

```text
16

32

64

128

256

512
```

Among these,

**32** and **64** are the most common starting choices in Deep Learning.

---

# 10. Advantages of Mini-Batch Gradient Descent

## 1. Faster than Batch Gradient Descent

Weights are updated more frequently.

---

## 2. More Stable than SGD

Gradients are averaged over multiple samples,

reducing noise.

---

## 3. Lower Memory Usage

Only one mini-batch is loaded into memory at a time.

---

## 4. Efficient GPU Utilization

GPUs perform parallel computations efficiently on batches.

---

## 5. Faster Convergence

Mini-Batch Gradient Descent usually converges faster than both Batch Gradient Descent and pure SGD.

---

# 11. Disadvantages

- Batch size must be selected carefully.
- Very small batches behave like noisy SGD.
- Very large batches behave like slow Batch Gradient Descent.
- Poor batch-size selection may reduce training efficiency.

---

# 12. Visualization

## Batch Gradient Descent

```text
1000 Samples

↓

1 Update
```

---

## Stochastic Gradient Descent

```text
1 Sample

↓

1 Update
```

---

## Mini-Batch Gradient Descent

```text
100 Samples

↓

1 Update

↓

100 Samples

↓

1 Update

↓

...

↓

100 Samples

↓

1 Update
```

---

# 13. Real-Life Analogy

Imagine a teacher grading assignments.

---

## Batch Gradient Descent

```text
1000 Assignments

↓

One Suggestion
```

---

## Stochastic Gradient Descent

```text
One Assignment

↓

One Suggestion
```

---

## Mini-Batch Gradient Descent

```text
100 Assignments

↓

One Suggestion

↓

Next 100 Assignments

↓

One Suggestion
```

This balances speed and stability.

---

# 14. Batch GD vs SGD vs Mini-Batch GD

| Feature | Batch GD | SGD | Mini-Batch GD |
|----------|----------|-----|---------------|
| Samples Used | Entire Dataset | One Sample | Small Batch |
| Weight Updates | 1 per Epoch | N per Epoch | N / Batch Size per Epoch |
| Speed | Slow | Fast | Fast |
| Memory Usage | High | Low | Medium |
| Gradient | Stable | Noisy | Moderately Stable |
| Loss Curve | Smooth | Fluctuating | Relatively Smooth |
| GPU Friendly | Poor | Poor | Excellent |
| Used in Modern Deep Learning | Rarely | Occasionally | Almost Always |

---

# 15. Why is Mini-Batch Gradient Descent the Standard?

Mini-Batch Gradient Descent provides the best balance.

It combines

- the stability of Batch Gradient Descent,
- the speed of Stochastic Gradient Descent,
- efficient GPU computation,
- lower memory usage.

This is why frameworks like **TensorFlow** and **PyTorch** use Mini-Batch Gradient Descent as the standard training approach.

---

# 16. Complete Comparison Example

Suppose

```text
Dataset Size = 1000 Samples
```

Batch Size

```text
100
```

| Algorithm | Samples Used for One Update | Updates per Epoch |
|-----------|-----------------------------:|------------------:|
| Batch Gradient Descent | 1000 | 1 |
| Stochastic Gradient Descent | 1 | 1000 |
| Mini-Batch Gradient Descent | 100 | 10 |

This table clearly shows why Mini-Batch Gradient Descent provides a balance between speed and stability.

---

# Interview Questions

## Q1. What is Mini-Batch Gradient Descent?

**Answer**

Mini-Batch Gradient Descent updates the weights after processing a small batch of training samples.

---

## Q2. What is Batch Size?

**Answer**

Batch Size is the number of training samples processed before one weight update.

---

## Q3. How many updates occur in one epoch?

**Answer**

$$
\boxed{ \text{Updates per Epoch} = \frac{\text{Dataset Size}} {\text{Batch Size}} }
$$

---

## Q4. Why is Mini-Batch Gradient Descent preferred over SGD?

**Answer**

Because it reduces noisy updates while maintaining fast learning.

---

## Q5. Why is Mini-Batch Gradient Descent preferred over Batch Gradient Descent?

**Answer**

Because it performs more frequent updates, requires less memory, and trains much faster on large datasets.

---

## Q6. Why do GPUs work well with Mini-Batch Gradient Descent?

**Answer**

Because GPUs are designed for parallel computation and can efficiently process multiple samples simultaneously.

---

# Summary

Mini-Batch Gradient Descent divides the training dataset into small batches and updates the model parameters after processing each batch.

It combines

- the stability of Batch Gradient Descent,
- the speed of Stochastic Gradient Descent,
- efficient GPU utilization,
- and lower memory usage.

Because of these advantages, Mini-Batch Gradient Descent has become the **standard optimization method** in modern Deep Learning.

---

# Key Takeaways

✔ Mini-Batch Gradient Descent uses a **small batch of samples**.

✔ Batch Size determines how many samples are processed before each update.

✔ Updates per Epoch are calculated as

$$
\frac{\text{Dataset Size}} {\text{Batch Size}}
$$

✔ Mini-Batch Gradient Descent is faster than Batch Gradient Descent.

✔ Mini-Batch Gradient Descent is more stable than SGD.

✔ It efficiently utilizes GPUs.

✔ Most modern Deep Learning frameworks use Mini-Batch Gradient Descent by default.

✔ Mini-Batch Gradient Descent provides the best balance between speed, memory usage, and convergence.
