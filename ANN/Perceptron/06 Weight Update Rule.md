# Chapter 6: Weight Update Rule

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand how the Perceptron updates its weights and bias after making an incorrect prediction, derive the Perceptron Learning Rule, and understand the mathematical intuition behind learning.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why weights need to be updated.
- Derive the Perceptron Weight Update Rule.
- Understand the role of the error term.
- Understand the Learning Rate.
- Update weights using numerical examples.
- Understand the geometric meaning of weight updates.

---

# 1. Recap

In the previous chapter we learned

```
Prediction

↓

Compare with Actual Label

↓

Wrong?

↓

Update Weights
```

Now the important question is

> **How exactly are the weights updated?**

The answer is the **Perceptron Learning Rule**.

---

# 2. Why Update the Weights?

Suppose the Perceptron predicts

```
Dog
```

But the actual answer is

```
Cat
```

The Perceptron has made a mistake.

If the weights remain unchanged,

it will make the same mistake again.

Therefore,

the weights must be adjusted.

Learning simply means

> **Changing the weights so that future predictions become more accurate.**

---

# 3. The Perceptron Learning Rule

The Perceptron updates each weight using

\[
w_{new}=w_{old}+\eta(y-\hat{y})x
\]

The bias is updated using

\[
b_{new}=b_{old}+\eta(y-\hat{y})
\]

These equations form the core of the Perceptron Learning Algorithm. They represent the update process described in your PDF. :contentReference[oaicite:1]{index=1}

---

# 4. Understanding Every Symbol

| Symbol | Meaning |
|---------|---------|
| \(w\) | Weight |
| \(x\) | Input Feature |
| \(y\) | Actual Label |
| \(\hat{y}\) | Predicted Label |
| \(\eta\) | Learning Rate |
| \(b\) | Bias |

---

# 5. The Error Term

The most important part of the equation is

\[
(y-\hat{y})
\]

This tells the Perceptron

> **Was the prediction correct?**

---

## Case 1

Actual

```
1
```

Predicted

```
1
```

Error

\[
1-1=0
\]

Weight Update

```
No
```

---

## Case 2

Actual

```
0
```

Predicted

```
0
```

Error

\[
0-0=0
\]

Again,

No update.

---

## Case 3

Actual

```
1
```

Predicted

```
0
```

Error

\[
1-0=1
\]

Positive error.

The weights increase.

---

## Case 4

Actual

```
0
```

Predicted

```
1
```

Error

\[
0-1=-1
\]

Negative error.

The weights decrease.

---

# 6. Why Multiply by the Input?

Notice

\[
\eta(y-\hat{y})x
\]

contains

```
x
```

Suppose

Feature A

```
100
```

Feature B

```
0
```

Feature B contributed nothing to the prediction.

Therefore,

its weight should not change.

Multiplying by the input automatically ensures that only influential features receive larger updates.

---

# 7. Learning Rate

The symbol

\[
\eta
\]

is called the **Learning Rate**.

It controls

> **How much should the weights change after each mistake?**

Small learning rate

```
Tiny Updates
```

Large learning rate

```
Large Updates
```

A good learning rate balances speed and stability.

---

# 8. Numerical Example 1

Suppose

```
Current Weight = 2

Input = 3

Learning Rate = 0.1

Actual = 1

Predicted = 0
```

### Step 1

Error

\[
1-0=1
\]

### Step 2

Apply the update rule

\[
w_{new}=2+0.1(1)(3)
\]

\[
=2+0.3
\]

\[
=2.3
\]

The weight has increased.

---

# 9. Numerical Example 2

Suppose

```
Current Weight = 5

Input = 4

Learning Rate = 0.2

Actual = 0

Predicted = 1
```

Error

\[
0-1=-1
\]

Update

\[
5+0.2(-1)(4)
\]

\[
5-0.8
\]

\[
=4.2
\]

The weight decreases.

---

# 10. Updating Multiple Weights

Suppose we have

```
x₁

x₂

x₃
```

Each weight is updated independently.

\[
w_1=w_1+\eta(y-\hat{y})x_1
\]

\[
w_2=w_2+\eta(y-\hat{y})x_2
\]

\[
w_3=w_3+\eta(y-\hat{y})x_3
\]

The same error term is used,

but each weight changes according to its own feature value.

---

# 11. Updating the Bias

Bias update

\[
b_{new}=b_{old}+\eta(y-\hat{y})
\]

Notice

Bias does **not** multiply any feature.

Why?

Because bias is independent of the inputs.

It simply shifts the decision boundary.

---

# 12. Geometric Interpretation

Suppose the current Decision Boundary is

```
------------

```

One training sample lies on the wrong side.

Updating the weights rotates the boundary.

```
/////////////
```

Updating the bias shifts the boundary.

```
=============
```

Together,

weights and bias gradually move the Decision Boundary toward its optimal position.

---

# 13. Complete Learning Cycle

```
Training Sample

↓

Compute Weighted Sum

↓

Apply Step Function

↓

Prediction

↓

Compare with Actual Label

↓

Compute Error

↓

Update Weights

↓

Update Bias

↓

Next Sample
```

This cycle repeats for every sample in every epoch.

---

# 14. Why Does This Rule Work?

Suppose the Perceptron predicts

```
0
```

instead of

```
1
```

The positive error increases the weights,

making the weighted sum larger the next time the same sample is seen.

Similarly,

if the Perceptron predicts

```
1
```

instead of

```
0
```

the negative error decreases the weights,

reducing the weighted sum.

Thus,

the Perceptron gradually corrects its own mistakes.

---

# Common Misconceptions

### Mistake 1

Thinking that weights change after every prediction.

❌ Incorrect

Weights change only after incorrect predictions.

---

### Mistake 2

Thinking all weights change equally.

❌ Incorrect

Each weight changes according to its corresponding feature value.

---

### Mistake 3

Ignoring the bias update.

❌ Incorrect

Bias is updated separately and plays an important role in shifting the Decision Boundary.

---

# Chapter Summary

The Perceptron learns by updating its weights and bias whenever it makes an incorrect prediction.

The Weight Update Rule is

\[
w_{new}=w_{old}+\eta(y-\hat{y})x
\]

and the Bias Update Rule is

\[
b_{new}=b_{old}+\eta(y-\hat{y})
\]

These updates gradually improve the Decision Boundary, enabling the Perceptron to correctly classify the training data.

---

# Key Takeaways

✔ Learning occurs by updating weights.

✔ Weight Update Rule

\[
w_{new}=w_{old}+\eta(y-\hat{y})x
\]

✔ Bias Update Rule

\[
b_{new}=b_{old}+\eta(y-\hat{y})
\]

✔ Error determines the direction of the update.

✔ Learning Rate determines the size of the update.

✔ The Decision Boundary improves after each update.

---

# Interview Questions

### Q1. What is the Perceptron Weight Update Rule?

**Answer:**

\[
w_{new}=w_{old}+\eta(y-\hat{y})x
\]

---

### Q2. When does the Perceptron update its weights?

**Answer:**

Only when it makes an incorrect prediction.

---

### Q3. What is the role of the error term?

**Answer:**

It determines whether the weights should increase, decrease, or remain unchanged.

---

### Q4. Why is the learning rate important?

**Answer:**

It controls how much the weights change after each mistake.

---

# Practice Questions

## Conceptual

1. Explain the Perceptron Learning Rule.
2. Why is the error term necessary?
3. Why is the learning rate multiplied with the update?
4. Explain the role of the bias update.

---

## Numerical

### Question 1

Given

```
Weight = 4

Input = 5

η = 0.2

Actual = 1

Predicted = 0
```

Find the updated weight.

---

### Question 2

Given

```
Weight = 3

Input = 2

η = 0.1

Actual = 0

Predicted = 1
```

Find the updated weight.

---

## MCQs

### 1. The Perceptron updates its weights using

A. Gradient Descent

B. Newton's Method

C. Perceptron Learning Rule

D. Random Search

**Answer:** C

---

### 2. If the prediction is correct, the weight update is

A. Positive

B. Negative

C. Zero

D. Random

**Answer:** C

---

### 3. The learning rate controls

A. Number of inputs

B. Number of classes

C. Size of the weight update

D. Dataset size

**Answer:** C

---

# What's Next?

In **Chapter 7**, we will study the **Complete Perceptron Learning Algorithm**.

Topics include:

- Step-by-step training algorithm
- Epochs
- Iterations
- Stopping criteria
- Convergence
- Complete worked examples
