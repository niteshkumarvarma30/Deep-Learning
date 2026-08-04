# Unit 2 – Loss Functions

# Chapter 2 – Regression Loss Functions

## Part 2 – Mean Absolute Error (MAE)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Mean Absolute Error (MAE) is.
- Explain why MAE uses the absolute value instead of squaring the error.
- Derive the MAE formula.
- Solve numerical examples.
- Compare MAE with MSE.
- Understand the advantages and disadvantages of MAE.
- Know when MAE should be used.

---

# 1. Why Was MAE Introduced?

In the previous section, we studied **Mean Squared Error (MSE).**

MSE squares the prediction errors.

Suppose the prediction errors are

| Error |
|------:|
| 2 |
| 3 |
| 50 |

Using MSE

| Error | Squared Error |
|------:|--------------:|
| 2 | 4 |
| 3 | 9 |
| 50 | 2500 |

Notice that the error **50** contributes **2500** to the loss.

A single large error can dominate the entire loss value.

Therefore,

MSE is **highly sensitive to outliers**.

To overcome this limitation,

**Mean Absolute Error (MAE)** was introduced.

---

# 2. What is Mean Absolute Error (MAE)?

## Definition

Mean Absolute Error (MAE) is the average of the absolute differences between the actual values and the predicted values.

Instead of squaring the prediction error,

MAE simply takes its **absolute value**.

---

# Mathematical Formula

$$
\boxed{
MAE
=
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat{y}_i|
}
$$

where

- \(n\) = Number of training examples
- \(y_i\) = Actual value
- \(\hat{y}_i\) = Predicted value
- \(|y_i-\hat{y}_i|\) = Absolute prediction error

---

# Understanding the Formula

The formula consists of four simple steps.

### Step 1

Find the prediction error.

$$
y_i-\hat{y}_i
$$

---

### Step 2

Take the absolute value.

$$
|y_i-\hat{y}_i|
$$

---

### Step 3

Add all absolute errors.

$$
\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

---

### Step 4

Divide by the total number of samples.

$$
\frac{1}{n}
$$

This gives the **average absolute prediction error.**

---

# Why is it Called Mean Absolute Error?

The name has three parts.

## Mean

Take the average.

---

## Absolute

Ignore the positive or negative sign.

---

## Error

Difference between

```text
Actual Value

↓

Predicted Value
```

Therefore,

```text
Mean

↓

Absolute

↓

Error

↓

Mean Absolute Error (MAE)
```

---

# 3. Why Do We Use the Absolute Value?

Suppose

| Actual | Predicted | Error |
|--------:|----------:|------:|
| 50 | 55 | -5 |
| 50 | 45 | 5 |

If we average these errors,

$$
-5+5=0
$$

This incorrectly suggests that there is no prediction error.

Now take the absolute value.

$$
|-5|=5
$$

$$
|5|=5
$$

Average

$$
5
$$

Now both prediction errors contribute equally.

---

# 4. Numerical Example

Suppose

| Actual | Predicted |
|--------:|----------:|
| 10 | 9 |
| 20 | 18 |
| 30 | 32 |

---

## Step 1 — Compute Prediction Error

| Actual | Predicted | Error |
|--------:|----------:|------:|
| 10 | 9 | 1 |
| 20 | 18 | 2 |
| 30 | 32 | -2 |

---

## Step 2 — Compute Absolute Error

| Error | Absolute Error |
|------:|---------------:|
| 1 | 1 |
| 2 | 2 |
| -2 | 2 |

---

## Step 3 — Add Absolute Errors

$$
1+2+2=5
$$

---

## Step 4 — Divide by Number of Samples

There are

$$
3
$$

samples.

Therefore

$$
MAE
=
\frac{5}{3}
=
1.67
$$

Final Answer

$$
\boxed{MAE=1.67}
$$

---

# 5. Graphical Intuition

Suppose the prediction error increases.

```text
Prediction Error

↓

0

↓

1

↓

2

↓

3

↓

4
```

The absolute error becomes

```text
Absolute Error

↓

0

↓

1

↓

2

↓

3

↓

4
```

Notice that

the penalty increases **linearly**.

Unlike MSE,

large errors are **not amplified**.

---

# 6. Interpretation of MAE

### Case 1

```text
MAE = 0
```

Meaning

```text
Perfect Prediction
```

Every prediction exactly matches the actual value.

---

### Case 2

```text
MAE = 2
```

Meaning

On average,

the predictions are **2 units away** from the correct values.

---

### Case 3

```text
MAE = 15
```

Meaning

Predictions are far from the actual values.

The model requires improvement.

---

# 7. Advantages of MAE

- Easy to understand.
- Less sensitive to outliers.
- Maintains the original unit of the target variable.
- Every prediction error contributes proportionally.
- More robust for noisy datasets.

---

# 8. Disadvantages of MAE

The main limitation is that

MAE is **not differentiable at zero**.

This makes mathematical optimization more difficult than MSE.

Although modern optimization algorithms can handle this issue,

MSE is often preferred because it provides smoother gradients.

---

# 9. MSE vs MAE

Consider the following prediction errors.

| Error | MSE Contribution | MAE Contribution |
|------:|-----------------:|-----------------:|
| 1 | 1 | 1 |
| 2 | 4 | 2 |
| 5 | 25 | 5 |
| 10 | 100 | 10 |

Notice

- MSE increases **quadratically**.
- MAE increases **linearly**.

Therefore,

MSE penalizes large prediction errors much more heavily.

MAE treats every prediction error more uniformly.

---

# 10. When Should You Use MAE?

MAE is recommended when

- The dataset contains many outliers.
- Every prediction error should have equal importance.
- Robustness is more important than strongly penalizing large errors.
- The prediction error should remain easy to interpret.

---

# Common Applications

- Demand Forecasting
- Sales Prediction
- Weather Forecasting
- Traffic Prediction
- Time-Series Forecasting
- Financial Forecasting

---

# 11. MSE vs MAE Comparison

| Feature | MSE | MAE |
|---------|-----|-----|
| Formula | Squares Error | Absolute Error |
| Outlier Sensitivity | High | Low |
| Growth | Quadratic | Linear |
| Differentiable Everywhere | Yes | No (at Zero) |
| Penalizes Large Errors | Strongly | Moderately |
| Interpretation | Squared Units | Original Units |

---

# 12. Deep Learning Pipeline Using MAE

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Mean Absolute Error

↓

Loss Value

↓

Backpropagation

↓

Gradient Descent

↓

Updated Weights

↓

Better Prediction
```

The objective remains the same.

The model attempts to minimize the MAE during training.

---

# Interview Questions

## Q1. Why is MAE less sensitive to outliers than MSE?

**Answer**

Because MAE uses the **absolute value** of the error instead of squaring it.

Large errors increase linearly rather than quadratically.

---

## Q2. Can MAE ever be negative?

No.

Since absolute values are always non-negative,

$$
MAE \ge 0
$$

---

## Q3. What is the best possible MAE?

$$
\boxed{0}
$$

An MAE of zero means every prediction exactly matches the actual value.

---

## Q4. What is the biggest disadvantage of MAE?

MAE is **not differentiable at zero**, making optimization mathematically less smooth than MSE.

---

## Q5. Is MAE suitable for classification problems?

No.

MAE is designed for **regression problems** where the output is a continuous numerical value.

Classification problems generally use **Cross Entropy Loss**.

---

# Summary

Mean Absolute Error (MAE) measures the average absolute difference between the actual and predicted values.

Unlike Mean Squared Error (MSE), it does not square the error.

As a result,

MAE is much less sensitive to outliers and provides an error measurement in the original units of the target variable.

However,

because MAE is not differentiable at zero, optimization is mathematically less convenient than MSE.

---

# Key Takeaways

✔ MAE measures the average absolute prediction error.

✔ Formula

$$
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

✔ Absolute value removes negative signs.

✔ MAE increases linearly with prediction error.

✔ MAE is less sensitive to outliers than MSE.

✔ MAE is always greater than or equal to zero.

✔ Lower MAE indicates better model performance.

✔ MAE preserves the original unit of the target variable.

✔ MAE is widely used for regression problems involving noisy or outlier-prone datasets.
