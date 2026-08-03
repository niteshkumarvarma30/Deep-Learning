# Unit 1 – Introduction to Neural Networks

# Chapter 2 – Multi-Layer Perceptron (MLP)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why a Single Perceptron is not sufficient.
- Explain linear and non-linear problems.
- Understand the XOR problem.
- Explain the architecture of a Multi-Layer Perceptron (MLP).
- Understand Input Layer, Hidden Layer, and Output Layer.
- Explain Fully Connected (Dense) Networks.
- Calculate the number of trainable parameters.
- Understand how an MLP processes information.

---

# 1. Introduction

In Chapter 1, we learned about the Perceptron.

A Perceptron

- receives inputs,
- multiplies them by weights,
- adds a bias,
- applies an activation function,
- produces an output.

Although it is the basic building block of neural networks, it has one major limitation.

A single perceptron can solve **only linear problems**.

Many real-world problems are not linear.

To solve them, researchers introduced the **Multi-Layer Perceptron (MLP).**

---

# 2. Why Does a Single Perceptron Fail?

Suppose we want to classify students into

- Pass
- Fail

Dataset

| Study Hours | Result |
|-------------|--------|
| 2 | Fail |
| 3 | Fail |
| 4 | Fail |
| 7 | Pass |
| 8 | Pass |
| 10 | Pass |

Graphically

```text
Pass

○ ○ ○

--------------------

● ● ●

Fail
```

A single straight line separates the classes.

A Perceptron solves this easily.

---

# 3. Linear Problems

A problem is called **linearly separable** if one straight line can correctly separate all classes.

Example

```text
○ ○ ○ ○

----------------

× × × ×
```

One straight line is sufficient.

Mathematically,

the perceptron learns

$$
w_1x_1+w_2x_2+b=0
$$

which represents a straight line.

---

# 4. Non-Linear Problems

Now consider

```text
○       ×

    ○

×       ○

    ×
```

No straight line can separate the two classes.

This is called a **Non-Linear Problem**.

A single perceptron fails because it can learn only one straight-line decision boundary.

---

# 5. XOR Problem

The XOR problem is the most famous example of a non-linear problem.

Truth Table

| Input A | Input B | Output |
|----------|----------|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Graph

```text
(0,1)      ○

(1,1)      ×



(0,0)      ×

(1,0)      ○
```

No single straight line can separate these classes.

Therefore,

a single perceptron cannot solve XOR.

---

# 6. Solution — Multi-Layer Perceptron (MLP)

Researchers solved this problem by combining multiple perceptrons.

Instead of

```text
Input

↓

Perceptron

↓

Output
```

they built

```text
Input

↓

Hidden Layer

↓

Hidden Layer

↓

Output
```

This architecture is called a

**Multi-Layer Perceptron (MLP).**

---

# 7. Definition

A Multi-Layer Perceptron is an Artificial Neural Network containing

- One Input Layer
- One or More Hidden Layers
- One Output Layer

The hidden layers allow the network to learn complex, non-linear relationships.

---

# 8. Layers of an MLP

An MLP consists of three types of layers.

---

## Input Layer

The Input Layer receives the input features.

Example

```text
Area

Bedrooms

Age

Distance
```

These become

```text
x₁

x₂

x₃

x₄
```

The Input Layer performs **no computation**.

It only forwards the data to the next layer.

---

## Hidden Layer

The Hidden Layer performs learning.

Each neuron computes

$$
z=w^Tx+b
$$

followed by an activation function.

Different neurons learn different features.

Example

Neuron 1 learns

```text
Large House
```

Neuron 2 learns

```text
Near City
```

Neuron 3 learns

```text
Luxury Area
```

These learned features are forwarded to the next layer.

---

## Output Layer

The Output Layer produces the final prediction.

Examples

### Binary Classification

```text
Spam

Not Spam
```

### Regression

```text
House Price
```

### Multi-Class Classification

```text
Cat

Dog

Horse

Car
```

---

# 9. Hidden Layer

The Hidden Layer is called "hidden" because

- the input is visible,
- the output is visible,
- but the computations inside are not directly observable.

Hidden neurons learn intermediate representations of the data.

They are often called

**Feature Extractors.**

---

# 10. Information Flow

During prediction,

information flows only in one direction.

```text
Input Layer

↓

Hidden Layer 1

↓

Hidden Layer 2

↓

Output Layer
```

This process is called

**Forward Propagation.**

---

# 11. Fully Connected (Dense) Network

In an MLP,

every neuron of one layer is connected to every neuron in the next layer.

Example

```text
Input Layer

●   ●   ●

|\ /|\ /|

| X | X |

|/ \|/ \|

●   ●

 \ /

  X

  |

  ●
```

Every connection has its own weight.

This is called a

**Fully Connected Layer**

or

**Dense Layer**.

---

# 12. Why Fully Connected?

Each hidden neuron should have access to every input feature.

Example

House Price Prediction

Features

- Area
- Bedrooms
- Age
- Distance

Each hidden neuron may require information from all four features.

Therefore,

every neuron is connected to every neuron in the next layer.

---

# 13. Number of Parameters

Suppose

- Input Neurons = 4
- Hidden Neurons = 3
- Output Neurons = 2

---

## Between Input and Hidden Layer

Weights

$$
4\times3=12
$$

Biases

$$
3
$$

Total

$$
15
$$

---

## Between Hidden and Output Layer

Weights

$$
3\times2=6
$$

Biases

$$
2
$$

Total

$$
8
$$

---

## Total Parameters

$$
15+8=23
$$

These are called

**Trainable Parameters.**

During training,

the network learns all these values automatically.

---

# 14. Working of an MLP

Suppose we are recognizing handwritten digits.

Input

```text
28 × 28 Image
```

↓

Hidden Layer 1 learns

```text
Edges

Lines

Curves
```

↓

Hidden Layer 2 learns

```text
Loops

Corners

Shapes
```

↓

Output Layer

```text
0

1

2

...

9
```

Each hidden layer learns increasingly complex information.

---

# 15. Advantages of MLP

- Solves non-linear problems.
- Learns complex patterns automatically.
- Supports multiple hidden layers.
- Performs feature extraction.
- Foundation of Deep Learning.
- Used for Classification and Regression.

---

# 16. Limitations of MLP

- More computationally expensive.
- Requires larger datasets.
- Training is slower than a single perceptron.
- Performance depends on hyperparameters.
- Can overfit small datasets.

---

# Difference Between Perceptron and MLP

| Perceptron | Multi-Layer Perceptron |
|------------|------------------------|
| One Layer | Multiple Layers |
| No Hidden Layer | One or More Hidden Layers |
| Solves Linear Problems | Solves Linear and Non-Linear Problems |
| Limited Learning Capacity | Learns Complex Patterns |
| Simple Decision Boundary | Complex Decision Boundary |

---

# Chapter Summary

A Single Perceptron is capable of learning only **linear decision boundaries**.

Real-world problems such as image recognition, speech recognition, and natural language processing are highly **non-linear**.

To solve these problems, multiple perceptrons are connected together to form a **Multi-Layer Perceptron (MLP).**

An MLP consists of

- Input Layer
- Hidden Layer(s)
- Output Layer

Every neuron in one layer connects to every neuron in the next layer, creating a **Fully Connected (Dense) Network**.

During training,

the network learns all weights and biases automatically.

This ability to learn complex, non-linear relationships makes the MLP the foundation of modern Deep Learning.

---

# Key Takeaways

✔ A Single Perceptron solves only linearly separable problems.

✔ XOR is a classic example of a non-linear problem.

✔ MLP overcomes the limitations of a single perceptron.

✔ An MLP contains an Input Layer, one or more Hidden Layers, and an Output Layer.

✔ Hidden Layers perform feature learning.

✔ Every connection has a trainable weight.

✔ Every neuron has one trainable bias.

✔ Fully Connected Networks connect every neuron to every neuron in the next layer.

✔ The total number of trainable parameters equals the total number of weights plus biases.

✔ The MLP is the foundation of modern Deep Learning architectures such as CNNs, RNNs, LSTMs, and Transformers.
