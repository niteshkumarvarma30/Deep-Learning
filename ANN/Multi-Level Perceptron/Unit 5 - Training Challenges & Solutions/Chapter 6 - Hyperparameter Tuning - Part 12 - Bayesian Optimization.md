# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 12 – Bayesian Optimization

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Bayesian Optimization is.
- Learn how Bayesian Optimization differs from Grid Search and Random Search.
- Understand surrogate models and acquisition functions.
- Learn why Bayesian Optimization is efficient for expensive models.
- Understand when Bayesian Optimization should be used.

---

# 1. Introduction

Suppose training one neural network takes

```text
5 Hours
```

Testing

```text
100 Hyperparameter Combinations
```

would require

```text
500 Hours
```

Clearly,

trying random combinations becomes expensive.

Instead,

we would like to

> **Learn from previous experiments and intelligently choose the next hyperparameters.**

This idea is called

```text
Bayesian Optimization
```

---

# 2. What is Bayesian Optimization?

Bayesian Optimization is

> **A sequential hyperparameter optimization technique that uses the results of previous experiments to intelligently choose the next hyperparameter combination.**

Unlike

- Grid Search
- Random Search

Bayesian Optimization

**learns while searching.**

---

# 3. Basic Idea

Instead of

```text
Guess

↓

Train

↓

Repeat
```

Bayesian Optimization performs

```text
Train

↓

Observe Performance

↓

Build Mathematical Model

↓

Predict Better Hyperparameters

↓

Train Again
```

Every experiment improves the search.

---

# 4. Why Is Bayesian Optimization Needed?

Suppose training one model costs

```text
6 Hours
```

Testing

```text
1000 Models
```

would require

```text
6000 Hours
```

Bayesian Optimization tries to find excellent hyperparameters using

```text
Far Fewer Experiments
```

This is why it is popular in expensive Deep Learning training.

---

# 5. How Bayesian Optimization Works

The workflow is

```text
Choose Initial Hyperparameters

↓

Train Model

↓

Measure Validation Score

↓

Build Surrogate Model

↓

Predict Promising Hyperparameters

↓

Train New Model

↓

Update Surrogate Model

↓

Repeat
```

The search becomes smarter after every experiment.

---

# 6. Surrogate Model

Training a neural network is expensive.

Instead,

Bayesian Optimization builds a

```text
Surrogate Model
```

A surrogate model

- Approximates the true objective function.
- Predicts which hyperparameters are likely to perform well.
- Is much faster than training a full neural network.

Common surrogate models include

- Gaussian Processes
- Tree-structured models
- Random Forests (in some implementations)

---

# 7. Acquisition Function

Once the surrogate model is built,

Bayesian Optimization must decide

```text
Where Should We Search Next?
```

This decision is made using the

```text
Acquisition Function
```

The acquisition function balances

```text
Exploration

↓

Try New Regions
```

and

```text
Exploitation

↓

Improve Known Good Regions
```

---

# 8. Exploration vs Exploitation

Suppose we are searching for the best Learning Rate.

### Exploration

```text
Search New Values

↓

0.5

↓

0.05

↓

0.0005
```

---

### Exploitation

```text
Current Best

↓

0.001

↓

Search Nearby

↓

0.0008

↓

0.0012
```

A good optimization strategy balances both.

---

# 9. Visual Comparison

### Grid Search

```text
□□□□□□□□□□

Tests Everything
```

---

### Random Search

```text
■ □ □ ■ □ □

□ ■ □ □ □ ■
```

Random Sampling

---

### Bayesian Optimization

```text
■

↓

Learn

↓

■■

↓

Learn

↓

■■■

↓

Focus Near Good Regions
```

Every experiment improves future decisions.

---

# 10. Advantages

### Very Efficient

Requires fewer model evaluations.

---

### Learns During Search

Previous experiments guide future experiments.

---

### Suitable for Expensive Models

Ideal when

- CNN training is slow.
- Transformer training is expensive.
- GPU resources are limited.

---

### Better Than Random Search

Often finds excellent hyperparameters using fewer experiments.

---

# 11. Limitations

### More Complex

Implementation is more difficult than Grid Search or Random Search.

---

### Computational Overhead

The surrogate model itself requires computation.

---

### Less Effective in Extremely High Dimensions

As the number of hyperparameters becomes very large,

building an accurate surrogate model becomes more difficult.

---

# 12. Practical Use

Bayesian Optimization is widely used in

- Deep Learning
- AutoML
- Neural Architecture Search
- Industrial AI Systems
- Hyperparameter Optimization Libraries

Examples

- Optuna
- Hyperopt
- SMAC
- BoTorch
- Ax Platform

---

# 13. Framework Example

Using Optuna

```python
import optuna

def objective(trial):

    learning_rate = trial.suggest_float(
        "learning_rate",
        1e-5,
        1e-1,
        log=True
    )

    batch_size = trial.suggest_categorical(
        "batch_size",
        [16,32,64,128]
    )

    ...
```

The framework automatically

- Suggests hyperparameters
- Learns from previous trials
- Improves future suggestions

---

# 14. Real-Life Analogy

Imagine searching for the best restaurant.

### Grid Search

```text
Visit

Every Restaurant
```

---

### Random Search

```text
Visit

Random Restaurants
```

---

### Bayesian Optimization

```text
Visit Restaurant

↓

Rate It

↓

Learn Which Area Has Better Restaurants

↓

Visit Better Area Next
```

Instead of searching blindly,

you learn from experience.

---

# 15. One Important Insight

Many beginners think

> **Bayesian Optimization guarantees the globally optimal hyperparameters.**

This is incorrect.

Bayesian Optimization

does not guarantee the global optimum.

Instead,

it intelligently balances exploration and exploitation,

often finding excellent solutions with far fewer evaluations than Grid Search or Random Search.

---

# Visual Summary

```text
Train Model

↓

Evaluate Performance

↓

Build Surrogate Model

↓

Predict Best Next Trial

↓

Train Again

↓

Update Knowledge

↓

Repeat
```

---

# Comparison of Hyperparameter Search Methods

| Method | Strategy | Computational Cost | Efficiency |
|---------|----------|-------------------|------------|
| Grid Search | Exhaustive | Very High | Good for small search spaces |
| Random Search | Random Sampling | Moderate | Good for large search spaces |
| Bayesian Optimization | Intelligent Sequential Search | Low to Moderate | Excellent for expensive models |

---

# Interview Questions

## Q1. What is Bayesian Optimization?

**Answer**

Bayesian Optimization is a sequential hyperparameter optimization technique that uses the results of previous experiments to intelligently select the next hyperparameter combination.

---

## Q2. Why is Bayesian Optimization more efficient than Grid Search?

**Answer**

Because it learns from previous experiments and evaluates only the most promising hyperparameter configurations instead of exhaustively searching the entire space.

---

## Q3. What is a surrogate model?

**Answer**

A surrogate model is an inexpensive mathematical approximation of the objective function that predicts how different hyperparameter values are likely to perform.

---

## Q4. What is the purpose of the acquisition function?

**Answer**

The acquisition function decides which hyperparameter configuration should be evaluated next by balancing exploration of new regions and exploitation of promising regions.

---

## Q5. When is Bayesian Optimization most useful?

**Answer**

When model training is computationally expensive, such as with deep neural networks, Transformers, or large-scale Machine Learning models.

---

# Summary

Bayesian Optimization is an intelligent hyperparameter optimization technique that learns from previous experiments to guide future searches.

Instead of evaluating every combination or selecting combinations randomly, it builds a surrogate model of the objective function and uses an acquisition function to determine the most promising hyperparameters to evaluate next.

This approach significantly reduces the number of expensive model training runs while often achieving performance comparable to or better than Grid Search and Random Search.

---

# Key Takeaways

✔ Bayesian Optimization learns from previous experiments.

✔ It uses a surrogate model to approximate the objective function.

✔ The acquisition function balances exploration and exploitation.

✔ It requires far fewer model evaluations than Grid Search.

✔ It is ideal for computationally expensive Deep Learning models.

✔ Popular libraries include Optuna, Hyperopt, SMAC, BoTorch, and Ax.

---

# Next Part

## **Part 13 – Practical Guidelines for Hyperparameter Tuning**

In the next chapter, we will combine everything learned so far and study **practical strategies for tuning hyperparameters in real-world Deep Learning projects**, including where to start, which hyperparameters matter most, recommended tuning order, common mistakes, and industry best practices.
