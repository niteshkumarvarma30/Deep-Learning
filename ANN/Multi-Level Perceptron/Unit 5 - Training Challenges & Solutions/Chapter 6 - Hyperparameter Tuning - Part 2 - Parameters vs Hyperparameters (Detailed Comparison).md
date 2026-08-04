# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 2 – Parameters vs Hyperparameters (Detailed Comparison)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Clearly distinguish Parameters and Hyperparameters.
- Understand who determines each of them.
- Learn when they are created and updated.
- Understand their role during model training.
- Answer interview questions related to Parameters and Hyperparameters confidently.

---

# 1. Introduction

Every Machine Learning and Deep Learning model contains two different types of values.

```text
Hyperparameters

↓

Control Learning

↓

Training Starts

↓

Parameters

↓

Learned Automatically
```

Although both influence model performance,

they serve completely different purposes.

---

# 2. Parameters

Parameters are

> **Values that are automatically learned from the training data during the learning process.**

Examples

- Weights
- Biases

Initially,

these values are randomly initialized.

```text
Weight = Random

↓

Training

↓

Updated

↓

Best Weight Found
```

The optimizer continuously updates these values until the model converges.

---

# 3. Hyperparameters

Hyperparameters are

> **Configuration settings chosen before training begins.**

They determine

- How the model learns
- How fast it learns
- How much it learns

Unlike parameters,

they are not updated by Gradient Descent.

Examples include

```text
Learning Rate

Batch Size

Epochs

Optimizer

Hidden Layers

Dropout Rate
```

---

# 4. Who Determines Them?

### Parameters

Determined automatically by

```text
Training Data

+

Backpropagation

+

Gradient Descent
```

---

### Hyperparameters

Determined by

- Developer
- Researcher
- AutoML
- Hyperparameter Tuning algorithms

---

# 5. When Are They Created?

### Hyperparameters

Chosen

```text
Before Training
```

---

### Parameters

Initialized

```text
Before Training
```

but

learned

```text
During Training
```

---

# 6. Do They Change During Training?

### Parameters

```text
Epoch 1

↓

Updated

↓

Epoch 2

↓

Updated

↓

Epoch 3

↓

Updated
```

They change after every optimization step.

---

### Hyperparameters

Normally

```text
Remain Fixed
```

throughout training.

(Some advanced techniques such as Learning Rate Scheduling intentionally modify certain hyperparameters.)

---

# 7. Mathematical Perspective

Consider

$$
z = Wx + b
$$

Here

```text
W

↓

Weight

↓

Parameter
```

```text
b

↓

Bias

↓

Parameter
```

Now consider

```text
Learning Rate = 0.001
```

This is **not** inside the equation.

Instead,

it controls

```text
How W and b are updated.
```

Therefore,

Learning Rate is a Hyperparameter.

---

# 8. Complete Training Pipeline

```text
Choose Hyperparameters

↓

Initialize Parameters

↓

Forward Propagation

↓

Loss Calculation

↓

Backpropagation

↓

Update Parameters

↓

Repeat Until Training Ends
```

Notice

Hyperparameters define the training process,

while Parameters are the values being learned.

---

# 9. Real-Life Analogy

Imagine building a house.

### Hyperparameters

```text
Number of Floors

Room Size

Building Material

Budget
```

These decisions are made before construction begins.

---

### Parameters

```text
Actual Wall Positions

Concrete Placement

Brick Arrangement
```

These are determined during construction.

The blueprint controls the construction,

just as Hyperparameters control learning.

---

# 10. Common Confusion

Many beginners think

```text
Learning Rate

↓

Updated Automatically
```

This is incorrect.

Gradient Descent uses the Learning Rate,

but does not automatically discover its best value.

The Learning Rate must be selected separately.

---

# 11. Side-by-Side Comparison

| Property | Parameters | Hyperparameters |
|----------|------------|-----------------|
| Definition | Values learned by the model | Values chosen before training |
| Updated During Training | ✅ Yes | ❌ Usually No |
| Learned Automatically | ✅ Yes | ❌ No |
| Examples | Weights, Biases | Learning Rate, Batch Size, Epochs |
| Controlled By | Gradient Descent | Developer or Tuning Algorithm |
| Affect Learning | Indirectly | Directly |
| Number | Often Millions | Usually Tens |

---

# 12. One Important Insight

A neural network may have

```text
50 Million Parameters
```

but only

```text
20 Hyperparameters
```

Even though there are far fewer Hyperparameters,

choosing poor values can make the model perform badly.

This is why Hyperparameter Tuning is such an important topic.

---

# Visual Summary

```text
Hyperparameters

↓

Control Training

↓

Gradient Descent

↓

Learns Parameters

↓

Trained Model
```

---

# Parameters vs Hyperparameters

| Parameters | Hyperparameters |
|------------|-----------------|
| Learned automatically | Selected before training |
| Updated during Backpropagation | Not updated during Backpropagation |
| Include weights and biases | Include Learning Rate, Batch Size, Epochs, Optimizer |
| Can number in millions | Usually only a few |
| Represent learned knowledge | Control how learning occurs |

---

# Interview Questions

## Q1. What are Parameters?

**Answer**

Parameters are values such as weights and biases that are automatically learned from the training data during optimization.

---

## Q2. What are Hyperparameters?

**Answer**

Hyperparameters are configuration settings selected before training that control how the learning algorithm operates.

---

## Q3. Is Learning Rate a Parameter?

**Answer**

No.

Learning Rate is a Hyperparameter because it controls how parameters are updated rather than being learned itself.

---

## Q4. Which values are updated by Backpropagation?

**Answer**

Only Parameters (weights and biases) are updated by Backpropagation.

---

## Q5. Why is Hyperparameter Tuning necessary?

**Answer**

Because different Hyperparameter values can significantly affect convergence speed, generalization, training stability, and final model performance.

---

# Summary

Parameters and Hyperparameters serve different roles in a neural network.

Parameters represent the knowledge learned from the training data and are continuously updated through Backpropagation and Gradient Descent.

Hyperparameters, on the other hand, are configuration choices made before training that determine how the learning process operates.

Although Hyperparameters are far fewer in number, selecting appropriate values is essential for achieving good model performance.

---

# Key Takeaways

✔ Parameters are learned automatically during training.

✔ Hyperparameters are selected before training begins.

✔ Backpropagation updates only Parameters.

✔ Learning Rate is a Hyperparameter.

✔ Weights and Biases are Parameters.

✔ Hyperparameters control the learning process.

---

# Next Part

## **Part 3 – Learning Rate (The Most Important Hyperparameter)**

In the next chapter, we will study the **Learning Rate** in depth, understand why it is considered the most important Hyperparameter, learn what happens when it is too small or too large, visualize its effect on Gradient Descent, and explore practical strategies for choosing an appropriate Learning Rate.
