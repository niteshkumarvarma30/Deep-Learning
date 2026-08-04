# Unit 2 – Loss Functions

# Chapter 2 – Regression Loss Functions

## Part 3 – Huber Loss

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Huber Loss was developed.
- Explain the intuition behind Huber Loss.
- Understand the Delta (\(\delta\)) parameter.
- Derive the Huber Loss formula.
- Solve numerical examples.
- Compare Huber Loss with MSE and MAE.
- Know when Huber Loss should be used.

---

# 1. Why Was Huber Loss Introduced?

Previously, we studied two regression loss functions.

## Mean Squared Error (MSE)

- Squares the prediction error.
- Strongly penalizes large errors.
- Highly sensitive to outliers.

---

## Mean Absolute Error (MAE)

- Uses the absolute value of the error.
- Less sensitive to outliers.
- More difficult to optimize because it is not differentiable at zero.

---

Researchers wanted a loss function that

- behaves like **MSE** for small errors,
- behaves like **MAE** for large errors.

The result was

**Huber Loss.**

---

# 2. What is Huber Loss?

## Definition

Huber Loss is a regression loss function that combines the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

It behaves differently depending on the size of the prediction error.

- Small Errors → Behaves like MSE
- Large Errors → Behaves like MAE

This makes Huber Loss

- Robust to outliers
- Easy to optimize

---

# 3. The Delta (\(\delta\)) Parameter

Huber Loss introduces a threshold called

$$
\delta
$$

(pronounced **delta**).

The value of \(\delta\) determines when the loss changes from quadratic behavior to linear behavior.

---

## Case 1

If

$$
|y-\hat{y}| \leq \delta
$$

Huber Loss behaves like **MSE**.

---

## Case 2

If

$$
|y-\hat{y}| > \delta
$$

Huber Loss behaves like **MAE**.

---

# Why is Delta Needed?

Suppose

```text
Prediction Error

↓

Very Small
```

The model should carefully reduce this error.

Therefore,

Huber Loss uses the quadratic penalty of MSE.

---

Now suppose

```text
Prediction Error

↓

Very Large
```

This could be caused by an outlier.

Instead of squaring this large error,

Huber Loss switches to a linear penalty like MAE.

This prevents outliers from dominating the total loss.

---

# 4. Mathematical Formula

The Huber Loss function is

$$
\boxed{
L_\delta(y,\hat{y})=
\begin{cases}
\frac{1}{2}(y-\hat{y})^2,
&
|y-\hat{y}| \leq \delta
\\[8pt]
\delta|y-\hat{y}|
-
\frac{1}{2}\delta^2,
&
|y-\hat{y}|>\delta
\end{cases}
}
$$

where

- \(y\) = Actual value
- \(\hat{y}\) = Predicted value
- \(\delta\) = Threshold parameter

---

# Understanding the Formula

The formula has two parts.

---

## Region 1 — Small Errors

When

$$
|y-\hat{y}| \leq \delta
$$

Huber Loss becomes

$$
\frac12(y-\hat{y})^2
$$

This is the same quadratic behavior as MSE.

---

## Region 2 — Large Errors

When

$$
|y-\hat{y}|>\delta
$$

Huber Loss becomes

$$
\delta|y-\hat{y}|
-
\frac12\delta^2
$$

This behaves like MAE.

Instead of increasing quadratically,

the loss increases linearly.

---

# 5. Numerical Example

Suppose

$$
\delta=1
$$

---

## Example 1 — Small Prediction Error

Actual Value

$$
10
$$

Predicted Value

$$
10.5
$$

Prediction Error

$$
|10-10.5|
=
0.5
$$

Since

$$
0.5<1
$$

we use the first equation.

$$
L
=
\frac12(0.5)^2
=
0.125
$$

Final Loss

$$
\boxed{0.125}
$$

---

## Example 2 — Large Prediction Error

Actual Value

$$
10
$$

Predicted Value

$$
13
$$

Prediction Error

$$
|10-13|
=
3
$$

Since

$$
3>1
$$

we use the second equation.

$$
L
=
1(3)
-
\frac12(1)^2
=
3-0.5
=
2.5
$$

Final Loss

$$
\boxed{2.5}
$$

---

# 6. Graphical Intuition

### Mean Squared Error (MSE)

```text
Loss

│
│         /
│      /
│   /
│ /
└──────────────── Error
```

The curve becomes steeper as the prediction error increases.

Large errors are heavily penalized.

---

### Mean Absolute Error (MAE)

```text
Loss

│
│      /
│    /
│  /
│/
└──────────────── Error
```

The loss increases linearly.

Every prediction error contributes equally.

---

### Huber Loss

```text
Loss

│
│        /
│      /
│   __/
│__/
└──────────────── Error
```

Near zero,

the curve behaves like MSE.

Far from zero,

the curve behaves like MAE.

---

# 7. Advantages of Huber Loss

- Combines the advantages of MSE and MAE.
- Less sensitive to outliers than MSE.
- Smooth near zero.
- Easier to optimize than MAE.
- Frequently used in practical regression problems.

---

# 8. Disadvantages of Huber Loss

- Requires choosing an appropriate value of \(\delta\).
- Performance depends on the chosen threshold.
- Slightly more complicated than MSE or MAE.

---

# 9. Comparison of MSE, MAE and Huber Loss

| Feature | MSE | MAE | Huber Loss |
|----------|-----|-----|------------|
| Small Errors | Quadratic | Linear | Quadratic |
| Large Errors | Quadratic | Linear | Linear |
| Outlier Sensitivity | High | Low | Moderate |
| Differentiable | Yes | No (at Zero) | Yes |
| Requires Hyperparameter | No | No | Yes (\(\delta\)) |

---

# 10. When Should You Use Huber Loss?

Huber Loss is recommended when

- The dataset contains some outliers.
- Smooth optimization is required.
- MSE is too sensitive to extreme values.
- A balance between robustness and optimization is desired.

---

# Common Applications

- Autonomous Driving
- Object Detection
- Financial Forecasting
- Robotics
- Time-Series Forecasting
- General Regression Problems

---

# 11. Deep Learning Pipeline Using Huber Loss

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Huber Loss

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

The objective is to minimize the Huber Loss during training.

---

# Interview Questions

## Q1. Why was Huber Loss introduced?

**Answer**

To combine the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

---

## Q2. What is the purpose of Delta (\(\delta\))?

It determines the threshold where Huber Loss changes from quadratic behavior to linear behavior.

---

## Q3. What happens when the prediction error is smaller than Delta?

Huber Loss behaves like MSE.

---

## Q4. What happens when the prediction error is larger than Delta?

Huber Loss behaves like MAE.

---

## Q5. Why is Huber Loss widely used?

Because it provides

- Smooth optimization,
- Reduced sensitivity to outliers,
- Better practical performance than using only MSE or MAE.

---

# Summary

Huber Loss is a hybrid regression loss function that combines the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

For small prediction errors,

it behaves like MSE and provides smooth optimization.

For large prediction errors,

it behaves like MAE and prevents outliers from dominating the loss.

The transition between these two behaviors is controlled by the Delta (\(\delta\)) parameter.

Because of this balance,

Huber Loss is widely used in real-world regression applications.

---

# Key Takeaways

✔ Huber Loss combines MSE and MAE.

✔ Small errors are penalized quadratically.

✔ Large errors are penalized linearly.

✔ Delta (\(\delta\)) determines the switching point.

✔ Huber Loss is less sensitive to outliers than MSE.

✔ Huber Loss is smoother and easier to optimize than MAE.

✔ Huber Loss is commonly used in practical regression applications.

✔ It provides a good balance between optimization efficiency and robustness.
