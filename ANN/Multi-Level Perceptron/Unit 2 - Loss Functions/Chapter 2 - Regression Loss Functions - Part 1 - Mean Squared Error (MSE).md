# Unit 2 – Loss Functions

# Chapter 2 – Regression Loss Functions

## Part 1 – Mean Squared Error (MSE)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Mean Squared Error (MSE) is.
- Explain why the error is squared.
- Derive the MSE formula.
- Solve numerical examples.
- Understand the advantages and disadvantages of MSE.
- Know when MSE should be used.

---

# 1. Why Do We Need MSE?

Suppose we are predicting house prices.

| House | Actual Price (₹ Lakhs) | Predicted Price (₹ Lakhs) |
|--------|------------------------:|--------------------------:|
| A | 50 | 48 |
| B | 70 | 75 |
| C | 90 | 85 |

The predictions are not perfect.

We need a single numerical value that tells us

> **How good or bad are these predictions overall?**

This value is called the **Mean Squared Error (MSE).**

---

# 2. What is Mean Squared Error?

## Definition

Mean Squared Error (MSE) is the average of the squared differences between the actual values and the predicted values.

It measures how far the model's predictions are from the true values.

---

# Mathematical Formula

$$
\boxed{
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
}
$$

where

- \(n\) = Number of training examples
- \(y_i\) = Actual value
- \(\hat{y}_i\) = Predicted value
- \((y_i-\hat{y}_i)\) = Prediction error

---

# Understanding the Formula

The formula consists of four steps.

### Step 1

Find the prediction error.

$$
y_i-\hat{y}_i
$$

---

### Step 2

Square the error.

$$
(y_i-\hat{y}_i)^2
$$

---

### Step 3

Add all squared errors.

$$
\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

---

### Step 4

Divide by the total number of samples.

$$
\frac{1}{n}
$$

This gives the average squared error.

---

# Why is it Called Mean Squared Error?

The name has three parts.

## Mean

Take the average.

---

## Squared

Square every error.

---

## Error

Difference between

```text
Actual Value

↓

Predicted Value
```

Therefore

```text
Mean

↓

Squared

↓

Error

↓

Mean Squared Error (MSE)
```

---

# 3. Why Do We Square the Error?

This is one of the most frequently asked interview questions.

There are two important reasons.

---

## Reason 1 — Remove Negative Signs

Suppose

| Actual | Predicted | Error |
|---------|----------:|------:|
| 50 | 55 | -5 |
| 50 | 45 | +5 |

If we directly average the errors,

$$
-5+5=0
$$

This incorrectly indicates that there is no error.

Now square the errors.

$$
(-5)^2=25
$$

$$
(+5)^2=25
$$

Average

$$
25
$$

Both prediction errors now contribute correctly.

---

## Reason 2 — Penalize Large Errors More

Suppose

| Error | Squared Error |
|------:|--------------:|
| 1 | 1 |
| 2 | 4 |
| 5 | 25 |
| 10 | 100 |

Notice that larger errors increase much more rapidly after squaring.

This makes MSE heavily penalize large prediction mistakes.

---

# 4. Numerical Example

Suppose

| Actual | Predicted |
|--------:|----------:|
| 10 | 9 |
| 20 | 18 |
| 30 | 32 |

---

## Step 1 — Calculate Error

| Actual | Predicted | Error |
|--------:|----------:|------:|
| 10 | 9 | 1 |
| 20 | 18 | 2 |
| 30 | 32 | -2 |

---

## Step 2 — Square Each Error

| Error | Squared Error |
|------:|--------------:|
| 1 | 1 |
| 2 | 4 |
| -2 | 4 |

---

## Step 3 — Add the Squared Errors

$$
1+4+4=9
$$

---

## Step 4 — Compute the Mean

There are

$$
3
$$

training examples.

Therefore

$$
MSE=\frac{9}{3}=3
$$

Final Answer

$$
\boxed{MSE=3}
$$

---

# 5. Graphical Intuition

Suppose prediction errors increase gradually.

```text
Error

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

The squared errors become

```text
Squared Error

↓

0

↓

1

↓

4

↓

9

↓

16
```

Notice that the penalty grows rapidly as the error increases.

This is why MSE strongly discourages large prediction errors.

---

# 6. Interpretation of MSE

### Case 1

```text
MSE = 0
```

Meaning

```text
Perfect Prediction
```

Every prediction exactly matches the actual value.

---

### Case 2

```text
MSE = 2
```

Meaning

Predictions are close to the correct values.

---

### Case 3

```text
MSE = 100
```

Meaning

Predictions are far from the actual values.

The model needs significant improvement.

---

# 7. Advantages of MSE

- Easy to understand and compute.
- Differentiable everywhere.
- Works efficiently with Gradient Descent.
- Strongly penalizes large prediction errors.
- Widely used in Machine Learning and Deep Learning.
- Provides smooth optimization.

---

# 8. Disadvantages of MSE

The biggest drawback is its sensitivity to **outliers**.

Suppose the prediction errors are

```text
2

3

2

50
```

Their squared values become

```text
4

9

4

2500
```

Notice that the error **50** dominates the total loss.

As a result,

the model may focus too much on outliers while ignoring normal observations.

---

# 9. When Should You Use MSE?

MSE is recommended when

- Large prediction errors should be penalized heavily.
- Outliers are rare.
- Smooth optimization is required.
- Training Deep Learning regression models.

---

# Common Applications

- House Price Prediction
- Stock Price Forecasting
- Temperature Prediction
- Energy Consumption Prediction
- Sales Forecasting
- Demand Prediction

---

# 10. MSE in Deep Learning

During model training,

the complete pipeline becomes

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Mean Squared Error

↓

Loss Value

↓

Backpropagation

↓

Gradient Descent

↓

Update Weights

↓

Better Prediction
```

The objective of Gradient Descent is to minimize the Mean Squared Error.

---

# Interview Questions

## Q1. Why is the error squared in MSE?

**Answer**

- To remove negative signs.
- To penalize larger errors more heavily.

---

## Q2. Can MSE ever be negative?

No.

Since every squared value is non-negative,

$$
MSE \ge 0
$$

---

## Q3. What is the best possible value of MSE?

$$
\boxed{0}
$$

This means every prediction exactly matches the actual value.

---

## Q4. What is the biggest disadvantage of MSE?

MSE is highly sensitive to outliers because squaring amplifies large prediction errors.

---

## Q5. Is MSE suitable for classification problems?

No.

MSE is designed for **regression problems** where the output is a continuous numerical value.

Classification problems generally use **Cross Entropy Loss** instead.

---

# Summary

Mean Squared Error (MSE) is one of the most widely used regression loss functions.

It calculates the average of the squared prediction errors.

Squaring the errors removes negative signs and strongly penalizes large prediction mistakes.

This makes MSE easy to optimize using Gradient Descent and highly effective for many regression tasks.

However, because large errors are squared, MSE is sensitive to outliers.

---

# Key Takeaways

✔ MSE measures the average squared prediction error.

✔ Formula

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

✔ Squaring removes negative signs.

✔ Squaring penalizes large errors more heavily.

✔ MSE is always greater than or equal to zero.

✔ Lower MSE indicates better model performance.

✔ MSE is differentiable and works well with Gradient Descent.

✔ MSE is commonly used for regression problems.

✔ The major disadvantage of MSE is its sensitivity to outliers.
