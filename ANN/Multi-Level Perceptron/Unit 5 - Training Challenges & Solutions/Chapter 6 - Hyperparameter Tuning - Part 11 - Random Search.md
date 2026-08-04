# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 11 – Random Search

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Random Search is.
- Learn how Random Search works.
- Compare Random Search with Grid Search.
- Understand why Random Search is often more efficient.
- Learn when Random Search should be used.

---

# 1. Introduction

In the previous chapter,

we learned that

```text
Grid Search

↓

Tests Every Possible Combination
```

Although Grid Search is systematic,

it becomes very expensive when the number of hyperparameters increases.

An alternative approach is

```text
Random Search
```

Instead of testing every combination,

Random Search evaluates only randomly selected combinations.

---

# 2. What is Random Search?

Random Search is

> **A hyperparameter optimization technique that randomly samples combinations from the search space instead of evaluating every possible combination.**

Unlike Grid Search,

it does **not** test every configuration.

---

# 3. Why Use Random Search?

Suppose we have

```text
Learning Rate

↓

100 Possible Values

Batch Size

↓

10 Values

Optimizer

↓

5 Values
```

Grid Search would evaluate

```text
100 × 10 × 5

=

5000 Models
```

Instead,

Random Search might evaluate only

```text
100 Random Combinations
```

This saves a tremendous amount of computation.

---

# 4. How Random Search Works

The workflow is

```text
Define Search Space

↓

Randomly Select Hyperparameters

↓

Train Model

↓

Evaluate Validation Performance

↓

Repeat

↓

Select Best Combination
```

Unlike Grid Search,

each experiment uses a randomly selected configuration.

---

# 5. Example

Suppose

Learning Rate

```text
0.1

0.01

0.001

0.0001
```

Batch Size

```text
16

32

64

128
```

Optimizer

```text
SGD

Adam
```

Grid Search would test

```text
4 × 4 × 2

=

32 Models
```

Random Search may evaluate only

```text
10 Random Models
```

Example

```text
(0.01,32,Adam)

(0.0001,64,SGD)

(0.1,128,Adam)

...

10 Random Combinations
```

---

# 6. Why Does Random Search Work Well?

In many Machine Learning problems,

only a few hyperparameters have a large impact on performance.

For example,

```text
Learning Rate

↓

Very Important
```

```text
Batch Size

↓

Moderately Important
```

```text
Optimizer

↓

Less Sensitive
```

Grid Search wastes time testing many unimportant combinations.

Random Search explores more unique values of the important hyperparameters.

---

# 7. Visual Comparison

### Grid Search

```text
□□□□□□□□□□□□□□□□

Tests Every Point
```

---

### Random Search

```text
■ □ □ ■ □ □

□ ■ □ □ □ ■

□ □ ■ □ ■ □

Random Samples
```

Grid Search covers every point.

Random Search explores different regions of the search space.

---

# 8. Advantages of Random Search

### Faster

Only a subset of combinations is evaluated.

---

### More Efficient

Can explore large search spaces quickly.

---

### Better for High Dimensions

Works well when many hyperparameters exist.

---

### Flexible

You can decide in advance

```text
Train

20 Models

50 Models

100 Models
```

depending on available computation.

---

# 9. Limitations of Random Search

### No Guarantee

The optimal combination might never be sampled.

---

### Random Results

Different runs may produce different hyperparameters.

---

### Depends on Sampling Budget

The fewer models you evaluate,

the greater the chance of missing good combinations.

---

# 10. Grid Search vs Random Search

Suppose

```text
Grid Search

↓

1000 Models
```

Random Search

```text
↓

100 Models
```

If Random Search discovers nearly the same performance,

it saves

```text
900 Model Trainings
```

This is why Random Search is widely used in Deep Learning.

---

# 11. Practical Use

Random Search is recommended for

- Deep Neural Networks
- CNNs
- Transformers
- Large datasets
- Large search spaces

Grid Search is usually preferred only when

- Search space is very small
- Model training is inexpensive

---

# 12. Framework Example

Scikit-learn provides Random Search through

```python
from sklearn.model_selection import RandomizedSearchCV
```

Example

```python
param_distributions = {
    "learning_rate": [0.1, 0.01, 0.001, 0.0001],
    "batch_size": [16, 32, 64, 128],
    "optimizer": ["adam", "sgd"]
}
```

Instead of evaluating every combination,

the framework randomly samples a specified number of configurations.

---

# 13. Real-Life Analogy

Imagine choosing a restaurant.

### Grid Search

```text
Visit

Every Restaurant

↓

Choose Best
```

This takes a long time.

---

### Random Search

```text
Visit

Random Restaurants

↓

Choose Best Among Them
```

Much faster,

and often good enough.

---

# 14. One Important Insight

Many beginners think

> **Random Search is less intelligent because it is random.**

This is incorrect.

Research has shown that Random Search often performs **better than Grid Search** when many hyperparameters are involved because it explores a wider variety of values for the most important hyperparameters.

---

# Visual Summary

```text
Define Search Space

↓

Randomly Sample

↓

Train Model

↓

Evaluate Performance

↓

Repeat

↓

Best Configuration
```

---

# Grid Search vs Random Search

| Grid Search | Random Search |
|--------------|---------------|
| Tests every combination | Tests randomly selected combinations |
| Exhaustive | Sampling-based |
| Very expensive | More computationally efficient |
| Best within predefined grid | Best among sampled configurations |
| Better for small search spaces | Better for large search spaces |

---

# Interview Questions

## Q1. What is Random Search?

**Answer**

Random Search is a hyperparameter optimization technique that randomly samples hyperparameter combinations instead of evaluating every possible combination.

---

## Q2. Why is Random Search often faster than Grid Search?

**Answer**

Because it evaluates only a subset of the search space rather than every possible combination.

---

## Q3. Does Random Search guarantee finding the best hyperparameters?

**Answer**

No.

It finds the best configuration among the randomly sampled combinations.

---

## Q4. Why can Random Search outperform Grid Search?

**Answer**

Because it explores a larger variety of values for important hyperparameters while avoiding exhaustive evaluation of less important combinations.

---

## Q5. When is Random Search preferred?

**Answer**

For large search spaces, computationally expensive models, and Deep Learning applications.

---

# Summary

Random Search is a sampling-based hyperparameter optimization technique that evaluates randomly selected hyperparameter combinations instead of exhaustively testing every possibility.

Although it does not guarantee finding the global optimum, it is significantly more computationally efficient than Grid Search and often achieves comparable or even better performance in high-dimensional search spaces.

---

# Key Takeaways

✔ Random Search samples hyperparameter combinations randomly.

✔ It evaluates only a subset of the search space.

✔ It is much faster than Grid Search for large problems.

✔ It does not guarantee finding the global optimum.

✔ It is widely used for Deep Learning hyperparameter tuning.

✔ Random Search is often the preferred choice when computational resources are limited.

---

# Next Part

## **Part 12 – Bayesian Optimization**

In the next chapter, we will study **Bayesian Optimization**, understand how it intelligently selects promising hyperparameter combinations based on previous experiments, compare it with Grid Search and Random Search, and learn why it is one of the most powerful hyperparameter optimization techniques used in modern AI research.
