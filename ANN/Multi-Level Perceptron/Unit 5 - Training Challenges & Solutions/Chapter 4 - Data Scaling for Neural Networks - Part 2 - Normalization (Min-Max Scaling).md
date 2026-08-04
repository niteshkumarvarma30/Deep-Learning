# Unit 5 – Training Challenges & Solutions

# Chapter 4 – Data Scaling for Neural Networks

## Part 2 – Normalization (Min-Max Scaling)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Normalization is.
- Learn the mathematical formula for Min-Max Scaling.
- Perform Normalization manually.
- Understand why the output lies between 0 and 1.
- Learn when Normalization should be used.
- Understand its advantages and limitations.

---

# 1. Introduction

In the previous chapter,

we learned that neural networks require input features to have similar numerical ranges.

One of the most common techniques used to achieve this is

> **Normalization (Min-Max Scaling).**

Normalization rescales every feature into a fixed interval,

usually

$$
[0,1]
$$

This makes all input features comparable in magnitude before training begins.

---

# 2. What is Normalization?

Normalization transforms every feature so that

- The minimum value becomes **0**
- The maximum value becomes **1**
- Every other value lies between **0 and 1**

Example

Original values

```text
20

40

60

80

100
```

Normalized values

```text
0

0.25

0.50

0.75

1
```

Notice that

the relative ordering of the data remains unchanged.

---

# 3. Mathematical Formula

The Min-Max Scaling formula is

$$
x_{normalized} = \frac{x-x_{min}} {x_{max}-x_{min}}
$$

where

- \(x\) = Original feature value
- \(x_{min}\) = Minimum value of the feature
- \(x_{max}\) = Maximum value of the feature

This guarantees

$$
0 \le x_{normalized} \le 1
$$

---

# 4. Step-by-Step Example

Suppose the dataset contains

```text
Age

20

30

40

50

60
```

Here

```text
Minimum = 20

Maximum = 60
```

---

### Step 1 – Normalize Age = 20

$$
\frac{20-20}{60-20} = 0
$$

---

### Step 2 – Normalize Age = 30

$$
\frac{30-20}{60-20} = \frac{10}{40} = 0.25
$$

---

### Step 3 – Normalize Age = 40

$$
\frac{40-20}{60-20} = \frac{20}{40} = 0.50
$$

---

### Step 4 – Normalize Age = 50

$$
\frac{50-20}{60-20} = \frac{30}{40} = 0.75
$$

---

### Step 5 – Normalize Age = 60

$$
\frac{60-20}{60-20} = 1
$$

---

### Final Result

| Original Value | Normalized Value |
|---------------:|-----------------:|
| 20 | 0.00 |
| 30 | 0.25 |
| 40 | 0.50 |
| 50 | 0.75 |
| 60 | 1.00 |

---

# 5. Why Does the Formula Work?

Suppose

$$
x=x_{min}
$$

Then

$$
\frac{x_{min}-x_{min}} {x_{max}-x_{min}} = 0
$$

Therefore,

the minimum value always becomes

```text
0
```

---

Suppose

$$
x=x_{max}
$$

Then

$$
\frac{x_{max}-x_{min}} {x_{max}-x_{min}} = 1
$$

Therefore,

the maximum value always becomes

```text
1
```

Every other value automatically lies between **0** and **1**.

---

# 6. Visual Representation

Before Normalization

```text
20 ------------------------------ 100
```

After Normalization

```text
0 ------------------------------- 1
```

The numerical scale changes,

but the relative positions of the data remain exactly the same.

---

# 7. Advantages of Normalization

Normalization provides several benefits.

- Faster Gradient Descent
- Similar numerical ranges for all features
- Better numerical stability
- Faster convergence
- Improved optimization performance

It is particularly useful when feature values naturally have fixed upper and lower bounds.

---

# 8. Limitations of Normalization

Normalization has one major limitation.

## Sensitive to Outliers

Suppose the data is

```text
20

25

30

35

5000
```

The maximum becomes

```text
5000
```

After Normalization,

```text
20   → 0.000

25   → 0.001

30   → 0.002

35   → 0.003

5000 → 1.000
```

Most observations become compressed very close to zero.

This can make learning more difficult.

---

# 9. When Should We Use Normalization?

Normalization is commonly used when

- Features already have fixed limits.
- Pixel values are used in image data.
- Neural networks expect inputs between 0 and 1.

Examples include

- Images (0–255 → 0–1)
- Probability values
- Sensor measurements with known ranges

---

# 10. Real-Life Analogy

Suppose students from two schools are graded differently.

School A

```text
Marks: 0–100
```

School B

```text
Marks: 0–500
```

Direct comparison is unfair.

Normalization converts both grading systems into

```text
0–1
```

Now,

student performance can be compared fairly.

Neural networks use the same principle.

---

# 11. One Important Insight

Many beginners think

> **Normalization always means scaling data between 0 and 1.**

This is not entirely true.

Min-Max Scaling commonly uses

$$
[0,1]
$$

but it can scale to **any desired interval**.

For example,

to scale into

$$
[-1,1]
$$

we use

$$
x_{scaled} = a + \frac{(x-x_{min})(b-a)} {x_{max}-x_{min}}
$$

where

- \(a\) = New minimum
- \(b\) = New maximum

---

# 12. Visual Summary

```text
Original Feature

↓

Find Minimum

↓

Find Maximum

↓

Apply Min-Max Formula

↓

Values Between 0 and 1

↓

Train Neural Network
```

---

# Difference Between Original and Normalized Data

| Original Data | Normalized Data |
|---------------|-----------------|
| Different numerical ranges | Common numerical range |
| Large values dominate | Equal contribution from features |
| Slower optimization | Faster optimization |
| Difficult Gradient Descent | Smooth Gradient Descent |

---

# Interview Questions

## Q1. What is Normalization?

**Answer**

Normalization is a feature scaling technique that rescales data into a fixed numerical range, usually between **0 and 1**.

---

## Q2. What is the formula for Min-Max Scaling?

**Answer**

$$
x_{normalized} = \frac{x-x_{min}} {x_{max}-x_{min}}
$$

---

## Q3. Why does the minimum value always become 0?

**Answer**

Because when \(x=x_{min}\), the numerator becomes zero, making the normalized value equal to zero.

---

## Q4. What is the biggest disadvantage of Normalization?

**Answer**

Normalization is highly sensitive to outliers because the minimum and maximum values determine the scaling.

---

## Q5. Where is Normalization commonly used?

**Answer**

- Image preprocessing
- Computer Vision
- Deep Learning
- Features with known minimum and maximum values

---

# Summary

Normalization, also called **Min-Max Scaling**, transforms input features into a fixed numerical range, most commonly **0 to 1**.

It preserves the relative ordering of the data while making feature magnitudes comparable.

This leads to smoother Gradient Descent, faster convergence, and more stable neural network training.

However, because the transformation depends on the minimum and maximum values, Normalization is sensitive to outliers and should be used carefully when extreme values exist.

---

# Key Takeaways

✔ Normalization rescales features into a fixed numerical range.

✔ The most common range is **0 to 1**.

✔ It preserves the ordering of the data.

✔ It improves Gradient Descent convergence.

✔ It is sensitive to outliers.

✔ It is widely used for image preprocessing and bounded numerical features.

---

## Next Part

**Part 3 – Standardization (Z-Score Scaling)**

In the next chapter, we will study **Standardization**, derive the Z-score formula, perform manual calculations, compare it with Normalization, and understand why it is the most widely used scaling technique in modern Machine Learning and Deep Learning.
