# Unit 4 – Learning in Neural Networks

# Chapter 1 – Introduction to Learning in Neural Networks

## Part 2 – What is Backpropagation?

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Backpropagation is.
- Learn why Backpropagation is needed.
- Understand why it is called **Backpropagation**.
- Learn what information travels backward through the network.
- Understand the role of gradients.
- Differentiate between Backpropagation and the Optimizer.

---

# 1. Recap: Where Are We?

From the previous units, we have already learned the following pipeline.

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
```

Suppose the neural network predicts

```text
Prediction = 0.95
```

Actual value

```text
Actual = 0
```

The loss becomes

```text
Loss = High
```

Now the network knows

> "I made a mistake."

But another important question appears.

- Which weight caused the mistake?
- How much did each weight contribute?
- Which weights should change?
- By how much should they change?

Neither Forward Propagation nor the Loss Function can answer these questions.

---

# 2. A Real-Life Analogy

Imagine five students working together on a project.

The project receives

```text
40 / 100
```

Now the teacher asks

> **Who is responsible for the low score?**

Was it

```text
Student A?
```

or

```text
Student B?
```

or

```text
Everyone together?
```

Before improving,

the teacher must first determine who contributed to the poor result.

The same idea applies to a neural network.

---

# 3. The Problem Inside a Neural Network

Consider a simple neural network.

```text
Input

↓

Weight W₁

↓

Hidden Layer

↓

Weight W₂

↓

Output Layer

↓

Prediction
```

Suppose the prediction is wrong.

Now we ask

- Was the error caused mainly by **W₁**?
- Was it caused mainly by **W₂**?
- Did both weights contribute?

The network must answer these questions before updating the weights.

This is exactly what **Backpropagation** helps us determine.

---

# 4. What is Backpropagation?

## Definition

**Backpropagation** is the algorithm used to compute the gradient of the loss with respect to every weight and bias in a neural network by propagating the error backward from the output layer toward the input layer.

In simple words,

> **Backpropagation tells us how much each weight contributed to the prediction error.**

---

# 5. Why is it Called "Backpropagation"?

The word can be divided into two parts.

## Back

Instead of moving

```text
Input

↓

Output
```

Backpropagation starts from

```text
Output

↓

Hidden Layer

↓

Input Layer
```

It moves in the opposite direction.

---

## Propagation

Propagation means

> **Passing information from one place to another.**

During Forward Propagation,

the information being propagated is

```text
Input

↓

Output
```

During Backpropagation,

the information being propagated is

```text
Error Information

↓

Backward
```

Therefore,

the name

```text
Back

+

Propagation

↓

Backpropagation
```

---

# 6. What Travels Backward?

Many beginners believe

```text
Prediction travels backward.
```

❌ Incorrect.

Others believe

```text
Weights travel backward.
```

❌ Incorrect.

The quantity that actually travels backward is

```text
Error Information
```

More precisely,

what travels backward is

```text
Gradients
```

These gradients describe how sensitive the loss is to each weight.

---

# 7. A Detective Analogy

Imagine a factory.

The finished product is defective.

Instead of starting the investigation from the beginning,

the manager starts from the finished product.

```text
Finished Product

↓

Assembly Line

↓

Machine 4

↓

Machine 3

↓

Machine 2

↓

Machine 1
```

The manager traces the defect backward until the source of the problem is found.

Backpropagation follows exactly the same idea.

It starts from the prediction error and traces it backward through the network.

---

# 8. What Does Backpropagation Compute?

Suppose

```text
Loss = 5
```

Backpropagation computes

```text
Weight W₁

↓

Gradient = 0.02

Weight W₂

↓

Gradient = 1.80
```

Notice

Weight **W₂** has a much larger gradient.

This means

W₂ contributed much more to the prediction error.

Therefore,

the optimizer will update W₂ more than W₁.

---

# 9. Forward Propagation vs Backpropagation

## Forward Propagation

```text
Input

↓

Weighted Sum

↓

Activation Function

↓

Prediction
```

Purpose

Generate the prediction.

---

## Backpropagation

```text
Loss

↓

Output Layer

↓

Hidden Layer

↓

Input Layer

↓

Gradients
```

Purpose

Compute the gradients of every parameter.

---

# 10. Why Are Gradients Important?

Suppose

```text
Weight W₁

Gradient = 0.0001
```

Very small.

Only a tiny update is needed.

---

Now consider

```text
Weight W₂

Gradient = 3.5
```

Large.

A much larger correction is needed.

Without gradients,

the optimizer has no information about how the weights should change.

---

# 11. Complete Learning Pipeline

Now the complete ANN learning process becomes

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

Repeat
```

Each iteration reduces the loss,

allowing the neural network to learn from its mistakes.

---

# 12. Backpropagation vs Optimizer

One of the most common misconceptions is

```text
Backpropagation updates the weights.
```

This is **incorrect**.

The responsibilities are different.

## Backpropagation

```text
Compute Gradients
```

## Optimizer

```text
Use Gradients

↓

Update Weights
```

For example,

- Gradient Descent
- Momentum
- RMSProp
- Adam

are all optimizers.

They use the gradients computed by Backpropagation.

---

# 13. Responsibilities of Each Component

| Component | Responsibility |
|------------|----------------|
| Forward Propagation | Generate prediction |
| Loss Function | Measure prediction error |
| Backpropagation | Compute gradients |
| Optimizer | Update weights |

---

# Interview Questions

## Q1. What is Backpropagation?

**Answer**

Backpropagation is the algorithm used to compute the gradients of the loss with respect to every weight and bias by propagating the error backward through the network.

---

## Q2. Why is it called Backpropagation?

**Answer**

Because the error information is propagated backward from the output layer toward the input layer.

---

## Q3. What travels backward during Backpropagation?

**Answer**

The gradients (error information) travel backward through the network.

---

## Q4. Does Backpropagation update the weights?

**Answer**

No.

Backpropagation only computes gradients.

The optimizer updates the weights using those gradients.

---

## Q5. Why are gradients important?

**Answer**

Gradients indicate how much each weight contributed to the prediction error and determine how the optimizer should update the weights.

---

# Summary

Backpropagation is one of the most important algorithms in Deep Learning.

Its purpose is to determine how much each weight and bias contributed to the prediction error by propagating the error backward through the neural network.

It computes the gradients required by the optimizer but does **not** update the weights itself.

The optimizer then uses these gradients to reduce the loss and improve the model.

---

# Key Takeaways

✔ Backpropagation computes gradients.

✔ It starts from the output layer and moves toward the input layer.

✔ The quantity propagated backward is the **gradient (error information)**.

✔ Backpropagation does **not** update the weights.

✔ Optimizers such as Gradient Descent, Momentum, RMSProp, and Adam use the computed gradients to update the weights.

✔ Backpropagation is the bridge between the **Loss Function** and the **Optimizer**.

---

## Next Part

**Part 3 – What is a Gradient?**

In the next chapter, we will understand what a **gradient** actually is, why it is central to Backpropagation, and how it tells us the direction and magnitude in which the weights should be updated.
