# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 3 – Categorical Cross Entropy (CCE)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Binary Cross Entropy (BCE) cannot be used for multi-class classification.
- Understand what Categorical Cross Entropy (CCE) is.
- Learn about One-Hot Encoding.
- Derive the CCE formula.
- Solve numerical examples.
- Understand why CCE is used with the Softmax activation function.
- Know when to use CCE.

---

# 1. Why Can't We Use Binary Cross Entropy (BCE)?

Binary Cross Entropy (BCE) is designed for **binary classification**, where there are only **two possible classes**.

Examples

- Spam / Not Spam
- Disease / Healthy
- Fraud / Not Fraud

However, many real-world problems involve **more than two classes**.

Examples

| Problem | Classes |
|----------|----------|
| Animal Classification | Cat, Dog, Horse |
| Digit Recognition | 0,1,2,...,9 |
| Fruit Classification | Apple, Banana, Orange, Mango |
| Image Classification | Hundreds or Thousands of Classes |

For these problems,

Binary Cross Entropy is not suitable.

We need a loss function that can compare probabilities across **multiple classes simultaneously**.

This loss function is called

**Categorical Cross Entropy (CCE).**

---

# 2. What is Multi-Class Classification?

Multi-class classification means

Each input belongs to **exactly one class** out of multiple possible classes.

Example

```text
Image

↓

Neural Network

↓

Cat
```

Possible Classes

```text
Cat

Dog

Horse
```

Only **one class** is the correct answer.

---

# 3. How Does a Neural Network Predict Multiple Classes?

The output layer contains **one neuron for each class**.

Example

```text
Cat    → 0.80

Dog    → 0.15

Horse  → 0.05
```

These numbers represent probabilities.

Notice

```text
0.80 + 0.15 + 0.05 = 1
```

The probabilities always sum to **1**.

This is achieved using the **Softmax Activation Function**.

---

# 4. One-Hot Encoding

Before computing CCE,

the actual class labels are converted into **One-Hot Encoded vectors**.

Suppose there are three classes.

| Class | One-Hot Encoding |
|--------|------------------|
| Cat | [1,0,0] |
| Dog | [0,1,0] |
| Horse | [0,0,1] |

---

## Example

Suppose

Actual Class

```text
Dog
```

One-Hot Encoding

```text
[0,1,0]
```

Predicted Probabilities

```text
[0.10,0.80,0.10]
```

Categorical Cross Entropy compares these two vectors.

---

# 5. What is Categorical Cross Entropy (CCE)?

## Definition

Categorical Cross Entropy (CCE) measures the difference between

- the **actual probability distribution** (One-Hot Encoded labels),
- and the **predicted probability distribution**.

Like Binary Cross Entropy,

- Small Loss → Correct and confident prediction.
- Large Loss → Incorrect or low-confidence prediction.

---

# 6. Mathematical Formula

For one training example,

$$
\boxed{
L
=
-
\sum_{i=1}^{C}
y_i
\log(\hat y_i)
}
$$

where

- \(C\) = Number of Classes
- \(y_i\) = Actual Label (One-Hot Encoded)
- \(\hat y_i\) = Predicted Probability for Class \(i\)

---

# Understanding the Formula

The formula consists of four steps.

### Step 1

Take the predicted probability for every class.

---

### Step 2

Take the logarithm.

$$
\log(\hat y_i)
$$

---

### Step 3

Multiply by the actual label.

Since One-Hot Encoding contains

- one **1**
- remaining **0's**

only the correct class contributes.

---

### Step 4

Add the values and multiply by **−1**.

This gives the final loss.

---

# 7. Why Does Only the Correct Class Matter?

Suppose

Actual Class

```text
Dog
```

One-Hot Encoding

```text
[0,1,0]
```

Prediction

```text
[0.10,0.80,0.10]
```

Substitute into the formula.

$$
L
=
-
[
0\log(0.10)
+
1\log(0.80)
+
0\log(0.10)
]
$$

Since

$$
0\times anything = 0
$$

the equation becomes

$$
L
=
-
\log(0.80)
$$

Only the probability assigned to the **correct class** affects the loss.

---

# 8. Numerical Example 1

Suppose

Actual Class

```text
Cat
```

One-Hot Encoding

```text
[1,0,0]
```

Prediction

```text
[0.90,0.08,0.02]
```

Loss

$$
L
=
-
\log(0.90)
$$

Approximate Value

$$
L
\approx
0.105
$$

Small loss because the prediction is highly confident and correct.

---

# 9. Numerical Example 2

Suppose

Actual Class

```text
Cat
```

Prediction

```text
[0.20,0.60,0.20]
```

Loss

$$
L
=
-
\log(0.20)
$$

Approximate Value

$$
L
\approx
1.609
$$

The model assigned a low probability to the correct class.

Therefore,

the loss is much larger.

---

# 10. Behavior of CCE

Suppose the correct class probability changes.

| Correct Class Probability | Loss |
|---------------------------:|-----:|
| 0.99 | Very Small |
| 0.90 | Small |
| 0.70 | Moderate |
| 0.50 | Large |
| 0.20 | Very Large |
| 0.01 | Extremely Large |

Observation

As the probability assigned to the correct class decreases,

the loss increases rapidly.

---

# 11. Relationship with Softmax

Categorical Cross Entropy is almost always used together with the **Softmax Activation Function**.

Training Pipeline

```text
Input

↓

Hidden Layers

↓

Output Layer

↓

Softmax

↓

Probability Distribution

↓

Categorical Cross Entropy

↓

Loss

↓

Backpropagation

↓

Gradient Descent
```

The Softmax function converts the output neurons into a valid probability distribution.

CCE then measures how close this probability distribution is to the true class.

---

# 12. When Should You Use CCE?

Use Categorical Cross Entropy when

- There are more than two classes.
- Each sample belongs to exactly one class.
- Labels are One-Hot Encoded.
- The output layer uses Softmax.

---

# Common Applications

- Image Classification
- Handwritten Digit Recognition (MNIST)
- Animal Classification
- Flower Classification
- Language Identification
- Traffic Sign Recognition

---

# 13. BCE vs CCE

| Feature | BCE | CCE |
|----------|-----|-----|
| Number of Classes | Two | More than Two |
| Output Activation | Sigmoid | Softmax |
| Label Format | 0 or 1 | One-Hot Encoding |
| Typical Applications | Spam Detection | Image Classification |

---

# 14. Interview Questions

## Q1. Why can't BCE be used for multi-class classification?

**Answer**

Because BCE is designed for only **two classes**.

CCE is specifically designed for multiple mutually exclusive classes.

---

## Q2. Which activation function is commonly used with CCE?

**Answer**

Softmax.

---

## Q3. Why is One-Hot Encoding required?

Because CCE compares the predicted probability distribution with the actual probability distribution.

---

## Q4. Which probability contributes to the CCE loss?

Only the probability assigned to the **correct class**.

---

## Q5. What is the minimum possible CCE loss?

$$
\boxed{0}
$$

This occurs when the model predicts the correct class with probability **1**.

---

# Summary

Categorical Cross Entropy (CCE) is the standard loss function for **multi-class classification** problems.

Unlike Binary Cross Entropy, which is limited to two classes, CCE measures the difference between the predicted probability distribution and the actual One-Hot Encoded distribution.

CCE is almost always paired with the **Softmax Activation Function**, making it one of the most important loss functions in modern Deep Learning.

---

# Key Takeaways

✔ CCE is used for multi-class classification.

✔ CCE compares two probability distributions.

✔ Labels must be One-Hot Encoded.

✔ Formula

$$
L
=
-
\sum_{i=1}^{C}
y_i
\log(\hat y_i)
$$

✔ Only the probability of the correct class contributes to the loss.

✔ CCE is almost always used with Softmax.

✔ Lower CCE indicates better model performance.

✔ CCE is widely used in image classification, NLP, speech recognition, and many other Deep Learning applications.
