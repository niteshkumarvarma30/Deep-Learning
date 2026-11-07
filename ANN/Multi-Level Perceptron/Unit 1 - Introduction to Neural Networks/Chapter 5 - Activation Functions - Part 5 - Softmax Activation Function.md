# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 5 – Softmax Activation Function

---

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the Softmax activation function.
- Explain the mathematical formula of Softmax.
- Differentiate between binary classification (Sigmoid) and multi-class classification (Softmax).
- Understand why Softmax is commonly applied in the output layer rather than hidden layers.

---

## 1. Introduction

So far, we have discussed activation functions that are applied to individual neurons independently, such as Sigmoid, Tanh, and ReLU.

These functions are useful in hidden layers and for binary classification, where we often need to predict a single probability.

But what if we are building a neural network to classify an image into one of 10 different categories, such as recognizing handwritten digits from 0 to 9?

Suppose the network has three output neurons representing Dog, Cat, and Bird.

The raw outputs might look like this:

```text
Neuron 1 (Dog):   2.5
Neuron 2 (Cat):   4.1
Neuron 3 (Bird): -1.2
```

These raw scores are called **Logits**.

Logits are difficult to interpret directly because they can be positive, negative, or greater than 1.

We need a function that converts these raw scores into a valid probability distribution.

This is where the **Softmax Activation Function** comes in.

---

## 2. What Is Softmax?

Softmax is an activation function commonly used in the output layer of a neural network for **Multi-Class Classification**.

It takes a vector of raw scores (logits) and converts them into a vector of probabilities.

The resulting probabilities satisfy two important properties:

1. Every probability is between 0 and 1.
2. The sum of all probabilities is exactly 1.

Mathematically:

$$
0 \leq P(y=i) \leq 1
$$

And:

$$
\sum_{i=1}^{K} P(y=i) = 1
$$

Where $K$ represents the total number of classes.

This makes it possible to interpret the network's output as a probability distribution over the available classes.

---

## 3. Mathematical Equation

For a given output node $i$, the Softmax probability is calculated as:

$$
\text{Softmax}(z_i) =
\frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

Where:

- $z_i$ = Raw score (logit) of the current class.
- $e$ = Euler's number (approximately 2.718).
- $K$ = Total number of classes.
- $j$ = Index used to iterate through all classes.
- Denominator = Sum of the exponentials of all logits.

### Understanding the Formula

The formula has two main components:

**Numerator:**

$$
e^{z_i}
$$

Calculates the exponential of the current class's logit.

**Denominator:**

$$
\sum_{j=1}^{K} e^{z_j}
$$

Calculates the sum of the exponentials of all class logits.

Finally, the numerator is divided by the denominator to obtain the probability of the current class.

---

## 4. Numerical Example

Let's calculate Softmax for our previous example.

### Given Raw Scores (Logits)

| Class | Logit |
|---|---:|
| Dog | 2.5 |
| Cat | 4.1 |
| Bird | -1.2 |

We need to convert these three logits into probabilities.

### Step 1: Calculate Exponentials ($e^z$)

Calculate the exponential of each logit:

$$
e^{2.5} \approx 12.18
$$

$$
e^{4.1} \approx 60.34
$$

$$
e^{-1.2} \approx 0.30
$$

The results are:

| Class | Logit ($z$) | Exponential ($e^z$) |
|---|---:|---:|
| Dog | 2.5 | 12.18 |
| Cat | 4.1 | 60.34 |
| Bird | -1.2 | 0.30 |

### Step 2: Calculate the Sum

Add all the exponential values:

$$
S = 12.18 + 60.34 + 0.30
$$

$$
S = 72.82
$$

### Step 3: Calculate Each Probability

Now divide each exponential value by the total sum.

**Probability of Dog:**

$$
P(\text{Dog}) = \frac{12.18}{72.82}
$$

$$
P(\text{Dog}) \approx 0.167 = 16.7\%
$$

**Probability of Cat:**

$$
P(\text{Cat}) = \frac{60.34}{72.82}
$$

$$
P(\text{Cat}) \approx 0.828 = 82.8\%
$$

**Probability of Bird:**

$$
P(\text{Bird}) = \frac{0.30}{72.82}
$$

$$
P(\text{Bird}) \approx 0.004 = 0.4\%
$$

### Step 4: Verify the Probability Distribution

Add all the probabilities:

$$
0.167 + 0.828 + 0.004 \approx 0.999
$$

The slight difference from 1 is due to rounding.

Therefore:

$$
\sum P(\text{Class}) \approx 1
$$

### Final Output

| Class | Probability | Percentage |
|---|---:|---:|
| Dog | 0.167 | 16.7% |
| Cat | 0.828 | 82.8% |
| Bird | 0.004 | 0.4% |
| **Total** | **0.999** | **99.9%** |

<text>The model predicts **Cat** because it has the highest probability, approximately 82.8%.</text>

---

## 5. Why Does Softmax Use the Exponential Function ($e^z$)?

You might wonder:

Why don't we simply divide each raw score by the sum of all raw scores?

Why do we need the exponential function?

There are two important reasons.

### Reason 1: Handling Negative Numbers

Raw scores can be negative.

For example:

$$
z = -1.2
$$

If we directly use raw scores, we may obtain negative values, which cannot represent valid probabilities.

However, the exponential function always produces a positive output:

$$
e^z > 0
$$

For example:

$$
e^{-1.2} \approx 0.30
$$

Therefore, Softmax converts both positive and negative logits into positive values before normalization.

### Reason 2: Exaggerating Differences

The exponential function amplifies differences between logits.

Consider two logits:

$$
z_1 = 2
$$

$$
z_2 = 4
$$

Their exponential values are:

$$
e^2 \approx 7.39
$$

$$
e^4 \approx 54.60
$$

Although the second logit is only twice the first, its exponential value is significantly larger.

This makes higher logits contribute more strongly to the final probability distribution.

As a result, Softmax generally assigns a higher probability to the class with the highest logit.

---

## 6. Softmax vs Sigmoid

Both Sigmoid and Softmax are used to convert neural network outputs into probabilities, but they serve different classification tasks.

| Feature | Sigmoid | Softmax |
|---|---|---|
| Primary use case | Binary classification or independent multi-label predictions | Single-label multi-class classification |
| Output | A probability for each output | A probability distribution across classes |
| Output range | Between 0 and 1 | Each probability is between 0 and 1 |
| Sum of outputs | Not necessarily 1 | Always 1 (mathematically) |
| Relationship between outputs | Independent | Interdependent |
| Typical application | Spam vs Not Spam | Dog vs Cat vs Bird |

### Example: Sigmoid

For binary classification:

```text
Input Image
     |
     v
Neural Network
     |
     v
Sigmoid Output
     |
     v
Probability = 0.85
     |
     v
Prediction = Dog
```

The output represents the probability of the positive class.

### Example: Softmax

For multi-class classification:

```text
Input Image
     |
     v
Neural Network
     |
     v
Three Output Logits
     |
     v
Softmax
     |
     v
Dog = 0.167
Cat = 0.828
Bird = 0.004
     |
     v
Prediction = Cat
```

Softmax produces probabilities that sum to 1 across the mutually exclusive classes.

---

## 7. Why Is Softmax Used in the Output Layer Rather Than Hidden Layers?

Hidden layers are responsible for learning useful features and representations from the input data.

For this purpose, activation functions such as ReLU and its variants are commonly used.

Softmax is generally used in the output layer for multi-class classification because:

1. It converts the final logits into a probability distribution.
2. It makes the output easier to interpret.
3. It allows the model to assign probabilities across mutually exclusive classes.
4. It works naturally with loss functions such as Categorical Cross-Entropy.

Applying Softmax in hidden layers would unnecessarily force intermediate neuron outputs to form a probability distribution that sums to 1.

This is generally not desirable when learning intermediate representations.

---

## 8. Softmax and Categorical Cross-Entropy

Softmax is commonly paired with **Categorical Cross-Entropy** for multi-class classification.

Softmax converts logits into predicted probabilities.

Categorical Cross-Entropy measures how different the predicted probability distribution is from the actual target distribution.

Its mathematical formula is:

$$
L = -\sum_{i=1}^{K} y_i \log(p_i)
$$

Where:

- $K$ = Number of classes.
- $y_i$ = Actual target value for class $i$.
- $p_i$ = Predicted probability for class $i$.

For one-hot encoded labels, the correct class has a target value of 1, while all other classes have a target value of 0.

The loss therefore penalizes the model when it assigns a low probability to the correct class.

---

## 9. Interview Questions

### Q1. When should you use Softmax instead of Sigmoid?

**Answer:**

Sigmoid is commonly used for binary classification, where the network predicts a single probability for the positive class.

Softmax is used for single-label multi-class classification, where the network must choose one class from several mutually exclusive classes.

For example:

- Sigmoid: Spam vs Not Spam.
- Softmax: Dog vs Cat vs Bird.

Softmax converts a vector of logits into a probability distribution whose values sum to 1.

### Q2. Why does the Softmax formula use the exponential function?

**Answer:**

The exponential function converts all logits, including negative values, into strictly positive numbers.

This is necessary for constructing a valid probability distribution.

It also amplifies differences between logits, making higher scores contribute more strongly to the final probability distribution.

### Q3. Why must Softmax probabilities sum to 1?

**Answer:**

Softmax represents a probability distribution over mutually exclusive classes.

The sum of the probabilities must equal 1 because the model distributes the total probability across all possible classes.

Mathematically:

$$
\sum_{i=1}^{K} P(y=i) = 1
$$

### Q4. What are logits?

**Answer:**

Logits are the raw, unnormalized scores produced by the final linear layer of a neural network before applying Softmax.

They can be positive, negative, or zero.

Softmax converts these raw scores into normalized probabilities.

### Q5. Can Softmax be used for multi-label classification?

**Answer:**

Softmax is generally not appropriate for multi-label classification because it forces the probabilities across classes to sum to 1.

In multi-label classification, multiple classes can be correct simultaneously.

Therefore, independent Sigmoid outputs are commonly used instead.

---

## 10. Summary

Softmax is a standard output activation function for single-label multi-class classification.

It converts raw logits into a probability distribution, making neural network predictions easier to interpret.

Its key properties are:

- Every output probability is between 0 and 1.
- The sum of all output probabilities equals 1.
- It handles negative logits using the exponential function.
- It emphasizes differences between class scores.
- It is commonly paired with Categorical Cross-Entropy.

---

## 11. Key Takeaways

- Softmax is commonly used in the output layer for multi-class classification.
- It converts raw logits into probabilities.
- Every probability lies between 0 and 1.
- The sum of all Softmax probabilities equals 1.
- The exponential function ensures positive values and amplifies differences between logits.
- Sigmoid is commonly used for binary classification and multi-label classification.
- Softmax is commonly paired with Categorical Cross-Entropy.
- The class with the highest Softmax probability is selected as the predicted class.

---

## Chapter 5 – Activation Functions: Completed

You have now covered the following activation functions and concepts:

1. Sigmoid Activation Function
2. Tanh Activation Function
3. ReLU and Its Variants
4. The Dying ReLU Problem
5. Softmax Activation Function

**Next:** Continue to the next chapter of Unit 1 – Introduction to Neural Networks.
