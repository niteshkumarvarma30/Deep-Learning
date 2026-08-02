# Chapter 7: The Complete Perceptron Learning Algorithm

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand the complete Perceptron Learning Algorithm, including initialization, training, epochs, convergence, stopping criteria, and the overall workflow of learning.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the complete Perceptron Learning Algorithm.
- Explain each step involved in training.
- Understand epochs and iterations.
- Understand convergence.
- Explain stopping criteria.
- Solve complete training examples.

---

# 1. Recap

From the previous chapters, we know that the Perceptron learns by updating its weights whenever it makes an incorrect prediction.

The update rule is

\[
w_{new}=w_{old}+\eta(y-\hat y)x
\]

But an important question still remains.

> **How does the Perceptron train on an entire dataset instead of just one sample?**

The answer is the **Perceptron Learning Algorithm**.

---

# 2. What is the Perceptron Learning Algorithm?

The Perceptron Learning Algorithm is a sequence of steps that teaches the Perceptron how to classify data correctly.

Instead of processing only one sample,

it processes **every training example**.

After one complete pass,

it repeats the entire process again if necessary.

---

# 3. Overall Workflow

```
Initialize Weights

↓

Choose Training Sample

↓

Compute Weighted Sum

↓

Apply Activation Function

↓

Prediction

↓

Compare with Actual Label

↓

Prediction Correct?

     /        \

   Yes        No

   │           │

Next Sample  Update Weights

      ↓

Repeat Until All Samples Are Processed

↓

Repeat Next Epoch (if needed)

↓

Training Complete
```

---

# 4. Step 1 – Initialize Parameters

Initially,

the Perceptron has no knowledge.

Therefore,

initialize

```
Weights

↓

Random Values
```

Example

```
w₁ = 0

w₂ = 0

b = 0
```

Some implementations initialize them with small random numbers.

---

# 5. Step 2 – Select a Training Sample

Suppose the dataset contains

| x₁ | x₂ | Class |
|----|----|-------|
| 2 | 1 | 1 |
| 1 | 3 | 0 |
| 4 | 2 | 1 |

The algorithm starts with

```
Sample 1
```

After processing Sample 1,

it moves to Sample 2,

then Sample 3,

and so on.

---

# 6. Step 3 – Compute the Weighted Sum

For every sample,

calculate

\[
z=w^Tx+b
\]

Example

```
w₁ = 2

w₂ = -1

x₁ = 3

x₂ = 2

b = 1
```

\[
z=2(3)+(-1)(2)+1
\]

\[
=6-2+1
\]

\[
=5
\]

---

# 7. Step 4 – Apply the Activation Function

Apply

\[
f(z)=
\begin{cases}
1,&z\ge0\\
0,&z<0
\end{cases}
\]

Since

```
z = 5
```

Prediction

```
1
```

---

# 8. Step 5 – Compare Prediction

Suppose

```
Prediction = 1

Actual = 1
```

Correct.

No update.

Move to the next sample.

---

Suppose instead

```
Prediction = 0

Actual = 1
```

Incorrect.

Now update the weights.

---

# 9. Step 6 – Update the Weights

Apply

\[
w_{new}=w_{old}+\eta(y-\hat y)x
\]

Update

- Weight 1
- Weight 2
- Weight 3
- ...
- Bias

The updated parameters are then used for the next training sample.

---

# 10. Repeat for Every Sample

Suppose there are

```
5 Samples
```

The algorithm performs

```
Sample 1

↓

Sample 2

↓

Sample 3

↓

Sample 4

↓

Sample 5
```

This completes one full pass through the dataset.

---

# 11. What is an Epoch?

An **Epoch** is one complete pass through the entire training dataset.

Example

Dataset

```
100 Samples
```

Processing

```
Sample 1

↓

Sample 2

↓

...

↓

Sample 100
```

equals

```
1 Epoch
```

If the model still makes mistakes,

another epoch begins.

---

# 12. Iteration vs Epoch

Many beginners confuse these two terms.

| Iteration | Epoch |
|-----------|-------|
| One weight update using one sample | One complete pass through all samples |

Example

Dataset

```
100 Samples
```

Then

```
1 Iteration

↓

Process One Sample
```

```
1 Epoch

↓

Process All 100 Samples
```

---

# 13. Convergence

The Perceptron gradually improves its decision boundary.

Initially

```
Wrong Boundary
```

↓

After updates

```
Better Boundary
```

↓

After more updates

```
Correct Boundary
```

When no more updates are needed,

the algorithm has **converged**.

---

# 14. Stopping Criteria

Training stops when

### Condition 1

All training samples are classified correctly.

OR

### Condition 2

The maximum number of epochs has been reached.

Example

```
Maximum Epochs

=

100
```

Even if a few mistakes remain,

training stops after the limit.

---

# 15. Complete Numerical Example

Dataset

| x | Class |
|---|------|
| 2 | 1 |
| 4 | 1 |
| -1 | 0 |

Initialize

```
Weight = 0

Bias = 0

η = 1
```

### Sample 1

Weighted Sum

```
0×2+0=0
```

Prediction

```
1
```

Actual

```
1
```

Correct.

No update.

---

### Sample 2

Weighted Sum

```
0×4=0
```

Prediction

```
1
```

Correct.

---

### Sample 3

Weighted Sum

```
0×(-1)=0
```

Prediction

```
1
```

Actual

```
0
```

Wrong.

Update

\[
w=0+1(0-1)(-1)
\]

\[
=1
\]

Bias

\[
b=0+1(0-1)
=-1
\]

The Perceptron has learned from its mistake.

---

# 16. Algorithm (Pseudo-Code)

```
Initialize weights and bias

Repeat until stopping condition

    For every training sample

        Compute weighted sum

        Apply activation function

        Compare prediction with actual label

        If prediction is incorrect

            Update weights

            Update bias

Return final weights and bias
```

---

# 17. Flowchart

```
Start

↓

Initialize Parameters

↓

Choose Training Sample

↓

Compute Weighted Sum

↓

Activation Function

↓

Prediction

↓

Correct?

↓

Yes → Next Sample

↓

No

↓

Update Weights

↓

Next Sample

↓

All Samples Processed?

↓

No → Continue

↓

Yes

↓

Another Epoch?

↓

Yes → Repeat

↓

No

↓

Stop
```

---

# Common Mistakes

### Mistake 1

Thinking one sample equals one epoch.

❌ Incorrect.

One sample is one **iteration**.

---

### Mistake 2

Thinking training stops after one epoch.

❌ Incorrect.

Training continues until convergence or the stopping condition.

---

### Mistake 3

Updating weights even after correct predictions.

❌ Incorrect.

Weights change only after incorrect predictions.

---

# Chapter Summary

The Perceptron Learning Algorithm repeatedly processes every training sample.

For each sample,

it computes the weighted sum,

predicts the class,

compares it with the true label,

and updates the weights if necessary.

One complete pass through the dataset is called an **Epoch**.

The algorithm continues until the model converges or reaches the maximum number of epochs.

---

# Key Takeaways

✔ Initialize weights and bias.

✔ Process one training sample at a time.

✔ Compute weighted sum.

✔ Apply Step Function.

✔ Compare prediction with actual label.

✔ Update weights only after incorrect predictions.

✔ One complete pass is called an Epoch.

✔ Training stops after convergence or the maximum number of epochs.

---

# Interview Questions

### Q1. What is the Perceptron Learning Algorithm?

**Answer:**

It is the iterative training procedure that repeatedly updates the weights until the Perceptron correctly classifies the training data or reaches a stopping condition.

---

### Q2. What is an Epoch?

**Answer:**

One complete pass through the entire training dataset.

---

### Q3. What is an Iteration?

**Answer:**

One processing step involving a single training sample.

---

### Q4. When does the Perceptron stop training?

**Answer:**

When all samples are correctly classified or when the maximum number of epochs is reached.

---

# Practice Questions

## Conceptual

1. Explain the complete Perceptron Learning Algorithm.
2. Differentiate between an Iteration and an Epoch.
3. What is convergence?
4. Why are stopping criteria required?

---

## Numerical

### Question 1

A dataset contains **250 samples**.

How many iterations occur in **5 epochs**?

**Answer:**

\[
250 \times 5 = 1250 \text{ iterations}
\]

---

### Question 2

If a dataset has **1000 samples**, how many iterations occur in one epoch?

---

## MCQs

### 1. One complete pass through the dataset is called

A. Iteration

B. Epoch

C. Batch

D. Update

**Answer:** B

---

### 2. The Perceptron updates its weights

A. After every epoch

B. After every correct prediction

C. Only after incorrect predictions

D. Never

**Answer:** C

---

### 3. Training usually stops when

A. Dataset becomes empty

B. Weights become zero

C. Convergence or maximum epochs are reached

D. Inputs become zero

**Answer:** C

---

# What's Next?

In **Chapter 8**, we will study one of the most important concepts in Machine Learning:

**Linear Separability and XOR Problem**

Topics include:

- What is Linearly Separable Data?
- Linearly vs Non-Linearly Separable Data
- XOR Problem
- Why a Single Perceptron Fails
- Why Multi-Layer Perceptrons Were Invented
