# Unit 4 – Learning in Neural Networks

# Chapter 1 – Introduction to Learning in Neural Networks

## Part 1 – Why Do Neural Networks Need Learning?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what "learning" means in a neural network.
- Learn why Forward Propagation alone is not sufficient.
- Understand how a neural network improves over time.
- Differentiate between prediction and learning.
- Understand the complete learning cycle of an Artificial Neural Network (ANN).

---

# 1. What Does Learning Mean?

When humans learn, they improve by learning from their mistakes.

For example,

Imagine a student taking a mathematics exam.

```text
Exam

↓

Mistakes

↓

Understands Errors

↓

Studies Again

↓

Scores Better
```

The student becomes better because they analyze their mistakes and improve.

A neural network learns in a very similar way.

Instead of marks,

it uses a **Loss Function** to measure how wrong its prediction is.

---

# 2. Forward Propagation Only Makes Predictions

From **Unit 1**, we learned how a neural network makes predictions.

```text
Input

↓

Weighted Sum (z)

↓

Activation Function

↓

Prediction
```

This process is called

> **Forward Propagation**

Forward Propagation answers only one question:

> **"Given the current weights, what is the prediction?"**

Example

Suppose

```text
Input = [2,3]

↓

Prediction = 0.91
```

Forward Propagation stops here.

It does **not** know

- whether the prediction is correct,
- how wrong the prediction is,
- which weights caused the error.

It simply produces an output.

---

# 3. How Does the Network Know It Made a Mistake?

This is where the **Loss Function** comes in.

From **Unit 2**, we learned

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss Value
```

The Loss Function tells the neural network

> **How wrong its prediction is.**

Example 1

```text
Prediction = 0.91

Actual = 1

↓

Loss = Small
```

Good prediction.

---

Example 2

```text
Prediction = 0.91

Actual = 0

↓

Loss = Large
```

Bad prediction.

Now the network knows

> "I made a mistake."

---

# 4. The Biggest Question

Knowing that a mistake exists is **not enough**.

The neural network must answer another question.

> **Which weights caused the mistake?**

Consider a simple neural network.

```text
Input

↓

W₁

↓

Hidden Layer

↓

W₂

↓

Output Layer

↓

Prediction
```

Suppose the prediction is incorrect.

Which weight should change?

- W₁?
- W₂?
- Both?

And

by how much?

Neither Forward Propagation nor the Loss Function can answer these questions.

---

# 5. What Does Learning Mean?

Learning means

> **Changing the weights so that future predictions become better.**

Think of a child learning mathematics.

### First Attempt

```text
Question

↓

Wrong Answer
```

The teacher says

```text
Wrong.
```

Is that enough?

No.

The teacher explains

- where the mistake occurred,
- why it happened,
- how to correct it.

The child studies again.

### Second Attempt

```text
Better Answer
```

### Third Attempt

```text
Correct Answer
```

The child learns from mistakes.

A neural network follows the same principle.

---

# 6. The Complete Learning Cycle

Every neural network repeatedly performs the following steps.

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Measure Error

↓

???

↓

Update Weights

↓

Repeat
```

There is one missing step.

```text
???
```

This missing step is

> **Backpropagation**

---

# 7. What is Backpropagation?

Very simply,

Backpropagation answers the question

> **Which weights caused the error?**

Suppose

```text
Loss = High
```

Backpropagation might determine

```text
Weight W₁

↓

30% Responsible

Weight W₂

↓

70% Responsible
```

The optimizer then updates the weights accordingly.

---

# 8. Connecting Everything We Have Learned

## Unit 1

```text
Input

↓

Forward Propagation

↓

Prediction
```

Answers

> **What does the network predict?**

---

## Unit 2

```text
Prediction

↓

Loss Function

↓

Loss
```

Answers

> **How wrong is the prediction?**

---

## Unit 3

```text
Gradients

↓

Optimizer

↓

Update Weights
```

Answers

> **How should the weights be updated?**

---

## Unit 4

This unit answers

```text
Loss

↓

Backpropagation

↓

Gradients
```

In other words,

> **How are the gradients computed?**

---

# 9. A Common Misconception

Many beginners think

```text
Loss

↓

Gradient Descent
```

This is **incorrect**.

The correct learning pipeline is

```text
Loss

↓

Backpropagation

↓

Gradients

↓

Optimizer

↓

Update Weights
```

Gradient Descent cannot work without gradients.

Backpropagation computes those gradients.

The optimizer simply uses them.

---

# 10. Real-Life Analogy

Imagine taking a school examination.

```text
Exam

↓

Score = 35/100
```

The score tells you

> "You performed poorly."

But it does not tell you

- Which chapter was weak?
- Which question was wrong?
- Which concept needs improvement?

Now imagine the teacher checks every answer.

```text
Question 2

↓

Wrong

Question 5

↓

Wrong

Question 8

↓

Correct
```

Now you know exactly where to improve.

Backpropagation plays the role of this teacher.

It identifies **which weights contributed most to the prediction error**.

---

# 11. The Complete ANN Learning Process

By combining everything learned so far,

the complete learning pipeline becomes

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss

↓

Backpropagation

↓

Gradients

↓

Optimizer

↓

Updated Weights

↓

Better Prediction

↓

Repeat
```

Every iteration makes the neural network a little better.

After thousands of iterations,

the model learns patterns from the training data.

---

# Interview Questions

## Q1. What does learning mean in a neural network?

**Answer**

Learning is the process of improving the model by updating its weights based on prediction errors.

---

## Q2. Is Forward Propagation enough for learning?

**Answer**

No.

Forward Propagation only produces predictions.

It does not update the weights.

---

## Q3. Which component measures prediction error?

**Answer**

The Loss Function.

---

## Q4. Which component determines how each weight contributed to the error?

**Answer**

Backpropagation.

---

## Q5. Which component actually updates the weights?

**Answer**

The Optimizer (such as Gradient Descent, Momentum, RMSProp, or Adam).

---

# Summary

Learning is the process that enables a neural network to improve over time.

Forward Propagation generates predictions, while the Loss Function measures how wrong those predictions are.

However, knowing the error alone is not enough.

The network must determine **which weights caused the error**.

This is the purpose of **Backpropagation**, which computes gradients for every parameter.

These gradients are then used by an **Optimizer** to update the weights.

By repeating this learning cycle thousands of times, the neural network gradually becomes more accurate.

---

# Key Takeaways

✔ Learning means improving the model using previous mistakes.

✔ Forward Propagation only makes predictions.

✔ The Loss Function measures prediction error.

✔ Backpropagation computes the gradients.

✔ The Optimizer updates the weights using those gradients.

✔ Learning is an iterative process repeated until the model converges.

✔ The complete learning pipeline is

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Backpropagation

↓

Gradients

↓

Optimizer

↓

Updated Weights

↓

Repeat
```

---

## Next Part

**Part 2 – What is Backpropagation?**

In the next chapter, we will formally introduce the **Backpropagation algorithm**, understand why it is called *Backpropagation*, and build the intuition behind how errors travel backward through a neural network before studying the mathematical derivation.
