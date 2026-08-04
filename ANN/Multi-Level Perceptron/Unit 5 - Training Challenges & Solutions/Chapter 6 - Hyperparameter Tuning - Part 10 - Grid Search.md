# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 10 – Grid Search

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Grid Search is.
- Learn how Grid Search works.
- Understand why Grid Search is used.
- Learn its advantages and limitations.
- Understand when Grid Search should and should not be used.

---

# 1. Introduction

Suppose you are training a neural network.

You must choose

```text
Learning Rate

Batch Size

Optimizer
```

Which combination is the best?

Instead of guessing,

we can systematically test every possible combination.

This method is called

> **Grid Search**

---

# 2. What is Grid Search?

Grid Search is

> **A hyperparameter tuning technique that evaluates every possible combination of specified hyperparameter values.**

It searches through a predefined grid of values.

---

# 3. Why is Grid Search Needed?

Suppose we want to tune

```text
Learning Rate

↓

0.1

0.01

0.001
```

and

```text
Batch Size

↓

32

64
```

Which combination is best?

Grid Search tests

```text
(0.1,32)

(0.1,64)

(0.01,32)

(0.01,64)

(0.001,32)

(0.001,64)
```

Every combination is evaluated.

---

# 4. How Grid Search Works

The workflow is

```text
Choose Hyperparameter Values

↓

Generate Every Combination

↓

Train Model

↓

Evaluate Validation Performance

↓

Repeat

↓

Select Best Combination
```

---

# 5. Example

Suppose

Learning Rate

```text
0.1

0.01

0.001
```

Optimizer

```text
SGD

Adam
```

Batch Size

```text
32

64
```

Total combinations

```text
3 × 2 × 2

=

12 Models
```

Grid Search trains

```text
12 Different Models
```

The model with the best validation score is selected.

---

# 6. Visual Representation

Imagine a table.

| Learning Rate | Batch Size |
|---------------|-----------:|
| 0.1 | 32 |
| 0.1 | 64 |
| 0.01 | 32 |
| 0.01 | 64 |
| 0.001 | 32 |
| 0.001 | 64 |

Each row represents

```text
One Complete Training Experiment
```

---

# 7. Advantages of Grid Search

### Exhaustive Search

Every possible combination is tested.

No specified combination is missed.

---

### Simple

Easy to understand and implement.

---

### Reliable

If the best combination exists inside the search grid,

Grid Search will find it.

---

### Reproducible

Running the same Grid Search again produces identical combinations.

---

# 8. Limitations of Grid Search

### Computationally Expensive

Suppose

```text
10 Hyperparameters

↓

10 Values Each
```

Total combinations

```text
10^10

=

10 Billion Models
```

Clearly,

this is impractical.

---

### Slow

Every combination requires

- Training
- Validation
- Performance evaluation

Training hundreds or thousands of models can take days or weeks.

---

### Limited by the Search Grid

Suppose

```text
Learning Rate

↓

0.1

0.01

0.001
```

The true best Learning Rate might be

```text
0.005
```

Grid Search cannot discover it,

because it only evaluates the values that were explicitly provided.

---

# 9. Time Complexity

Suppose

| Hyperparameter | Values |
|---------------|-------:|
| Learning Rate | 5 |
| Batch Size | 4 |
| Optimizer | 3 |

Total experiments

```text
5 × 4 × 3

=

60 Models
```

Adding more hyperparameters increases the search space exponentially.

This phenomenon is known as

```text
Curse of Dimensionality
```

---

# 10. Real-Life Analogy

Imagine buying a laptop.

You choose

```text
3 CPUs

×

4 RAM Options

×

2 SSD Options
```

Possible laptops

```text
3 × 4 × 2

=

24 Configurations
```

You inspect every configuration.

That is exactly how Grid Search works.

---

# 11. Practical Use

Grid Search works well when

- Few hyperparameters
- Small datasets
- Fast model training

It becomes inefficient when

- Many hyperparameters
- Large datasets
- Deep neural networks
- Large Language Models

---

# 12. Framework Example

Scikit-learn provides Grid Search through

```python
from sklearn.model_selection import GridSearchCV
```

Example

```python
param_grid = {
    "learning_rate": [0.1, 0.01, 0.001],
    "batch_size": [32, 64],
    "optimizer": ["adam", "sgd"]
}
```

The framework automatically

- Trains every combination
- Evaluates each model
- Returns the best hyperparameters

---

# 13. One Important Insight

Many beginners think

> **Grid Search always finds the globally best hyperparameters.**

This is not always true.

Grid Search only searches

```text
Inside

Your Search Grid
```

If the optimal value is outside the predefined grid,

Grid Search cannot find it.

---

# Visual Summary

```text
Choose Hyperparameters

↓

Generate All Combinations

↓

Train Model

↓

Evaluate Performance

↓

Repeat

↓

Select Best Combination
```

---

# Advantages vs Limitations

| Advantages | Limitations |
|------------|-------------|
| Exhaustive search | Computationally expensive |
| Easy to implement | Slow for large models |
| Guaranteed best combination within the grid | Cannot find values outside the predefined grid |
| Reproducible | Search space grows exponentially |

---

# Interview Questions

## Q1. What is Grid Search?

**Answer**

Grid Search is a hyperparameter tuning technique that evaluates every possible combination of predefined hyperparameter values.

---

## Q2. Why is Grid Search called an exhaustive search?

**Answer**

Because it systematically evaluates every combination within the specified search space.

---

## Q3. What is the main disadvantage of Grid Search?

**Answer**

Its computational cost grows rapidly as the number of hyperparameters and candidate values increases.

---

## Q4. Can Grid Search find values outside the predefined search grid?

**Answer**

No.

It evaluates only the values explicitly specified by the user.

---

## Q5. When is Grid Search most suitable?

**Answer**

For problems with a small number of hyperparameters and relatively inexpensive model training.

---

# Summary

Grid Search is a systematic hyperparameter optimization technique that evaluates every possible combination of predefined hyperparameter values.

It is simple, reliable, and guarantees finding the best combination within the specified search space.

However, its computational cost grows exponentially with the number of hyperparameters, making it less practical for large Deep Learning models.

---

# Key Takeaways

✔ Grid Search tests every possible hyperparameter combination.

✔ It is an exhaustive search method.

✔ It is simple and easy to implement.

✔ It becomes computationally expensive as the search space grows.

✔ It can only evaluate values included in the predefined search grid.

✔ Grid Search is best suited for small search spaces.

---

# Next Part

## **Part 11 – Random Search**

In the next chapter, we will study **Random Search**, understand why it often outperforms Grid Search for high-dimensional problems, learn how it samples hyperparameters randomly, and compare its efficiency with exhaustive search methods.
