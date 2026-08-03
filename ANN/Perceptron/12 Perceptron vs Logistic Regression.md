# Chapter 12: Perceptron vs Logistic Regression

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand the differences between the Perceptron and Logistic Regression, why Logistic Regression replaced the Perceptron in many applications, and how both algorithms relate to modern Neural Networks.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Compare Perceptron and Logistic Regression.
- Understand the difference between Step and Sigmoid activation functions.
- Understand why Logistic Regression predicts probabilities.
- Explain why Logistic Regression uses Gradient Descent.
- Explain why Logistic Regression performs better than the original Perceptron.
- Understand how Logistic Regression serves as a bridge toward Deep Learning.

---

# 1. Recap

The original Perceptron

- Uses the Step Function
- Performs Binary Classification
- Learns using the Perceptron Learning Rule
- Produces only 0 or 1

Now researchers wanted a better classifier.

The result was

```
Logistic Regression
```

---

# 2. Why Was Logistic Regression Introduced?

The Perceptron has several limitations.

- Produces only binary outputs
- Does not predict probabilities
- Cannot use Gradient Descent directly
- Uses a non-differentiable Step Function

Researchers wanted a model that

✔ Predicts probabilities

✔ Uses Gradient Descent

✔ Learns more smoothly

This led to Logistic Regression.

---

# 3. Similarities

Both algorithms

- Perform Binary Classification
- Use weighted sums
- Learn linear decision boundaries
- Require labeled training data

Mathematical model

$$
z=w^Tx+b
$$

Both algorithms compute exactly the same weighted sum.

The difference comes **after** this computation.

---

# 4. Activation Function

## Perceptron

Uses

```
Step Function
```

$$
f(z)=
\begin{cases}
1,&z\ge0\\
0,&z<0
\end{cases}
$$

Output

```
0

or

1
```

---

## Logistic Regression

Uses the

```
Sigmoid Function
```

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Output

```
0.00

↓

1.00
```

The output is a probability.

---

# 5. Visual Comparison

## Step Function

```
Output

1 ───────────

|

|

0______________
```

Sudden jump.

---

## Sigmoid Function

```
Output

1 |

  |          _____

  |       __/

  |    __/

0 |___/

      z
```

Smooth curve.

---

# 6. Output Comparison

Suppose

```
Input Image
```

Perceptron

```
Prediction

↓

1
```

That's all.

---

Logistic Regression

```
Prediction

↓

0.94
```

Meaning

```
94% probability
```

Since

```
0.94 > 0.5
```

Final prediction

```
Class 1
```

---

# 7. Why Are Probabilities Better?

Imagine two students.

Student A

```
51%
```

Student B

```
99%
```

Perceptron

```
Pass

Pass
```

Both look identical.

---

Logistic Regression

```
0.51

0.99
```

Now we know

Student B is much more confidently classified.

---

# 8. Learning Algorithm

## Perceptron

Uses

$$
w=w+\eta(y-\hat y)x
$$

Weights change only after incorrect predictions.

---

## Logistic Regression

Uses Gradient Descent

$$
w=w-\eta\frac{\partial L}{\partial w}
$$

The model continuously minimizes the loss.

---

# 9. Loss Function

## Perceptron

Uses only the prediction error

$$
y-\hat y
$$

---

## Logistic Regression

Uses

```
Binary Cross-Entropy Loss
```

This loss function provides smoother optimization and is compatible with Gradient Descent.

---

# 10. Why Can Logistic Regression Use Gradient Descent?

The Sigmoid Function is

```
Continuous
```

and

```
Differentiable
```

Therefore,

its derivative exists.

Gradient Descent requires derivatives,

so Logistic Regression can be optimized efficiently.

---

# 11. Decision Boundary

An interesting fact

Both models learn

$$
w^Tx+b=0
$$

Therefore,

both are

```
Linear Classifiers
```

The difference lies in

- how they learn
- what they output

not in the shape of the decision boundary.

---

# 12. Confidence

Suppose

Prediction

```
0.52
```

This means

```
Probably Class 1
```

Now

Prediction

```
0.99
```

This means

```
Almost certainly Class 1
```

This confidence information is extremely useful in

- Medical Diagnosis
- Fraud Detection
- Finance
- Autonomous Driving

---

# 13. Advantages of Logistic Regression

Compared to the original Perceptron

✔ Predicts probabilities

✔ Uses Gradient Descent

✔ Uses differentiable activation

✔ Better optimization

✔ More stable learning

✔ Foundation of Neural Networks

---

# 14. Comparison Table

| Feature | Perceptron | Logistic Regression |
|----------|------------|---------------------|
| Task | Binary Classification | Binary Classification |
| Weighted Sum | ✔ | ✔ |
| Decision Boundary | Linear | Linear |
| Activation | Step | Sigmoid |
| Output | 0 or 1 | Probability (0–1) |
| Gradient Descent | ✘ | ✔ |
| Differentiable | ✘ | ✔ |
| Confidence Score | ✘ | ✔ |
| Loss | Simple error-based update | Binary Cross-Entropy |

---

# 15. Relationship to Deep Learning

Deep Learning neurons

```
Weighted Sum

↓

Activation Function

↓

Loss

↓

Gradient Descent

↓

Update Weights
```

Notice

This workflow is almost identical to Logistic Regression.

The only difference is

Deep Learning stacks many such neurons together.

---

# 16. Historical Evolution

```
Perceptron (1957)

↓

Logistic Regression

↓

Multi-Layer Perceptron

↓

Neural Networks

↓

Deep Learning

↓

Large Language Models
```

Every stage improved the previous one.

---

# Common Misconceptions

### Mistake 1

Thinking Logistic Regression performs regression.

❌ Incorrect.

Despite its name,

it is a **classification algorithm**.

---

### Mistake 2

Thinking Logistic Regression and Perceptron are identical.

❌ Incorrect.

Their mathematical foundations differ after the weighted sum.

---

### Mistake 3

Thinking probabilities are the final prediction.

❌ Incorrect.

Probabilities are converted into class labels using a threshold (commonly 0.5).

---

# Chapter Summary

The Perceptron and Logistic Regression are both binary classifiers.

Both compute the same weighted sum,

$$
w^Tx+b
$$

However,

the Perceptron uses the Step Function and produces only binary outputs,

while Logistic Regression uses the Sigmoid Function and predicts probabilities.

Because Logistic Regression uses differentiable functions,

it can be optimized using Gradient Descent,

making it much more suitable for modern Machine Learning.

---

# Key Takeaways

✔ Both are Binary Classifiers.

✔ Both compute

$$
w^Tx+b
$$

✔ Perceptron uses the Step Function.

✔ Logistic Regression uses the Sigmoid Function.

✔ Logistic Regression predicts probabilities.

✔ Logistic Regression uses Gradient Descent.

✔ Logistic Regression forms the foundation of many modern neural network concepts.

---

# Interview Questions

### Q1. What is the main difference between the Perceptron and Logistic Regression?

**Answer:**

The Perceptron uses a Step Function and predicts only binary labels, whereas Logistic Regression uses a Sigmoid Function and predicts probabilities.

---

### Q2. Why can Logistic Regression use Gradient Descent?

**Answer:**

Because the Sigmoid Function is differentiable, allowing gradients to be computed.

---

### Q3. Are both algorithms linear classifiers?

**Answer:**

Yes.

Both learn linear decision boundaries of the form

$$
w^Tx+b=0
$$

---

### Q4. Why is Logistic Regression preferred in practice?

**Answer:**

Because it predicts probabilities, uses Gradient Descent, has smoother optimization, and generally performs better than the original Perceptron.

---

# Practice Questions

## Conceptual

1. Compare the Perceptron and Logistic Regression.
2. Why is the Sigmoid Function preferred over the Step Function?
3. Why does Logistic Regression predict probabilities?
4. Explain why Logistic Regression is considered a bridge to Deep Learning.

---

## MCQs

### 1. Logistic Regression uses

A. Step Function

B. ReLU

C. Sigmoid Function

D. Tanh

**Answer:** C

---

### 2. Which algorithm predicts probabilities?

A. Perceptron

B. Logistic Regression

C. K-Means

D. Decision Tree

**Answer:** B

---

### 3. Which algorithm can directly use Gradient Descent?

A. Original Perceptron

B. Logistic Regression

C. Naive Bayes

D. KNN

**Answer:** B

---

### 4. The output of Logistic Regression lies between

A. -1 and 1

B. 0 and 10

C. 0 and 1

D. -∞ and +∞

**Answer:** C

---

# What's Next?

In **Chapter 13**, we will study

**Multi-Layer Perceptron (MLP)**

Topics include:

- Why Hidden Layers are needed
- Solving the XOR problem
- Architecture of an MLP
- Forward Propagation
- Activation Functions (Sigmoid, ReLU, Tanh)
- Why MLP is the foundation of Deep Learning
