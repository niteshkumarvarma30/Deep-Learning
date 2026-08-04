# Unit 5 – Training Challenges & Solutions

# Chapter 6 – Hyperparameter Tuning

## Part 8 – Activation Function Selection

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why activation functions are important.
- Learn how to choose the appropriate activation function.
- Compare Sigmoid, Tanh, ReLU, Leaky ReLU, ELU, GELU, and Softmax.
- Understand which activation functions are used in modern Deep Learning.
- Learn best practices for selecting activation functions.

---

# 1. Introduction

Every neuron in a neural network performs two operations.

```text
Weighted Sum

↓

Activation Function

↓

Output
```

The activation function decides

> **Whether the neuron should become active and what output it should produce.**

Without activation functions,

deep neural networks cannot learn complex, non-linear relationships.

---

# 2. Why Are Activation Functions Needed?

Suppose every neuron performs only

```text
Weighted Sum
```

without any activation.

Then

```text
Input

↓

Linear Layer

↓

Linear Layer

↓

Linear Layer

↓

Output
```

No matter how many layers we add,

the entire network behaves like

```text
One Linear Layer
```

The network cannot learn complex patterns.

Activation functions introduce

```text
Non-Linearity
```

which allows deep networks to model real-world data.

---

# 3. Common Activation Functions

Modern Deep Learning commonly uses

| Activation Function | Typical Use |
|---------------------|-------------|
| Sigmoid | Binary classification output |
| Tanh | Older hidden layers |
| ReLU | Most hidden layers |
| Leaky ReLU | Hidden layers with dead neuron prevention |
| ELU | Hidden layers |
| GELU | Transformers and LLMs |
| Softmax | Multi-class classification output |

---

# 4. Sigmoid

Formula

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Output range

```text
0

↓

1
```

Advantages

- Probability interpretation
- Smooth curve

Disadvantages

- Vanishing Gradient Problem
- Slow convergence
- Not suitable for deep hidden layers

Typical use

```text
Binary Classification Output Layer
```

---

# 5. Tanh

Formula

$$
\tanh(x)
=
\frac{e^x-e^{-x}}
{e^x+e^{-x}}
$$

Output range

```text
-1

↓

1
```

Advantages

- Zero-centered outputs
- Better than Sigmoid for hidden layers

Disadvantages

- Still suffers from Vanishing Gradients

Typical use

Older neural networks.

---

# 6. ReLU (Rectified Linear Unit)

Formula

$$
f(x)
=
\max(0,x)
$$

Output

```text
Negative → 0

Positive → x
```

Advantages

- Very fast
- Simple
- Reduces Vanishing Gradient Problem
- Easy optimization

Disadvantages

- Dead ReLU Problem

Typical use

```text
Most Hidden Layers
```

ReLU is the default activation for many neural networks.

---

# 7. Leaky ReLU

Formula

$$
f(x)
=
\begin{cases}
x,&x>0\\
0.01x,&x<0
\end{cases}
$$

Instead of producing zero for negative values,

Leaky ReLU produces a small negative output.

Advantages

- Solves Dead ReLU Problem
- Stable optimization

Typical use

Deep neural networks where dead neurons become a concern.

---

# 8. ELU (Exponential Linear Unit)

ELU behaves similarly to ReLU,

but smoothly approaches a negative value for negative inputs.

Advantages

- Faster convergence than ReLU in some cases
- Reduces bias shift
- Produces smoother gradients

Disadvantages

- More computationally expensive than ReLU

Typical use

Specialized deep neural networks.

---

# 9. GELU (Gaussian Error Linear Unit)

GELU is one of the most important modern activation functions.

Instead of sharply removing negative values,

it smoothly weights neuron activations.

Advantages

- Smooth gradients
- Excellent optimization
- State-of-the-art performance

Typical use

- BERT
- GPT
- Llama
- Vision Transformers (ViT)
- Modern Transformer architectures

---

# 10. Softmax

Softmax converts outputs into probabilities.

Example

```text
Dog

0.10

Cat

0.75

Horse

0.15
```

Notice

All probabilities

```text
Sum = 1
```

Typical use

```text
Multi-Class Classification

Output Layer
```

---

# 11. Choosing the Right Activation Function

| Layer | Recommended Activation |
|-------|------------------------|
| Hidden Layer | ReLU |
| Hidden Layer (Dead ReLU issue) | Leaky ReLU |
| Transformer Models | GELU |
| Binary Classification Output | Sigmoid |
| Multi-Class Output | Softmax |

These are the most commonly used choices in practice.

---

# 12. Modern Deep Learning Practice

Today,

most deep learning models use

```text
Hidden Layers

↓

ReLU

or

GELU
```

Output layer depends on the task

```text
Binary Classification

↓

Sigmoid
```

```text
Multi-Class Classification

↓

Softmax
```

---

# 13. Real-Life Analogy

Imagine selecting employees.

Some applicants

```text
Rejected
```

Some

```text
Accepted
```

Activation functions decide

how strongly each neuron contributes to the next layer,

similar to deciding which employees continue to the next interview stage.

---

# 14. One Important Insight

Many beginners think

> **There is one best activation function for every neural network.**

This is incorrect.

The appropriate activation depends on

- Layer type
- Problem type
- Network architecture

For example,

ReLU is excellent for hidden layers,

while Softmax is designed specifically for multi-class outputs.

---

# Visual Summary

```text
Input

↓

Weighted Sum

↓

Activation Function

↓

Non-Linearity

↓

Prediction
```

---

# Comparison of Activation Functions

| Activation | Output Range | Typical Use | Main Limitation |
|------------|--------------|-------------|-----------------|
| Sigmoid | 0 to 1 | Binary output | Vanishing gradients |
| Tanh | -1 to 1 | Older hidden layers | Vanishing gradients |
| ReLU | 0 to ∞ | Hidden layers | Dead ReLU |
| Leaky ReLU | (-∞,∞) | Hidden layers | Small extra computation |
| ELU | (-α,∞) | Hidden layers | Slower than ReLU |
| GELU | Smooth | Transformers | Higher computation |
| Softmax | Probabilities | Multi-class output | Output layer only |

---

# Interview Questions

## Q1. Why are activation functions required?

**Answer**

They introduce non-linearity, enabling neural networks to learn complex relationships that cannot be modeled using only linear transformations.

---

## Q2. Which activation function is most commonly used in hidden layers?

**Answer**

ReLU is the most commonly used activation function for hidden layers.

---

## Q3. Which activation function is used for binary classification?

**Answer**

Sigmoid is typically used in the output layer for binary classification.

---

## Q4. Which activation function is used for multi-class classification?

**Answer**

Softmax is used in the output layer because it converts outputs into probabilities that sum to one.

---

## Q5. Which activation function is commonly used in Transformer models such as BERT and GPT?

**Answer**

GELU is widely used in modern Transformer architectures.

---

# Summary

Activation functions introduce non-linearity into neural networks, allowing them to learn complex patterns from data.

Different activation functions are suitable for different parts of a network.

ReLU is the standard choice for hidden layers, GELU is widely used in Transformer-based models, Sigmoid is used for binary classification outputs, and Softmax is used for multi-class classification outputs.

Selecting the correct activation function is an important hyperparameter decision that significantly influences optimization and model performance.

---

# Key Takeaways

✔ Activation functions introduce non-linearity.

✔ Without activation functions, deep networks behave like linear models.

✔ ReLU is the default choice for most hidden layers.

✔ GELU is commonly used in modern Transformer models.

✔ Sigmoid is used for binary classification outputs.

✔ Softmax is used for multi-class classification outputs.

✔ The best activation function depends on the task and network architecture.

---

# Next Part

## **Part 9 – Optimizer Selection**

In the next chapter, we will compare the major optimizers used in Deep Learning—**SGD, Momentum, Nesterov, AdaGrad, RMSProp, Adam, and AdamW**—learn how to choose the appropriate optimizer for different problems, and understand why **Adam and AdamW** are the default optimizers in many modern AI systems.
