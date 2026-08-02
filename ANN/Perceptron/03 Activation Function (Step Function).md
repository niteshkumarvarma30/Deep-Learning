# Chapter 03: Activation Function (Step Function)

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand what an Activation Function is, why it is required in a Perceptron, how the Step Function works, and how the Perceptron converts a weighted sum into a binary prediction.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why an activation function is required.
- Explain the Step Activation Function.
- Convert a weighted sum into a prediction.
- Understand thresholds in binary classification.
- Solve numerical problems involving activation functions.
- Understand the limitations of the Step Function.

---

# 1. Recap

In Chapter 2, we learned that the Perceptron computes a weighted sum.

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

The weighted sum **z** is only a numerical score.

Example:

```
z = 8

or

z = -3

or

z = 0.7
```

But our final prediction should be something like:

```
Spam

Not Spam
```

or

```
1

0
```

So,

**How do we convert the score into a decision?**

The answer is the **Activation Function**.

---

# 2. What is an Activation Function?

An **Activation Function** is a mathematical function that converts the weighted sum into the final output of the Perceptron.

It acts like the decision-maker of the neuron.

```
Input Features
       │
       ▼
Weighted Sum (z)
       │
       ▼
Activation Function
       │
       ▼
Final Prediction
```

Without an activation function, the Perceptron would only produce numbers, not class labels.

---

# 3. Why Do We Need an Activation Function?

Suppose the weighted sum is

```
z = 12
```

Does this mean

```
Spam?

Healthy?

Approved?
```

We don't know.

Similarly,

```
z = -7
```

does not directly tell us the class.

Therefore,

the Perceptron needs a rule that converts

```
Any Number

↓

Binary Output
```

---

# 4. The Step Function

The original Perceptron uses the **Step Function**.

It is defined as

\[
f(z)=
\begin{cases}
1,& z \ge 0\\
0,& z < 0
\end{cases}
\]

This is the activation function used in the original Perceptron. :contentReference[oaicite:1]{index=1}

---

# 5. Understanding the Step Function

The Step Function checks only one thing.

```
Is z greater than or equal to zero?
```

If YES

↓

Output

```
1
```

If NO

↓

Output

```
0
```

---

# 6. Visual Representation

```
Output

1 ─────────────────────────────

|
|
|
|
0_______________________________

             z = 0
```

Notice the sudden jump.

This is why it is called the **Step Function**.

It behaves like climbing a staircase.

---

# 7. Numerical Example 1

Suppose

```
z = 15
```

Since

```
15 ≥ 0
```

Prediction becomes

```
1
```

---

# Numerical Example 2

Suppose

```
z = -4
```

Since

```
-4 < 0
```

Prediction becomes

```
0
```

---

# Numerical Example 3

Suppose

```
z = 0
```

Since

```
0 ≥ 0
```

Prediction becomes

```
1
```

Notice that the original Perceptron includes zero in **Class 1**.

---

# 8. Complete Working Example

Suppose

```
x₁ = 2

x₂ = 5

w₁ = 4

w₂ = -1

b = -2
```

### Step 1

Compute the weighted sum

\[
z = 4(2)+(-1)(5)-2
\]

\[
=8-5-2
\]

\[
=1
\]

### Step 2

Apply the Step Function

Since

```
1 ≥ 0
```

Prediction

```
1
```

The Perceptron predicts **Class 1**.

---

# Another Example

Suppose

```
x₁ = 1

x₂ = 2

w₁ = 2

w₂ = 1

b = -8
```

Weighted Sum

\[
z = 2(1)+1(2)-8
\]

\[
=4-8
\]

\[
=-4
\]

Apply Step Function

```
-4 < 0
```

Prediction

```
0
```

---

# 9. Threshold

The value

```
0
```

is called the **threshold**.

It separates the two classes.

```
z < 0

↓

Class 0

---------------- Threshold ----------------

z ≥ 0

↓

Class 1
```

Every prediction depends on which side of the threshold the weighted sum lies.

---

# 10. Real-Life Analogy

Imagine a university admission rule.

```
Cutoff = 90 Marks
```

Students scoring

```
90 or more

↓

Admission
```

Students scoring

```
Below 90

↓

Rejected
```

The cutoff behaves exactly like the threshold in the Step Function.

---

# 11. Binary Classification

The Step Function always produces one of two outputs.

```
0

or

1
```

Therefore,

the original Perceptron is suitable only for **binary classification**.

Examples

```
Spam / Not Spam

Disease / Healthy

Pass / Fail

Approve / Reject
```

---

# 12. Why Is the Step Function So Simple?

When the Perceptron was invented, researchers wanted a neuron that behaved like an electrical switch.

```
OFF

↓

0
```

```
ON

↓

1
```

The Step Function perfectly models this behaviour.

---

# 13. Limitations of the Step Function

Although simple,

the Step Function has several limitations.

### 1. No Probability

Output

```
0

or

1
```

It cannot say

```
0.82

0.65

0.11
```

---

### 2. Abrupt Decision

A tiny change near zero can completely change the prediction.

Example

```
z = -0.0001

↓

0
```

```
z = 0.0001

↓

1
```

Even though the values are almost identical, the prediction changes suddenly.

---

### 3. Not Differentiable

The sudden jump makes the Step Function **non-differentiable**.

Because of this,

modern neural networks do **not** use the Step Function.

Instead,

they use smooth activation functions such as

- Sigmoid
- Tanh
- ReLU

---

# Common Mistakes

### Mistake 1

Thinking that the weighted sum is the prediction.

❌ Incorrect

The weighted sum must first pass through the activation function.

---

### Mistake 2

Thinking that the Step Function outputs probabilities.

❌ Incorrect

It outputs only

```
0

or

1
```

---

### Mistake 3

Ignoring the threshold.

The threshold is the point where the prediction changes from one class to the other.

---

# Chapter Summary

The weighted sum computed by the Perceptron is only a score.

The Activation Function converts this score into the final binary prediction.

The original Perceptron uses the Step Function

\[
f(z)=
\begin{cases}
1,& z \ge 0\\
0,& z < 0
\end{cases}
\]

which acts as a threshold-based decision maker.

Although simple,

its inability to produce probabilities and its non-differentiable nature led to the development of more advanced activation functions used in modern neural networks.

---

# Key Takeaways

✔ The weighted sum is **not** the final prediction.

✔ The Activation Function converts the weighted sum into a class label.

✔ The original Perceptron uses the Step Function.

✔ The Step Function outputs only

```
0

or

1
```

✔ Threshold = 0.

✔ The Step Function is not differentiable.

---

# Interview Questions

### Q1. Why is an Activation Function required?

**Answer:**

It converts the weighted sum into the final prediction.

---

### Q2. Which activation function is used in the original Perceptron?

**Answer:**

The Step Function.

---

### Q3. What is the output of the Step Function?

**Answer:**

Either

```
0

or

1
```

---

### Q4. Why is the Step Function not used in Deep Learning?

**Answer:**

Because it is not differentiable and cannot be optimized using Gradient Descent.

---

# Practice Questions

## Conceptual

1. Explain the purpose of an Activation Function.
2. Why is the Step Function suitable for binary classification?
3. What is the threshold in a Perceptron?

---

## Numerical

### Question 1

Given

```
z = -8
```

Find the prediction.

---

### Question 2

Given

```
z = 4.2
```

Find the prediction.

---

### Question 3

Compute the prediction.

```
x₁ = 3

x₂ = 1

w₁ = 2

w₂ = -1

b = -4
```

---

## MCQs

### 1. The Step Function produces

A. Any real number

B. Probability

C. Binary output

D. Continuous output

**Answer:** C

---

### 2. The threshold in the original Perceptron is

A. 1

B. -1

C. 0

D. 10

**Answer:** C

---

### 3. Which activation function is used in the original Perceptron?

A. ReLU

B. Sigmoid

C. Tanh

D. Step Function

**Answer:** D

---

# What's Next?

In **Chapter 4**, we will study the **Decision Boundary**.

Topics include:

- What is a Decision Boundary?
- Why is the boundary represented by

\[
w^Tx+b=0
\]

- How the Perceptron separates two classes.
- Linear classifier.
- Geometry of the Perceptron.
- Hyperplanes in higher dimensions.
