# Unit 2 – Loss Functions

# Chapter 2 – Regression Loss Functions

## Part 4 – Comparison of MSE, MAE, and Huber Loss

---

# Learning Objectives

After completing this part, you will be able to:

- Compare MSE, MAE, and Huber Loss.
- Understand their mathematical differences.
- Compare their behavior for small and large prediction errors.
- Understand sensitivity to outliers.
- Choose the appropriate loss function for different regression problems.
- Answer interview questions related to regression loss functions.

---

# 1. Why Do We Need Different Loss Functions?

There is no single loss function that works best for every regression problem.

Different datasets have different characteristics.

Some datasets

- contain many outliers,
- contain very little noise,
- require large prediction errors to be heavily penalized,
- require robustness against extreme values.

Therefore, different regression loss functions have been developed.

---

# 2. Mathematical Formulas

## Mean Squared Error (MSE)

$$
\boxed{
MSE
=
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
}
$$

MSE squares every prediction error before averaging.

---

## Mean Absolute Error (MAE)

$$
\boxed{
MAE
=
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat{y}_i|
}
$$

MAE takes the absolute value of every prediction error before averaging.

---

## Huber Loss

$$
\boxed{ L_\delta(y,\hat{y}) = \begin{cases} \frac12(y-\hat{y})^2, & |y-\hat{y}|\le\delta \\[8pt] \delta|y-\hat{y}| - \frac12\delta^2, & |y-\hat{y}|>\delta \end{cases} }
$$

Huber Loss combines the behavior of MSE and MAE.

---

# 3. Error Growth Comparison

Suppose the prediction errors are

| Prediction Error | MSE | MAE | Huber Loss (δ = 1) |
|-----------------:|----:|----:|-------------------:|
| 1 | 1 | 1 | 0.5 |
| 2 | 4 | 2 | 1.5 |
| 5 | 25 | 5 | 4.5 |
| 10 | 100 | 10 | 9.5 |

---

## Observation

### Mean Squared Error

Error increases

```text
1

↓

4

↓

25

↓

100
```

The penalty grows **quadratically**.

Large prediction errors receive extremely high penalties.

---

### Mean Absolute Error

Error increases

```text
1

↓

2

↓

5

↓

10
```

The penalty grows **linearly**.

Every prediction error contributes proportionally.

---

### Huber Loss

Small errors behave like

```text
MSE
```

Large errors behave like

```text
MAE
```

This provides a balance between the two approaches.

---

# 4. Graphical Intuition

## Mean Squared Error (MSE)

```text
Loss

│
│          /
│       /
│    /
│ /
└────────────────── Error
```

The curve becomes steeper as the prediction error increases.

Large errors dominate the loss.

---

## Mean Absolute Error (MAE)

```text
Loss

│
│      /
│    /
│  /
│/
└────────────────── Error
```

The increase is linear.

All prediction errors contribute equally.

---

## Huber Loss

```text
Loss

│
│        /
│      /
│   __/
│__/
└────────────────── Error
```

Near zero,

the curve behaves like MSE.

For large errors,

it becomes linear like MAE.

---

# 5. Sensitivity to Outliers

Suppose the prediction errors are

```text
2

3

4

50
```

---

## Mean Squared Error

Squares the prediction errors.

```text
4

9

16

2500
```

Notice that

the error **50** becomes **2500**.

The outlier dominates the total loss.

---

## Mean Absolute Error

Absolute prediction errors become

```text
2

3

4

50
```

The outlier still contributes more,

but it does not dominate the loss.

---

## Huber Loss

Small prediction errors receive quadratic penalties.

The large prediction error receives only a linear penalty.

Therefore,

the influence of outliers is reduced.

---

# 6. Optimization Behavior

## Mean Squared Error

- Smooth gradient.
- Differentiable everywhere.
- Easy to optimize using Gradient Descent.

---

## Mean Absolute Error

- Not differentiable at zero.
- Optimization is mathematically less smooth.

---

## Huber Loss

- Smooth near zero.
- Linear for large prediction errors.
- Easier to optimize than MAE.

---

# 7. Advantages and Disadvantages

| Loss Function | Advantages | Disadvantages |
|---------------|------------|---------------|
| **MSE** | Smooth optimization, strongly penalizes large errors | Highly sensitive to outliers |
| **MAE** | Robust to outliers, easy to interpret | Not differentiable at zero |
| **Huber Loss** | Combines the strengths of MSE and MAE | Requires selecting the Delta (\(\delta\)) parameter |

---

# 8. When Should You Use Each Loss Function?

## Use Mean Squared Error (MSE)

When

- Outliers are rare.
- Large prediction errors should be heavily penalized.
- Smooth optimization is important.

### Applications

- House Price Prediction
- Temperature Prediction
- Stock Price Prediction

---

## Use Mean Absolute Error (MAE)

When

- The dataset contains many outliers.
- Every prediction error should have equal importance.
- Interpretability is important.

### Applications

- Sales Forecasting
- Demand Forecasting
- Traffic Prediction

---

## Use Huber Loss

When

- Some outliers exist.
- Smooth optimization is required.
- You want a balance between MSE and MAE.

### Applications

- Autonomous Driving
- Robotics
- Financial Forecasting
- Object Detection

---

# 9. Complete Comparison Table

| Feature | MSE | MAE | Huber Loss |
|---------|-----|-----|------------|
| Formula | Squares Error | Absolute Error | Piecewise Function |
| Error Growth | Quadratic | Linear | Quadratic + Linear |
| Outlier Sensitivity | High | Low | Moderate |
| Differentiable | Yes | No (at Zero) | Yes |
| Gradient Smoothness | Smooth | Less Smooth | Smooth |
| Hyperparameter Required | No | No | Yes (\(\delta\)) |
| Optimization | Easy | Harder | Easy |
| Interpretation | Squared Units | Original Units | Mixed Behavior |

---

# 10. Which Loss Function is Best?

There is **no universally best** regression loss function.

The choice depends on the dataset.

| Situation | Recommended Loss Function |
|------------|--------------------------|
| Very few outliers | Mean Squared Error (MSE) |
| Many outliers | Mean Absolute Error (MAE) |
| Moderate outliers with smooth optimization | Huber Loss |

---

# 11. Real-World Decision Tree

```text
Regression Problem

↓

Are there many outliers?

├── No

│     ↓

│   Use MSE

│
└── Yes

      ↓

Need smooth optimization?

      │

      ├── Yes

      │      ↓

      │   Use Huber Loss

      │

      └── No

             ↓

          Use MAE
```

---

# 12. Interview Questions

## Q1. Which loss function is most sensitive to outliers?

**Answer**

Mean Squared Error (MSE).

---

## Q2. Which loss function is least sensitive to outliers?

**Answer**

Mean Absolute Error (MAE).

---

## Q3. Why is Huber Loss widely used?

Because it combines the advantages of MSE and MAE.

---

## Q4. Which loss function is easiest to optimize?

**Answer**

Mean Squared Error (MSE),

because it is smooth and differentiable everywhere.

---

## Q5. Which loss function preserves the original units of the target variable?

**Answer**

Mean Absolute Error (MAE).

---

## Q6. Which loss function requires a hyperparameter?

**Answer**

Huber Loss,

because it requires the Delta (\(\delta\)) parameter.

---

# Summary

Regression problems use different loss functions depending on the characteristics of the dataset.

- **Mean Squared Error (MSE)** strongly penalizes large prediction errors and is suitable when outliers are rare.
- **Mean Absolute Error (MAE)** treats every prediction error equally and is more robust to outliers.
- **Huber Loss** combines the advantages of both by using quadratic penalties for small errors and linear penalties for large errors.

Choosing the appropriate loss function depends on the amount of noise, the presence of outliers, and the optimization requirements of the problem.

---

# Key Takeaways

✔ MSE squares the prediction error.

✔ MAE uses the absolute prediction error.

✔ Huber Loss combines MSE and MAE.

✔ MSE is highly sensitive to outliers.

✔ MAE is robust to outliers.

✔ Huber Loss provides a balance between robustness and smooth optimization.

✔ There is no universally best regression loss function.

✔ The appropriate loss function depends on the dataset and the application's requirements.
