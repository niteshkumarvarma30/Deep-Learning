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

\[
x_1,x_2,x_3,\ldots,x_n
\]

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

\[
w_1,w_2,w_3,\ldots,w_n
\]

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

\[
z=x_1w_1+x_2w_2+\cdots+x_nw_n
\]

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

\[
z=5\times4+2\times1+8\times2
\]

\[
z=20+2+16=38
\]

This value is called the **weighted sum**.

---

# Component 5 — Bias

Bias is an additional value added after the weighted sum.

The equation becomes

\[
z=x_1w_1+x_2w_2+\cdots+x_nw_n+b
\]

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

\[
a=f(z)
\]

where

- z = weighted sum + bias
- f = activation function
- a = neuron output

---

# Why Do We Need Activation Functions?

Without activation functions, every layer performs only a linear transformation.

Suppose

\[
y=2x+3
\]

Another layer

\[
z=4y+5
\]

Substituting,

\[
z=4(2x+3)+5
\]

\[
z=8x+17
\]

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

\[
f(z)=
\begin{cases}
1,&z\ge0\\
0,&z<0
\end{cases}
\]

Example

If

\[
z=6
\]

Output

```text
1
```

If

\[
z=-2
\]

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

\[
b=1
\]

Step 1

\[
2\times0.5=1
\]

\[
3\times0.2=0.6
\]

\[
1\times0.8=0.8
\]

Step 2

\[
1+0.6+0.8=2.4
\]

Step 3

\[
z=2.4+1=3.4
\]

Step 4

Apply Step Function

Since

\[
z>0
\]

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

\[
z=\sum_{i=1}^{n}x_iw_i+b
\]

\[
a=f(z)
\]

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
