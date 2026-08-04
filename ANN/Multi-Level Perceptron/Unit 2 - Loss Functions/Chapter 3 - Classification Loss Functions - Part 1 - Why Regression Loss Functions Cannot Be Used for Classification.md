# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 1 – Why Regression Loss Functions Cannot Be Used for Classification

---

# Learning Objectives

After completing this part, you will be able to:

- Understand the difference between Regression and Classification.
- Explain why MSE and MAE are not suitable for classification problems.
- Understand why Classification requires a different loss function.
- Understand the importance of probability predictions.
- Explain why Cross Entropy Loss is used.

---

# 1. Introduction

In the previous chapter, we studied regression loss functions.

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Huber Loss

These loss functions work well for **Regression Problems**.

However,

they are **not suitable for Classification Problems**.

Before learning Cross Entropy Loss,

we must first understand **why regression loss functions fail in classification.**

---

# 2. Regression vs Classification

Machine Learning problems are broadly divided into two categories.

## Regression

Regression predicts a **continuous numerical value**.

Examples

- House Price Prediction
- Temperature Prediction
- Salary Prediction
- Stock Price Prediction

Example

```text
Area = 1500 sq ft

↓

Neural Network

↓

₹72,50,000
```

The output is a number.

---

## Classification

Classification predicts a **category (class)**.

Examples

- Spam / Not Spam
- Cat / Dog
- Disease / Healthy
- Positive / Negative Review

Example

```text
Email

↓

Neural Network

↓

Spam
```

The output is a class.

---

# 3. How Does a Neural Network Predict Classes?

A neural network does **not** directly predict class names.

Instead,

it predicts **probabilities**.

Example

```text
Spam Probability

↓

0.95
```

Meaning

```text
There is a 95% probability that the email is Spam.
```

---

Another example

```text
Cat

↓

0.92

Dog

↓

0.08
```

Since

```text
0.92 > 0.08
```

the model predicts

```text
Cat
```

Therefore,

classification models work with **probabilities**, not numerical values.

---

# 4. Why Can't We Use Mean Squared Error (MSE)?

Suppose

Actual Label

```text
Spam

↓

1
```

Model Prediction

```text
0.90
```

Using MSE

$$
(1-0.90)^2
=
0.01
$$

Now suppose another prediction

```text
0.99
```

Using MSE

$$
(1-0.99)^2
=
0.0001
$$

Although the second prediction is better,

MSE does not strongly encourage the model to produce highly confident probabilities.

---

# 5. Another Example

Suppose the actual class is

```text
Dog
```

Model A predicts

```text
Dog = 0.51

Cat = 0.49
```

---

Model B predicts

```text
Dog = 0.99

Cat = 0.01
```

Both models predict

```text
Dog
```

However,

Model B is much more confident.

MSE treats these predictions as only slightly different.

In reality,

Model B should be rewarded much more.

---

# 6. The Bigger Problem

Now suppose

Actual Class

```text
Dog
```

Model predicts

```text
Dog = 0.01

Cat = 0.99
```

The model is

- Wrong
- Extremely confident

A good classification loss function should assign a **very large penalty** to this prediction.

MSE does not penalize this type of mistake strongly enough.

---

# 7. What Should a Classification Loss Function Do?

A good classification loss function should

- Produce **small loss** when the correct class has high probability.
- Produce **large loss** when the correct class has low probability.
- Penalize confident incorrect predictions very heavily.
- Encourage the model to assign maximum probability to the correct class.

This is exactly what **Cross Entropy Loss** does.

---

# 8. Real-Life Analogy

Imagine a multiple-choice examination.

Question

```text
Which animal is shown?
```

Correct Answer

```text
Cat
```

---

### Student A

```text
Cat

Confidence = 99%
```

Excellent prediction.

---

### Student B

```text
Cat

Confidence = 55%
```

Correct,

but not very confident.

---

### Student C

```text
Dog

Confidence = 99%
```

Wrong,

and extremely confident.

A good loss function should

- Give a very small penalty to Student A.
- Give a moderate penalty to Student B.
- Give a very large penalty to Student C.

Cross Entropy Loss behaves exactly this way.

---

# 9. Comparison

| Regression Loss Functions | Classification Loss Functions |
|----------------------------|-------------------------------|
| Predict numerical values | Predict probabilities |
| Measure numerical error | Measure probability error |
| MSE, MAE, Huber Loss | Cross Entropy Loss |
| Suitable for regression | Suitable for classification |

---

# 10. Why Cross Entropy Loss?

Cross Entropy Loss is designed specifically for probability predictions.

It

- Rewards confident correct predictions.
- Penalizes confident wrong predictions.
- Works well with Sigmoid and Softmax activation functions.
- Produces smooth gradients for optimization.

Because of these advantages,

it has become the standard loss function for classification problems.

---

# 11. Transition to the Next Part

Now that we understand why regression loss functions are unsuitable for classification,

we are ready to study

**Binary Cross Entropy (BCE)**.

Binary Cross Entropy is used when there are exactly **two classes**.

Examples

- Spam / Not Spam
- Yes / No
- Fraud / Not Fraud
- Disease / Healthy

It is one of the most important loss functions in Deep Learning.

---

# Summary

Regression and Classification are two different types of Machine Learning problems.

Regression predicts continuous numerical values,

whereas Classification predicts probabilities for different classes.

Regression loss functions such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and Huber Loss are designed for numerical outputs and are therefore not ideal for classification.

Classification requires a loss function that measures the quality of probability predictions.

Cross Entropy Loss satisfies this requirement by rewarding confident correct predictions and heavily penalizing confident incorrect predictions.

---

# Key Takeaways

✔ Regression predicts continuous numerical values.

✔ Classification predicts classes using probabilities.

✔ Classification models output probabilities instead of class names.

✔ MSE, MAE, and Huber Loss are designed for regression.

✔ Regression loss functions are not suitable for classification problems.

✔ Classification requires probability-based loss functions.

✔ Cross Entropy Loss rewards confident correct predictions.

✔ Cross Entropy Loss strongly penalizes confident incorrect predictions.

✔ Binary Cross Entropy is used for binary classification problems.

✔ The next concept is **Binary Cross Entropy (BCE)**, the most widely used loss function for binary classification.
