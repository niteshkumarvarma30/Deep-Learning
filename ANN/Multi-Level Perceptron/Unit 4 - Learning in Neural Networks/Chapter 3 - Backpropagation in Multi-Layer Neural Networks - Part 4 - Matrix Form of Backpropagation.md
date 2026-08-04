# Unit 4 – Learning in Neural Networks

# Chapter 3 – Backpropagation in Multi-Layer Neural Networks

## Part 4 – Matrix Form of Backpropagation

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why matrices are used instead of individual neurons.
- Learn the matrix notation used in neural networks.
- Write Forward Propagation using matrices.
- Write Backpropagation using matrices.
- Understand how PyTorch and TensorFlow internally perform neural network training.

---

# 1. Why Do We Need Matrices?

Until now, we considered only one neuron per layer.

```text
One Input

↓

One Hidden Neuron

↓

One Output Neuron
```

This was useful for learning the mathematics.

However, real neural networks are much larger.

Example

```text
784 Inputs

↓

512 Hidden Neurons

↓

256 Hidden Neurons

↓

10 Output Neurons
```

If we computed every neuron separately,

we would need thousands or even millions of equations.

Instead,

we combine all neurons into **vectors and matrices**.

This allows an entire layer to be computed using a single matrix multiplication.

---

# 2. Scalar Representation

Previously, for one neuron, we wrote

Hidden Layer

$$
z_1=W_1x+b_1
$$

Output Layer

$$
z_2=W_2a_1+b_2
$$

These equations work only for a single neuron.

---

# 3. Matrix Representation

Suppose the hidden layer contains three neurons and the input contains two features.

The weight matrix becomes

$$
W= \begin{bmatrix} w_{11} & w_{12}\\ w_{21} & w_{22}\\ w_{31} & w_{32} \end{bmatrix}
$$

Each row represents one neuron.

Each column corresponds to one input feature.

---

The input vector is

$$
x= \begin{bmatrix} x_1\\ x_2 \end{bmatrix}
$$

The bias vector is

$$
b= \begin{bmatrix} b_1\\ b_2\\ b_3 \end{bmatrix}
$$

Now the weighted sum becomes

$$
\boxed{ z=Wx+b }
$$

This single equation computes the weighted sums of **all neurons simultaneously**.

---

# 4. Matrix Form of Forward Propagation

For any layer \(l\),

the weighted sum is

$$
\boxed{ Z^{[l]} = W^{[l]}A^{[l-1]} + b^{[l]} }
$$

where

- \(W^{[l]}\) = Weight Matrix
- \(A^{[l-1]}\) = Activations from the previous layer
- \(b^{[l]}\) = Bias Vector
- \(Z^{[l]}\) = Weighted Sum Matrix

---

Next,

apply the activation function.

$$
\boxed{ A^{[l]} = f(Z^{[l]}) }
$$

The activation function is applied **element-wise** to every element of the matrix.

---

# 5. Complete Forward Propagation

For every layer,

Forward Propagation becomes

```text
Input Matrix

↓

Matrix Multiplication

↓

Weighted Sum (Z)

↓

Activation Function

↓

Activation Matrix (A)

↓

Next Layer
```

Instead of computing one neuron,

the entire layer is computed in one matrix operation.

---

# 6. Matrix Form of Backpropagation

Previously,

for one output neuron,

we computed

$$
\delta_2=\hat y-y
$$

In a real neural network,

the output layer contains many neurons.

Therefore,

the output delta becomes

$$
\boxed{ \delta^{[L]} = A^{[L]} - Y }
$$

where

- \(L\) = Output layer
- \(A^{[L]}\) = Predicted outputs
- \(Y\) = True labels

This computes the error for every output neuron simultaneously.

---

# 7. Matrix Form of Hidden Layer Delta

Previously,

we wrote

$$
\delta_1 = W_2^T \delta_2 \odot f'(z_1)
$$

For any hidden layer,

the matrix equation becomes

$$
\boxed{ \delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(Z^{[l]}) }
$$

where

- \((W^{[l+1]})^T\) = Transpose of the next layer's weight matrix
- \(\delta^{[l+1]}\) = Error from the next layer
- \(f'(Z^{[l]})\) = Derivative of the activation function
- \(\odot\) = Element-wise (Hadamard) multiplication

This equation propagates the error backward through the network.

---

# 8. Matrix Form of Weight Gradients

Once the delta has been computed,

the weight gradients are

$$
\boxed{ \frac{\partial L} {\partial W^{[l]}} = \delta^{[l]} (A^{[l-1]})^T }
$$

where

- \(\delta^{[l]}\) = Error vector of the current layer
- \((A^{[l-1]})^T\) = Transpose of the previous layer's activations

This computes the gradients of **all weights** simultaneously.

---

# 9. Matrix Form of Bias Gradients

The bias gradients are

$$
\boxed{ \frac{\partial L} {\partial b^{[l]}} = \delta^{[l]} }
$$

Each neuron has one corresponding bias gradient.

---

# 10. Matrix Form of Gradient Descent

Previously,

for one weight,

we wrote

$$
W = W - \eta \frac{\partial L}{\partial W}
$$

Now,

the update is performed on the entire weight matrix.

$$
\boxed{ W^{[l]} = W^{[l]} - \eta \frac{\partial L} {\partial W^{[l]}} }
$$

Similarly,

the bias vector is updated using

$$
\boxed{ b^{[l]} = b^{[l]} - \eta \frac{\partial L} {\partial b^{[l]}} }
$$

Every parameter in the layer is updated simultaneously.

---

# 11. Complete Matrix Backpropagation Algorithm

## Forward Propagation

Weighted Sum

$$
Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}
$$

Activation

$$
A^{[l]} = f(Z^{[l]})
$$

---

## Output Layer Delta

$$
\delta^{[L]} = A^{[L]} - Y
$$

---

## Hidden Layer Delta

$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(Z^{[l]})
$$

---

## Weight Gradient

$$
\frac{\partial L} {\partial W^{[l]}} = \delta^{[l]} (A^{[l-1]})^T
$$

---

## Bias Gradient

$$
\frac{\partial L} {\partial b^{[l]}} = \delta^{[l]}
$$

---

## Parameter Updates

$$
W^{[l]} = W^{[l]} - \eta \frac{\partial L} {\partial W^{[l]}}
$$

$$
b^{[l]} = b^{[l]} - \eta \frac{\partial L} {\partial b^{[l]}}
$$

---

# 12. Why Is Matrix Form Important?

Suppose a neural network has

```text
1000 Inputs

↓

500 Hidden Neurons
```

Without matrices,

you would compute

```text
500 Separate Equations
```

With matrices,

the entire layer is computed using **one matrix multiplication**.

This is why GPUs are extremely efficient for Deep Learning.

---

# 13. How PyTorch Works Internally

When you write

```python
output = model(x)

loss = criterion(output, target)

loss.backward()

optimizer.step()
```

PyTorch internally performs

```text
Forward Propagation

↓

Compute Loss

↓

Matrix Backpropagation

↓

Matrix Gradients

↓

Matrix Weight Updates
```

It never computes neurons individually.

Everything is vectorized.

---

# 14. Real-Life Analogy

Imagine grading students.

Without matrices

```text
Student 1

↓

Student 2

↓

Student 3

↓

...
```

Each student is graded separately.

With matrices

```text
Entire Class

↓

Spreadsheet

↓

One Formula
```

All students are processed simultaneously.

Neural networks work the same way.

---

# 15. One Important Insight

Many beginners imagine that neural networks perform Backpropagation

```text
Neuron

↓

Neuron

↓

Neuron
```

This is useful for learning,

but it is **not** how modern Deep Learning libraries work.

In reality,

they perform

```text
Matrix Multiplication

↓

Matrix Differentiation

↓

Matrix Gradient Computation

↓

Matrix Parameter Updates
```

This vectorized computation is one of the main reasons GPUs can train networks containing millions or billions of parameters efficiently.

---

# Difference Between Scalar and Matrix Backpropagation

| Scalar Form | Matrix Form |
|-------------|-------------|
| One neuron at a time | Entire layer at once |
| One weight | Weight matrix |
| One bias | Bias vector |
| Individual equations | Matrix equations |
| Educational understanding | Real-world implementation |
| Slow for large networks | Highly efficient |

---

# Interview Questions

## Q1. Why do Deep Learning frameworks use matrices?

**Answer**

Matrices allow all neurons in a layer to be processed simultaneously, making training much faster and more computationally efficient.

---

## Q2. What is the matrix form of Forward Propagation?

**Answer**

$$
Z^{[l]}=W^{[l]}A^{[l-1]}+b^{[l]}
$$

$$
A^{[l]}=f(Z^{[l]})
$$

---

## Q3. What is the matrix form of the hidden-layer delta?

**Answer**

$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(Z^{[l]})
$$

---

## Q4. How are weight gradients computed in matrix form?

**Answer**

$$
\frac{\partial L}{\partial W^{[l]}} = \delta^{[l]} (A^{[l-1]})^T
$$

---

## Q5. Does PyTorch compute gradients neuron by neuron?

**Answer**

No.

PyTorch performs vectorized matrix operations, allowing entire layers to be processed simultaneously.

---

# Summary

Real neural networks contain many neurons in each layer.

Instead of computing every neuron individually, Deep Learning frameworks represent inputs, weights, activations, biases, and gradients as **vectors and matrices**.

Forward Propagation becomes matrix multiplication followed by element-wise activation.

Backpropagation computes matrix-based error terms (delta vectors), matrix gradients, and matrix parameter updates.

This vectorized representation enables efficient GPU computation and forms the mathematical foundation of modern Deep Learning libraries.

---

# Key Takeaways

✔ Matrix notation replaces individual neuron equations.

✔ Forward Propagation uses matrix multiplication.

✔ Activation functions are applied element-wise.

✔ Backpropagation computes matrix deltas.

✔ Matrix gradients update all weights simultaneously.

✔ Modern frameworks such as PyTorch and TensorFlow use vectorized matrix operations internally.

✔ Matrix representation is essential for training large neural networks efficiently.

---

## Next Part

**Part 5 – Complete Backpropagation Algorithm (Pseudo-code and Training Pipeline)**

In the next chapter, we will combine everything learned in Unit 4 into a complete neural network training algorithm, showing the exact sequence of operations performed during every training iteration from initialization to convergence.
