# Unit 5 – Training Challenges & Solutions

# Chapter 4 – Data Scaling for Neural Networks

## Part 3 – Standardization (Z-Score Scaling)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Standardization is.
- Learn the Z-score formula.
- Perform Standardization manually.
- Understand why the transformed data has a mean of **0** and a standard deviation of **1**.
- Learn when Standardization should be preferred over Normalization.
- Understand its advantages and limitations.

---

# 1. Introduction

In the previous chapter,

we studied **Normalization (Min-Max Scaling)**, where feature values were transformed into the range

$$
[0,1]
$$

However,

many real-world datasets do not have fixed minimum and maximum values.

New observations may contain values larger than the previous maximum or smaller than the previous minimum.

For such datasets,

we use

> **Standardization (Z-Score Scaling).**

Unlike Normalization,

Standardization centers the data around the mean rather than forcing it into a fixed range.

---

# 2. What is Standardization?

Standardization transforms every feature so that

- Mean becomes **0**
- Standard Deviation becomes **1**

Instead of restricting values between **0 and 1**,

it measures how far each value is from the mean.

Example

Original values

```text
20

30

40

50

60
```

Standardized values

```text
-1.41

-0.71

0

0.71

1.41
```

Notice that

the transformed values are **not limited between 0 and 1**.

---

# 3. Mathematical Formula

The Z-score formula is

$$
z = \frac{x-\mu}{\sigma}
$$

where

- \(x\) = Original feature value
- \(\mu\) = Mean of the feature
- \(\sigma\) = Standard deviation of the feature

The transformed value is called the **Z-score**.

---

# 4. Step-by-Step Example

Suppose the dataset contains

```text
20

30

40

50

60
```

---

## Step 1 – Compute the Mean

$$
\mu = \frac{20+30+40+50+60}{5} = 40
$$

---

## Step 2 – Compute the Standard Deviation

Assume

$$
\sigma = 14.14
$$

---

## Step 3 – Compute the Z-score

### For x = 20

$$
z = \frac{20-40}{14.14} = -1.41
$$

---

### For x = 30

$$
z = \frac{30-40}{14.14} = -0.71
$$

---

### For x = 40

$$
z = \frac{40-40}{14.14} = 0
$$

---

### For x = 50

$$
z = \frac{50-40}{14.14} = 0.71
$$

---

### For x = 60

$$
z = \frac{60-40}{14.14} = 1.41
$$

---

## Final Result

| Original Value | Standardized Value |
|---------------:|-------------------:|
| 20 | -1.41 |
| 30 | -0.71 |
| 40 | 0.00 |
| 50 | 0.71 |
| 60 | 1.41 |

---

# 5. Why Does the Formula Work?

Suppose

$$
x=\mu
$$

Then

$$
z = \frac{\mu-\mu}{\sigma} = 0
$$

Therefore,

the mean always becomes

```text
0
```

Dividing by the standard deviation scales the spread of the data,

making

```text
Standard Deviation = 1
```

---

# 6. Interpretation of the Z-score

A Z-score tells us

> **How many standard deviations a value is away from the mean.**

Examples

### Z = 0

```text
Exactly at the Mean
```

---

### Z = +2

```text
Two Standard Deviations Above the Mean
```

---

### Z = -2

```text
Two Standard Deviations Below the Mean
```

---

# 7. Advantages of Standardization

Standardization offers several advantages.

- Centers data around zero.
- Produces balanced feature scales.
- Works well for normally distributed data.
- Handles unseen values better than Normalization.
- Less affected by changing minimum and maximum values.
- Improves optimization for many Machine Learning algorithms.

---

# 8. Limitations of Standardization

Although Standardization is very useful,

it still has some limitations.

- Sensitive to extreme outliers because mean and standard deviation are affected.
- Does not produce values within a fixed interval.
- Can generate large positive and negative values.

---

# 9. When Should We Use Standardization?

Standardization is commonly used with

- Neural Networks
- Logistic Regression
- Linear Regression
- Support Vector Machines (SVM)
- Principal Component Analysis (PCA)

It is especially useful when data is approximately normally distributed.

---

# 10. Real-Life Analogy

Suppose the average exam score is

```text
Mean = 70
```

Student A scores

```text
90
```

Student B scores

```text
60
```

Instead of comparing raw scores,

we ask

> **How far is each student from the average?**

That is exactly what the Z-score measures.

---

# 11. One Important Insight

Many beginners think

> **Standardization always produces values between -1 and 1.**

This is incorrect.

Standardized values can be

```text
-3

-2

-1

0

1

2

5
```

There is **no fixed range**.

Only the mean and standard deviation are standardized.

---

# 12. Visual Summary

```text
Original Feature

↓

Compute Mean

↓

Compute Standard Deviation

↓

Apply Z-score Formula

↓

Mean = 0

↓

Standard Deviation = 1

↓

Train Neural Network
```

---

# Difference Between Original and Standardized Data

| Original Data | Standardized Data |
|---------------|-------------------|
| Different numerical ranges | Similar numerical ranges |
| Mean depends on data | Mean = 0 |
| Standard deviation varies | Standard deviation = 1 |
| Large values may dominate | Balanced feature contribution |
| Slower optimization | Faster optimization |

---

# Interview Questions

## Q1. What is Standardization?

**Answer**

Standardization is a feature scaling technique that transforms data so that it has a mean of **0** and a standard deviation of **1**.

---

## Q2. What is the formula for Standardization?

**Answer**

$$
z = \frac{x-\mu}{\sigma}
$$

---

## Q3. What does a Z-score represent?

**Answer**

A Z-score represents the number of standard deviations a data point is above or below the mean.

---

## Q4. Does Standardization produce values only between -1 and 1?

**Answer**

No.

Standardized values can be any real number depending on their distance from the mean.

---

## Q5. Where is Standardization commonly used?

**Answer**

- Neural Networks
- Logistic Regression
- Linear Regression
- Support Vector Machines
- Principal Component Analysis

---

# Summary

Standardization transforms input features by subtracting the mean and dividing by the standard deviation.

Unlike Normalization, it does not force values into a fixed range. Instead, it produces transformed data with a **mean of 0** and a **standard deviation of 1**.

This makes optimization more stable and allows many Machine Learning and Deep Learning algorithms to train more effectively, especially when the data approximately follows a normal distribution.

---

# Key Takeaways

✔ Standardization uses the **Z-score formula**.

✔ The transformed data has **mean = 0**.

✔ The transformed data has **standard deviation = 1**.

✔ Values are **not restricted** to the range **0–1**.

✔ It is one of the most widely used feature scaling techniques.

✔ It is commonly preferred for Machine Learning and Deep Learning models.

---

## Next Part

**Part 4 – Normalization vs Standardization**

In the next chapter, we will compare **Normalization** and **Standardization** in detail, understand their mathematical differences, advantages, disadvantages, practical use cases, and learn **which scaling technique should be selected for different Machine Learning and Deep Learning algorithms**.
