# Unit 2 – Loss Functions

# Chapter 1 – Introduction to Loss Functions

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why a Loss Function is needed.
- Differentiate between Prediction and Actual Value.
- Understand the concept of Error.
- Understand the meaning of Loss.
- Explain what a Loss Function is.
- Differentiate between Loss Function and Cost Function.
- Understand why Loss Functions are essential for learning.

---

# 1. Introduction

In Unit 1, we studied **Forward Propagation**.

During Forward Propagation, the neural network receives an input and produces a prediction.

Example

```text
Input

↓

Neural Network

↓

Prediction
```

However, after obtaining the prediction, an important question arises.

> **How does the neural network know whether its prediction is correct or incorrect?**

The answer is

**Loss Function.**

A Loss Function measures the quality of the prediction made by the neural network.

---

# 2. Why Do We Need a Loss Function?

Imagine you have just completed an examination.

After writing the exam, you naturally want to know

- How many answers are correct?
- How many answers are incorrect?
- What is your score?

Without checking your answers, you cannot improve.

A neural network faces the same situation.

After making a prediction, it requires feedback to determine whether it performed well or poorly.

The Loss Function provides this feedback.

---

# 3. Prediction vs Actual Value

Every supervised learning problem contains two important values.

## Actual Value

The correct answer available in the training dataset.

It is represented by

$$
y
$$

---

## Predicted Value

The value predicted by the neural network.

It is represented by

$$
\hat{y}
$$

(pronounced **y-hat**)

---

### Example

Suppose the actual house price is

```text
₹50 Lakhs
```

The neural network predicts

```text
₹47 Lakhs
```

Therefore,

$$
y=50
$$

$$
\hat{y}=47
$$

The prediction is close to the correct value but not exactly correct.

---

# 4. What is Error?

The difference between the actual value and the predicted value is called the **Error**.

Mathematically,

$$
\text{Error}
=
y-\hat{y}
$$

---

## Example 1

Actual Value

```text
50
```

Predicted Value

```text
47
```

Error

$$
50-47=3
$$

The prediction is off by **3 units**.

---

## Example 2

Actual Value

```text
50
```

Predicted Value

```text
55
```

Error

$$
50-55=-5
$$

The negative sign indicates that the prediction is larger than the actual value.

---

# Why Can't We Use Error Directly?

Suppose

Example 1

```text
Error = +5
```

Example 2

```text
Error = -5
```

If we simply average these values,

$$
5+(-5)=0
$$

This incorrectly suggests that there is no error.

To avoid this problem, Loss Functions usually

- Square the error
- Take the absolute value of the error

This ensures that the error is always measured correctly.

---

# 5. What is Loss?

Loss is a numerical value that represents **how bad a prediction is**.

Smaller Loss

↓

Better Prediction

Larger Loss

↓

Poor Prediction

---

### Examples

```text
Loss = 0
```

Perfect Prediction

---

```text
Loss = 0.02
```

Very Good Prediction

---

```text
Loss = 10
```

Poor Prediction

---

The objective of training is to make the Loss as small as possible.

---

# 6. What is a Loss Function?

A Loss Function is a mathematical function that converts the prediction error into a single numerical value.

General representation

$$
L(y,\hat{y})
$$

where

- \(y\) = Actual Value
- \(\hat{y}\) = Predicted Value

Output

```text
One Number

↓

Loss
```

Different machine learning problems use different Loss Functions.

---

# 7. Why Can't a Neural Network Learn Without a Loss Function?

Suppose the neural network predicts

```text
Dog
```

The actual answer is

```text
Cat
```

Without a Loss Function,

the network only knows

```text
Prediction = Dog
```

It does **not** know

- How wrong the prediction is.
- Whether the mistake is small or large.
- Which weights should be updated.
- How much each weight should change.

The Loss Function provides this information.

Without it, learning is impossible.

---

# 8. Real-Life Analogy

Imagine throwing darts at a dartboard.

```text
Target

↓

Bullseye
```

If your dart lands far from the center,

the distance from the bullseye tells you how inaccurate your throw was.

This distance behaves like a **Loss**.

Smaller distance

↓

Better throw

Larger distance

↓

Poor throw

Similarly,

the Loss Function tells the neural network how far its prediction is from the correct answer.

---

# 9. Loss Function vs Cost Function

The terms **Loss Function** and **Cost Function** are often used interchangeably.

However, there is a small difference.

## Loss Function

Measures the error for **one training example**.

Example

Predicting the price of one house.

---

## Cost Function

Measures the **average loss** over an entire dataset or batch.

Example

Average error for 10,000 house price predictions.

---

### Comparison

| Loss Function | Cost Function |
|---------------|---------------|
| Calculated for one training example | Calculated for all training examples |
| Measures individual prediction error | Measures average prediction error |
| Used during individual computations | Used during model optimization |

---

# 10. Complete Training Pipeline

The neural network training process now becomes

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Loss Function

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

This complete cycle is repeated many times during training.

---

# 11. Characteristics of a Good Loss Function

A good Loss Function should

- Measure prediction error accurately.
- Increase when predictions become worse.
- Decrease when predictions improve.
- Be mathematically easy to optimize.
- Help the model learn efficiently.

---

# 12. Applications of Loss Functions

Loss Functions are used in almost every Machine Learning and Deep Learning task.

Examples

### Regression

- House Price Prediction
- Stock Price Prediction
- Temperature Forecasting

Common Loss Functions

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Huber Loss

---

### Classification

- Email Spam Detection
- Disease Detection
- Image Classification
- Sentiment Analysis

Common Loss Functions

- Binary Cross Entropy
- Categorical Cross Entropy

---

# 13. Summary

Forward Propagation allows the neural network to make predictions.

However,

the network cannot improve unless it knows how good or bad those predictions are.

A Loss Function measures the difference between the **Actual Value** and the **Predicted Value** and converts that difference into a numerical value.

The objective of the neural network is to **minimize this Loss** during training.

Without a Loss Function,

the network cannot learn.

---

# Key Takeaways

✔ Forward Propagation produces predictions.

✔ Every prediction is compared with the actual value.

✔ The difference between them is called **Error**.

✔ A Loss Function converts the Error into a numerical value.

✔ Smaller Loss indicates better predictions.

✔ Larger Loss indicates poorer predictions.

✔ Loss Function measures the error for one training example.

✔ Cost Function measures the average loss over multiple training examples.

✔ The Loss Function provides the feedback required for learning.

✔ The next step after computing Loss is **Backpropagation**, which updates the network's weights to reduce future errors.
