# Unit 4 – Learning in Neural Networks

# Chapter 3 – Backpropagation in Multi-Layer Neural Networks

## Part 5 – Complete Backpropagation Algorithm (Pseudo-code and Training Pipeline)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the complete neural network training pipeline.
- Learn the complete Backpropagation algorithm.
- Understand how all previously learned concepts fit together.
- Learn the exact sequence followed by PyTorch and TensorFlow during training.
- Understand what happens during every training iteration.

---

# 1. Introduction

So far, we have studied every individual component of neural network training.

We learned

- Forward Propagation
- Loss Functions
- Partial Derivatives
- Gradient Vector
- Chain Rule
- Delta (δ)
- Backpropagation
- Gradient Descent

Now it is time to combine everything into one complete algorithm.

This is the exact process followed by every modern Deep Learning framework.

---

# 2. Complete Training Pipeline

A neural network learns through a repeating cycle.

```text
Training Data

↓

Initialize Parameters

↓

Forward Propagation

↓

Prediction

↓

Loss Function

↓

Compute Loss

↓

Backpropagation

↓

Compute Gradients

↓

Gradient Descent

↓

Update Parameters

↓

Next Iteration

↓

Repeat Until Convergence
```

Every epoch repeats this entire pipeline.

---

# 3. Step 1 – Initialize Parameters

Before training begins,

all weights and biases are initialized.

Example

```text
W₁

↓

Random Values

W₂

↓

Random Values

Biases

↓

Usually Zero or Small Random Values
```

Proper initialization is important because poor initialization can slow down learning.

---

# 4. Step 2 – Forward Propagation

For each layer,

compute

## Weighted Sum

$$
Z^{[l]} = W^{[l]}A^{[l-1]} + b^{[l]}
$$

---

## Activation

$$
A^{[l]} = f(Z^{[l]})
$$

Repeat this process until the output layer.

The final activation becomes the prediction.

---

# 5. Step 3 – Compute Prediction

The output layer produces

$$
\hat{Y} = A^{[L]}
$$

For binary classification,

the prediction is obtained using Sigmoid.

For multi-class classification,

Softmax is used.

---

# 6. Step 4 – Compute the Loss

Compare

Prediction

$$
\hat{Y}
$$

with

Actual Labels

$$
Y
$$

using an appropriate loss function.

Examples

Binary Classification

↓

Binary Cross Entropy

Multi-class Classification

↓

Categorical Cross Entropy

Regression

↓

Mean Squared Error

This gives

$$
L
$$

---

# 7. Step 5 – Start Backpropagation

Now learning begins.

Compute the output-layer error.

For BCE + Sigmoid,

$$
\boxed{ \delta^{[L]} = A^{[L]} - Y }
$$

This represents the prediction error.

---

# 8. Step 6 – Propagate Errors Backward

Move backward through every hidden layer.

For each hidden layer,

compute

$$
\boxed{ \delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(Z^{[l]}) }
$$

This propagates the error from the output layer toward the input layer.

---

# 9. Step 7 – Compute Gradients

After computing delta,

calculate

Weight Gradient

$$
\boxed{ \frac{\partial L} {\partial W^{[l]}} = \delta^{[l]} (A^{[l-1]})^T }
$$

Bias Gradient

$$
\boxed{ \frac{\partial L} {\partial b^{[l]}} = \delta^{[l]} }
$$

These gradients indicate how each parameter should change.

---

# 10. Step 8 – Update Parameters

Gradient Descent updates

Weights

$$
\boxed{ W^{[l]} = W^{[l]} - \eta \frac{\partial L} {\partial W^{[l]}} }
$$

Biases

$$
\boxed{ b^{[l]} = b^{[l]} - \eta \frac{\partial L} {\partial b^{[l]}} }
$$

where

$$
\eta
$$

is the learning rate.

---

# 11. Step 9 – Repeat

One update is **not enough**.

Repeat the process.

```text
Epoch 1

↓

Epoch 2

↓

Epoch 3

↓

...

↓

Loss Decreases

↓

Model Learns
```

Eventually,

the model converges to good parameter values.

---

# 12. Complete Algorithm in Pseudo-code

```text
Initialize all weights and biases

Repeat until convergence

    Perform Forward Propagation

        Compute weighted sums

        Apply activation functions

        Obtain predictions

    Compute Loss

    Perform Backpropagation

        Compute output-layer delta

        Compute hidden-layer deltas

        Compute weight gradients

        Compute bias gradients

    Update all weights

    Update all biases

End Repeat
```

This is the complete learning algorithm for feedforward neural networks.

---

# 13. Visual Flowchart

```text
Initialize Parameters

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

Output Delta

↓

Hidden Deltas

↓

Weight Gradients

↓

Bias Gradients

↓

Gradient Descent

↓

Updated Parameters

↓

Repeat
```

---

# 14. How PyTorch Performs Training

When you write

```python
for epoch in range(epochs):

    output = model(x)

    loss = criterion(output, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

Internally,

PyTorch performs

```text
Forward Propagation

↓

Loss Computation

↓

Automatic Differentiation

↓

Matrix Backpropagation

↓

Gradient Computation

↓

Parameter Updates
```

All gradient calculations are performed automatically.

---

# 15. How TensorFlow Performs Training

TensorFlow follows the same process.

```python
with tf.GradientTape() as tape:

    predictions = model(x)

    loss = loss_fn(y, predictions)

gradients = tape.gradient(loss, model.trainable_variables)

optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

The mathematics is identical.

Only the implementation differs.

---

# 16. Real-Life Analogy

Imagine a student preparing for an exam.

```text
Study

↓

Take Test

↓

Receive Marks

↓

Identify Mistakes

↓

Improve Weak Areas

↓

Take Test Again

↓

Repeat
```

Neural networks learn in exactly the same way.

Each epoch is another attempt to improve.

---

# 17. One Important Insight

Many beginners think

```text
Backpropagation

=

Entire Training Process
```

This is incorrect.

Backpropagation is **only one step** of training.

The complete pipeline is

```text
Initialize Parameters

↓

Forward Propagation

↓

Loss Computation

↓

Backpropagation

↓

Gradient Descent

↓

Repeat
```

Backpropagation computes gradients.

Gradient Descent uses those gradients to update parameters.

---

# Difference Between Backpropagation and Gradient Descent

| Backpropagation | Gradient Descent |
|-----------------|------------------|
| Computes gradients | Updates parameters |
| Uses Chain Rule | Uses gradients |
| Mathematical differentiation | Optimization algorithm |
| Runs before parameter update | Runs after gradients are available |

---

# Complete ANN Training Pipeline

```text
Training Dataset

↓

Initialize Parameters

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

Gradient Descent

↓

Updated Parameters

↓

Next Epoch

↓

Repeat Until Convergence
```

---

# Interview Questions

## Q1. What are the main stages of neural network training?

**Answer**

1. Parameter Initialization
2. Forward Propagation
3. Loss Computation
4. Backpropagation
5. Gradient Descent
6. Repeat until convergence

---

## Q2. What is the role of Backpropagation?

**Answer**

Backpropagation computes the gradients of the loss with respect to all trainable parameters.

---

## Q3. What is the role of Gradient Descent?

**Answer**

Gradient Descent updates the weights and biases using the gradients computed by Backpropagation.

---

## Q4. Why are multiple epochs required?

**Answer**

One iteration makes only a small improvement. Multiple epochs allow the network to gradually reduce the loss and learn better parameters.

---

## Q5. Does PyTorch compute gradients manually?

**Answer**

No.

PyTorch uses Automatic Differentiation (Autograd) to compute gradients automatically.

---

# Summary

A neural network learns through a repeating cycle.

First,

the parameters are initialized.

Next,

Forward Propagation computes predictions.

The Loss Function measures prediction error.

Backpropagation computes gradients for every trainable parameter.

Gradient Descent updates the parameters.

This entire process repeats over many epochs until the model converges.

This complete pipeline is the foundation of modern Deep Learning and is implemented internally by frameworks such as PyTorch, TensorFlow, and JAX.

---

# Key Takeaways

✔ Neural network training follows a fixed sequence of operations.

✔ Forward Propagation computes predictions.

✔ Loss Functions measure prediction error.

✔ Backpropagation computes gradients.

✔ Gradient Descent updates parameters.

✔ Training requires multiple epochs.

✔ Modern Deep Learning frameworks automate the entire pipeline.

✔ Understanding this pipeline provides a complete picture of how neural networks learn.

---

# 🎉 Chapter 3 Completed

You have now completed:

- ✅ Part 1 – Why Multi-Layer Backpropagation?
- ✅ Part 2 – Mathematical Derivation
- ✅ Part 3 – Complete Numerical Example
- ✅ Part 4 – Matrix Form of Backpropagation
- ✅ Part 5 – Complete Backpropagation Algorithm (Pseudo-code and Training Pipeline)

---

# Next Chapter

## **Unit 4 – Chapter 4: Optimization Algorithms**

We will now study how different optimizers improve upon standard Gradient Descent:

1. Gradient Descent
2. Batch Gradient Descent
3. Stochastic Gradient Descent (SGD)
4. Mini-Batch Gradient Descent
5. Momentum
6. Nesterov Accelerated Gradient (NAG)
7. AdaGrad
8. RMSProp
9. Adam
10. AdamW
11. Learning Rate Scheduling

This chapter explains **how modern neural networks are optimized efficiently**.
