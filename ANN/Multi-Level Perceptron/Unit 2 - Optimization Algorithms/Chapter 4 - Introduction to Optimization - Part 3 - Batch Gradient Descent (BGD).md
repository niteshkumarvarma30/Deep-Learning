# Unit 2 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 3 – Batch Gradient Descent (BGD)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Batch Gradient Descent (BGD) is.
- Learn why it uses the entire training dataset before updating the weights.
- Understand the complete Batch Gradient Descent algorithm.
- Learn the mathematical formulation.
- Understand its advantages and disadvantages.
- Know when Batch Gradient Descent is used.
- Understand why Stochastic Gradient Descent (SGD) and Mini-Batch Gradient Descent were developed.

---

# 1. Introduction

In the previous part, we learned the Gradient Descent update equation.

$$
\boxed{ w_{new} = w_{old} - \eta \frac{\partial L}{\partial w} }
$$

This equation tells us **how the weights are updated**.

However,

it does **not** tell us

> **How many training samples should be used to compute the gradient?**

There are three possibilities.

- Entire Dataset
- One Training Sample
- Small Batch of Samples

Batch Gradient Descent uses the **entire dataset**.

---

# 2. What is Batch Gradient Descent?

## Definition

Batch Gradient Descent (BGD) is an optimization algorithm that computes the gradient using **all training samples** before updating the model parameters.

In other words,

```text
Entire Dataset

↓

Forward Propagation

↓

Compute Total Loss

↓

Backpropagation

↓

Average Gradient

↓

Update Weights Once
```

Only **one weight update** occurs after processing the complete dataset.

---

# 3. Why is it Called "Batch"?

The word

**Batch**

means

> **The complete training dataset.**

Suppose we have

```text
Training Dataset

↓

1000 Images
```

Batch Gradient Descent processes

```text
Image 1

↓

Image 2

↓

Image 3

↓

...

↓

Image 1000

↓

Average Gradient

↓

Update Weights
```

Notice

The weights are updated **only once** after processing all 1000 images.

---

# 4. Working of Batch Gradient Descent

Suppose

Training Dataset

```text
1000 Samples
```

The algorithm performs the following steps.

---

## Step 1

Initialize random weights.

---

## Step 2

Pass all training samples through the neural network.

---

## Step 3

Compute predictions for every sample.

---

## Step 4

Compute the loss for every sample.

---

## Step 5

Calculate the average loss of the entire dataset.

---

## Step 6

Perform Backpropagation.

---

## Step 7

Compute the average gradient using all samples.

---

## Step 8

Update the weights once.

---

## Step 9

Repeat for the next epoch.

---

# 5. Complete Workflow

```text
Entire Training Dataset

↓

Forward Propagation

↓

Predictions

↓

Loss Function

↓

Average Loss

↓

Backpropagation

↓

Average Gradient

↓

Update Weights Once

↓

Next Epoch
```

---

# 6. Mathematical Representation

Suppose

The dataset contains

$$
N
$$

training samples.

The average gradient is

$$
\boxed{ \frac1N \sum_{i=1}^{N} \frac{\partial L_i}{\partial w} }
$$

The weight update equation becomes

$$
\boxed{ w_{new} = w_{old} - \eta \left( \frac1N \sum_{i=1}^{N} \frac{\partial L_i}{\partial w} \right) }
$$

where

- \(N\) = Number of Training Samples
- \(\eta\) = Learning Rate
- \(L_i\) = Loss of the \(i^{th}\) sample

The optimizer updates the weights using the **average gradient of the entire dataset**.

---

# 7. Example

Suppose

Training Dataset

```text
1000 Images
```

Batch Gradient Descent performs

```text
Image 1

↓

Image 2

↓

Image 3

↓

...

↓

Image 1000

↓

Average Gradient

↓

Update Weights
```

Even though 1000 images are processed,

only **one weight update** is performed.

---

# 8. One Epoch in Batch Gradient Descent

Suppose

Dataset Size

```text
1000 Samples
```

Then

```text
Epoch 1

↓

Process 1000 Samples

↓

Update Once

------------------------

Epoch 2

↓

Process 1000 Samples

↓

Update Once

------------------------

Epoch 3

↓

Process 1000 Samples

↓

Update Once
```

Therefore,

if

```text
100 Epochs
```

then

```text
100 Weight Updates
```

---

# 9. Visualization

Suppose

```text
Dataset

↓

1000 Samples
```

Training proceeds as

```text
Sample 1

↓

Sample 2

↓

...

↓

Sample 1000

↓

Average Gradient

↓

Update Weights
```

Notice

The weights remain unchanged while processing all samples.

Only after processing every sample does the optimizer perform a single update.

---

# 10. Advantages of Batch Gradient Descent

## 1. Stable Learning

Since the gradient is computed using the entire dataset,

the updates are smooth and stable.

---

## 2. Accurate Gradient

The gradient represents the complete dataset,

making it less noisy.

---

## 3. Predictable Convergence

The loss generally decreases in a smooth manner.

---

## 4. Easy to Understand

Batch Gradient Descent is mathematically simple and is commonly used to explain optimization concepts.

---

# 11. Disadvantages of Batch Gradient Descent

## 1. Very Slow

Suppose

```text
Dataset

↓

10 Million Images
```

The optimizer must process all images before updating the weights.

Training becomes very slow.

---

## 2. High Computational Cost

The entire dataset must be processed for every update.

---

## 3. High Memory Usage

Large datasets require significant computational resources.

---

## 4. Slow Learning

Only one update occurs after processing the complete dataset.

If the dataset is huge,

learning becomes slow.

---

# 12. Real-Life Analogy

Imagine a teacher checking

```text
1000 Answer Sheets
```

The teacher

- checks every answer sheet,
- calculates the average performance,
- then gives one overall suggestion.

Similarly,

Batch Gradient Descent

- processes every training sample,
- computes the average gradient,
- updates the weights once.

---

# 13. Batch Gradient Descent vs General Gradient Descent

The term

**Gradient Descent**

is often used in two different ways.

### Meaning 1

The general optimization principle

```text
Update weights using the negative gradient.
```

---

### Meaning 2

The specific algorithm

```text
Compute gradients using the entire dataset.

↓

Update weights once.
```

This specific algorithm is called

**Batch Gradient Descent (BGD).**

---

# 14. When is Batch Gradient Descent Used?

Suitable for

- Small datasets
- Educational examples
- Convex optimization problems
- Situations where stable gradients are preferred

Not suitable for

- Large datasets
- Deep Learning with millions of samples
- Online learning
- Real-time applications

---

# 15. Batch Gradient Descent vs Other Methods

| Method | Samples Used | Weight Updates per Epoch |
|----------|-------------:|-------------------------:|
| Batch Gradient Descent | Entire Dataset | 1 |
| Stochastic Gradient Descent (SGD) | 1 Sample | Number of Samples |
| Mini-Batch Gradient Descent | Small Batch | Number of Batches |

Example

Suppose

```text
Dataset Size = 1000

Batch Size = 100
```

| Algorithm | Updates per Epoch |
|------------|------------------:|
| Batch GD | 1 |
| SGD | 1000 |
| Mini-Batch GD | 10 |

---

# Interview Questions

## Q1. What is Batch Gradient Descent?

**Answer**

Batch Gradient Descent computes the gradient using the **entire training dataset** before updating the weights.

---

## Q2. Why is it called "Batch"?

**Answer**

Because one **batch** consists of the complete training dataset.

---

## Q3. How many weight updates occur in one epoch?

**Answer**

Exactly **one**.

---

## Q4. Why is Batch Gradient Descent slow?

**Answer**

Because it must process every training sample before updating the weights.

---

## Q5. What is the main advantage of Batch Gradient Descent?

**Answer**

It provides stable and accurate gradient estimates because they are computed from the entire dataset.

---

# Summary

Batch Gradient Descent (BGD) computes the gradient using **all training samples** before updating the model parameters.

During each epoch,

the optimizer

- processes the complete dataset,
- computes the average gradient,
- performs exactly one weight update.

Although this produces stable and accurate updates,

it becomes inefficient for very large datasets because of its high computational cost and slow learning speed.

---

# Key Takeaways

✔ Batch Gradient Descent uses the **entire training dataset**.

✔ One **batch** means the complete dataset.

✔ One **epoch** results in exactly **one weight update**.

✔ The optimizer computes the **average gradient** of all samples.

✔ Batch Gradient Descent provides smooth and stable convergence.

✔ It is computationally expensive for large datasets.

✔ Modern Deep Learning rarely uses pure Batch Gradient Descent because it is too slow.

✔ Batch Gradient Descent laid the foundation for **SGD** and **Mini-Batch Gradient Descent**, which are much more efficient for modern neural networks.
