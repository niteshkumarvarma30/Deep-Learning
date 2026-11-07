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

# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 4.1 – Sparse Categorical Cross Entropy (SCCE): Dataset and Numerical Example

---

## Learning Objectives

After completing this lesson, you will be able to:

- Understand SCCE using a practical classification dataset.
- Understand how integer labels map to class indices.
- Interpret Softmax probability predictions.
- Calculate SCCE for individual training examples.
- Calculate the average SCCE loss for an entire dataset.
- Implement SCCE using Python and NumPy.
- Understand how SCCE is used during neural network training.

---

## 1. Introduction – Building an Animal Classifier

Let's understand Sparse Categorical Cross Entropy (SCCE) using a practical example.

Suppose we are building a neural network that classifies images into four animal categories:

| Class Index | Animal |
|---:|---|
| 0 | Cat |
| 1 | Dog |
| 2 | Horse |
| 3 | Elephant |

Our neural network receives an animal image and predicts the probability that the image belongs to each class.

For example:

```text
Input Image
     |
     v
Neural Network
     |
     v
Softmax Activation
     |
     v
[0.05, 0.15, 0.20, 0.60]
     |
     v
Predicted Class: Elephant
```

The objective is to compare the predicted probabilities with the actual class labels using SCCE.

---

## 2. Create a Small Dataset

Suppose we have five training images.

| Image ID | Actual Animal | Integer Label |
|---|---|---:|
| Image 1 | Cat | 0 |
| Image 2 | Dog | 1 |
| Image 3 | Horse | 2 |
| Image 4 | Elephant | 3 |
| Image 5 | Dog | 1 |

Our actual labels are:

```python
y_true = [0, 1, 2, 3, 1]
```

Notice that we store the actual class as an integer instead of a One-Hot Encoded vector.

For example:

```text
One-Hot Encoding:

Dog = [0, 1, 0, 0]

Integer Encoding:

Dog = 1
```

This is why we use Sparse Categorical Cross Entropy.

---

## 3. Neural Network Predictions

Suppose our trained neural network produces the following probability distributions after applying Softmax.

| Image | Cat (0) | Dog (1) | Horse (2) | Elephant (3) |
|---|---:|---:|---:|---:|
| Image 1 | 0.80 | 0.10 | 0.05 | 0.05 |
| Image 2 | 0.10 | 0.70 | 0.10 | 0.10 |
| Image 3 | 0.10 | 0.20 | 0.60 | 0.10 |
| Image 4 | 0.05 | 0.15 | 0.20 | 0.60 |
| Image 5 | 0.40 | 0.30 | 0.20 | 0.10 |

These are the model's predictions.

Each row represents the probability distribution for one image.

For example, Image 1 has:

```python
[0.80, 0.10, 0.05, 0.05]
```

The model predicts:

- Cat: 80%
- Dog: 10%
- Horse: 5%
- Elephant: 5%

Each row sums to 1.

---

## 4. Mathematical Formula of SCCE

For one training example:

$$
\boxed{
L = -\log(\hat{y}_{\text{correct class}})
}
$$

Where:

- $L$ = Loss value.
- $\hat{y}_{\text{correct class}}$ = Predicted probability of the actual class.
- $\log$ = Natural logarithm.

For a dataset containing $N$ training examples, the average SCCE loss is:

$$
\boxed{
L_{\text{average}} =
-\frac{1}{N}
\sum_{i=1}^{N}
\log(\hat{y}_{i,y_i})
}
$$

The important idea is:

**Select the probability of the correct class using the integer label, then calculate its negative logarithm.**

---

## 5. Calculate SCCE for Each Training Example

Let's calculate the loss for all five images.

### Example 1 – Actual Label = 0 (Cat)

Predicted probabilities:

```python
[0.80, 0.10, 0.05, 0.05]
```

Actual label:

```python
y_true = 0
```

Since the actual label is `0`, select the probability at index `0`.

$$
\hat{y}_{\text{correct class}} = 0.80
$$

Apply the SCCE formula:

$$
L_1 = -\log(0.80)
$$

$$
\boxed{L_1 = 0.2231}
$$

### Example 2 – Actual Label = 1 (Dog)

Predicted probabilities:

```python
[0.10, 0.70, 0.10, 0.10]
```

Actual label:

```python
y_true = 1
```

Since the actual label is `1`, select the probability at index `1`.

$$
\hat{y}_{\text{correct class}} = 0.70
$$

Apply the SCCE formula:

$$
L_2 = -\log(0.70)
$$

$$
\boxed{L_2 = 0.3567}
$$

### Example 3 – Actual Label = 2 (Horse)

Predicted probabilities:

```python
[0.10, 0.20, 0.60, 0.10]
```

Actual label:

```python
y_true = 2
```

Since the actual label is `2`, select the probability at index `2`.

$$
\hat{y}_{\text{correct class}} = 0.60
$$

Apply the SCCE formula:

$$
L_3 = -\log(0.60)
$$

$$
\boxed{L_3 = 0.5108}
$$

### Example 4 – Actual Label = 3 (Elephant)

Predicted probabilities:

```python
[0.05, 0.15, 0.20, 0.60]
```

Actual label:

```python
y_true = 3
```

Since the actual label is `3`, select the probability at index `3`.

Remember that Python uses zero-based indexing.

Therefore, index `3` represents the fourth element.

$$
\hat{y}_{\text{correct class}} = 0.60
$$

Apply the SCCE formula:

$$
L_4 = -\log(0.60)
$$

$$
\boxed{L_4 = 0.5108}
$$

### Example 5 – Actual Label = 1 (Dog)

Predicted probabilities:

```python
[0.40, 0.30, 0.20, 0.10]
```

Actual label:

```python
y_true = 1
```

Since the actual label is `1`, select the probability at index `1`.

$$
\hat{y}_{\text{correct class}} = 0.30
$$

Apply the SCCE formula:

$$
L_5 = -\log(0.30)
$$

$$
\boxed{L_5 = 1.2040}
$$

---

## 6. Summary of Individual Losses

We have calculated the SCCE loss for all five images.

| Image | Actual Label | Correct Class Probability | SCCE Loss |
|---|---:|---:|---:|
| Image 1 | 0 | 0.80 | 0.2231 |
| Image 2 | 1 | 0.70 | 0.3567 |
| Image 3 | 2 | 0.60 | 0.5108 |
| Image 4 | 3 | 0.60 | 0.5108 |
| Image 5 | 1 | 0.30 | 1.2040 |

Notice that Image 5 has the highest loss.

Why?

Because the actual class is Dog, but the model assigns only 30% probability to Dog.

The model is less confident about the correct class.

---

## 7. Calculate the Average Dataset Loss

During training, we generally calculate the average loss across a batch of training examples.

The formula is:

$$
L_{\text{average}} =
\frac{L_1+L_2+L_3+L_4+L_5}{5}
$$

Substitute the calculated values:

$$
L_{\text{average}} =
\frac{
0.2231+0.3567+0.5108+0.5108+1.2040
}{5}
$$

$$
L_{\text{average}} =
\frac{2.8054}{5}
$$

$$
\boxed{
L_{\text{average}} \approx 0.5611
}
$$

This is the average SCCE loss for our five training examples.

---

## 8. Understanding the Effect of Prediction Probability

One of the most important properties of SCCE is:

- Higher probability for the correct class produces lower loss.
- Lower probability for the correct class produces higher loss.

Let's understand this with an example.

Suppose the actual class is Dog.

Actual integer label:

```python
y_true = 1
```

Now consider three different predictions.

### Case 1 – High Confidence

```python
y_pred = [0.05, 0.90, 0.03, 0.02]
```

Correct class probability:

$$
P(\text{Dog}) = 0.90
$$

Loss:

$$
L = -\log(0.90)
$$

$$
\boxed{L = 0.1054}
$$

### Case 2 – Moderate Confidence

```python
y_pred = [0.10, 0.60, 0.20, 0.10]
```

Correct class probability:

$$
P(\text{Dog}) = 0.60
$$

Loss:

$$
L = -\log(0.60)
$$

$$
\boxed{L = 0.5108}
$$

### Case 3 – Low Confidence

```python
y_pred = [0.40, 0.10, 0.30, 0.20]
```

Correct class probability:

$$
P(\text{Dog}) = 0.10
$$

Loss:

$$
L = -\log(0.10)
$$

$$
\boxed{L = 2.3026}
$$

### Comparison

| Correct Class Probability | SCCE Loss |
|---:|---:|
| 0.90 | 0.1054 |
| 0.60 | 0.5108 |
| 0.10 | 2.3026 |

The lower the probability assigned to the correct class, the higher the loss.

---

## 9. Python Implementation Using NumPy

Now let's implement the complete SCCE calculation.

```python
import numpy as np

# Actual integer labels
y_true = np.array([0, 1, 2, 3, 1])

# Predicted probabilities after Softmax
y_pred = np.array([
    [0.80, 0.10, 0.05, 0.05],
    [0.10, 0.70, 0.10, 0.10],
    [0.10, 0.20, 0.60, 0.10],
    [0.05, 0.15, 0.20, 0.60],
    [0.40, 0.30, 0.20, 0.10]
])

# Select the probability of each correct class
correct_probs = y_pred[
    np.arange(len(y_true)),
    y_true
]

# Calculate individual losses
individual_losses = -np.log(correct_probs)

# Calculate average dataset loss
average_loss = np.mean(individual_losses)

print("Correct probabilities:", correct_probs)

print("Individual losses:", individual_losses)

print("Average SCCE Loss:", average_loss)
```

### Output

```text
Correct probabilities:
[0.8 0.7 0.6 0.6 0.3]

Individual losses:
[0.2231 0.3567 0.5108 0.5108 1.2040]

Average SCCE Loss:
0.5611
```

---

## 10. Understanding the NumPy Indexing

One of the most important lines in the implementation is:

```python
correct_probs = y_pred[
    np.arange(len(y_true)),
    y_true
]
```

Let's understand it.

### First: `np.arange(len(y_true))`

Our actual labels are:

```python
y_true = [0, 1, 2, 3, 1]
```

The number of examples is 5.

Therefore:

```python
np.arange(len(y_true))
```

Produces:

```python
[0, 1, 2, 3, 4]
```

These are the row indices.

### Second: `y_true`

The actual labels are:

```python
[0, 1, 2, 3, 1]
```

These are the column indices.

### Third: NumPy Advanced Indexing

NumPy selects the following pairs:

| Row Index | Column Index | Selected Probability |
|---:|---:|---:|
| 0 | 0 | 0.80 |
| 1 | 1 | 0.70 |
| 2 | 2 | 0.60 |
| 3 | 3 | 0.60 |
| 4 | 1 | 0.30 |

Therefore:

```python
correct_probs = [0.80, 0.70, 0.60, 0.60, 0.30]
```

Now we can calculate:

```python
individual_losses = -np.log(correct_probs)
```

This gives the loss for every training example.

---

## 11. TensorFlow / Keras Implementation

TensorFlow provides a built-in implementation of Sparse Categorical Cross Entropy.

```python
import tensorflow as tf

# Actual integer labels
y_true = tf.constant([0, 1, 2, 3, 1])

# Predicted probabilities
y_pred = tf.constant([
    [0.80, 0.10, 0.05, 0.05],
    [0.10, 0.70, 0.10, 0.10],
    [0.10, 0.20, 0.60, 0.10],
    [0.05, 0.15, 0.20, 0.60],
    [0.40, 0.30, 0.20, 0.10]
])

# Create SCCE loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

# Calculate average loss
loss = loss_fn(y_true, y_pred)

print("SCCE Loss:", loss.numpy())
```

Expected output:

```text
SCCE Loss: approximately 0.5611
```

The framework automatically:

1. Reads the integer labels.
2. Identifies the correct class probabilities.
3. Calculates the negative logarithm.
4. Computes the average loss.

**Important:** The example above passes probabilities to the loss function. If your model outputs raw logits, use `from_logits=True` and do not apply Softmax separately before passing the logits to the loss function.

---

## 12. Deep Learning Training Pipeline Using SCCE

The complete training process looks like this:

```text
Input Images
     |
     v
Neural Network
     |
     v
Forward Propagation
     |
     v
Output Layer
     |
     v
Softmax Activation
     |
     v
Predicted Probabilities
     |
     v
Sparse Categorical Cross Entropy
     |
     v
Calculate Loss
     |
     v
Backpropagation
     |
     v
Calculate Gradients
     |
     v
Gradient Descent
     |
     v
Update Weights
     |
     v
Improved Predictions
```

The objective is to minimize the SCCE loss during training.

---

## 13. Interview Questions

### Q1. How do you calculate SCCE for a single example?

**Answer:**

First, identify the actual integer label.

Then select the predicted probability at the corresponding class index.

Finally, calculate the negative natural logarithm:

$$
L = -\log(\hat{y}_{\text{correct class}})
$$

### Q2. Suppose the actual label is 3. Which probability should you select?

**Answer:**

Select the probability at index `3`, which is the fourth element of the prediction array because indexing starts from zero.

For example:

```python
y_pred = [0.05, 0.15, 0.20, 0.60]
y_true = 3
```

Therefore:

$$
L = -\log(0.60)
$$

### Q3. How do you calculate the average SCCE loss for a dataset?

**Answer:**

Calculate the individual loss for each training example and take their arithmetic mean:

$$
L_{\text{average}} =
\frac{1}{N}\sum_{i=1}^{N}L_i
$$

### Q4. Why does a lower probability for the correct class produce a higher loss?

**Answer:**

Because SCCE uses the negative logarithm of the correct class probability.

As the correct class probability decreases, its negative logarithm increases.

Therefore, incorrect or less confident predictions receive higher loss values.

### Q5. Does SCCE require One-Hot Encoding?

**Answer:**

No.

SCCE directly accepts integer class labels.

For example:

```python
y_true = 2
```

The framework automatically identifies the probability at index `2`.

---

## 14. Summary

Sparse Categorical Cross Entropy is used to measure the difference between the predicted probability distribution and the actual class label in multi-class classification.

For each training example:

1. The neural network generates probabilities using Softmax.
2. The actual integer label identifies the correct class.
3. The probability of that class is selected.
4. The negative logarithm is calculated.
5. The individual losses are averaged across the batch.

For our five-example animal classification dataset, the average SCCE loss is:

$$
\boxed{L_{\text{average}} \approx 0.5611}
$$

---

## 15. Key Takeaways

- SCCE is used for multi-class classification.
- Actual labels are stored as integer class indices.
- Softmax generates the predicted probability distribution.
- The integer label identifies the correct class.
- SCCE selects only the probability of the correct class for each example.
- The loss for one example is $-\log(\hat{y}_{\text{correct class}})$.
- Dataset loss is generally calculated by averaging individual losses.
- Higher probability for the correct class produces lower loss.
- Lower probability for the correct class produces higher loss.
- NumPy can calculate SCCE using advanced indexing.
- TensorFlow and Keras provide built-in SCCE implementations.

---

## 16. Practice Exercise

Now solve this example yourself.

Suppose we have four classes:

```text
Class 0 → Cat
Class 1 → Dog
Class 2 → Horse
Class 3 → Elephant
```

The model predicts:

```python
y_pred = [0.10, 0.20, 0.50, 0.20]
```

The actual label is:

```python
y_true = 2
```

Answer the following questions:

1. Which class is the correct class?
2. Which probability should you select?
3. Which SCCE formula should you apply?
4. What is the final loss?

### Solution

The actual label is `2`, so we select the probability at index `2`.

$$
\hat{y}_{\text{correct class}} = 0.50
$$

Apply the formula:

$$
L = -\log(0.50)
$$

$$
\boxed{L \approx 0.6931}
$$

---

## Next Topic

**Part 5 – Practical Implementation of Classification Loss Functions**

Continue exploring how different classification loss functions are implemented and used during neural network training.
