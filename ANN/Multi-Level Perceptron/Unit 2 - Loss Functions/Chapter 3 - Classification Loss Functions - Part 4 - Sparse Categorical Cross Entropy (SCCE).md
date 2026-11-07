# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 4 – Sparse Categorical Cross Entropy (SCCE)

---

## Learning Objectives

After completing this part, you will be able to:

- Understand why Sparse Categorical Cross Entropy (SCCE) was introduced.
- Understand the difference between One-Hot Encoding and Integer Encoding.
- Learn the SCCE formula.
- Compare SCCE with Categorical Cross Entropy (CCE).
- Understand when to use SCCE.
- Understand why TensorFlow and Keras provide both CCE and SCCE.

---

## 1. Why Was Sparse Categorical Cross Entropy Introduced?

In the previous chapter, we learned that **Categorical Cross Entropy (CCE)** requires **One-Hot Encoded labels**.

### Example

Suppose there are three classes:

| Class | One-Hot Encoding |
|---|---|
| Cat | `[1, 0, 0]` |
| Dog | `[0, 1, 0]` |
| Horse | `[0, 0, 1]` |

This works well when the number of classes is small.

However, suppose there are:

```text
1000 classes
```

Then every label becomes a vector containing 1000 elements.

Example:

```text
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ...]
```

Most of these values are zeros.

This leads to:

- Higher memory usage.
- Larger label representations.
- Additional preprocessing.

To avoid explicitly storing these large One-Hot vectors, **Sparse Categorical Cross Entropy (SCCE)** can be used.

---

## 2. Integer Encoding

Instead of storing an entire One-Hot vector, we simply store the **class index**.

### Example

| Class | Integer Label |
|---|---:|
| Cat | 0 |
| Dog | 1 |
| Horse | 2 |

Instead of storing:

```text
[0, 1, 0]
```

We simply store:

```text
1
```

This is called **Integer Encoding**.

The integer represents the index of the correct class.

---

## 3. What Is Sparse Categorical Cross Entropy (SCCE)?

### Definition

Sparse Categorical Cross Entropy (SCCE) is a classification loss function that computes the same mathematical loss as **Categorical Cross Entropy (CCE)** but accepts **integer labels** instead of **One-Hot Encoded labels**.

The framework uses the integer label to identify the probability corresponding to the correct class.

---

## 4. Example

Suppose we have three classes:

```text
Cat
Dog
Horse
```

The model predicts the following probabilities:

```text
[0.10, 0.80, 0.10]
```

### Using CCE

Actual Label:

```text
[0, 1, 0]
```

### Using SCCE

Actual Label:

```text
1
```

Notice that the predicted probabilities remain exactly the same.

Only the representation of the actual label changes.

---

## 5. Mathematical Formula

Conceptually, Sparse Categorical Cross Entropy computes:

$$
\boxed{
L = -\log(\hat{y}_{\text{correct class}})
}
$$

Where:

- $\hat{y}_{\text{correct class}}$ = Predicted probability of the correct class.

For a dataset containing $N$ samples, the average SCCE loss is:

$$
\boxed{
L = -\frac{1}{N}
\sum_{i=1}^{N}
\log(\hat{y}_{i,y_i})
}
$$

Here:

- $N$ = Number of samples.
- $y_i$ = Integer label of the correct class for sample $i$.
- $\hat{y}_{i,y_i}$ = Predicted probability assigned to the correct class.

This is mathematically equivalent to Categorical Cross Entropy when the labels represent the same classes.

The difference lies in the representation of the labels.

---

## 6. Understanding the Formula

Suppose the model predicts:

```text
Cat    → 0.10
Dog    → 0.80
Horse  → 0.10
```

Actual Label:

```text
Dog
```

Integer Label:

```text
1
```

The framework identifies the probability at index `1`:

```text
0.80
```

Therefore:

$$
L = -\log(0.80)
$$

No explicit One-Hot Encoding is required.

---

## 7. Numerical Example

### Given

Predicted Probabilities:

```text
Cat    → 0.10
Dog    → 0.80
Horse  → 0.10
```

Actual Class:

```text
Dog
```

Integer Label:

```text
1
```

### Step 1 – Identify the Correct Class Probability

Since the correct class index is `1`, select:

$$
\hat{y}_{\text{correct class}} = 0.80
$$

### Step 2 – Apply the SCCE Formula

$$
L = -\log(0.80)
$$

### Step 3 – Calculate the Loss

Using the natural logarithm:

$$
L \approx 0.2231
$$

**Final Loss:**

$$
\boxed{L \approx 0.2231}
$$

This is exactly the same loss obtained using CCE with the equivalent One-Hot Encoded label.

---

## 8. Why Do CCE and SCCE Produce the Same Loss?

Suppose the model predicts:

```text
[0.10, 0.80, 0.10]
```

### Using CCE

Actual Label:

```text
[0, 1, 0]
```

The CCE formula is:

$$
L = -\sum_{i=1}^{C} y_i\log(\hat{y}_i)
$$

Substituting the values:

$$
L = -[
0\log(0.10)
+
1\log(0.80)
+
0\log(0.10)
]
$$

Therefore:

$$
L = -\log(0.80)
$$

### Using SCCE

Actual Label:

```text
1
```

The framework directly selects the probability of class index `1`.

Therefore:

$$
L = -\log(0.80)
$$

Hence:

$$
\boxed{
L_{\text{CCE}} = L_{\text{SCCE}}
}
$$

Both methods produce the same mathematical loss.

The only difference is how the labels are represented.

---

## 9. CCE vs SCCE

| Feature | CCE | SCCE |
|---|---|---|
| Full Name | Categorical Cross Entropy | Sparse Categorical Cross Entropy |
| Label Format | One-Hot Encoding | Integer Labels |
| Prediction Format | Probability Distribution | Probability Distribution |
| Activation Function | Softmax | Softmax |
| Loss Formula | Same | Same |
| Label Storage | One-Hot Vector | Integer Index |
| Memory Usage for Labels | Higher | Lower |
| Dataset Preparation | Requires One-Hot Encoding | No One-Hot Encoding Required |

---

## 10. Advantages of SCCE

- No One-Hot Encoding is required.
- Lower memory usage for label storage.
- Simpler dataset preparation.
- Less preprocessing.
- Convenient for datasets containing a large number of classes.
- Useful when labels are already stored as integer class indices.

---

## 11. Disadvantages of SCCE

- Requires labels to be represented as integer class indices.
- Not suitable for directly representing soft labels or probability distributions as target values.
- The integer labels must correspond to valid class indices.

---

## 12. When Should You Use SCCE?

Use Sparse Categorical Cross Entropy when:

- There are more than two classes.
- Labels are stored as integers.
- The output layer produces a Softmax probability distribution.
- You want to avoid One-Hot Encoding.

### Common Applications

- Image Classification.
- Face Recognition.
- Handwritten Digit Recognition (MNIST).
- Language Identification.
- Speech Recognition.
- Object Classification.

---

## 13. Deep Learning Pipeline Using SCCE

```text
Input
  |
  v
Hidden Layers
  |
  v
Output Layer
  |
  v
Softmax
  |
  v
Probability Distribution
  |
  v
Sparse Categorical Cross Entropy
  |
  v
Loss
  |
  v
Backpropagation
  |
  v
Gradient Descent
  |
  v
Updated Weights
```

The objective is to minimize the SCCE loss during training.

---

## 14. TensorFlow / Keras Example

### Using Categorical Cross Entropy

```python
import tensorflow as tf

loss = tf.keras.losses.CategoricalCrossentropy()
```

This requires One-Hot Encoded labels:

```python
y_true = [0, 1, 0]
```

### Using Sparse Categorical Cross Entropy

```python
import tensorflow as tf

loss = tf.keras.losses.SparseCategoricalCrossentropy()
```

This requires integer labels:

```python
y_true = 1
```

Both compute the same mathematical loss when the target representations are equivalent.

**Important:** By default, these loss functions expect probability predictions. If the model outputs raw logits instead of Softmax probabilities, configure the loss with `from_logits=True` and do not apply Softmax separately before passing the predictions to the loss function.

---

## 15. Interview Questions

### Q1. What is the main difference between CCE and SCCE?

**Answer:**

CCE requires One-Hot Encoded labels, whereas SCCE uses integer class labels.

For example:

```text
CCE  → [0, 1, 0]

SCCE → 1
```

Both calculate the same mathematical loss when the labels represent the same class.

### Q2. Do CCE and SCCE produce different loss values?

**Answer:**

No.

They compute the same mathematical loss when equivalent target representations and predictions are used.

Only the label representation differs.

### Q3. Which activation function is commonly used with SCCE?

**Answer:**

Softmax is commonly used in the output layer for multi-class classification with SCCE.

### Q4. Why is SCCE more memory efficient?

**Answer:**

Because it stores a single integer class index instead of an entire One-Hot Encoded vector.

For example:

```text
One-Hot Encoding → [0, 1, 0, 0, 0]

Integer Encoding → 1
```

### Q5. When should SCCE be preferred?

**Answer:**

SCCE should be preferred when:

- The problem involves multi-class classification.
- Labels are already stored as integer class indices.
- One-Hot Encoding is unnecessary.

### Q6. Can SCCE be used with soft labels?

**Answer:**

SCCE expects integer class indices rather than target probability distributions.

If the target is a probability distribution or soft label, Categorical Cross Entropy is generally the appropriate choice.

---

## 16. Summary

Sparse Categorical Cross Entropy (SCCE) is a variant of Categorical Cross Entropy (CCE).

Instead of requiring One-Hot Encoded labels, it directly accepts integer class labels.

The mathematical loss remains the same as CCE when both use equivalent target representations.

However, SCCE reduces label storage requirements and eliminates the need for One-Hot Encoding.

This is why modern Deep Learning frameworks such as TensorFlow and Keras provide both:

- `CategoricalCrossentropy`
- `SparseCategoricalCrossentropy`

---

## 17. Key Takeaways

- SCCE is used for multi-class classification.
- SCCE accepts integer labels instead of One-Hot Encoded vectors.
- SCCE produces the same mathematical loss as CCE for equivalent targets.
- Softmax is commonly used with SCCE.
- SCCE reduces memory usage for label storage.
- No One-Hot Encoding is required.
- SCCE is preferred when labels are stored as integer class indices.
- TensorFlow and Keras provide dedicated support for SCCE.

---

## Next Part

**Part 5 – Classification Loss Functions: Practical Implementation**

Continue exploring how classification loss functions are implemented and used during neural network training.
