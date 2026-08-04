# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 5 – Complete Comparison of BCE, CCE, and SCCE

---

# Learning Objectives

After completing this part, you will be able to:

- Compare Binary Cross Entropy (BCE), Categorical Cross Entropy (CCE), and Sparse Categorical Cross Entropy (SCCE).
- Understand when each loss function should be used.
- Understand the relationship between activation functions and loss functions.
- Understand different label formats.
- Choose the correct loss function for any classification problem.
- Answer interview questions confidently.

---

# 1. Why Do We Need Different Classification Loss Functions?

Not all classification problems are the same.

Some problems contain

- only **two classes**,

while others contain

- **multiple classes**.

Similarly,

some datasets store labels as

- One-Hot Encoded vectors,

while others store labels as

- Integer class labels.

Therefore,

Deep Learning provides different loss functions for different situations.

---

# 2. Binary Cross Entropy (BCE)

## Purpose

Used for

```text
Binary Classification
```

There are exactly **two classes**.

Examples

- Spam / Not Spam
- Disease / Healthy
- Fraud / Not Fraud
- Positive / Negative Review

---

## Activation Function

```text
Sigmoid
```

---

## Label Format

```text
0

or

1
```

---

## Output Example

```text
0.92
```

Meaning

```text
92% probability of Class 1
```

---

## Formula

$$
L = - \left[ y\log(\hat y) + (1-y)\log(1-\hat y) \right]
$$

---

# 3. Categorical Cross Entropy (CCE)

## Purpose

Used for

```text
Multi-Class Classification
```

There are more than two classes.

Examples

- Cat
- Dog
- Horse

---

## Activation Function

```text
Softmax
```

---

## Label Format

One-Hot Encoding

Example

```text
Dog

↓

[0,1,0]
```

---

## Output Example

```text
[0.10,0.80,0.10]
```

---

## Formula

$$
L = - \sum_{i=1}^{C} y_i \log(\hat y_i)
$$

---

# 4. Sparse Categorical Cross Entropy (SCCE)

## Purpose

Used for

```text
Multi-Class Classification
```

---

## Activation Function

```text
Softmax
```

---

## Label Format

Integer Labels

Example

```text
Dog

↓

1
```

---

## Output Example

```text
[0.10,0.80,0.10]
```

---

## Formula

Conceptually,

$$
L = - \log(\hat y_{\text{correct class}})
$$

Mathematically,

it produces the same loss as CCE.

---

# 5. Complete Comparison Table

| Feature | BCE | CCE | SCCE |
|----------|-----|------|------|
| Full Name | Binary Cross Entropy | Categorical Cross Entropy | Sparse Categorical Cross Entropy |
| Classification Type | Binary | Multi-Class | Multi-Class |
| Number of Classes | 2 | More than 2 | More than 2 |
| Output Activation | Sigmoid | Softmax | Softmax |
| Label Format | 0 or 1 | One-Hot Encoding | Integer Labels |
| Prediction Format | Single Probability | Probability Distribution | Probability Distribution |
| Output Example | 0.95 | [0.1,0.8,0.1] | [0.1,0.8,0.1] |
| Loss Formula | BCE Formula | CCE Formula | Same as CCE |
| Memory Usage | Low | Higher | Lower |
| One-Hot Encoding Required | No | Yes | No |
| Typical Applications | Binary Problems | Multi-Class Problems | Multi-Class Problems |

---

# 6. Activation Function Relationship

Every classification loss function is paired with a specific activation function.

| Activation Function | Loss Function |
|---------------------|---------------|
| Sigmoid | Binary Cross Entropy (BCE) |
| Softmax | Categorical Cross Entropy (CCE) |
| Softmax | Sparse Categorical Cross Entropy (SCCE) |

---

# 7. Label Representation

## BCE

Actual Labels

```text
0

or

1
```

---

## CCE

Actual Labels

```text
Cat

↓

[1,0,0]
```

---

## SCCE

Actual Labels

```text
Cat

↓

0
```

---

# 8. Example Comparison

Suppose there are three classes.

```text
Cat

Dog

Horse
```

Predicted Probabilities

```text
[0.10,0.80,0.10]
```

---

## Using BCE

Cannot be used.

Reason

BCE supports only **binary classification**.

---

## Using CCE

Actual Label

```text
[0,1,0]
```

Loss

$$
L = - \log(0.80)
$$

---

## Using SCCE

Actual Label

```text
1
```

Loss

$$
L = - \log(0.80)
$$

Notice

Both CCE and SCCE produce exactly the same loss.

Only the label representation changes.

---

# 9. Memory Comparison

Suppose there are

```text
1000 classes
```

---

## Using CCE

Each label becomes

```text
[0,0,0,0,0,0,1,0,0,0,...]
```

Length

```text
1000
```

Memory usage is higher.

---

## Using SCCE

Each label becomes

```text
6
```

Only one integer is stored.

Memory usage is much lower.

---

# 10. Decision Tree

```text
Classification Problem

↓

How many classes?

↓

Exactly Two?

├── Yes

│

│   ↓

│ Sigmoid

│

│   ↓

│ Binary Cross Entropy (BCE)

│

└── No

      ↓

   Softmax

      ↓

Labels One-Hot Encoded?

      │

      ├── Yes

      │

      │  ↓

      │ Categorical Cross Entropy (CCE)

      │

      └── No

            ↓

 Sparse Categorical Cross Entropy (SCCE)
```

---

# 11. TensorFlow / Keras Examples

## Binary Classification

```python
model.compile(
    loss="binary_crossentropy"
)
```

---

## Multi-Class with One-Hot Labels

```python
model.compile(
    loss="categorical_crossentropy"
)
```

---

## Multi-Class with Integer Labels

```python
model.compile(
    loss="sparse_categorical_crossentropy"
)
```

---

# 12. Real-World Applications

| Application | Recommended Loss Function |
|--------------|--------------------------|
| Spam Detection | BCE |
| Disease Detection | BCE |
| Fraud Detection | BCE |
| Sentiment Analysis (Positive/Negative) | BCE |
| Animal Classification | CCE / SCCE |
| Flower Classification | CCE / SCCE |
| MNIST Digit Recognition | SCCE |
| Face Recognition | SCCE |
| ImageNet Classification | SCCE |

---

# 13. Interview Questions

## Q1. Which loss function is used for binary classification?

**Answer**

Binary Cross Entropy (BCE).

---

## Q2. Which loss function is used for multi-class classification?

**Answer**

Categorical Cross Entropy (CCE) or Sparse Categorical Cross Entropy (SCCE).

---

## Q3. What is the main difference between CCE and SCCE?

**Answer**

CCE requires **One-Hot Encoded labels**,

whereas SCCE uses **integer labels**.

---

## Q4. Which activation function is used with BCE?

**Answer**

Sigmoid.

---

## Q5. Which activation function is used with CCE and SCCE?

**Answer**

Softmax.

---

## Q6. Which loss function is more memory efficient?

**Answer**

Sparse Categorical Cross Entropy (SCCE),

because it stores only an integer instead of an entire One-Hot vector.

---

## Q7. Do CCE and SCCE compute different mathematical losses?

**Answer**

No.

They compute exactly the same mathematical loss.

Only the label representation differs.

---

# Summary

Binary Cross Entropy (BCE), Categorical Cross Entropy (CCE), and Sparse Categorical Cross Entropy (SCCE) are the three primary classification loss functions used in Deep Learning.

- **Binary Cross Entropy (BCE)** is designed for binary classification and works with the **Sigmoid activation function**.
- **Categorical Cross Entropy (CCE)** is designed for multi-class classification using **One-Hot Encoded labels** and **Softmax**.
- **Sparse Categorical Cross Entropy (SCCE)** is mathematically identical to CCE but accepts **integer class labels**, making it more memory efficient.

Choosing the correct loss function depends on

- the number of classes,
- the label representation,
- and the activation function used in the output layer.

---

# Key Takeaways

✔ BCE is used for binary classification.

✔ CCE is used for multi-class classification with One-Hot Encoded labels.

✔ SCCE is used for multi-class classification with integer labels.

✔ BCE works with Sigmoid.

✔ CCE and SCCE work with Softmax.

✔ CCE and SCCE compute the same mathematical loss.

✔ SCCE is more memory efficient because it avoids One-Hot Encoding.

✔ Selecting the correct loss function depends on the problem type and label format.
