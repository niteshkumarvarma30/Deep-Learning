# Unit 2 – Loss Functions

# Chapter 2 – Regression Loss Functions

## Part 3 – Huber Loss

---

## Learning Objectives

After completing this part, you will be able to:

- Understand why Huber Loss was developed.
- Explain the intuition behind Huber Loss.
- Understand the Delta ($\delta$) parameter.
- Derive the Huber Loss formula.
- Solve numerical examples.
- Compare Huber Loss with MSE and MAE.
- Understand when Huber Loss should be used.

---

## 1. Why Was Huber Loss Introduced?

Previously, we studied two important regression loss functions.

### Mean Squared Error (MSE)

- Squares the prediction error.
- Strongly penalizes large errors.
- Highly sensitive to outliers.

### Mean Absolute Error (MAE)

- Uses the absolute value of the prediction error.
- Less sensitive to outliers.
- Not differentiable at zero, which can make optimization more challenging.

Researchers wanted a loss function that:

- Behaves like **MSE** for small errors.
- Behaves like **MAE** for large errors.

The result was **Huber Loss**.

---

## 2. What Is Huber Loss?

### Definition

Huber Loss is a regression loss function that combines the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

It behaves differently depending on the magnitude of the prediction error:

- **Small Errors:** Behaves like MSE.
- **Large Errors:** Behaves like MAE.

This makes Huber Loss:

- Less sensitive to outliers than MSE.
- Smooth and differentiable.
- Suitable for gradient-based optimization.

---

## 3. The Delta ($\delta$) Parameter

Huber Loss introduces a threshold called **Delta ($\delta$)**.

The value of $\delta$ determines when the loss changes from quadratic behavior to linear behavior.

### Case 1: Small Prediction Error

If:

$$
|y - \hat{y}| \leq \delta
$$

Huber Loss behaves like **MSE**.

### Case 2: Large Prediction Error

If:

$$
|y - \hat{y}| > \delta
$$

Huber Loss behaves like **MAE**.

### Why Is Delta Needed?

Suppose the prediction error is very small.

```text
Prediction Error
       |
       v
   Very Small
```

The model should carefully reduce this error.

Therefore, Huber Loss uses the quadratic penalty of MSE.

Now suppose the prediction error is very large.

```text
Prediction Error
       |
       v
   Very Large
```

This could be caused by an outlier.

Instead of squaring this large error, Huber Loss switches to a linear penalty like MAE.

This prevents extreme prediction errors from dominating the total loss.

---

## 4. Mathematical Formula

The Huber Loss function is defined as:

$$
\boxed{
L_\delta(y,\hat{y}) =
\begin{cases}
\frac{1}{2}(y-\hat{y})^2, & |y-\hat{y}| \leq \delta \\[8pt]
\delta|y-\hat{y}|-\frac{1}{2}\delta^2, & |y-\hat{y}| > \delta
\end{cases}
}
$$

Where:

- $y$ = Actual value.
- $\hat{y}$ = Predicted value.
- $\delta$ = Threshold parameter.
- $|y-\hat{y}|$ = Absolute prediction error.

### Understanding the Formula

The formula has two regions.

### Region 1 – Small Errors

When:

$$
|y-\hat{y}| \leq \delta
$$

Huber Loss becomes:

$$
L = \frac{1}{2}(y-\hat{y})^2
$$

This has the same quadratic behavior as MSE.

The loss increases quadratically as the prediction error increases.

### Region 2 – Large Errors

When:

$$
|y-\hat{y}| > \delta
$$

Huber Loss becomes:

$$
L = \delta|y-\hat{y}|-\frac{1}{2}\delta^2
$$

This has linear behavior similar to MAE.

Instead of increasing quadratically, the loss increases linearly.

Therefore, extremely large errors have less influence on the loss compared with MSE.

---

## 5. Numerical Examples

Suppose:

$$
\delta = 1
$$

We will calculate Huber Loss for two different prediction errors.

### Example 1 – Small Prediction Error

**Actual Value:**

$$
y = 10
$$

**Predicted Value:**

$$
\hat{y} = 10.5
$$

**Step 1: Calculate the Prediction Error**

$$
|y-\hat{y}| = |10-10.5|
$$

$$
= 0.5
$$

**Step 2: Compare the Error with Delta**

$$
0.5 < 1
$$

Since the prediction error is smaller than $\delta$, we use the first equation.

**Step 3: Apply the Huber Loss Formula**

$$
L = \frac{1}{2}(0.5)^2
$$

$$
L = \frac{1}{2}\times 0.25
$$

$$
L = 0.125
$$

**Final Loss:**

$$
\boxed{0.125}
$$

### Example 2 – Large Prediction Error

**Actual Value:**

$$
y = 10
$$

**Predicted Value:**

$$
\hat{y} = 13
$$

**Step 1: Calculate the Prediction Error**

$$
|y-\hat{y}| = |10-13|
$$

$$
= 3
$$

**Step 2: Compare the Error with Delta**

$$
3 > 1
$$

Since the prediction error is greater than $\delta$, we use the second equation.

**Step 3: Apply the Huber Loss Formula**

$$
L = \delta|y-\hat{y}|-\frac{1}{2}\delta^2
$$

Substituting the values:

$$
L = 1(3)-\frac{1}{2}(1)^2
$$

$$
L = 3-0.5
$$

$$
L = 2.5
$$

**Final Loss:**

$$
\boxed{2.5}
$$

### Numerical Example Summary

| Example | Actual Value | Predicted Value | Error | Applied Region | Huber Loss |
|---|---:|---:|---:|---|---:|
| 1 | 10 | 10.5 | 0.5 | Quadratic | 0.125 |
| 2 | 10 | 13 | 3 | Linear | 2.5 |

---

## 6. Graphical Intuition

### Mean Squared Error (MSE)

```text
Loss
  |
  |              /
  |           /
  |        /
  |     /
  |  /
  +-------------------- Error
```

The curve becomes steeper as the prediction error increases.

Large errors are heavily penalized because the error is squared.

### Mean Absolute Error (MAE)

```text
Loss
  |
  |          /
  |        /
  |      /
  |    /
  |  /
  +-------------------- Error
```

The loss increases linearly.

Every additional unit of absolute error contributes the same amount to the loss.

### Huber Loss

```text
Loss
  |
  |                /
  |             /
  |          __/
  |       __/
  |    __/
  +-------------------- Error
```

Near zero, the curve behaves like MSE.

Far from zero, the curve behaves like MAE.

**Important:** The transition between quadratic and linear behavior is controlled by $\delta$.

---

## 7. Advantages of Huber Loss

- Combines the advantages of MSE and MAE.
- Less sensitive to outliers than MSE.
- Smooth near zero.
- Differentiable everywhere, including at the transition point.
- Easier to optimize using gradient-based methods than MAE in many practical settings.
- Frequently used in practical regression problems.

---

## 8. Disadvantages of Huber Loss

- Requires choosing an appropriate value of $\delta$.
- Performance depends on the selected threshold.
- Slightly more complicated than MSE or MAE.
- A poorly selected threshold may reduce its effectiveness.

---

## 9. Comparison of MSE, MAE, and Huber Loss

| Feature | MSE | MAE | Huber Loss |
|---|---|---|---|
| Small Errors | Quadratic | Linear | Quadratic |
| Large Errors | Quadratic | Linear | Linear |
| Outlier Sensitivity | High | Low | Lower than MSE |
| Differentiability | Yes | No, at zero | Yes |
| Smooth Near Zero | Yes | No | Yes |
| Requires Hyperparameter | No | No | Yes ($\delta$) |
| Optimization | Gradient-based | Subgradient-based | Gradient-based |

---

## 10. When Should You Use Huber Loss?

Huber Loss is recommended when:

- The dataset contains some outliers.
- Smooth optimization is required.
- MSE is too sensitive to extreme values.
- A balance between robustness and optimization efficiency is desired.

### Common Applications

- Autonomous Driving.
- Object Detection.
- Financial Forecasting.
- Robotics.
- Time-Series Forecasting.
- General Regression Problems.

---

## 11. Deep Learning Pipeline Using Huber Loss

Huber Loss is used during neural network training to measure the difference between actual and predicted values.

The training pipeline looks like this:

```text
Input Data
    |
    v
Forward Propagation
    |
    v
Prediction
    |
    v
Calculate Huber Loss
    |
    v
Loss Value
    |
    v
Backpropagation
    |
    v
Calculate Gradients
    |
    v
Gradient Descent
    |
    v
Update Weights
    |
    v
Improved Predictions
```

The objective is to minimize the Huber Loss during training.

---

## 12. Interview Questions

### Q1. Why was Huber Loss introduced?

**Answer:**

Huber Loss was introduced to combine the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

It behaves like MSE for small prediction errors and like MAE for large prediction errors.

This provides smooth optimization while reducing sensitivity to outliers.

### Q2. What is the purpose of Delta ($\delta$)?

**Answer:**

Delta determines the threshold at which Huber Loss changes from quadratic behavior to linear behavior.

- If the absolute prediction error is less than or equal to $\delta$, the loss behaves like MSE.
- If the absolute prediction error is greater than $\delta$, the loss behaves like MAE.

### Q3. What happens when the prediction error is smaller than Delta?

**Answer:**

Huber Loss uses its quadratic region:

$$
L = \frac{1}{2}(y-\hat{y})^2
$$

This is similar to MSE.

### Q4. What happens when the prediction error is larger than Delta?

**Answer:**

Huber Loss uses its linear region:

$$
L = \delta|y-\hat{y}|-\frac{1}{2}\delta^2
$$

This is similar to MAE and reduces the influence of large errors.

### Q5. Why is Huber Loss widely used?

**Answer:**

Huber Loss is useful because it provides:

- Smooth optimization.
- Reduced sensitivity to outliers compared with MSE.
- A balance between quadratic and linear error penalties.
- Better robustness when datasets contain extreme observations.

---

## 13. Summary

Huber Loss is a hybrid regression loss function that combines the advantages of Mean Squared Error (MSE) and Mean Absolute Error (MAE).

For small prediction errors, it behaves like MSE and provides a quadratic penalty.

For large prediction errors, it behaves like MAE and applies a linear penalty.

The transition between these two behaviors is controlled by the Delta ($\delta$) parameter.

Because of this balance, Huber Loss is useful in real-world regression problems where datasets may contain outliers.

---

## 14. Key Takeaways

- Huber Loss combines MSE and MAE.
- Small errors are penalized quadratically.
- Large errors are penalized linearly.
- Delta ($\delta$) determines the switching threshold.
- Huber Loss is less sensitive to outliers than MSE.
- Huber Loss is differentiable everywhere.
- It is suitable for gradient-based optimization.
- It provides a balance between optimization efficiency and robustness.
- It is commonly used in practical regression applications.

---

## Next Part

**Part 4 – Next Regression Loss Function**

Continue exploring regression loss functions and understand how different loss functions influence model training and prediction accuracy.
