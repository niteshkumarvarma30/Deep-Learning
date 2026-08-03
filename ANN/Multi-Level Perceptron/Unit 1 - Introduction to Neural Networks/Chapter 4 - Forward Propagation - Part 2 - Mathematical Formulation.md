# Unit 1 – Introduction to Neural Networks

# Chapter 4 – Forward Propagation

## Part 2 – Mathematical Formulation

---

# Learning Objectives

After completing this part, you will be able to:

- Understand the mathematical representation of a neural network.
- Define the Input Matrix.
- Define the Weight Matrix.
- Define the Bias Vector.
- Compute the weighted sum using matrix multiplication.
- Understand activation vectors.
- Write the complete Forward Propagation equations.
- Verify matrix dimensions.

---

# 1. Introduction

In Part 1, we learned that during Forward Propagation, information moves from the Input Layer to the Output Layer.

Now we will learn **how every layer performs its calculations mathematically.**

Instead of computing each neuron separately, modern neural networks perform calculations using **matrices**.

This approach is

- Faster
- Simpler
- Computationally efficient

---

# 2. Why Do We Use Matrix Form?

Suppose a neural network contains

- 1000 input neurons
- 500 hidden neurons

If we compute each neuron individually,

the calculations become extremely lengthy.

Instead,

all neurons are computed simultaneously using **matrix multiplication**.

This technique is called

**Vectorized Computation.**

---

# 3. Network Used in This Chapter

Throughout this chapter, consider the following neural network.

```text
Layer 0 (Input)

4 Neurons

↓

Layer 1 (Hidden)

3 Neurons

↓

Layer 2 (Output)

2 Neurons
```

---

# 4. Input Vector

Suppose we want to predict the price of a house.

Input Features

| Feature | Value |
|----------|------:|
| Area | 1200 |
| Bedrooms | 3 |
| Age | 5 |
| Distance | 10 |

The input vector becomes

$$
X=
\begin{bmatrix}
1200\\
3\\
5\\
10
\end{bmatrix}
$$

General form

$$
X=
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
\vdots\\
x_n
\end{bmatrix}
$$

---

# Why is X a Column Vector?

Each row represents one feature.

Example

```text
x₁

x₂

x₃

x₄
```

instead of

```text
x₁ x₂ x₃ x₄
```

This arrangement allows proper matrix multiplication.

---

# 5. Weight Matrix

Suppose

- Input Neurons = 4
- Hidden Neurons = 3

Every input neuron is connected to every hidden neuron.

Total number of weights

$$
4\times3=12
$$

Instead of storing them individually,

we organize them into one matrix.

$$
W^{(1)}
=
\begin{bmatrix}
w_{11}^{1} & w_{12}^{1} & w_{13}^{1}\\
w_{21}^{1} & w_{22}^{1} & w_{23}^{1}\\
w_{31}^{1} & w_{32}^{1} & w_{33}^{1}\\
w_{41}^{1} & w_{42}^{1} & w_{43}^{1}
\end{bmatrix}
$$

Rows correspond to

```text
Input Neurons
```

Columns correspond to

```text
Hidden Neurons
```

---

# Meaning of a Weight

Example

$$
w_{23}^{1}
$$

means

```text
Layer 1

Input Neuron 2

↓

Hidden Neuron 3
```

Another example

$$
w_{41}^{1}
$$

means

```text
Layer 1

Input Neuron 4

↓

Hidden Neuron 1
```

---

# 6. Bias Vector

Each neuron has exactly one bias.

Since the hidden layer contains three neurons,

its bias vector is

$$
B^{(1)}
=
\begin{bmatrix}
b_{11}\\
b_{12}\\
b_{13}
\end{bmatrix}
$$

General form

$$
B=
\begin{bmatrix}
b_1\\
b_2\\
\vdots
\end{bmatrix}
$$

---

# Important Observation

Weights belong to

```text
Connections
```

Bias belongs to

```text
Neurons
```

Every neuron has exactly one bias.

---

# 7. Weighted Sum

For one neuron,

the weighted sum is

$$
z=w_1x_1+w_2x_2+\cdots+w_nx_n+b
$$

Instead of calculating every neuron separately,

we compute all neurons together.

$$
Z^{(1)}
=
W^{(1)^T}X+B^{(1)}
$$

The result is

$$
Z^{(1)}
=
\begin{bmatrix}
z_1\\
z_2\\
z_3
\end{bmatrix}
$$

Each element represents the weighted sum of one hidden neuron.

---

# 8. What Does Z Represent?

Z represents

```text
Weighted Sum

Before Activation
```

Example

```text
Neuron 1

↓

8.5

Neuron 2

↓

−2

Neuron 3

↓

4.1
```

These values are **not** the final outputs.

They are only intermediate computations.

---

# 9. Activation Vector

The activation function is applied to every element of Z.

$$
A^{(1)}
=
f(Z^{(1)})
$$

Suppose

$$
Z=
\begin{bmatrix}
8\\
-2\\
4
\end{bmatrix}
$$

Using the Sigmoid activation function,

$$
A=
\begin{bmatrix}
0.9997\\
0.1192\\
0.9820
\end{bmatrix}
$$

The activation vector becomes the input to the next layer.

---

# 10. Second Layer Computation

Exactly the same process is repeated.

Weight Matrix

$$
W^{(2)}
$$

Bias Vector

$$
B^{(2)}
$$

Weighted Sum

$$
Z^{(2)}
=
W^{(2)^T}
A^{(1)}
+
B^{(2)}
$$

Activation

$$
A^{(2)}
=
f(Z^{(2)})
$$

---

# 11. General Forward Propagation Equation

For any layer

Weighted Sum

$$
\boxed{
Z^{(l)}
=
W^{(l)^T}
A^{(l-1)}
+
B^{(l)}
}
$$

Activation

$$
\boxed{
A^{(l)}
=
f(Z^{(l)})
}
$$

where

- \(l\) = Current Layer
- \(A^{(l-1)}\) = Output of Previous Layer
- \(W^{(l)}\) = Weight Matrix
- \(B^{(l)}\) = Bias Vector
- \(Z^{(l)}\) = Weighted Sum
- \(A^{(l)}\) = Activation Output

These two equations are repeated for every hidden layer and the output layer.

---

# 12. Matrix Dimensions

Dimension checking is very important.

Suppose

```text
Input Layer

4 Neurons

↓

Hidden Layer

3 Neurons
```

Then

Input

$$
X
=
4\times1
$$

Weight Matrix

$$
W^{(1)}
=
4\times3
$$

Weight Transpose

$$
W^{(1)^T}
=
3\times4
$$

Bias

$$
B^{(1)}
=
3\times1
$$

Weighted Sum

$$
Z^{(1)}
=
3\times1
$$

Activation

$$
A^{(1)}
=
3\times1
$$

Everything matches perfectly.

---

# 13. Complete Forward Flow

```text
Input Vector

↓

X

↓

Weight Matrix

↓

W

↓

Matrix Multiplication

↓

WX

↓

Bias Addition

↓

WX+B

↓

Activation Function

↓

A

↓

Next Layer
```

The same sequence is repeated until the output layer.

---

# 14. Relation with Professor's Notation

Your class notes use

```text
xᵢⱼ

↓

wᵏᵢⱼ

↓

bᵢⱼ

↓

oᵢⱼ
```

The equivalent matrix notation is

| Professor's Notation | Matrix Notation |
|----------------------|-----------------|
| \(x_{ij}\) | Input Matrix \(X\) |
| \(w_{ij}^{k}\) | Weight Matrix \(W^{(k)}\) |
| \(b_{ij}\) | Bias Vector \(B^{(k)}\) |
| \(o_{ij}\) | Activation Matrix \(A^{(k)}\) |

The matrix equations are simply a compact representation of the same computations.

---

# Why Matrix Representation?

Matrix representation offers several advantages:

- Reduces lengthy calculations.
- Makes implementation easier.
- Allows efficient GPU computation.
- Enables vectorized operations.
- Used by frameworks such as TensorFlow, PyTorch, and JAX.

Without matrix operations, training modern deep learning models would be computationally impractical.

---

# Chapter Summary

Forward Propagation in matrix form consists of two fundamental equations.

### Linear Transformation

$$
Z^{(l)}
=
W^{(l)^T}
A^{(l-1)}
+
B^{(l)}
$$

### Activation

$$
A^{(l)}
=
f(Z^{(l)})
$$

Every layer repeats these two operations.

The output of one layer becomes the input of the next layer until the final prediction is produced.

---

# Key Takeaways

✔ Neural networks use matrix operations instead of individual neuron calculations.

✔ Inputs are stored in an Input Vector.

✔ Weights are stored in Weight Matrices.

✔ Biases are stored in Bias Vectors.

✔ The weighted sum is computed using matrix multiplication.

✔ Activation functions convert weighted sums into neuron outputs.

✔ Every layer performs the same two operations:

1. Linear Transformation

$$
Z=W^TA+B
$$

2. Activation

$$
A=f(Z)
$$

✔ Matrix representation makes neural networks fast, efficient, and scalable.

✔ This mathematical formulation is the foundation of all modern Deep Learning architectures.
