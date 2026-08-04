# Unit 5 – Training Challenges & Solutions

# Chapter 4 – Data Scaling for Neural Networks

## Part 4 – Normalization vs Standardization

---

# Learning Objectives

After completing this chapter, you will be able to:

- Compare Normalization and Standardization.
- Understand their mathematical differences.
- Learn when to use each technique.
- Understand their advantages and disadvantages.
- Choose the correct scaling method for different Machine Learning and Deep Learning algorithms.

---

# 1. Introduction

So far,

we have studied two major feature scaling techniques.

### Normalization

Transforms feature values into

$$
[0,1]
$$

using **Min-Max Scaling**.

---

### Standardization

Transforms feature values so that

- Mean = 0
- Standard Deviation = 1

using the **Z-score**.

Now,

let us compare these two techniques in detail.

---

# 2. Mathematical Comparison

## Normalization

Formula

$$
x_{normalized} = \frac{x-x_{min}} {x_{max}-x_{min}}
$$

Output

```text
Range

0

↓

1
```

---

## Standardization

Formula

$$
z = \frac{x-\mu}{\sigma}
$$

Output

```text
Mean = 0

Standard Deviation = 1
```

Unlike Normalization,

Standardization has **no fixed numerical range**.

---

# 3. Output Range Comparison

Suppose the original feature values are

```text
20

30

40

50

60
```

---

### After Normalization

```text
0

0.25

0.50

0.75

1
```

---

### After Standardization

```text
-1.41

-0.71

0

0.71

1.41
```

Notice

Normalization always produces values between **0 and 1**,

whereas Standardization can produce

- Negative values
- Positive values
- Values greater than 1
- Values less than -1

---

# 4. Dependence on Statistics

Normalization depends on

```text
Minimum

Maximum
```

---

Standardization depends on

```text
Mean

Standard Deviation
```

Therefore,

Normalization changes whenever the minimum or maximum changes.

Standardization changes whenever the mean or spread of the data changes.

---

# 5. Effect of Outliers

Suppose the dataset is

```text
20

25

30

35

5000
```

---

## Normalization

The maximum becomes

```text
5000
```

After scaling,

most observations become compressed very close to zero.

---

## Standardization

The mean and standard deviation increase,

but the remaining observations generally remain more spread out.

Therefore,

Standardization usually handles outliers **better than Normalization**,

although it is **still affected by extreme outliers**.

---

# 6. Which Technique Is Better?

There is **no universal best choice**.

The correct technique depends on

- The learning algorithm
- The data distribution
- The application

Different problems require different scaling strategies.

---

# 7. When Should We Use Normalization?

Normalization is preferred when

- Features have fixed minimum and maximum values.
- Inputs naturally lie within a bounded range.
- Pixel values are used.

Common applications include

- Image Processing
- Computer Vision
- Autoencoders
- Deep Learning models using bounded inputs

---

# 8. When Should We Use Standardization?

Standardization is preferred when

- Data approximately follows a normal distribution.
- Features do not have fixed limits.
- Statistical Machine Learning algorithms are used.

Common applications include

- Neural Networks
- Logistic Regression
- Linear Regression
- Support Vector Machines (SVM)
- Principal Component Analysis (PCA)

---

# 9. Which Technique Is Used Most Often?

In practice,

Standardization is the most commonly used feature scaling technique in Machine Learning.

Normalization is especially common for

- Images
- Pixel values
- Features naturally bounded within a fixed interval

---

# 10. Real-Life Analogy

Imagine measuring temperatures.

## Normalization

You convert temperatures into percentages.

```text
0%

↓

25%

↓

50%

↓

75%

↓

100%
```

---

## Standardization

You measure

> **How far each temperature is from the average temperature.**

```text
Below Average

↓

Average

↓

Above Average
```

Both approaches are useful,

but they answer different questions.

---

# 11. Complete Comparison Table

| Feature | Normalization | Standardization |
|----------|---------------|-----------------|
| Formula | \(\frac{x-x_{min}}{x_{max}-x_{min}}\) | \(\frac{x-\mu}{\sigma}\) |
| Output Range | Usually 0 to 1 | No fixed range |
| Uses Minimum | ✅ Yes | ❌ No |
| Uses Maximum | ✅ Yes | ❌ No |
| Uses Mean | ❌ No | ✅ Yes |
| Uses Standard Deviation | ❌ No | ✅ Yes |
| Sensitive to Outliers | Highly | Moderately |
| Common Applications | Images, bounded features | Most ML & DL algorithms |

---

# 12. One Important Insight

Many beginners ask

> **Which scaling technique gives better model accuracy?**

Neither technique directly improves accuracy.

Both preserve the information contained in the dataset.

Their primary purpose is to

- Improve optimization
- Speed up Gradient Descent
- Increase numerical stability

The best technique depends on the characteristics of the dataset and the algorithm.

---

# Visual Summary

```text
Raw Features

↓

Choose Scaling Technique

↓

Normalization

or

Standardization

↓

Balanced Feature Values

↓

Stable Gradient Descent

↓

Faster Training
```

---

# Difference Between Normalization and Standardization

| Normalization | Standardization |
|---------------|-----------------|
| Uses Min-Max Scaling | Uses Z-score Scaling |
| Output usually between 0 and 1 | Mean = 0, Standard Deviation = 1 |
| Highly sensitive to outliers | Less sensitive to outliers |
| Suitable for bounded features | Suitable for normally distributed features |
| Common for image data | Common for Machine Learning algorithms |

---

# Interview Questions

## Q1. What is the main difference between Normalization and Standardization?

**Answer**

Normalization scales data into a fixed range (usually **0–1**), whereas Standardization transforms data so that it has a **mean of 0** and a **standard deviation of 1**.

---

## Q2. Which technique is more sensitive to outliers?

**Answer**

Normalization,

because it depends directly on the minimum and maximum values.

---

## Q3. Which scaling technique is commonly used for image data?

**Answer**

Normalization,

because image pixel values are typically scaled from **0–255** to **0–1**.

---

## Q4. Which scaling technique is more commonly used in Machine Learning?

**Answer**

Standardization,

because many Machine Learning algorithms perform better when features are centered around zero.

---

## Q5. Does either technique directly improve model accuracy?

**Answer**

No.

Both techniques primarily improve optimization speed, numerical stability, and training efficiency rather than directly increasing accuracy.

---

# Summary

Normalization and Standardization are the two most widely used feature scaling techniques.

Normalization rescales features into a fixed numerical range, making it suitable for bounded inputs such as image pixels.

Standardization centers data around zero with unit variance, making it the preferred choice for many Machine Learning and Deep Learning algorithms.

Choosing the correct technique depends on the data characteristics and the algorithm being used.

---

# Key Takeaways

✔ Normalization uses **minimum** and **maximum** values.

✔ Standardization uses **mean** and **standard deviation**.

✔ Normalization produces values between **0 and 1**.

✔ Standardization produces values with **mean = 0** and **standard deviation = 1**.

✔ Normalization is ideal for bounded features such as images.

✔ Standardization is the default choice for many Machine Learning and Deep Learning algorithms.

---

## Next Part

**Part 5 – Effect of Feature Scaling on Gradient Descent**

In the next chapter, we will visually understand **how Feature Scaling changes the optimization landscape**, why unscaled features cause the famous **zig-zag path** in Gradient Descent, and how scaling enables much faster convergence in neural networks.
