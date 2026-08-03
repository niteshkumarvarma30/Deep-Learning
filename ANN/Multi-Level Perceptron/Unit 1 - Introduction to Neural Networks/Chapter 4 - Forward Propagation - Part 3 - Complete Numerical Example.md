# Unit 1 – Introduction to Neural Networks

# Chapter 4 – Forward Propagation

## Part 3 – Complete Numerical Example

---

# Learning Objectives

After completing this part, you will be able to:

- Perform Forward Propagation manually.
- Calculate the weighted sum for every neuron.
- Add bias correctly.
- Apply the activation function.
- Compute hidden layer outputs.
- Compute the final network prediction.
- Understand the complete prediction process of a neural network.

---

# 1. Introduction

In Part 1, we learned what Forward Propagation is.

In Part 2, we studied its mathematical formulation.

Now, we will manually calculate every value exactly as a neural network does internally.

This example demonstrates how information flows from the Input Layer to the Output Layer.

---

# 2. Problem Statement

Consider the following neural network.

```text
          Layer 0              Layer 1             Layer 2

Input Layer             Hidden Layer          Output Layer

x₁ ───────────────► ○
                    │\
x₂ ───────────────► ○ ─────────────► ○
                    │/
x₃ ───────────────► ○
```

The network contains

- 3 Input Neurons
- 2 Hidden Neurons
- 1 Output Neuron

Our goal is to compute the final prediction.

---

# 3. Step 1 – Input Vector

Suppose the input values are

| Feature | Value |
|----------|------:|
| x₁ | 2 |
| x₂ | 3 |
| x₃ | 1 |

The input vector is

$$
X=
\begin{bmatrix}
2\\
3\\
1
\end{bmatrix}
$$

---

# 4. Step 2 – Weight Matrix (Input → Hidden Layer)

Suppose the weight matrix is

$$
W^{(1)}
=
\begin{bmatrix}
0.5 & 0.8\\
0.2 & 0.4\\
0.3 & 0.6
\end{bmatrix}
$$

Meaning

| Weight | Connection |
|---------|------------|
| 0.5 | x₁ → Hidden Neuron 1 |
| 0.8 | x₁ → Hidden Neuron 2 |
| 0.2 | x₂ → Hidden Neuron 1 |
| 0.4 | x₂ → Hidden Neuron 2 |
| 0.3 | x₃ → Hidden Neuron 1 |
| 0.6 | x₃ → Hidden Neuron 2 |

---

# 5. Step 3 – Hidden Layer Bias

Suppose

$$
B^{(1)}
=
\begin{bmatrix}
0.5\\
0.2
\end{bmatrix}
$$

Meaning

- Hidden Neuron 1 Bias = 0.5
- Hidden Neuron 2 Bias = 0.2

---

# 6. Step 4 – Compute Hidden Neuron 1

Formula

$$
z_1
=
x_1w_{11}
+
x_2w_{21}
+
x_3w_{31}
+
b_1
$$

Substitute the values

$$
=
2(0.5)
+
3(0.2)
+
1(0.3)
+
0.5
$$

Calculation

$$
=
1
+
0.6
+
0.3
+
0.5
=
2.4
$$

Therefore,

$$
z_1=2.4
$$

---

# 7. Step 5 – Apply Activation Function

Using the Sigmoid activation function

$$
\sigma(z)
=
\frac1{1+e^{-z}}
$$

Substitute

$$
\sigma(2.4)
$$

Result

$$
a_1
=
0.9168
$$

This is the output of Hidden Neuron 1.

---

# 8. Step 6 – Compute Hidden Neuron 2

Formula

$$
z_2
=
x_1w_{12}
+
x_2w_{22}
+
x_3w_{32}
+
b_2
$$

Substitute

$$
=
2(0.8)
+
3(0.4)
+
1(0.6)
+
0.2
$$

Calculation

$$
=
1.6
+
1.2
+
0.6
+
0.2
=
3.6
$$

Therefore,

$$
z_2
=
3.6
$$

---

# 9. Step 7 – Apply Activation Function

Using Sigmoid

$$
\sigma(3.6)
=
0.9734
$$

Therefore,

$$
a_2
=
0.9734
$$

---

# 10. Hidden Layer Output

The hidden layer output vector becomes

$$
A^{(1)}
=
\begin{bmatrix}
0.9168\\
0.9734
\end{bmatrix}
$$

These outputs become the inputs to the output layer.

---

# 11. Step 8 – Weight Matrix (Hidden → Output Layer)

Suppose

$$
W^{(2)}
=
\begin{bmatrix}
0.7\\
0.5
\end{bmatrix}
$$

Bias

$$
B^{(2)}
=
0.4
$$

---

# 12. Step 9 – Compute Output Neuron

Formula

$$
z
=
a_1w_1
+
a_2w_2
+
b
$$

Substitute

$$
=
0.9168(0.7)
+
0.9734(0.5)
+
0.4
$$

Calculation

$$
=
0.6418
+
0.4867
+
0.4
=
1.5285
$$

Therefore,

$$
z=1.5285
$$

---

# 13. Step 10 – Final Activation

Apply the Sigmoid function

$$
\hat{y}
=
\sigma(1.5285)
$$

Result

$$
\hat{y}
=
0.8217
$$

This is the final prediction of the neural network.

---

# 14. Decision Rule

Suppose the classification rule is

```text
If Probability ≥ 0.5

↓

Positive Class

Else

↓

Negative Class
```

Since

$$
0.8217 > 0.5
$$

The network predicts

```text
Positive Class
```

---

# 15. Complete Forward Propagation Flow

```text
Input

↓

X = [2,3,1]

↓

Hidden Layer

↓

z₁ = 2.4

↓

a₁ = 0.9168

↓

z₂ = 3.6

↓

a₂ = 0.9734

↓

Output Layer

↓

z = 1.5285

↓

ŷ = 0.8217

↓

Prediction
```

---

# 16. Matrix Representation

Instead of computing every neuron individually,

the same computation can be written as

### Hidden Layer

$$
Z^{(1)}
=
W^{(1)^T}
X
+
B^{(1)}
$$

$$
A^{(1)}
=
\sigma
\left(
Z^{(1)}
\right)
$$

---

### Output Layer

$$
Z^{(2)}
=
W^{(2)^T}
A^{(1)}
+
B^{(2)}
$$

$$
\hat{Y}
=
\sigma
\left(
Z^{(2)}
\right)
$$

These equations produce exactly the same results as the manual calculations.

---

# 17. Understanding the Prediction Process

Notice what happened during Forward Propagation.

The network

1. Received the input values.
2. Computed weighted sums.
3. Added biases.
4. Applied the activation function.
5. Generated hidden layer outputs.
6. Passed those outputs to the next layer.
7. Produced the final prediction.

At no stage were the weights updated.

The network only **computed a prediction**.

Learning will begin later using

- Loss Function
- Backpropagation
- Gradient Descent

---

# Summary

Forward Propagation is simply a sequence of repeated computations.

For every neuron,

Step 1

Compute the weighted sum

$$
z
=
\sum xw
+
b
$$

Step 2

Apply the activation function

$$
a
=
f(z)
$$

Step 3

Pass the activation to the next layer.

This process continues until the final prediction is obtained.

---

# Key Takeaways

✔ Forward Propagation computes predictions.

✔ Every neuron performs the same sequence of operations.

✔ Hidden layer outputs become the inputs of the next layer.

✔ Matrix equations and manual calculations produce identical results.

✔ During Forward Propagation, weights and biases remain unchanged.

✔ The final output of the network is called the prediction (\(\hat{y}\)).

✔ Learning begins only after the prediction is compared with the actual output.
