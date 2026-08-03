# Unit 1 – Introduction to Neural Networks

# Chapter 1 – Artificial Neuron (Perceptron)

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why Artificial Neural Networks (ANNs) were invented.
- Explain the inspiration behind neural networks.
- Describe the biological neuron and its components.
- Explain the artificial neuron (Perceptron).
- Understand inputs, weights, bias, weighted sum, and activation function.
- Derive the mathematical equation of a perceptron.
- Explain the complete working of a perceptron.
- Understand the advantages and limitations of a perceptron.

---

# 1. Introduction

Artificial Intelligence aims to build machines capable of performing tasks that normally require human intelligence.

Examples include:

- Face Recognition
- Speech Recognition
- Machine Translation
- Medical Diagnosis
- Self-driving Cars
- Fraud Detection

Initially, these systems were built using **rule-based programming**.

Example:

```text
IF
Has Wings
AND Can Fly

THEN
Bird
```

This approach works only for simple problems.

For real-world applications, writing millions of rules becomes impossible.

Instead, we need systems that can **learn automatically from data.**

This gave birth to **Machine Learning**.

However, many Machine Learning algorithms struggle with highly complex data like:

- Images
- Videos
- Speech
- Natural Language

To solve these problems, researchers developed **Artificial Neural Networks (ANNs).**

---

# 2. Inspiration Behind Neural Networks

Artificial Neural Networks are inspired by the human brain.

The human brain contains approximately **86 billion neurons.**

These neurons communicate with each other continuously.

Each neuron:

- Receives information
- Processes information
- Sends information

Researchers simplified this biological process into a mathematical model known as an **Artificial Neuron**.

---

# 3. Biological Neuron

A biological neuron consists of four major components.

```text
Dendrites
     │
     ▼
Cell Body (Soma)
     │
     ▼
Axon
     │
     ▼
Axon Terminal
```

### Dendrites

Receive signals from other neurons.

### Cell Body (Soma)

Processes the received information.

### Axon

Carries the processed signal.

### Axon Terminal

Transfers the signal to the next neuron.

The biological neuron follows:

```text
Receive
   ↓
Process
   ↓
Send
```

---

# 4. Artificial Neuron

An Artificial Neuron is a mathematical model inspired by a biological neuron.

Instead of electrical impulses, it works with numbers.

Instead of biological learning, it adjusts mathematical parameters called **weights**.

Its job is to

- receive inputs
- process them
- produce an output

---

# Biological vs Artificial Neuron

| Biological Neuron | Artificial Neuron |
|-------------------|-------------------|
| Dendrites | Inputs |
| Synapse Strength | Weights |
| Cell Body | Weighted Sum |
| Brain Decision | Activation Function |
| Axon | Output |

---

# 5. Components of an Artificial Neuron

An artificial neuron consists of six components.

```text
Inputs
   │
   ▼
Weights
   │
   ▼
Weighted Sum
   │
   ▼
Bias
   │
   ▼
Activation Function
   │
   ▼
Output
```

---

# Component 1 — Inputs

Inputs are the information provided to the neuron.

They are represented as

$$
x_1,x_2,x_3,\ldots,x_n
$$

Examples:

### House Price Prediction

- Area
- Bedrooms
- House Age
- Distance from City

### Disease Prediction

- Age
- Weight
- Blood Sugar
- Blood Pressure

Each feature becomes one input variable.

Example

```text
x₁ = Area

x₂ = Bedrooms

x₃ = Age

x₄ = Distance
```

---

# Component 2 — Weights

Not every feature contributes equally.

Some features are more important than others.

Weights represent the importance of each input.

Weights are represented as

$$
w_1,w_2,w_3,\ldots,w_n
$$

Example

| Feature | Weight |
|----------|--------|
| Area | 0.90 |
| Bedrooms | 0.60 |
| Age | 0.30 |
| Paint Color | 0.05 |

A larger weight indicates greater influence on the prediction.

Weights are learned automatically during training.

---

# Component 3 — Input × Weight

Each input is multiplied by its corresponding weight.

Example

```text
x₁ × w₁

x₂ × w₂

x₃ × w₃
```

This determines how much each feature contributes.

Example

```text
Salary = 100

Weight = 0.8

Contribution = 80
```

Another feature

```text
Age = 45

Weight = 0.2

Contribution = 9
```

Salary influences the prediction more strongly.

---

# Component 4 — Weighted Sum

All contributions are added together.

$$
z=x_1w_1+x_2w_2+\cdots+x_nw_n
$$

Example

Suppose

```text
x₁ = 5

x₂ = 2

x₃ = 8
```

Weights

```text
w₁ = 4

w₂ = 1

w₃ = 2
```

Then

$$
z=5\times4+2\times1+8\times2
$$

$$
z=20+2+16=38
$$

This value is called the **weighted sum**.

---

# Component 5 — Bias

Bias is an additional value added after the weighted sum.

The equation becomes

$$
z=x_1w_1+x_2w_2+\cdots+x_nw_n+b
$$

Example

```text
Weighted Sum = 38

Bias = 4

Final z = 42
```

Bias allows the neuron to shift its decision boundary.

Without bias, the model becomes less flexible.

---

# Component 6 — Activation Function

The weighted sum can be any real number.

Example

```text
200

-35

8.5

1000
```

These values have no direct meaning.

An activation function converts the weighted sum into the neuron's final output.

Mathematically,

$$
a=f(z)
$$

where

- z = weighted sum + bias
- f = activation function
- a = neuron output

---

# Why Do We Need Activation Functions?

Without activation functions, every layer performs only a linear transformation.

Suppose

$$
y=2x+3
$$

Another layer

$$
z=4y+5
$$

Substituting,

$$
z=4(2x+3)+5
$$

$$
z=8x+17
$$

Even after combining multiple layers, the result remains a linear equation.

Therefore,

A neural network without activation functions behaves exactly like one linear model.

It cannot learn

- curves
- circles
- images
- speech
- language

Activation functions introduce **non-linearity**, allowing neural networks to solve complex problems.

---

# Step Activation Function

The original perceptron used the Step Function.

$$
f(z)=
\begin{cases}
1,&z\ge0\\
0,&z<0
\end{cases}
$$

Example

If

$$
z=6
$$

Output

```text
1
```

If

$$
z=-2
$$

Output

```text
0
```

The neuron simply answers

YES or NO.

---

# Limitations of Step Function

- Produces only 0 or 1.
- Cannot express probabilities.
- Not differentiable at the threshold.
- Cannot be trained effectively using Backpropagation.

These limitations led to modern activation functions like

- Sigmoid
- Tanh
- ReLU

---

# Complete Working of a Perceptron

```text
Input Features
      │
      ▼
Multiply by Weights
      │
      ▼
Weighted Sum
      │
      ▼
Add Bias
      │
      ▼
Activation Function
      │
      ▼
Output
```

---

# Numerical Example

Suppose

| Feature | Value | Weight |
|---------|------:|-------:|
| x₁ | 2 | 0.5 |
| x₂ | 3 | 0.2 |
| x₃ | 1 | 0.8 |

Bias

$$
b=1
$$

Step 1

$$
2\times0.5=1
$$

$$
3\times0.2=0.6
$$

$$
1\times0.8=0.8
$$

Step 2

$$
1+0.6+0.8=2.4
$$

Step 3

$$
z=2.4+1=3.4
$$

Step 4

Apply Step Function

Since

$$
z>0
$$

Output

```text
1
```

---

# Advantages of Perceptron

- Simple to understand.
- Easy to implement.
- Fast computation.
- Learns linear decision boundaries.
- Foundation of modern neural networks.

---

# Limitations of Perceptron

- Can solve only linearly separable problems.
- Cannot solve XOR-type problems.
- Uses Step Function.
- Cannot learn complex patterns.
- Single neuron has limited capability.

These limitations led to the development of the **Multi-Layer Perceptron (MLP)**.

---

# Chapter Summary

An Artificial Neuron is the smallest computational unit of a neural network.

Its working consists of:

1. Receive Inputs
2. Multiply by Weights
3. Compute Weighted Sum
4. Add Bias
5. Apply Activation Function
6. Produce Final Output

Mathematically,

$$
z=\sum_{i=1}^{n}x_iw_i+b
$$

$$
a=f(z)
$$

These two equations form the mathematical foundation of all modern deep learning models.

---

# Key Takeaways

✔ Artificial Neural Networks are inspired by the human brain.

✔ The perceptron is the basic building block of every neural network.

✔ Inputs represent features.

✔ Weights represent importance.

✔ Bias shifts the decision boundary.

✔ Weighted Sum combines all feature contributions.

✔ Activation Function introduces non-linearity.

✔ Without activation functions, deep neural networks collapse into a single linear model.

✔ The perceptron can solve only linearly separable problems.

✔ The Multi-Layer Perceptron was developed to overcome these limitations.



# Multi-Layer Perceptron (MLP) Notation
*(Based on the notation used in the class notes)*

---

# Introduction

In a Multi-Layer Perceptron (MLP), every layer, neuron, weight, bias, and output is represented using mathematical notation.

Understanding this notation is very important because the same symbols are used later in:

- Forward Propagation
- Backpropagation
- Gradient Descent
- Deep Learning algorithms

The notation below follows the convention used in the class notes.

---

# Layer Numbering

The network is divided into multiple layers.

```text
L₀ → Input Layer

L₁ → Hidden Layer 1

L₂ → Hidden Layer 2

L₃ → Output Layer
```

Notice that the **Input Layer is numbered as Layer 0**.

| Layer | Meaning |
|--------|---------|
| L₀ | Input Layer |
| L₁ | Hidden Layer 1 |
| L₂ | Hidden Layer 2 |
| L₃ | Output Layer |

---

# Network Architecture

Example network used in the notes

```text
               Layer 0             Layer 1             Layer 2             Layer 3

Input         Hidden Layer 1      Hidden Layer 2      Output Layer

x₁
x₂  ─────────► ○ ○ ○ ─────────► ○ ○ ─────────► ○
x₃
x₄
```

The network consists of

- 4 Input Neurons
- 3 Hidden Neurons (Layer 1)
- 2 Hidden Neurons (Layer 2)
- 1 Output Neuron

---

# 1. Input Notation

The input is represented as

\[
x_{ij}
\]

where

- **x** = Input
- **i** = Training Example (Sample Number)
- **j** = Feature Number

---

## Meaning

Suppose

Student 5 has

| Feature | Value |
|----------|------:|
| CGPA | 8.2 |
| IQ | 120 |
| Projects | 4 |
| Coding Score | 90 |

Then

```text
x₅₁ = 8.2

x₅₂ = 120

x₅₃ = 4

x₅₄ = 90
```

Meaning

- Sample Number = 5
- Feature Number = 1,2,3,4

---

## General Representation

\[
x_{ij}
\]

means

> Feature **j** of Training Example **i**.

---

# 2. Weight Notation

Weights are represented as

\[
w_{ij}^{k}
\]

This notation contains three indices.

---

## Meaning of Each Index

### Superscript

\[
k
\]

represents

**Layer Number**

Example

- \(w^1\) → Weights connecting Layer 0 to Layer 1
- \(w^2\) → Weights connecting Layer 1 to Layer 2
- \(w^3\) → Weights connecting Layer 2 to Layer 3

---

### First Subscript

\[
i
\]

represents

**Source Node (Current Layer)**

---

### Second Subscript

\[
j
\]

represents

**Destination Node (Next Layer)**

---

## General Meaning

\[
w_{ij}^{k}
\]

means

> Weight connecting

Node **i**

↓

Node **j**

in Layer **k**

---

# Examples

---

## Example 1

\[
w_{12}^{1}
\]

Meaning

```text
Layer 1

Input Node 1

↓

Hidden Layer 1

Neuron 2
```

---

## Example 2

\[
w_{43}^{1}
\]

Meaning

```text
Layer 1

Input Node 4

↓

Hidden Layer 1

Neuron 3
```

---

## Example 3

\[
w_{21}^{2}
\]

Meaning

```text
Layer 2

Hidden Layer 1

Neuron 2

↓

Hidden Layer 2

Neuron 1
```

---

## Example 4

\[
w_{12}^{2}
\]

Meaning

```text
Layer 2

Hidden Layer 1

Neuron 1

↓

Hidden Layer 2

Neuron 2
```

---

## Example 5

\[
w_{21}^{3}
\]

Meaning

```text
Layer 3

Hidden Layer 2

Neuron 2

↓

Output Neuron
```

---

# Why is the Superscript Necessary?

Suppose we simply write

\[
w_{12}
\]

Which connection is this?

- Input → Hidden Layer 1 ?
- Hidden Layer 1 → Hidden Layer 2 ?
- Hidden Layer 2 → Output Layer ?

Impossible to identify.

Therefore,

the superscript indicates **which layer of weights**.

---

# 3. Bias Notation

Bias is represented as

\[
b_{ij}
\]

where

- **i** = Layer Number
- **j** = Neuron Number

Each neuron has **one bias**.

Weights belong to **connections**.

Bias belongs to **neurons**.

---

## Example

### Hidden Layer 1

Biases

\[
b_{11},\;
b_{12},\;
b_{13}
\]

Meaning

```text
Layer 1

Neuron 1

Neuron 2

Neuron 3
```

---

### Hidden Layer 2

Biases

\[
b_{21},\;
b_{22}
\]

Meaning

```text
Layer 2

Neuron 1

Neuron 2
```

---

### Output Layer

Bias

\[
b_{31}
\]

Meaning

```text
Layer 3

Output Neuron
```

---

# Why Does Every Neuron Need a Bias?

Weights determine

> **How important is each input?**

Bias determines

> **How much should the decision boundary shift?**

Each neuron therefore requires exactly **one bias**.

---

# 4. Output Notation

Output is represented as

\[
o_{ij}
\]

where

- **i** = Layer Number
- **j** = Neuron Number

This follows exactly the same indexing convention as the bias notation.

---

## Hidden Layer 1 Outputs

\[
o_{11},\;
o_{12},\;
o_{13}
\]

Meaning

Outputs of

- Hidden Neuron 1
- Hidden Neuron 2
- Hidden Neuron 3

---

## Hidden Layer 2 Outputs

\[
o_{21},\;
o_{22}
\]

Meaning

Outputs of

- Hidden Neuron 1
- Hidden Neuron 2

---

## Output Layer

\[
o_{31}
\]

Meaning

Output produced by the final output neuron.

In prediction problems,

this is the network's final prediction.

---

# Complete Flow of Information

```text
Input Layer (L₀)

x

↓

Weights (w¹)

↓

Hidden Layer 1

↓

Outputs (o₁₁,o₁₂,o₁₃)

↓

Weights (w²)

↓

Hidden Layer 2

↓

Outputs (o₂₁,o₂₂)

↓

Weights (w³)

↓

Output Layer

↓

o₃₁
```

---

# Relationship Between Symbols

```text
Input

↓

x

↓

Weight

↓

w

↓

Bias

↓

b

↓

Neuron Computation

↓

Output

↓

o
```

---

# Summary Table

| Symbol | Meaning |
|----------|---------|
| \(L_0\) | Input Layer |
| \(L_1\) | Hidden Layer 1 |
| \(L_2\) | Hidden Layer 2 |
| \(L_3\) | Output Layer |
| \(x_{ij}\) | Feature **j** of Training Sample **i** |
| \(w_{ij}^{k}\) | Weight connecting Node **i** to Node **j** in Layer **k** |
| \(b_{ij}\) | Bias of Neuron **j** in Layer **i** |
| \(o_{ij}\) | Output of Neuron **j** in Layer **i** |

---

# Important Points to Remember

- Layers are numbered starting from **0**.
- Every **connection** has one **weight**.
- Every **neuron** has one **bias**.
- Every **neuron** produces one **output**.
- The superscript in the weight notation identifies **which layer of connections**.
- The first subscript identifies the **source node**.
- The second subscript identifies the **destination node**.
- This notation is used throughout **Forward Propagation**, **Backpropagation**, and the remaining Deep Learning topics.
