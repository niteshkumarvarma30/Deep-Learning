# Unit 1 – Introduction to Neural Networks

# Chapter 4 – Forward Propagation

## Part 5 – Complete Forward Propagation Pipeline

---

# Learning Objectives

After completing this part, you will be able to:

- Understand the complete Forward Propagation pipeline.
- Explain what happens at every layer of a neural network.
- Connect the mathematical equations with the actual computation.
- Understand how Deep Learning frameworks perform Forward Propagation.
- Prepare for the next chapter (Loss Function).

---

# 1. Introduction

In the previous parts, we studied Forward Propagation step by step.

- Part 1 explained the basic concept.
- Part 2 introduced the mathematical equations.
- Part 3 demonstrated a complete numerical example.
- Part 4 explained matrix computation and vectorization.

Now, we combine everything into one complete pipeline.

---

# 2. Complete Forward Propagation Pipeline

The complete prediction process of a neural network is

```text
Input

↓

Weights

↓

Weighted Sum

↓

Bias Addition

↓

Activation Function

↓

Hidden Layer Output

↓

Repeat for Every Layer

↓

Final Prediction
```

This entire sequence is called

**Forward Propagation**

---

# 3. Step-by-Step Pipeline

Consider the following neural network.

```text
Input Layer

↓

Hidden Layer 1

↓

Hidden Layer 2

↓

Output Layer
```

The computation proceeds layer by layer.

---

## Step 1 — Receive Input

The network receives the input features.

Example

```text
Area

Bedrooms

Age

Distance
```

These features are stored in

$$
X
$$

The Input Layer performs **no computation**.

It only forwards the input values to the first hidden layer.

---

## Step 2 — Hidden Layer 1

The first hidden layer performs two operations.

### Linear Transformation

$$
Z^{(1)}
=
W^{(1)^T}
X
+
B^{(1)}
$$

where

- \(W^{(1)}\) = Weight Matrix
- \(X\) = Input Vector
- \(B^{(1)}\) = Bias Vector

---

### Activation Function

$$
A^{(1)}
=
f
\left(
Z^{(1)}
\right)
$$

The activation function converts the weighted sums into neuron outputs.

These outputs become the inputs for the next hidden layer.

---

## Step 3 — Hidden Layer 2

The second hidden layer repeats the same computation.

### Linear Transformation

$$
Z^{(2)}
=
W^{(2)^T}
A^{(1)}
+
B^{(2)}
$$

### Activation Function

$$
A^{(2)}
=
f
\left(
Z^{(2)}
\right)
$$

Again,

the output of this layer becomes the input to the next layer.

---

## Step 4 — Output Layer

The output layer performs exactly the same computation.

### Linear Transformation

$$
Z^{(3)}
=
W^{(3)^T}
A^{(2)}
+
B^{(3)}
$$

### Activation Function

$$
A^{(3)}
=
f
\left(
Z^{(3)}
\right)
$$

The final output is

$$
\hat{Y}
=
A^{(3)}
$$

This is the prediction of the neural network.

---

# 4. Universal Forward Propagation Algorithm

Every Feed Forward Neural Network follows the same algorithm.

```text
Receive Input

↓

FOR Every Layer

↓

Multiply Inputs by Weights

↓

Add Bias

↓

Apply Activation Function

↓

Pass Output to Next Layer

↓

END FOR

↓

Return Final Prediction
```

This algorithm is independent of the network architecture.

Whether the model is

- ANN
- CNN
- RNN
- Transformer

the forward computation follows this same principle.

---

# 5. General Mathematical Form

For any layer \(l\),

### Step 1

Compute the weighted sum

$$
Z^{(l)}
=
W^{(l)^T}
A^{(l-1)}
+
B^{(l)}
$$

---

### Step 2

Apply the activation function

$$
A^{(l)}
=
f
\left(
Z^{(l)}
\right)
$$

Repeat these two equations until the Output Layer.

These are the fundamental equations of Forward Propagation.

---

# 6. Information Flow

During Forward Propagation,

information always flows in one direction.

```text
Input

↓

Hidden Layer

↓

Hidden Layer

↓

Output
```

There is **no backward movement** while making predictions.

Backward movement occurs only during Backpropagation.

---

# 7. What Changes During Forward Propagation?

Many beginners think everything changes.

Actually,

only one thing changes.

The **representation of the data**.

Example

```text
Pixels

↓

Edges

↓

Corners

↓

Shapes

↓

Objects
```

Every layer extracts more meaningful information than the previous layer.

The data becomes increasingly abstract and informative.

---

# 8. What Does NOT Change?

During Forward Propagation,

the following remain fixed.

### Weights

```text
Remain Constant
```

### Biases

```text
Remain Constant
```

### Network Architecture

```text
Remain Constant
```

The network only performs computation.

Learning does not occur during this phase.

---

# 9. Complete Forward Propagation Flow

```text
Input Features

↓

Input Layer

↓

Linear Transformation

(Z = WX + B)

↓

Activation Function

↓

Hidden Layer Output

↓

Linear Transformation

↓

Activation Function

↓

Output Layer

↓

Final Prediction (ŷ)
```

Every hidden layer repeats the same sequence of operations.

---

# 10. Why Forward Propagation Alone is Not Enough?

Suppose

Prediction

```text
Dog
```

Actual Answer

```text
Cat
```

Forward Propagation tells us only

```text
Prediction = Dog
```

It does **not** tell us

- How wrong the prediction is.
- How the weights should be updated.
- How to improve future predictions.

To answer these questions,

we need a method to measure the error.

That method is called the

**Loss Function**.

---

# 11. Transition to the Next Chapter

After Forward Propagation,

the neural network has produced its prediction.

The next logical question is

> **Was the prediction correct?**

To determine this,

the network compares

- Actual Output
- Predicted Output

The difference between them is measured using a

**Loss Function**.

Without a Loss Function,

the network has no way of knowing whether it should improve.

---

# Summary

Forward Propagation is the complete prediction pipeline of a neural network.

At every layer,

the network performs two operations.

### Linear Transformation

$$
Z^{(l)}
=
W^{(l)^T}
A^{(l-1)}
+
B^{(l)}
$$

### Activation Function

$$
A^{(l)}
=
f
\left(
Z^{(l)}
\right)
$$

The output of one layer becomes the input of the next layer.

This process continues until the final prediction is produced.

During Forward Propagation,

- Weights do not change.
- Biases do not change.
- Only information flows through the network.

Learning begins only after computing the Loss Function.

---

# Complete Forward Propagation Pipeline

```text
Input Data

↓

Input Layer

↓

Weighted Sum

↓

Bias Addition

↓

Activation Function

↓

Hidden Layer Output

↓

Repeat for Every Hidden Layer

↓

Output Layer

↓

Final Prediction (ŷ)

↓

Forward Propagation Ends

↓

Loss Function Begins
```

---

# Key Takeaways

✔ Forward Propagation is the prediction phase of a neural network.

✔ Every hidden layer performs the same two computations:

- Linear Transformation
- Activation Function

✔ Information always flows from the Input Layer to the Output Layer.

✔ Weights, biases, and network architecture remain unchanged during Forward Propagation.

✔ Each layer transforms the data into a more meaningful representation.

✔ The final output of Forward Propagation is the network's prediction (\(\hat{Y}\)).

✔ After Forward Propagation, the next step is to compute the **Loss Function**, which measures how good or bad the prediction is.
