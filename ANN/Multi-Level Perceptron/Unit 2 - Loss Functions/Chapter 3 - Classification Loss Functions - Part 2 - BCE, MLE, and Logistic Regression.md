# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 2 – Binary Cross Entropy (BCE), Maximum Likelihood Estimation (MLE), and Logistic Regression

---

# Introduction

One of the biggest realizations in Machine Learning and Deep Learning is that

> **Binary Cross Entropy (BCE) is exactly the same loss function that is derived in Logistic Regression using Maximum Likelihood Estimation (MLE).**

Many students think BCE is a new loss function introduced in Deep Learning.

It is **not**.

Deep Learning simply reuses the same mathematical result obtained from Logistic Regression.

The only difference is the **context**.

- **Logistic Regression** derives BCE using Probability Theory and Maximum Likelihood Estimation.
- **Deep Learning** directly uses BCE as the loss function for training binary neural networks.

---

# The Big Picture

```text
Logistic Regression

↓

Probability Theory

↓

Likelihood Function

↓

Maximum Likelihood Estimation (MLE)

↓

Log Likelihood

↓

Negative Log Likelihood (NLL)

↓

Binary Cross Entropy (BCE)

↓

Deep Learning uses the same BCE loss
```

---

# Step 1 — Logistic Regression Predicts a Probability

Logistic Regression first computes the linear equation

$$
z=w^Tx+b
$$

where

- \(w\) = Weight Vector
- \(x\) = Input Features
- \(b\) = Bias

This value is passed through the Sigmoid function.

$$
\hat y
=
\sigma(z)
=
\frac{1}{1+e^{-z}}
$$

where

- \(\hat y\) = Predicted Probability

Example

```text
ŷ = 0.92

↓

92% probability that the sample belongs to Class 1
```

Notice that Logistic Regression predicts a **probability**, not a class label.

---

# Step 2 — Build the Probability Model

Suppose

$$
y\in\{0,1\}
$$

There are two possible cases.

## Case 1

If

$$
y=1
$$

then

$$
P(y=1)=\hat y
$$

---

## Case 2

If

$$
y=0
$$

then

$$
P(y=0)=1-\hat y
$$

Instead of writing two separate equations,

both cases are combined into one elegant equation.

$$
P(y)
=
\hat y^{\,y}
(1-\hat y)^{1-y}
$$

This single equation works for both classes.

---

# Why Does This Equation Work?

### When \(y=1\)

$$
P(y)
=
\hat y^1
(1-\hat y)^0
=
\hat y
$$

---

### When \(y=0\)

$$
P(y)
=
\hat y^0
(1-\hat y)^1
=
1-\hat y
$$

Thus,

the same equation correctly represents both possible outcomes.

---

# Step 3 — Maximum Likelihood Estimation (MLE)

The goal of Maximum Likelihood Estimation is

> **Find the weights and bias that make the observed training data most probable.**

For one training example,

the likelihood is

$$
L
=
\hat y^{\,y}
(1-\hat y)^{1-y}
$$

For \(n\) training examples,

the total likelihood becomes

$$
L
=
\prod_{i=1}^{n}
\hat y_i^{\,y_i}
(1-\hat y_i)^{1-y_i}
$$

Our objective is

$$
\boxed{
\text{Maximize Likelihood}
}
$$

---

# Step 4 — Take the Log Likelihood

The likelihood contains a product.

Products are difficult to optimize.

Using the logarithm converts products into sums.

$$
\log L
=
\sum_{i=1}^{n}
\left[
y_i\log(\hat y_i)
+
(1-y_i)\log(1-\hat y_i)
\right]
$$

This simplifies optimization considerably.

---

# Step 5 — Convert Maximization into Minimization

Maximum Likelihood Estimation is a **maximization** problem.

However,

Gradient Descent is a **minimization** algorithm.

Therefore,

multiply the objective by **−1**.

$$
-\log L = - \sum_{i=1}^{n} \left[ y_i\log(\hat y_i) + (1-y_i)\log(1-\hat y_i) \right]
$$

Now divide by the number of training samples.

$$
\boxed{ J = - \frac1n \sum_{i=1}^{n} \left[ y_i\log(\hat y_i) + (1-y_i)\log(1-\hat y_i) \right] }
$$

This is exactly the

# Binary Cross Entropy (BCE)

---

# The Complete Derivation

```text
Logistic Regression

↓

Sigmoid Function

↓

Predicted Probability

↓

Likelihood Function

↓

Maximum Likelihood Estimation (MLE)

↓

Log Likelihood

↓

Negative Log Likelihood (NLL)

↓

Binary Cross Entropy (BCE)
```

---

# Why Doesn't Deep Learning Re-Derive It?

In Logistic Regression,

you learn

- Probability Theory
- Likelihood Function
- Maximum Likelihood Estimation
- Log Likelihood
- Negative Log Likelihood
- Binary Cross Entropy Derivation

Once this derivation is completed,

there is no need to derive it again.

Deep Learning simply says

```text
Binary Classification

↓

Sigmoid Activation

↓

Binary Cross Entropy Loss
```

because BCE has already been mathematically justified through Maximum Likelihood Estimation.

---

# Logistic Regression is Actually a Neural Network

A very interesting fact is

> **Logistic Regression is simply a Neural Network with no hidden layers.**

---

## Logistic Regression

```text
Input Features

↓

Weighted Sum

↓

Sigmoid

↓

Binary Cross Entropy

↓

Gradient Descent
```

---

## Binary Neural Network

```text
Input Features

↓

Hidden Layer(s)

↓

Output Neuron

↓

Sigmoid

↓

Binary Cross Entropy

↓

Backpropagation

↓

Gradient Descent
```

Notice

The

- Sigmoid Function
- Binary Cross Entropy

remain exactly the same.

The only difference is the addition of hidden layers.

---

# Does Deep Learning Compute the Likelihood Function Internally?

Many students ask

> "When we use Binary Cross Entropy, does Deep Learning first compute the Likelihood Function?"

The answer is

> **Yes mathematically, but No computationally.**

---

# Important Clarification

Deep Learning does **not** perform

```text
Likelihood

↓

Log Likelihood

↓

Negative Log Likelihood

↓

Binary Cross Entropy
```

during every training iteration.

Instead,

the Binary Cross Entropy formula already **contains** the entire derivation.

The likelihood mathematics is already built into the BCE formula.

---

# Think of It Like This

During Logistic Regression,

we derived

```text
Likelihood

↓

Log Likelihood

↓

Negative Log Likelihood

↓

Binary Cross Entropy
```

After the derivation,

Binary Cross Entropy becomes the final mathematical formula.

During Deep Learning,

the framework directly computes

$$
L = - \left[ y\log(\hat y) + (1-y)\log(1-\hat y) \right]
$$

It does **not** separately compute

- Likelihood
- Log Likelihood
- Negative Log

because these operations have already been mathematically combined.

---

# What Happens Internally?

When we write

```python
loss = BCELoss(prediction, target)
```

Conceptually,

the framework performs

```text
Prediction

↓

Binary Cross Entropy Formula

↓

Loss Value
```

It does **not** internally execute

```text
Likelihood

↓

Log Likelihood

↓

Negative Log

↓

Loss
```

because BCE is already the simplified mathematical result.

---

# Analogy

Suppose you know the identity

$$
(a+b)^2
=
a^2+2ab+b^2
$$

Later,

if you write

```python
(a+b)**2
```

Python does **not**

- derive the identity,
- expand the equation,

every time.

It simply evaluates

$$
(a+b)^2
$$

Similarly,

Deep Learning frameworks do **not** derive Maximum Likelihood Estimation every iteration.

They directly evaluate the Binary Cross Entropy formula.

---

# Mathematical Derivation vs Training Pipeline

## Mathematical Derivation

```text
Probability Model

↓

Likelihood Function

↓

Maximum Likelihood Estimation

↓

Log Likelihood

↓

Negative Log Likelihood

↓

Binary Cross Entropy Formula
```

This derivation is performed once during mathematical analysis.

---

## Actual Deep Learning Training

```text
Input

↓

Forward Propagation

↓

Sigmoid

↓

Predicted Probability

↓

Binary Cross Entropy Formula

↓

Loss

↓

Backpropagation

↓

Gradient Descent

↓

Update Weights
```

Notice

The **Likelihood Function does not explicitly appear** because it has already been incorporated into the BCE formula.

---

# The Deep Mathematical Truth

The real optimization objective has **never changed**.

Originally,

Maximum Likelihood Estimation wanted to

$$
\boxed{
\text{Maximize Likelihood}
}
$$

However,

Gradient Descent minimizes objective functions.

Therefore,

we instead minimize

$$
\boxed{
-\log(\text{Likelihood})
}
$$

Since

$$
-\log(\text{Likelihood})
=
\text{Binary Cross Entropy}
$$

we obtain

$$
\boxed{
\text{Minimize BCE}
\iff
\text{Minimize Negative Log Likelihood}
\iff
\text{Maximize Likelihood}
}
$$

These three optimization objectives are mathematically identical.

---

# Mental Model

You can remember the relationship as

```text
Linear Regression

↓

Mean Squared Error (MSE)

--------------------------------

Logistic Regression

↓

Binary Cross Entropy (BCE)

--------------------------------

Binary Neural Network

↓

Sigmoid

↓

Binary Cross Entropy (BCE)

--------------------------------

Multi-class Neural Network

↓

Softmax

↓

Categorical Cross Entropy (CCE)
```

---

# Logistic Regression vs Binary Neural Network

| Logistic Regression | Binary Neural Network |
|---------------------|----------------------|
| No Hidden Layers | One or More Hidden Layers |
| Sigmoid Output | Sigmoid Output |
| Binary Cross Entropy | Binary Cross Entropy |
| Gradient Descent | Backpropagation + Gradient Descent |
| Maximizes Likelihood | Maximizes Likelihood |

Both optimize **exactly the same probabilistic objective**.

---

# Summary

Binary Cross Entropy (BCE) is **not a new loss function introduced in Deep Learning**.

It is the **Negative Log Likelihood (NLL)** obtained from **Maximum Likelihood Estimation (MLE)** in Logistic Regression.

During Logistic Regression,

the BCE formula is derived from probability theory.

During Deep Learning,

this derivation is assumed to be already known.

Therefore,

Deep Learning frameworks directly use the BCE formula without recomputing the Likelihood Function during every training iteration.

Mathematically,

using Binary Cross Entropy is **equivalent** to maximizing the likelihood of the observed data.

---

# Key Takeaways

✔ Binary Cross Entropy (BCE) is derived from Maximum Likelihood Estimation (MLE).

✔ BCE is mathematically equivalent to Negative Log Likelihood (NLL).

✔ Logistic Regression derives BCE using Probability Theory.

✔ Deep Learning directly uses the final BCE formula.

✔ The Likelihood Function is mathematically embedded inside BCE.

✔ Deep Learning does **not** explicitly compute Likelihood → Log Likelihood → Negative Log during every training iteration.

✔ Minimizing BCE is mathematically identical to maximizing the likelihood of the observed data.

✔ Logistic Regression is a neural network with no hidden layers.

✔ Binary Neural Networks and Logistic Regression optimize the same probabilistic objective.

✔ The only major difference is that neural networks include hidden layers before the output layer.
