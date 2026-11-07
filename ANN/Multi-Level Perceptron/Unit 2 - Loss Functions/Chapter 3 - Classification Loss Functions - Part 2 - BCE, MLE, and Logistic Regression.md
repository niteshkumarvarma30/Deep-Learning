# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 2 – Binary Cross Entropy (BCE), Maximum Likelihood Estimation (MLE), and Logistic Regression

---

## Introduction

One of the biggest realizations in Machine Learning and Deep Learning is:

> **Binary Cross Entropy (BCE) is exactly the same loss function that is derived in Logistic Regression using Maximum Likelihood Estimation (MLE).**

Many students think BCE is a new loss function introduced in Deep Learning.

It is **not**.

Deep Learning simply reuses the same mathematical result obtained from Logistic Regression.

The only difference is the context:

- **Logistic Regression:** Derives BCE using Probability Theory and Maximum Likelihood Estimation.
- **Deep Learning:** Directly uses BCE as the loss function for training binary neural networks.

---

## The Big Picture

```text
Logistic Regression
        |
        v
Probability Theory
        |
        v
Likelihood Function
        |
        v
Maximum Likelihood Estimation (MLE)
        |
        v
Log Likelihood
        |
        v
Negative Log Likelihood (NLL)
        |
        v
Binary Cross Entropy (BCE)
        |
        v
Deep Learning uses the same BCE loss
```

---

## Step 1 – Logistic Regression Predicts a Probability

Logistic Regression first computes the linear equation:

$$
z = w^T x + b
$$

Where:

- $w$ = Weight Vector.
- $x$ = Input Features.
- $b$ = Bias.

This value is passed through the Sigmoid function:

$$
\hat{y} = \sigma(z) = \frac{1}{1+e^{-z}}
$$

Where:

- $\hat{y}$ = Predicted Probability.

### Example

```text
ŷ = 0.92
    |
    v
92% probability that the sample belongs to Class 1
```

Notice that Logistic Regression predicts a **probability**, not a class label.

---

## Step 2 – Build the Probability Model

Suppose the target variable has two possible values:

$$
y \in \{0,1\}
$$

There are two possible cases.

### Case 1 – When y = 1

If:

$$
y = 1
$$

Then:

$$
P(y=1) = \hat{y}
$$

### Case 2 – When y = 0

If:

$$
y = 0
$$

Then:

$$
P(y=0) = 1-\hat{y}
$$

Instead of writing two separate equations, both cases can be combined into one equation:

$$
P(y) = \hat{y}^{\,y}(1-\hat{y})^{1-y}
$$

This single equation works for both classes.

### Why Does This Equation Work?

**When y = 1:**

$$
P(y) = \hat{y}^1(1-\hat{y})^0
$$

$$
P(y) = \hat{y}
$$

**When y = 0:**

$$
P(y) = \hat{y}^0(1-\hat{y})^1
$$

$$
P(y) = 1-\hat{y}
$$

Thus, the same equation correctly represents both possible outcomes.

---

## Step 3 – Maximum Likelihood Estimation (MLE)

The goal of Maximum Likelihood Estimation is:

> **Find the weights and bias that make the observed training data most probable.**

For one training example, the likelihood is:

$$
L = \hat{y}^{\,y}(1-\hat{y})^{1-y}
$$

For $n$ independent training examples, the total likelihood becomes:

$$
L = \prod_{i=1}^{n}
\hat{y}_i^{\,y_i}
(1-\hat{y}_i)^{1-y_i}
$$

Our objective is:

$$
\boxed{\text{Maximize Likelihood}}
$$

---

## Step 4 – Take the Log Likelihood

The likelihood contains a product.

Products are difficult to optimize directly.

Using the logarithm converts products into sums:

$$
\log L =
\sum_{i=1}^{n}
\left[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
$$

This simplifies optimization considerably.

---

## Step 5 – Convert Maximization into Minimization

Maximum Likelihood Estimation is a **maximization** problem.

However, Gradient Descent is a **minimization** algorithm.

Therefore, multiply the objective by $-1$:

$$
-\log L =
-\sum_{i=1}^{n}
\left[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
$$

Now divide by the number of training samples:

$$
\boxed{
J =
-\frac{1}{n}
\sum_{i=1}^{n}
\left[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
}
$$

This is exactly the **Binary Cross Entropy (BCE)** loss function.

---

## The Complete Derivation

```text
Logistic Regression
        |
        v
Sigmoid Function
        |
        v
Predicted Probability
        |
        v
Likelihood Function
        |
        v
Maximum Likelihood Estimation (MLE)
        |
        v
Log Likelihood
        |
        v
Negative Log Likelihood (NLL)
        |
        v
Binary Cross Entropy (BCE)
```

---

## Why Doesn't Deep Learning Re-Derive It?

In Logistic Regression, you learn:

- Probability Theory.
- Likelihood Function.
- Maximum Likelihood Estimation.
- Log Likelihood.
- Negative Log Likelihood.
- Binary Cross Entropy Derivation.

Once this derivation is completed, there is no need to derive it again.

Deep Learning simply uses:

```text
Binary Classification
        |
        v
Sigmoid Activation
        |
        v
Binary Cross Entropy Loss
```

BCE has already been mathematically justified through Maximum Likelihood Estimation.

---

## Logistic Regression Is Actually a Neural Network

A very interesting fact is:

> **Logistic Regression is simply a neural network with no hidden layers.**

### Logistic Regression

```text
Input Features
      |
      v
Weighted Sum
      |
      v
Sigmoid
      |
      v
Binary Cross Entropy
      |
      v
Gradient Descent
```

### Binary Neural Network

```text
Input Features
      |
      v
Hidden Layer(s)
      |
      v
Output Neuron
      |
      v
Sigmoid
      |
      v
Binary Cross Entropy
      |
      v
Backpropagation
      |
      v
Gradient Descent
```

Notice that the following remain the same:

- Sigmoid Function.
- Binary Cross Entropy.

The main architectural difference is the addition of hidden layers.

---

## Does Deep Learning Compute the Likelihood Function Internally?

Many students ask:

> "When we use Binary Cross Entropy, does Deep Learning first compute the Likelihood Function?"

The answer is:

> **Yes mathematically, but no computationally.**

### Important Clarification

Deep Learning does not separately perform the following sequence during every training iteration:

```text
Likelihood
    |
    v
Log Likelihood
    |
    v
Negative Log Likelihood
    |
    v
Binary Cross Entropy
```

Instead, the Binary Cross Entropy formula already contains the entire mathematical derivation.

The likelihood mathematics is already incorporated into the BCE formula.

---

## Think of It Like This

During Logistic Regression, we derive:

```text
Likelihood
    |
    v
Log Likelihood
    |
    v
Negative Log Likelihood
    |
    v
Binary Cross Entropy
```

After the derivation, Binary Cross Entropy becomes the final mathematical formula.

During Deep Learning, the framework directly computes:

$$
L =
-\left[
y\log(\hat{y})
+
(1-y)\log(1-\hat{y})
\right]
$$

It does not separately compute:

- Likelihood.
- Log Likelihood.
- Negative Log Likelihood.

These operations have already been mathematically combined into the BCE objective.

---

## What Happens Internally?

When we write:

```python
loss = BCELoss(prediction, target)
```

Conceptually, the framework performs:

```text
Prediction
    |
    v
Binary Cross Entropy Formula
    |
    v
Loss Value
```

It does not need to separately execute:

```text
Likelihood
    |
    v
Log Likelihood
    |
    v
Negative Log Likelihood
    |
    v
Loss
```

BCE is already the simplified mathematical result.

---

## Analogy

Suppose you know the mathematical identity:

$$
(a+b)^2 = a^2+2ab+b^2
$$

Later, if you write:

```python
(a + b) ** 2
```

Python does not derive the identity or manually expand the equation every time.

It simply evaluates:

$$
(a+b)^2
$$

Similarly, Deep Learning frameworks do not derive Maximum Likelihood Estimation during every training iteration.

They directly evaluate the Binary Cross Entropy objective.

---

## Mathematical Derivation vs Training Pipeline

### 1. Mathematical Derivation

```text
Probability Model
       |
       v
Likelihood Function
       |
       v
Maximum Likelihood Estimation
       |
       v
Log Likelihood
       |
       v
Negative Log Likelihood
       |
       v
Binary Cross Entropy Formula
```

This derivation establishes the mathematical objective.

### 2. Actual Deep Learning Training

```text
Input
  |
  v
Forward Propagation
  |
  v
Sigmoid
  |
  v
Predicted Probability
  |
  v
Binary Cross Entropy Formula
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
Update Weights
```

Notice that the Likelihood Function does not explicitly appear because it has already been incorporated into the BCE formula.

---

## The Deep Mathematical Truth

The underlying optimization objective has never changed.

Originally, Maximum Likelihood Estimation wanted to:

$$
\boxed{\text{Maximize Likelihood}}
$$

However, Gradient Descent minimizes objective functions.

Therefore, we instead minimize:

$$
\boxed{-\log(\text{Likelihood})}
$$

Since:

$$
-\log(\text{Likelihood}) = \text{Binary Cross Entropy}
$$

We obtain:

$$
\boxed{
\text{Minimize BCE}
\iff
\text{Minimize Negative Log Likelihood}
\iff
\text{Maximize Likelihood}
}
$$

These three optimization objectives are mathematically equivalent.

---

## Mental Model

You can remember the relationship as follows:

```text
Linear Regression
       |
       v
Mean Squared Error (MSE)

--------------------------------

Logistic Regression
       |
       v
Binary Cross Entropy (BCE)

--------------------------------

Binary Neural Network
       |
       v
Sigmoid
       |
       v
Binary Cross Entropy (BCE)

--------------------------------

Multi-class Neural Network
       |
       v
Softmax
       |
       v
Categorical Cross Entropy (CCE)
```

---

## Logistic Regression vs Binary Neural Network

| Feature | Logistic Regression | Binary Neural Network |
|---|---|---|
| Architecture | No Hidden Layers | One or More Hidden Layers |
| Output Activation | Sigmoid | Sigmoid |
| Loss Function | Binary Cross Entropy | Binary Cross Entropy |
| Optimization | Gradient Descent | Backpropagation + Gradient Descent |
| Objective | Maximum Likelihood | Maximum Likelihood |

Both optimize the same probabilistic objective.

---

## Summary

Binary Cross Entropy (BCE) is **not a new loss function introduced in Deep Learning**.

It is the **Negative Log Likelihood (NLL)** obtained from **Maximum Likelihood Estimation (MLE)** in Logistic Regression.

During Logistic Regression, the BCE formula is derived using Probability Theory.

During Deep Learning, this derivation is already established.

Therefore, Deep Learning frameworks directly use the BCE formula without separately recomputing the Likelihood Function during every training iteration.

Mathematically, minimizing Binary Cross Entropy is equivalent to maximizing the likelihood of the observed training data.

---

## Key Takeaways

- Binary Cross Entropy (BCE) is derived from Maximum Likelihood Estimation (MLE).
- BCE is mathematically equivalent to Negative Log Likelihood (NLL).
- Logistic Regression derives BCE using Probability Theory.
- Deep Learning directly uses the final BCE formula.
- The Likelihood Function is mathematically incorporated into BCE.
- Deep Learning does not explicitly perform Likelihood → Log Likelihood → Negative Log Likelihood as separate optimization stages during every training iteration.
- Minimizing BCE is mathematically equivalent to maximizing the likelihood of the observed data.
- Logistic Regression can be viewed as a neural network with no hidden layers.
- Binary Neural Networks and Logistic Regression optimize the same probabilistic objective.
- The main architectural difference is that neural networks include hidden layers before the output layer.

---

## Next Topic

**Multi-class Classification – Softmax and Categorical Cross Entropy (CCE)**

Continue exploring how probability-based loss functions extend from binary classification to multi-class classification.
