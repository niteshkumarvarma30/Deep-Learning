# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 4 – Sparse Categorical Cross Entropy (SCCE)

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Sparse Categorical Cross Entropy (SCCE) was introduced.
- Understand the difference between One-Hot Encoding and Integer Encoding.
- Learn the SCCE formula.
- Compare SCCE with Categorical Cross Entropy (CCE).
- Know when to use SCCE.
- Understand why TensorFlow and Keras provide both CCE and SCCE.

---

# 1. Why Was Sparse Categorical Cross Entropy Introduced?

In the previous chapter, we learned that **Categorical Cross Entropy (CCE)** requires **One-Hot Encoded labels**.

Example

Suppose there are three classes.

| Class | One-Hot Encoding |
|--------|------------------|
| Cat | [1,0,0] |
| Dog | [0,1,0] |
| Horse | [0,0,1] |

This works well for a small number of classes.

However,

suppose there are

```text
1000 classes
```

Then every label becomes a vector containing **1000 elements**.

Example

```text
[0,0,0,0,0,0,1,0,0,0,0,...]
```

Most of these values are zeros.

This leads to

- Higher memory usage.
- Larger datasets.
- Extra preprocessing.

To solve this problem,

Sparse Categorical Cross Entropy (SCCE) was introduced.

---

# 2. Integer Encoding

Instead of storing an entire One-Hot vector,

we simply store the **class index**.

Example

| Class | Integer Label |
|--------|--------------:|
| Cat | 0 |
| Dog | 1 |
| Horse | 2 |

Instead of

```text
[0,1,0]
```

we simply write

```text
1
```

This is called **Integer Encoding**.

---

# 3. What is Sparse Categorical Cross Entropy (SCCE)?

## Definition

Sparse Categorical Cross Entropy (SCCE) is the same loss function as **Categorical Cross Entropy (CCE)**,

but it accepts **integer labels** instead of **One-Hot Encoded labels**.

Internally,

the framework automatically identifies the correct class using the integer label.

---

# 4. Example

Suppose

Classes

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

## Using CCE

Actual Label

```text
[0,1,0]
```

---

## Using SCCE

Actual Label

```text
1
```

Notice

The predicted probabilities remain exactly the same.

Only the label representation changes.

---

# 5. Mathematical Formula

Conceptually,

Sparse Categorical Cross Entropy computes

$$
\boxed{ L = -\log(\hat{y}_{\text{correct class}}) }
$$

where

- \(\hat{y}_{\text{correct class}}\) = Predicted probability of the correct class.

Internally,

this is mathematically equivalent to CCE.

The difference lies only in the representation of the labels.

---

# 6. Understanding the Formula

Suppose

Prediction

```text
Cat    → 0.10

Dog    → 0.80

Horse  → 0.10
```

Actual Label

```text
Dog
```

Integer Label

```text
1
```

The framework automatically selects

```text
0.80
```

because the correct class index is **1**.

Therefore,

$$
L = - \log(0.80)
$$

No One-Hot Encoding is required.

---

# 7. Numerical Example

Prediction

```text
Cat    → 0.10

Dog    → 0.80

Horse  → 0.10
```

Actual Label

```text
Dog
```

Integer Label

```text
1
```

Loss

$$
L = - \log(0.80)
$$

Approximate Value

$$
L \approx 0.223
$$

This is exactly the same loss obtained using CCE.

---

# 8. Why Do CCE and SCCE Produce the Same Loss?

Suppose

Prediction

```text
[0.10,0.80,0.10]
```

---

## CCE

Actual Label

```text
[0,1,0]
```

Only the second probability contributes.

Loss

$$
- \log(0.80)
$$

---

## SCCE

Actual Label

```text
1
```

The framework directly selects the second probability.

Loss

$$
- \log(0.80)
$$

Therefore,

both methods produce the **same mathematical loss**.

The only difference is how the labels are stored.

---

# 9. CCE vs SCCE

| Feature | CCE | SCCE |
|----------|-----|------|
| Label Format | One-Hot Encoding | Integer Labels |
| Prediction Format | Probability Distribution | Probability Distribution |
| Activation Function | Softmax | Softmax |
| Loss Formula | Same | Same |
| Memory Usage | Higher | Lower |
| Dataset Preparation | Requires One-Hot Encoding | No Encoding Required |

---

# 10. Advantages of SCCE

- No One-Hot Encoding required.
- Lower memory usage.
- Simpler dataset preparation.
- Faster preprocessing.
- Better suited for datasets with a large number of classes.
- Preferred in TensorFlow/Keras when labels are already integers.

---

# 11. Disadvantages of SCCE

- Only works when labels are stored as integer class indices.
- Cannot be used if the dataset already contains probability distributions (soft labels).

---

# 12. When Should You Use SCCE?

Use Sparse Categorical Cross Entropy when

- There are more than two classes.
- Labels are stored as integers.
- The output layer uses Softmax.
- You want to avoid One-Hot Encoding.

---

# Common Applications

- Image Classification
- Face Recognition
- Handwritten Digit Recognition (MNIST)
- Language Identification
- Speech Recognition
- Object Classification

---

# 13. Deep Learning Pipeline Using SCCE

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

Sparse Categorical Cross Entropy

↓

Loss

↓

Backpropagation

↓

Gradient Descent

↓

Updated Weights
```

---

# 14. TensorFlow Example

Using **Categorical Cross Entropy**

```python
loss = tf.keras.losses.CategoricalCrossentropy()
```

Requires

```python
y_true = [0,1,0]
```

---

Using **Sparse Categorical Cross Entropy**

```python
loss = tf.keras.losses.SparseCategoricalCrossentropy()
```

Requires

```python
y_true = 1
```

Both compute the same mathematical loss.

---

# Interview Questions

## Q1. What is the main difference between CCE and SCCE?

**Answer**

CCE requires **One-Hot Encoded labels**,

whereas SCCE uses **integer labels**.

---

## Q2. Do CCE and SCCE produce different loss values?

**Answer**

No.

They compute exactly the same mathematical loss.

Only the label representation differs.

---

## Q3. Which activation function is used with SCCE?

**Answer**

Softmax.

---

## Q4. Why is SCCE more memory efficient?

**Answer**

Because it stores only one integer instead of an entire One-Hot vector.

---

## Q5. When should SCCE be preferred?

**Answer**

When labels are already stored as integer class indices and One-Hot Encoding is unnecessary.

---

# Summary

Sparse Categorical Cross Entropy (SCCE) is a variant of Categorical Cross Entropy (CCE).

Instead of requiring One-Hot Encoded labels,

it directly accepts integer class labels.

The mathematical loss remains exactly the same as CCE,

but SCCE reduces memory usage and eliminates the need for One-Hot Encoding.

This is why modern Deep Learning frameworks such as TensorFlow and Keras provide both **CategoricalCrossentropy** and **SparseCategoricalCrossentropy**.

---

# Key Takeaways

✔ SCCE is used for multi-class classification.

✔ SCCE accepts integer labels instead of One-Hot vectors.

✔ SCCE produces exactly the same loss as CCE.

✔ Softmax is used with SCCE.

✔ SCCE reduces memory usage.

✔ No One-Hot Encoding is required.

✔ SCCE is preferred when labels are stored as integer class indices.

✔ TensorFlow and Keras provide dedicated support for SCCE.
