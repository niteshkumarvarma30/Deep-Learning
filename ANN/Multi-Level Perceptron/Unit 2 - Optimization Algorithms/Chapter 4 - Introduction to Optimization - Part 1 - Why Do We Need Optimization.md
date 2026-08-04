# Unit 2 – Optimization Algorithms

# Chapter 4 – Introduction to Optimization

## Part 1 – Why Do We Need Optimization?

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what optimization means in Deep Learning.
- Understand why an optimizer is needed.
- Understand the relationship between loss functions and optimization.
- Learn what the Loss Surface is.
- Understand why weights and biases must be updated.
- Build intuition before studying Gradient Descent.

---

# 1. What Have We Learned So Far?

Until now, we have learned the following Deep Learning pipeline.

```text
Input

↓

Neural Network

↓

Prediction

↓

Loss Function

↓

Loss Value
```

For example,

Suppose

Actual Label

```text
Cat
```

Model Prediction

```text
Dog
```

The loss function computes

```text
Loss = 2.35
```

Now ask yourself

> **The model made a mistake. How does it improve itself?**

This is exactly the purpose of **Optimization**.

---

# 2. What is Optimization?

## Definition

Optimization is the process of finding the **best values of the model's parameters (weights and biases)** so that the **loss function becomes as small as possible**.

In Deep Learning,

the parameters are

- Weights (W)
- Biases (b)

The optimizer updates these parameters after every training step.

---

# 3. Why Do We Need Optimization?

Suppose a neural network predicts

```text
Actual Value

↓

1
```

Prediction

```text
0.25
```

The loss function computes

```text
Loss = 0.75
```

A high loss means

> The prediction is far from the correct answer.

Simply computing the loss does **not** improve the model.

Someone (or something) must decide

- Which weight should change?
- How much should it change?
- In which direction should it change?

That "something" is called the **Optimizer**.

---

# 4. Role of the Optimizer

Think of the optimizer as a teacher.

The complete workflow becomes

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

↓

Optimizer

↓

Update Weights & Biases

↓

Better Prediction
```

The optimizer continuously adjusts the model until the loss becomes as small as possible.

---

# 5. Why Update Weights?

Consider a simple neuron.

$$
z=w^Tx+b
$$

Initially,

```text
Weight = 0.5

Bias = 0.2
```

Prediction

```text
0.30
```

Actual Output

```text
1
```

Clearly,

the prediction is poor.

If we keep the same weights forever,

the model will always make the same mistake.

Therefore,

the weights and biases must change after every learning step.

This is how learning occurs.

---

# 6. The Goal of Training

Training is simply a repeated cycle.

```text
Guess

↓

Measure Error

↓

Update Weights

↓

Guess Again

↓

Measure Error

↓

Update Weights

↓

Repeat
```

After many iterations,

the predictions improve because the weights have been optimized.

---

# 7. What is a Loss Surface?

Imagine the loss value as the height of a landscape.

```text
          ▲ Loss
          │

      /\        /\

    /    \____/    \

___/________________\______

         Lowest Point
```

Here,

- High mountains → High Loss
- Small valleys → Low Loss
- Lowest valley → Minimum Loss

This imaginary landscape is called the

**Loss Surface** (or **Loss Landscape**).

Every point on this surface represents a different combination of weights and biases.

---

# 8. Why Is It Called Optimization?

Suppose

```text
Weight = 0.2

Loss = 8.5
```

After updating the weight,

```text
Weight = 0.8

Loss = 3.1
```

After more updates,

```text
Weight = 1.4

Loss = 0.5
```

The optimizer keeps searching for better weights that produce smaller losses.

This search process is called

**Optimization**.

---

# 9. Optimization is an Iterative Process

Optimization does not happen in a single step.

Instead,

```text
Initialize Weights

↓

Prediction

↓

Compute Loss

↓

Update Weights

↓

Prediction Again

↓

Compute Loss

↓

Update Weights

↓

Repeat Many Times
```

Each iteration should ideally reduce the loss.

---

# 10. What Does an Optimizer Actually Do?

An optimizer answers three important questions.

### Question 1

Which parameter should be updated?

Answer:

- Weights
- Biases

---

### Question 2

In which direction should the parameter move?

Should the weight increase or decrease?

---

### Question 3

How much should the parameter change?

A very large update may overshoot the optimum.

A very small update may make learning extremely slow.

Different optimization algorithms answer these questions differently.

Examples include

- Gradient Descent
- Stochastic Gradient Descent (SGD)
- Momentum
- RMSProp
- Adam

Although their methods differ,

their goal is always the same.

> **Find better values of the weights and biases that minimize the loss function.**

---

# 11. Real-Life Analogy

Imagine you are standing on a mountain in thick fog.

Your goal is to reach the **lowest point of the valley**.

You cannot see the entire mountain.

So you

1. Feel the slope beneath your feet.
2. Take a small step downhill.
3. Check the slope again.
4. Take another small step.
5. Repeat until you reach the valley.

This is exactly how optimization works.

Mapping the analogy:

| Real Life | Deep Learning |
|-----------|---------------|
| Mountain | Loss Surface |
| Height | Loss Value |
| Your Position | Current Weights |
| Valley | Minimum Loss |
| Walking Downhill | Optimization |

---

# 12. Complete Training Pipeline

```text
Training Data

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Loss Value

↓

Optimizer

↓

Update Weights & Biases

↓

Forward Propagation Again

↓

New Prediction

↓

Repeat Until Loss is Minimized
```

---

# 13. What Will We Learn Next?

Optimization is a broad topic.

In the upcoming parts of this chapter, we will study:

- Gradient Descent
- Batch Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent
- Momentum
- RMSProp
- Adam Optimizer

These algorithms are different ways of optimizing the weights and biases.

---

# Interview Questions

## Q1. What is optimization in Deep Learning?

**Answer**

Optimization is the process of finding the best values of weights and biases that minimize the loss function.

---

## Q2. Why do we need an optimizer?

**Answer**

The loss function only measures how wrong the prediction is.

The optimizer decides how to update the weights and biases to reduce that error.

---

## Q3. What parameters are optimized during training?

**Answer**

- Weights
- Biases

---

## Q4. What is a Loss Surface?

**Answer**

A Loss Surface is a conceptual landscape where every point represents a different combination of weights and biases, and the height represents the corresponding loss value.

---

## Q5. What is the ultimate goal of optimization?

**Answer**

To find the values of weights and biases that produce the minimum possible loss.

---

# Summary

Optimization is the learning mechanism of a neural network.

After the model makes a prediction, the loss function measures the prediction error.

The optimizer then updates the model's weights and biases so that future predictions become more accurate.

This process repeats over many iterations until the loss becomes as small as possible.

Optimization is therefore the bridge between **calculating the error** and **improving the model**.

---

# Key Takeaways

✔ Optimization minimizes the loss function.

✔ The parameters being optimized are **weights** and **biases**.

✔ The optimizer decides

- which parameters to update,
- in which direction,
- and by how much.

✔ Training is an iterative process consisting of prediction, loss calculation, and parameter updates.

✔ The Loss Surface represents how the loss changes for different combinations of weights and biases.

✔ Different optimization algorithms use different strategies, but all aim to minimize the loss function.

✔ Optimization is the core learning mechanism of every Deep Learning model.
