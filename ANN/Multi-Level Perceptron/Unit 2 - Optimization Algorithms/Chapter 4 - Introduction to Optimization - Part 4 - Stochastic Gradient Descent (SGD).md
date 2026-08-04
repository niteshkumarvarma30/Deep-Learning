# Unit 2 – Optimization Algorithms

# Chapter 4 – Optimization Algorithms

## Part 4 – Stochastic Gradient Descent (SGD)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Stochastic Gradient Descent (SGD) is.
- Learn why SGD was introduced.
- Understand how SGD differs from Batch Gradient Descent.
- Learn the complete SGD algorithm.
- Understand its advantages and disadvantages.
- Learn where SGD is used in Deep Learning.

---

# 1. Why Was SGD Introduced?

In the previous chapter, we learned that **Batch Gradient Descent (BGD)** processes the **entire training dataset** before updating the weights.

Suppose

```text
Training Dataset

↓

10 Million Images
```

Batch Gradient Descent performs

```text
Image 1

↓

Image 2

↓

...

↓

Image 10,000,000

↓

Compute Average Gradient

↓

Update Weights Once
```

This has two major problems.

- It is slow because all samples must be processed before one update.
- Only one weight update occurs per epoch.

To solve these problems,

**Stochastic Gradient Descent (SGD)** was introduced.

---

# 2. What Does "Stochastic" Mean?

The word **Stochastic** means

> **Random** or **Randomly Selected**.

Instead of using the entire dataset,

SGD computes the gradient using **one randomly selected training sample**.

---

# 3. What is Stochastic Gradient Descent?

## Definition

Stochastic Gradient Descent (SGD) is an optimization algorithm that updates the model parameters **after processing each individual training sample**.

Instead of waiting for the complete dataset,

the model learns continuously.

```text
One Sample

↓

Forward Propagation

↓

Prediction

↓

Loss

↓

Gradient

↓

Update Weights

↓

Next Sample
```

---

# 4. Why is SGD Faster?

Suppose

```text
Training Dataset

↓

1000 Samples
```

### Batch Gradient Descent

```text
1000 Samples

↓

One Weight Update
```

---

### Stochastic Gradient Descent

```text
Sample 1

↓

Update

↓

Sample 2

↓

Update

↓

Sample 3

↓

Update

↓

...

↓

Sample 1000

↓

Update
```

Instead of waiting for all samples,

SGD updates the weights immediately.

---

# 5. Working of SGD

Suppose the dataset contains

```text
1000 Samples
```

The algorithm performs the following steps.

---

## Step 1

Initialize random weights.

---

## Step 2

Select one training sample.

---

## Step 3

Perform Forward Propagation.

---

## Step 4

Compute the prediction.

---

## Step 5

Calculate the loss for that sample.

---

## Step 6

Perform Backpropagation.

---

## Step 7

Compute the gradient.

---

## Step 8

Update the weights immediately.

---

## Step 9

Move to the next randomly selected sample.

---

## Step 10

Repeat until every sample has been processed.

This completes one epoch.

---

# 6. Complete Workflow

```text
One Training Sample

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss

↓

Backpropagation

↓

Gradient

↓

Update Weights

↓

Next Sample
```

Notice

Weights are updated **after every training sample**.

---

# 7. Mathematical Representation

For a single training sample,

the weight update equation is

$$
\boxed{ w_{new} = w_{old} - \eta \frac{\partial L_i}{\partial w} }
$$

Similarly,

the bias update equation is

$$
\boxed{ b_{new} = b_{old} - \eta \frac{\partial L_i}{\partial b} }
$$

where

- \(L_i\) = Loss of the current training sample
- \(\eta\) = Learning Rate

Unlike Batch Gradient Descent,

SGD **does not compute the average gradient** over the entire dataset.

---

# 8. Example

Suppose

```text
Training Dataset

↓

1000 Samples
```

Training proceeds as

```text
Sample 1

↓

Update

↓

Sample 2

↓

Update

↓

Sample 3

↓

Update

↓

...

↓

Sample 1000

↓

Update
```

Therefore,

during one epoch,

there are

```text
1000 Weight Updates
```

---

# 9. One Epoch in SGD

Suppose

```text
Dataset Size = 1000 Samples
```

Then

```text
Epoch 1

↓

1000 Updates

--------------------

Epoch 2

↓

1000 Updates

--------------------

Epoch 3

↓

1000 Updates
```

Therefore,

if training runs for

```text
100 Epochs
```

then

```text
100 × 1000

=

100,000 Weight Updates
```

---

# 10. Visualization

## Batch Gradient Descent

```text
1000 Samples

↓

Update Once
```

---

## Stochastic Gradient Descent

```text
Sample

↓

Update

↓

Sample

↓

Update

↓

Sample

↓

Update
```

Many small updates.

---

# 11. Advantages of SGD

## 1. Faster Learning

The model starts learning immediately.

---

## 2. Low Memory Usage

Only one training sample is needed at a time.

---

## 3. Suitable for Large Datasets

No need to process the complete dataset before updating.

---

## 4. Can Escape Local Minima

Because SGD updates are noisy,

it may escape shallow local minima and saddle points.

---

## 5. Online Learning

New data can be processed immediately without retraining on the entire dataset.

---

# 12. Disadvantages of SGD

## 1. Noisy Gradients

Every update is based on only one sample.

The gradient estimate is noisy.

---

## 2. Unstable Loss Curve

The loss fluctuates during training.

It may increase for some updates before decreasing again.

---

## 3. Slower Convergence

Although updates are frequent,

the optimization path is less smooth than Batch Gradient Descent.

---

# 13. Real-Life Analogy

Imagine a teacher checking answer sheets.

### Batch Gradient Descent

The teacher checks

```text
1000 Answer Sheets
```

then gives one overall suggestion.

---

### Stochastic Gradient Descent

The teacher checks

```text
One Answer Sheet

↓

Immediate Feedback

↓

Next Answer Sheet

↓

Immediate Feedback
```

Learning happens continuously.

---

# 14. Batch Gradient Descent vs SGD

| Feature | Batch Gradient Descent | Stochastic Gradient Descent |
|----------|------------------------|-----------------------------|
| Samples Used | Entire Dataset | One Sample |
| Weight Updates | One per Epoch | One per Sample |
| Speed | Slow | Fast |
| Memory Usage | High | Low |
| Gradient | Stable | Noisy |
| Loss Curve | Smooth | Fluctuating |
| Suitable For | Small Datasets | Large Datasets |

---

# 15. Why Isn't Pure SGD Used Everywhere?

Although SGD learns faster,

its updates are very noisy.

This causes

- unstable convergence,
- oscillating loss,
- slower convergence near the minimum.

Modern Deep Learning therefore prefers

**Mini-Batch Gradient Descent**,

which combines

- the stability of Batch Gradient Descent,
- with the speed of SGD.

---

# Interview Questions

## Q1. What is Stochastic Gradient Descent?

**Answer**

An optimization algorithm that updates the weights after processing each individual training sample.

---

## Q2. What does "Stochastic" mean?

**Answer**

Random or randomly selected.

---

## Q3. How many weight updates occur in one epoch if there are 1000 samples?

**Answer**

1000 updates.

---

## Q4. Why is SGD faster than Batch Gradient Descent?

**Answer**

Because it updates the weights immediately after processing each training sample instead of waiting for the entire dataset.

---

## Q5. What is the biggest disadvantage of SGD?

**Answer**

Its gradient estimates are noisy,

which causes the loss to fluctuate during training.

---

## Q6. Why can SGD escape local minima more easily?

**Answer**

Because its noisy updates may push the optimizer out of shallow local minima or saddle points.

---

# Summary

Stochastic Gradient Descent (SGD) is an optimization algorithm that updates the model parameters after processing **each individual training sample**.

Unlike Batch Gradient Descent, SGD does not wait for the entire dataset before updating the weights.

This makes learning much faster and more memory-efficient.

However,

because each update is based on only one sample,

the optimization path becomes noisy and the loss fluctuates during training.

These limitations led to the development of **Mini-Batch Gradient Descent**, which combines the strengths of Batch Gradient Descent and SGD.

---

# Key Takeaways

✔ SGD uses **one training sample** to compute each gradient.

✔ Weights are updated **after every sample**.

✔ If there are **N training samples**, SGD performs **N weight updates per epoch**.

✔ SGD is much faster than Batch Gradient Descent.

✔ SGD requires very little memory.

✔ SGD produces noisy gradients and an unstable loss curve.

✔ SGD is suitable for large datasets and online learning.

✔ Mini-Batch Gradient Descent is the modern improvement over pure SGD.
