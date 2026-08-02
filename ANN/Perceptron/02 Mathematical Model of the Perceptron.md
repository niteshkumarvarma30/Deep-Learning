# Chapter 02: Mathematical Model of the Perceptron

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand the mathematical model of a Perceptron, including inputs, weights, bias, weighted sum, dot product, and vector representation.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how a Perceptron processes information mathematically.
- Explain Inputs, Weights, and Bias.
- Derive the Perceptron equation.
- Understand the concept of Weighted Sum.
- Represent the Perceptron equation using vectors.
- Understand why weights and bias are necessary.

---

# 1. Recap

In Chapter 1, we learned that a Perceptron is an artificial neuron.

Now the question is:

> **How does a Perceptron make a decision mathematically?**

The answer is by computing a **weighted sum** of all input features.

---

# 2. Components of a Perceptron

A Perceptron consists of five main components.

```
Input Features
      │
      ▼
Multiply by Weights
      │
      ▼
Add Bias
      │
      ▼
Weighted Sum (z)
      │
      ▼
Activation Function
```

This chapter focuses on everything **before** the activation function.

---

# 3. Input Features

Input features are the information provided to the Perceptron.

Examples:

Predicting Student Placement

```
x₁ = CGPA

x₂ = Aptitude Score

x₃ = Communication Skills
```

Predicting House Price

```
x₁ = Area

x₂ = Number of Bedrooms

x₃ = Age of House
```

Each feature represents one measurable property of the data.

---

# 4. Weights

Each input has an associated weight.

```
x₁ → w₁

x₂ → w₂

x₃ → w₃
```

Weights indicate the importance of each feature.

Higher weight

↓

More influence on prediction.

Lower weight

↓

Less influence.

---

## Real-Life Analogy

Imagine selecting a candidate for a job.

Criteria:

```
CGPA

Projects

Communication Skills
```

Should all have equal importance?

No.

Maybe:

| Feature | Importance |
|----------|------------|
| CGPA | 20% |
| Projects | 50% |
| Communication | 30% |

These importance values are represented by the weights.

---

# 5. Why Multiply Inputs by Weights?

Suppose

```
CGPA = 8

Projects = 10
```

If projects are more important,

they should contribute more to the final decision.

Therefore,

```
Weighted Contribution

=

Input × Weight
```

Example

```
CGPA

8 × 2 = 16

Projects

10 × 5 = 50
```

Projects contribute much more because their weight is larger.

---

# 6. Bias

Bias is an additional parameter added after computing the weighted sum.

It is represented by

```
b
```

The complete equation becomes

```
Weighted Sum + Bias
```

---

## Why Do We Need Bias?

Imagine the equation without bias.

```
z = w₁x₁ + w₂x₂
```

The decision boundary must pass through the origin.

```
(0,0)
```

This is too restrictive.

Adding bias

```
z = w₁x₁ + w₂x₂ + b
```

allows the decision boundary to shift anywhere.

---

## Real-Life Analogy

Suppose a university says:

Admission requires:

```
Marks > 90
```

Later,

they decide to give every student

5 grace marks.

Now the rule becomes

```
Marks + 5
```

Bias acts like these additional grace marks.

It shifts the decision without changing the relative importance of the features.

---

# 7. Weighted Sum

The Perceptron multiplies every input by its corresponding weight.

Then adds everything.

Finally,

adds the bias.

This value is called the **Weighted Sum**.

It is usually represented by

```
z
```

---

# 8. Mathematical Equation

For two inputs,

\[
z = w_1x_1 + w_2x_2 + b
\]

For three inputs,

\[
z = w_1x_1 + w_2x_2 + w_3x_3 + b
\]

For n inputs,

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

This is the mathematical model of a Perceptron. It computes a single score that is later passed to the activation function. :contentReference[oaicite:1]{index=1}

---

# 9. Numerical Example

Suppose

```
x₁ = 2

x₂ = 5

w₁ = 3

w₂ = -1

b = 4
```

Compute

\[
z = 3(2) + (-1)(5) + 4
\]

Step 1

```
3 × 2 = 6
```

Step 2

```
-1 × 5 = -5
```

Step 3

```
6 - 5 = 1
```

Step 4

```
1 + 4 = 5
```

Therefore,

```
Weighted Sum = 5
```

Notice that this is **not yet the prediction**. It is only the score that will be sent to the activation function.

---

# 10. Vector Representation

Instead of writing long equations,

we can write

\[
z = \mathbf{w}^T\mathbf{x} + b
\]

where

\[
\mathbf{x} =
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
\]

and

\[
\mathbf{w} =
\begin{bmatrix}
w_1\\
w_2\\
w_3
\end{bmatrix}
\]

---

## Dot Product

The term

\[
\mathbf{w}^T\mathbf{x}
\]

is called the **dot product**.

It simply means

```
Multiply corresponding elements

↓

Add them together
```

Example

\[
\begin{bmatrix}
2\\
3
\end{bmatrix}
\cdot
\begin{bmatrix}
4\\
5
\end{bmatrix}
=
2(4)+3(5)
=
8+15
=
23
\]

Thus,

the dot product is another way of computing the weighted sum.

---

# 11. Why Is the Weighted Sum Important?

The weighted sum combines all features into **one numerical score**.

This score tells the Perceptron how strongly the inputs support one class over the other.

However,

the score itself is not the final answer.

The Perceptron still needs to convert it into a binary prediction.

That is the job of the **Activation Function**, which we will study in the next chapter.

---

# Common Mistakes

### Mistake 1

Thinking that the weighted sum is the final prediction.

❌ Incorrect

The weighted sum is only an intermediate value.

---

### Mistake 2

Thinking that weights are fixed.

❌ Incorrect

Weights are learned during training.

---

### Mistake 3

Ignoring the bias.

❌ Incorrect

Without bias, the Perceptron becomes much less flexible because the decision boundary is forced through the origin.

---

# Chapter Summary

A Perceptron receives multiple input features.

Each feature is multiplied by a learned weight.

The weighted values are added together, and a bias is added to produce the **weighted sum**:

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

This weighted sum is not yet a prediction. It is the input to the activation function, which converts it into the final binary output.

---

# Key Takeaways

✔ Inputs represent the features of the data.

✔ Weights represent the importance of each feature.

✔ Bias shifts the decision boundary.

✔ The weighted sum is computed as

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

✔ Vector notation

\[
z = \mathbf{w}^T\mathbf{x} + b
\]

is a compact way of writing the same computation.

✔ The weighted sum is an intermediate score, not the final prediction.

---

# Interview Questions

### Q1. What is the mathematical equation of a Perceptron?

**Answer:**

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

---

### Q2. What is the purpose of weights?

**Answer:**

Weights determine how important each input feature is in making the prediction.

---

### Q3. Why is bias needed?

**Answer:**

Bias shifts the decision boundary, allowing the model to classify data more flexibly instead of forcing the boundary through the origin.

---

### Q4. What is the weighted sum?

**Answer:**

The weighted sum is the linear combination of the inputs and weights plus the bias:

\[
z = \sum_{i=1}^{n} w_i x_i + b
\]

It is the input to the activation function.

---

# Practice Questions

## Conceptual

1. Explain the role of weights in a Perceptron.
2. Why is bias important?
3. Differentiate between an input feature and a weight.
4. What is the weighted sum?

---

## Numerical

### Question 1

Given

```
x₁ = 3

x₂ = 4

w₁ = 2

w₂ = -1

b = 5
```

Calculate the weighted sum.

**Answer:**

\[
z = 2(3) + (-1)(4) + 5 = 7
\]

---

### Question 2

Given

```
x₁ = 5

x₂ = 2

w₁ = -2

w₂ = 4

b = 1
```

Find the value of

\[
z
\]

---

## MCQs

### 1. Which parameter shifts the decision boundary?

A. Weight

B. Bias

C. Input

D. Activation Function

**Answer:** B

---

### 2. The weighted sum is represented by

A. y

B. x

C. z

D. η

**Answer:** C

---

### 3. The dot product computes

A. Maximum value

B. Average

C. Weighted sum

D. Bias

**Answer:** C

---

# What's Next?

In **Chapter 3**, we will study the **Activation Function (Step Function)**.

Topics include:

- Why the weighted sum is not the final prediction.
- Step Activation Function.
- Binary outputs.
- Thresholding.
- Decision making in a Perceptron.
- Numerical examples using the activation function.
