# Unit 1 – Introduction to Neural Networks

# Chapter 5 – Activation Functions

## Part 5 – Softmax Activation Function

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the Softmax activation function.
- Explain the mathematical formula of Softmax.
- Differentiate between binary classification (Sigmoid) and multi-class classification (Softmax).
- Understand why Softmax is applied in the output layer rather than hidden layers.

---

# 1. Introduction

So far, we have discussed activation functions that are applied to individual neurons independently (like Sigmoid, Tanh, and ReLU).

These functions are perfect for hidden layers, or for binary classification where we just need to output a single probability.

But what if we are building a neural network to classify an image into one of 10 different categories (e.g., recognizing handwritten digits 0-9)?

If we just use regular activation functions on the 10 output neurons, their raw outputs might look like this:

```text
Neuron 1 (Dog): 2.5
Neuron 2 (Cat): 4.1
Neuron 3 (Bird): -1.2
```

These raw scores (called **logits**) are hard to interpret. We need a function that can convert these raw scores into a **valid probability distribution**. This is where **Softmax** comes in.

---

# 2. What is Softmax?

Softmax is an activation function used in the output layer of a neural network for **Multi-Class Classification**.

It takes a vector of raw scores (logits) and squashes them into a vector of probabilities, such that:
1. Every probability is between 0 and 1.
2. The sum of all probabilities is exactly 1.0.

---

# 3. Mathematical Equation

For a given output node \( i \), the Softmax probability is calculated as:

$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

Where:
- \( z_i \) is the raw score (logit) of the current class.
- \( e \) is Euler's number (~2.718).
- \( K \) is the total number of classes.
- The denominator is the sum of the exponential of all raw scores.

---

# 4. Numerical Example

Let's calculate Softmax for our previous example:

Raw scores (logits):
- Dog (\( z_1 \)) = 2.5
- Cat (\( z_2 \)) = 4.1
- Bird (\( z_3 \)) = -1.2

### Step 1: Calculate Exponentials (\( e^z \))
- \( e^{2.5} \approx 12.18 \)
- \( e^{4.1} \approx 60.34 \)
- \( e^{-1.2} \approx 0.30 \)

### Step 2: Calculate the Sum
Sum = 12.18 + 60.34 + 0.30 = **72.82**

### Step 3: Divide Each Exponential by the Sum
- Probability of Dog = 12.18 / 72.82 = **0.167 (16.7%)**
- Probability of Cat = 60.34 / 72.82 = **0.828 (82.8%)**
- Probability of Bird = 0.30 / 72.82 = **0.004 (0.4%)**

Notice that:
0.167 + 0.828 + 0.004 ≈ **1.0 (100%)**

The network predicts "Cat" with 82.8% confidence.

---

# 5. Why use the Exponential Function (\( e^z \))?

You might wonder, why not just divide the raw score by the sum of raw scores? Why use exponentials?

1. **Handling Negative Numbers:** Raw scores can be negative (like the -1.2 for the bird). Exponentials always output a positive number, ensuring all probabilities are positive.
2. **Exaggerating Differences:** The exponential function heavily rewards the highest score. It pushes the highest score closer to 1 and the lower scores closer to 0, making the model's prediction much more decisive.

---

# 6. Softmax vs Sigmoid

| Feature | Sigmoid | Softmax |
|---------|---------|---------|
| **Use Case** | Binary Classification (2 classes) | Multi-Class Classification (3+ classes) |
| **Output Sum** | Outputs are independent (Sum is not 1) | Outputs depend on each other (Sum is exactly 1) |
| **Application** | Single output neuron | Multiple output neurons |

---

# Interview Questions

## Q1. When should you use Softmax instead of Sigmoid?

**Answer**

Sigmoid is used in the output layer for binary classification tasks, where the output is a single probability (e.g., spam vs not spam). Softmax is used for multi-class classification tasks (e.g., predicting 1 of 10 digits), where it converts a vector of raw scores into a valid probability distribution that sums to 1.

---

## Q2. Why does the Softmax formula use the exponential function?

**Answer**

The exponential function ensures that all raw scores (including negative ones) are converted to strictly positive values, which is required for probabilities. Furthermore, the exponential function exaggerates differences, making the highest raw score stand out distinctly as the predicted class.

---

# Summary

Softmax is the standard output activation function for multi-class classification. By converting raw logits into a clean, easy-to-interpret probability distribution, it allows us to easily pair the network's output with loss functions like Categorical Cross-Entropy to train the model.

---

# Key Takeaways

✔ Softmax is used exclusively in the output layer for multi-class classification.
✔ It converts raw scores into probabilities between 0 and 1.
✔ The sum of all output probabilities always equals exactly 1.0.
✔ The exponential component handles negative raw scores and accentuates the highest prediction.
