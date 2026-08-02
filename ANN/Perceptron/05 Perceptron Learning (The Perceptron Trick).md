# Chapter 05: Perceptron Learning (The Perceptron Trick)

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand how a Perceptron learns from training data, why random weights are insufficient, how incorrect predictions are corrected, and how the decision boundary gradually moves to classify the data correctly.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how learning occurs in a Perceptron.
- Explain the Perceptron Trick.
- Understand why weights are updated.
- Understand how the decision boundary changes during training.
- Visualize learning as an iterative improvement process.

---

# 1. Recap

In previous chapters, we learned

```
Inputs
      │
      ▼
Weighted Sum
      │
      ▼
Activation Function
      │
      ▼
Prediction
```

But one important question still remains.

> **Where do the weights come from?**

Does the computer already know them?

No.

The Perceptron **learns** them from data.

---

# 2. What Does "Learning" Mean?

Learning means

> Finding the best values of the weights and bias so that the Perceptron correctly classifies the training data.

Initially,

the Perceptron knows absolutely nothing.

Therefore,

it starts with **random weights**.

Example

```
w₁ = 0.2

w₂ = -0.7

b = 0.4
```

These values are simply an initial guess.

---

# 3. Why Are Random Weights a Problem?

Suppose the actual dataset looks like this.

```
Class 1

● ● ● ●

------------------------

○ ○ ○ ○

Class 0
```

Now imagine the Perceptron starts with a random decision boundary.

```
●      ○

///////////

●      ○
```

Some points are classified correctly.

Some are classified incorrectly.

The Perceptron must improve this boundary.

---

# 4. The Main Idea Behind Learning

The Perceptron follows one simple rule.

> If the prediction is correct,
>
> do nothing.

> If the prediction is wrong,
>
> change the weights.

This simple idea is called the **Perceptron Learning Rule** or **Perceptron Trick**.

---

# 5. The Learning Cycle

Every training sample follows the same process.

```
Training Example
        │
        ▼
Calculate Weighted Sum
        │
        ▼
Activation Function
        │
        ▼
Prediction
        │
        ▼
Compare with Actual Label
        │
        ▼
Correct?
      /   \
    Yes   No
     │      │
 Keep     Update
Weights   Weights
```

The Perceptron repeats this process for every training example.

---

# 6. Example of Learning

Suppose the training sample is

| Feature | Value |
|---------|------:|
| x₁ | 3 |
| x₂ | 4 |
| Actual Class | 1 |

Current weights

```
w₁ = 0.5

w₂ = -0.3

b = -1
```

Weighted Sum

```
z = w₁x₁ + w₂x₂ + b
```

Suppose

```
z = -2
```

Activation Function

```
Prediction = 0
```

Actual

```
1
```

Prediction

```
0
```

The prediction is wrong.

Therefore,

the Perceptron updates its weights.

---

# 7. Why Update the Weights?

Weights determine

- importance of features
- orientation of the decision boundary

Changing the weights means changing the decision boundary.

Imagine drawing a line on paper.

First attempt

```
● ●

------------

○ ●
```

One point is incorrect.

Erase the line.

Draw again.

```
● ●

///////////

○ ○
```

Now the separation is much better.

The Perceptron performs exactly this process mathematically.

---

# 8. Why Update the Bias?

Bias determines the position of the decision boundary.

Changing only the weights rotates the line.

Changing the bias shifts it.

```
Old Boundary

------------

New Boundary

============
```

Both weights and bias work together to improve classification.

---

# 9. Learning One Sample at a Time

Unlike some algorithms,

the Perceptron processes one training sample at a time.

```
Sample 1

↓

Update

↓

Sample 2

↓

Update

↓

Sample 3

↓

Update
```

This type of learning is called **Online Learning** or **Sequential Learning**.

---

# 10. One Complete Pass

Suppose the dataset contains

```
100 samples
```

The Perceptron processes

```
Sample 1

↓

Sample 2

↓

...

↓

Sample 100
```

This is called **one Epoch**.

After one epoch,

if mistakes still exist,

the Perceptron starts another epoch.

---

# 11. Visualizing Learning

Initially

```
Wrong Decision Boundary

●     ○

///////////

●     ○
```

After several updates

```
Better Boundary

● ●

------------

○ ○
```

After more updates

```
Final Boundary

● ● ●

=================

○ ○ ○
```

Notice how the line gradually moves toward the correct position.

---

# 12. Why Is It Called the Perceptron Trick?

Imagine you're separating red and blue marbles with a ruler.

If one marble is on the wrong side,

you slightly rotate or shift the ruler.

After repeating this several times,

all red marbles lie on one side,

and all blue marbles lie on the other.

This simple adjustment strategy is known as the **Perceptron Trick**.

---

# 13. Important Observation

The Perceptron never asks

> "How wrong am I?"

Instead,

it only asks

> "Am I correct or incorrect?"

If the prediction is correct,

nothing changes.

If the prediction is incorrect,

the weights are updated.

This makes the Perceptron learning algorithm very simple.

---

# Common Misconceptions

### Mistake 1

Thinking that learning happens only once.

❌ Incorrect

Learning occurs after every incorrectly classified sample.

---

### Mistake 2

Thinking that weights are fixed.

❌ Incorrect

Weights continuously change during training.

---

### Mistake 3

Thinking that the decision boundary is fixed.

❌ Incorrect

The decision boundary changes after every weight update.

---

# Chapter Summary

The Perceptron starts with random weights and bias.

These values usually produce an incorrect decision boundary.

For every training sample,

the Perceptron predicts a class.

If the prediction is correct,

nothing changes.

If the prediction is wrong,

the weights and bias are modified.

This process is repeated until the decision boundary correctly separates the training data.

---

# Key Takeaways

✔ Learning means finding better weights and bias.

✔ The Perceptron starts with random weights.

✔ Incorrect predictions cause weight updates.

✔ Correct predictions cause no updates.

✔ The decision boundary gradually improves during training.

✔ The Perceptron learns one sample at a time.

---

# Interview Questions

### Q1. What is meant by learning in a Perceptron?

**Answer:**

Learning means adjusting the weights and bias so that the Perceptron correctly classifies the training data.

---

### Q2. Why does the Perceptron start with random weights?

**Answer:**

Initially, the model has no knowledge about the data, so random values are used as the starting point for learning.

---

### Q3. What is the Perceptron Trick?

**Answer:**

The Perceptron Trick is the process of correcting incorrect predictions by updating the weights and bias, thereby gradually improving the decision boundary.

---

### Q4. Does the Perceptron update weights after every prediction?

**Answer:**

No.

Weights are updated only when the prediction is incorrect.

---

# Practice Questions

## Conceptual

1. Explain the Perceptron Learning process.
2. Why are random weights used initially?
3. What happens when the Perceptron predicts correctly?
4. Why does updating the weights improve classification?

---

## MCQs

### 1. The Perceptron starts learning with

A. Perfect weights

B. Random weights

C. Zero error

D. Gradient Descent

**Answer:** B

---

### 2. The Perceptron updates its weights when

A. Every prediction

B. Only after correct predictions

C. Only after incorrect predictions

D. Never

**Answer:** C

---

### 3. The purpose of updating weights is to

A. Increase the dataset size

B. Improve the decision boundary

C. Remove bias

D. Increase the number of inputs

**Answer:** B

---

# What's Next?

In **Chapter 6**, we will study the **Weight Update Rule**.

Topics include:

- The Perceptron Update Equation
- Error Term
- Learning Rate
- Updating Weights
- Updating Bias
- Complete Numerical Examples
- Geometric Interpretation of Weight Updates
