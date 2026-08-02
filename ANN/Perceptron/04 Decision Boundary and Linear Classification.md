# Chapter 04: Decision Boundary and Linear Classification

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand what a Decision Boundary is, how a Perceptron separates different classes, why it is called a Linear Classifier, and how the equation
>
> \[
> w^Tx+b=0
> \]
>
> represents the boundary between two classes.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the concept of a Decision Boundary.
- Explain why the Perceptron is a Linear Classifier.
- Derive the equation of the Decision Boundary.
- Understand how weights and bias affect the boundary.
- Interpret Perceptron classification geometrically.
- Understand hyperplanes in higher dimensions.

---

# 1. Recap

In the previous chapter we learned

```
Inputs

↓

Weighted Sum

↓

Activation Function

↓

Prediction
```

The weighted sum is

\[
z=w^Tx+b
\]

The Step Function says

\[
f(z)=
\begin{cases}
1,&z\ge0\\
0,&z<0
\end{cases}
\]

Now an important question arises.

> **How does the Perceptron know where Class 0 ends and Class 1 begins?**

The answer is

**Decision Boundary**

---

# 2. What is a Decision Boundary?

A Decision Boundary is the line (or surface) that separates different classes.

Imagine classifying students.

```
Pass

● ● ● ●

--------------------

○ ○ ○ ○

Fail
```

The line separating

```
Pass

and

Fail
```

is called the **Decision Boundary**.

---

# Definition

A **Decision Boundary** is the boundary that divides the feature space into different prediction regions.

Every point on one side belongs to one class.

Every point on the other side belongs to another class.

---

# 3. Where Does the Decision Boundary Come From?

Recall

\[
z=w^Tx+b
\]

Prediction

```
z ≥ 0

↓

Class 1
```

Prediction

```
z < 0

↓

Class 0
```

Now ask

Where does the prediction change?

Exactly at

```
z = 0
```

Therefore,

the Decision Boundary is

\[
w^Tx+b=0
\]

This equation is the foundation of linear classification in the Perceptron. :contentReference[oaicite:1]{index=1}

---

# 4. Why Set z = 0?

The Step Function changes its output only at

```
z = 0
```

For example

```
z = -3

↓

Output = 0
```

```
z = 5

↓

Output = 1
```

Between these two regions lies

```
z = 0
```

This is exactly the Decision Boundary.

---

# 5. Visual Representation

```
Class 1

● ● ● ●

=====================

Decision Boundary

=====================

○ ○ ○ ○

Class 0
```

Everything above belongs to one class.

Everything below belongs to the other.

---

# 6. Numerical Example

Suppose

\[
2x_1+x_2-6=0
\]

This is our Decision Boundary.

Now classify three points.

---

### Point A

\[
(4,2)
\]

Substitute

\[
2(4)+2-6
=
4
\]

Since

```
4 > 0
```

Prediction

```
Class 1
```

---

### Point B

\[
(1,1)
\]

Substitute

\[
2(1)+1-6
=
-3
\]

Prediction

```
Class 0
```

---

### Point C

\[
(2,2)
\]

Substitute

\[
2(2)+2-6
=
0
\]

This point lies exactly on the Decision Boundary.

---

# 7. Geometric Interpretation

Think of the Decision Boundary as a wall.

```
Cats

🐱 🐱 🐱

=================

Dogs

🐶 🐶 🐶
```

The wall separates the two categories.

The Perceptron tries to place this wall so that every class lies on its correct side.

---

# 8. Why Is the Perceptron Called a Linear Classifier?

The equation

\[
w^Tx+b=0
\]

is a **linear equation**.

A linear equation produces

- A line in 2D
- A plane in 3D
- A hyperplane in higher dimensions

Since the Perceptron separates data using a linear equation,

it is called a **Linear Classifier**.

---

# 9. Effect of Weights

Weights determine the **orientation (slope)** of the Decision Boundary.

Suppose

\[
x+y=0
\]

This gives one line.

Now change it to

\[
3x+y=0
\]

The line rotates.

```
Old Line

//////////

New Line

\\\\\\\\\\
```

Changing weights changes the direction of the boundary.

---

# 10. Effect of Bias

Bias shifts the Decision Boundary without changing its orientation.

Example

\[
x+y=0
\]

Now

\[
x+y-5=0
\]

The entire line moves.

```
Old Boundary

------------

New Boundary

============
```

Bias changes **position**, not **rotation**.

---

# Summary Table

| Parameter | Effect |
|-----------|--------|
| Weight | Rotates the Decision Boundary |
| Bias | Shifts the Decision Boundary |

---

# 11. Decision Regions

The Decision Boundary divides the feature space into two regions.

```
Region 1

↓

Predict Class 1

================

Decision Boundary

================

Region 2

↓

Predict Class 0
```

Every new data point is assigned to one of these regions.

---

# 12. Hyperplane

In Machine Learning,

the word

**Hyperplane**

means a generalized Decision Boundary.

Dimensions:

```
1D

↓

Point
```

```
2D

↓

Line
```

```
3D

↓

Plane
```

```
4D and above

↓

Hyperplane
```

Since real datasets often contain many features,

the Perceptron usually learns a **Hyperplane** rather than just a line.

---

# 13. Real-Life Example

Suppose a bank decides loan approval based on

```
Income

Credit Score
```

People with

```
High Income

Good Credit Score
```

↓

Loan Approved

Others

↓

Rejected

The bank's rule creates a Decision Boundary separating approved and rejected applicants.

---

# Common Mistakes

### Mistake 1

Thinking the Decision Boundary contains training samples.

❌ Incorrect

It separates the samples.

---

### Mistake 2

Thinking the boundary predicts classes.

❌ Incorrect

The boundary itself represents

```
z = 0
```

Predictions are made based on which side of the boundary a point lies.

---

### Mistake 3

Confusing weights and bias.

Weights rotate the boundary.

Bias shifts the boundary.

---

# Chapter Summary

The Perceptron divides the feature space into two regions.

The equation

\[
w^Tx+b=0
\]

defines the Decision Boundary.

Points with

\[
z\ge0
\]

belong to one class.

Points with

\[
z<0
\]

belong to the other.

Because this boundary is linear,

the Perceptron is called a **Linear Classifier**.

---

# Key Takeaways

✔ Decision Boundary separates different classes.

✔ Decision Boundary is obtained by setting

\[
z=0
\]

✔ Mathematical equation

\[
w^Tx+b=0
\]

✔ Weights rotate the boundary.

✔ Bias shifts the boundary.

✔ The Perceptron is a Linear Classifier.

✔ In higher dimensions the Decision Boundary is called a Hyperplane.

---

# Interview Questions

### Q1. What is a Decision Boundary?

**Answer:**

A Decision Boundary is the boundary that separates different prediction classes.

---

### Q2. Why is the equation

\[
w^Tx+b=0
\]

called the Decision Boundary?

**Answer:**

Because it is the point where the Perceptron changes its prediction from one class to another.

---

### Q3. Why is the Perceptron called a Linear Classifier?

**Answer:**

Because its Decision Boundary is always a linear equation.

---

### Q4. What is a Hyperplane?

**Answer:**

A Hyperplane is the generalized Decision Boundary in higher-dimensional feature spaces.

---

# Practice Questions

## Conceptual

1. Explain the concept of a Decision Boundary.
2. Why do we set

\[
z=0
\]

to obtain the Decision Boundary?

3. Differentiate between a line, plane and hyperplane.

4. Explain how weights affect the Decision Boundary.

---

## Numerical

### Question 1

Given

\[
x+y-5=0
\]

Classify

```
(3,4)

(1,2)

(2,3)
```

---

### Question 2

Determine whether

```
(4,5)
```

belongs to Class 0 or Class 1 for

\[
2x+y-8=0
\]

---

## MCQs

### 1. The Decision Boundary is obtained when

A. z=1

B. z=-1

C. z=0

D. z=10

**Answer:** C

---

### 2. The Perceptron is called a Linear Classifier because

A. It uses linear regression

B. It predicts probabilities

C. It separates data using a linear equation

D. It uses ReLU

**Answer:** C

---

### 3. Changing the bias mainly

A. Rotates the boundary

B. Changes activation

C. Shifts the boundary

D. Removes weights

**Answer:** C

---

# What's Next?

In **Chapter 5**, we will study **Perceptron Learning (The Perceptron Trick).**

Topics include:

- Why random weights fail.
- How the Perceptron learns from mistakes.
- Why weights are updated.
- How the Decision Boundary gradually moves.
- The intuition behind the Perceptron Learning Process.
