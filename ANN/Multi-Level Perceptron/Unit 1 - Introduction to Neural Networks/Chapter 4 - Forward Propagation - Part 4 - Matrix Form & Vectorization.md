# Unit 1 – Introduction to Neural Networks

# Chapter 4 – Forward Propagation

## Part 4 – Matrix Form & Vectorization

---

# Learning Objectives

After completing this part, you will be able to:

- Understand vectorization.
- Explain why loops are avoided in Deep Learning.
- Process multiple neurons simultaneously.
- Process multiple training examples simultaneously.
- Understand batch processing.
- Understand how TensorFlow, PyTorch and NumPy perform Forward Propagation.

---

# 1. Introduction

In the previous parts, we manually calculated the output of every neuron.

Although manual calculations help us understand the mathematics, they are **not** how modern Deep Learning frameworks work.

Imagine a neural network with

- 784 input neurons
- 512 hidden neurons
- 256 hidden neurons
- 10 output neurons

Calculating every neuron one by one would require thousands of calculations.

Instead,

modern Deep Learning libraries use **Matrix Operations**.

This technique is called

**Vectorization.**

---

# 2. What is Vectorization?

## Definition

Vectorization is the process of performing calculations on an entire vector or matrix at once instead of computing one value at a time.

Instead of

```python
for neuron in neurons:
    compute_output(neuron)
```

the entire layer is computed using one matrix multiplication.

---

# 3. Why Do We Need Vectorization?

Suppose a Hidden Layer contains

100 neurons.

Without vectorization

```text
Neuron 1

↓

Neuron 2

↓

Neuron 3

↓

...

↓

Neuron 100
```

Each neuron is computed separately.

This is slow.

---

Using vectorization

```text
Entire Hidden Layer

↓

One Matrix Multiplication
```

All neurons are computed simultaneously.

---

# 4. Manual Computation vs Matrix Computation

Without Vectorization

For three neurons,

$$
z_1=w_1x+b_1
$$

$$
z_2=w_2x+b_2
$$

$$
z_3=w_3x+b_3
$$

Three different equations.

---

With Vectorization

$$
Z=WX+B
$$

One equation computes every neuron together.

---

# 5. Example

Suppose

Input

$$
X=
\begin{bmatrix}
2\\
3\\
1
\end{bmatrix}
$$

Weight Matrix

$$
W=
\begin{bmatrix}
0.5&0.8\\
0.2&0.4\\
0.3&0.6
\end{bmatrix}
$$

Bias

$$
B=
\begin{bmatrix}
0.5\\
0.2
\end{bmatrix}
$$

Instead of calculating

```text
Neuron 1

↓

Neuron 2
```

individually,

we simply compute

$$
Z=W^TX+B
$$

Both neurons are computed together.

---

# 6. Vectorized Activation

After computing

$$
Z
$$

the activation function is applied to every element.

Without Vectorization

```text
a₁=sigmoid(z₁)

a₂=sigmoid(z₂)

a₃=sigmoid(z₃)
```

With Vectorization

$$
A=f(Z)
$$

Example

Suppose

$$
Z=
\begin{bmatrix}
2\\
4\\
-1
\end{bmatrix}
$$

Applying Sigmoid

$$
A=
\begin{bmatrix}
0.8808\\
0.9820\\
0.2689
\end{bmatrix}
$$

The activation function is applied automatically to every element.

---

# 7. Processing Multiple Training Examples

Until now,

we processed only one training example.

Example

```text
One House

↓

Prediction
```

Real Deep Learning systems process many examples together.

Suppose we have

4 houses.

Instead of

```text
House 1

↓

House 2

↓

House 3

↓

House 4
```

we create one matrix.

$$
X=
\begin{bmatrix}
1200&1500&1800&900\\
3&4&3&2\\
5&8&2&10
\end{bmatrix}
$$

Notice

Each column represents one training example.

Each row represents one feature.

One matrix multiplication computes predictions for all four houses.

---

# 8. Batch Processing

A collection of training examples processed together is called a

**Batch**.

Suppose we have

10,000 images.

Instead of processing them individually,

we divide them into batches.

Example

```text
Batch 1

32 Images
```

↓

```text
Batch 2

32 Images
```

↓

```text
Batch 3

32 Images
```

Each batch is processed independently.

---

# 9. Batch Size

The number of training examples in one batch is called the

**Batch Size.**

Common batch sizes are

```text
16

32

64

128

256
```

Batch size is a **hyperparameter** selected before training.

---

# 10. Why is Vectorization Faster?

Modern CPUs and GPUs are optimized for matrix operations.

Instead of performing

```text
Multiply

↓

Add

↓

Multiply

↓

Add
```

thousands of times,

they execute large matrix operations in parallel.

This significantly reduces computation time.

---

# 11. GPU Acceleration

GPUs contain thousands of small processing cores.

These cores perform

- Matrix Multiplication
- Matrix Addition
- Element-wise Operations

simultaneously.

This is why GPUs are much faster than CPUs for training Deep Learning models.

---

# 12. How Deep Learning Libraries Work

Libraries such as

- NumPy
- TensorFlow
- PyTorch
- JAX

do not calculate each neuron manually.

Instead, they execute operations such as

```python
Z = W.T @ X + B
A = activation(Z)
```

These operations are internally optimized and often executed on GPUs.

---

# 13. Manual vs Vectorized Computation

| Manual Computation | Vectorized Computation |
|--------------------|------------------------|
| One neuron at a time | Entire layer together |
| Uses loops | Uses matrix multiplication |
| Slower | Faster |
| Good for understanding | Used in real applications |

---

# 14. Complete Vectorized Forward Propagation

For every layer,

Step 1

Linear Transformation

$$
Z^{(l)}
=
W^{(l)^T}
A^{(l-1)}
+
B^{(l)}
$$

Step 2

Activation

$$
A^{(l)}
=
f
\left(
Z^{(l)}
\right)
$$

Repeat these two steps until the Output Layer.

---

# 15. Complete Flow

```text
Input Matrix

↓

Matrix Multiplication

↓

Weighted Sum

↓

Bias Addition

↓

Activation Function

↓

Output Matrix

↓

Next Layer

↓

Repeat

↓

Final Prediction
```

---

# 16. Advantages of Vectorization

- Faster computation.
- Eliminates explicit loops.
- Efficient GPU utilization.
- Simpler mathematical representation.
- Enables batch processing.
- Reduces execution time.
- Used in all modern Deep Learning frameworks.

---

# 17. Real-World Analogy

Imagine checking exam papers.

### Manual Method

```text
Student 1

↓

Student 2

↓

Student 3

↓

...

Student 100
```

One paper is checked at a time.

---

### Vectorized Method

All answer sheets are scanned into software.

The software checks every paper simultaneously.

This is exactly how vectorization works in Deep Learning.

---

# Chapter Summary

Vectorization is the process of replacing repeated neuron-by-neuron calculations with matrix operations.

Instead of calculating each neuron individually,

the outputs of all neurons are computed together using matrix multiplication.

Similarly,

instead of processing one training example at a time,

multiple training examples are grouped into batches and processed simultaneously.

This makes neural networks extremely fast and scalable.

Modern Deep Learning libraries such as TensorFlow, PyTorch, NumPy and JAX all rely heavily on vectorized computations.

---

# Key Takeaways

✔ Vectorization computes entire layers simultaneously.

✔ Matrix multiplication replaces loops.

✔ The activation function is applied element-wise to the output matrix.

✔ Batch processing allows multiple training examples to be processed together.

✔ GPUs accelerate vectorized matrix operations.

✔ TensorFlow, PyTorch, NumPy and JAX all use vectorized computations internally.

✔ Vectorization is one of the key reasons modern Deep Learning models can be trained efficiently.
