# Unit 5 – Training Challenges & Solutions

# Chapter 7 – Weight Initialization

## Part 1 – Zero Initialization and its Failures

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what weight initialization is and why it happens before training.
- Explain what happens mathematically if all weights in a neural network are initialized to zero.
- Understand the "Symmetry Breaking" problem.
- Conclude why zero initialization fundamentally prevents a neural network from learning.

---

# 1. Introduction

Before a neural network can begin training (performing Forward and Backward Propagation), it needs starting values for its weights and biases.

This process is called **Initialization**.

Since we want the network to learn the optimal weights via Gradient Descent, we might intuitively think: *"Why not just start from a clean slate and set all weights to zero?"*

It turns out, initializing weights to zero completely destroys the neural network's ability to learn.

---

# 2. The Setup: Zero Initialization

Imagine a simple network with:
- 2 Input Neurons (\( x_1, x_2 \))
- 2 Hidden Neurons (\( h_1, h_2 \))
- 1 Output Neuron

Suppose we initialize all weights to exactly `0`, and all biases to `0`.

$$
W^{[1]} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}, \quad b^{[1]} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Let's pass an input, say \( x = [2, 3] \), into this network.

---

# 3. Forward Propagation with Zero Weights

For the first hidden neuron \( h_1 \):
$$
z_1 = (x_1 \cdot 0) + (x_2 \cdot 0) + 0 = 0
$$

For the second hidden neuron \( h_2 \):
$$
z_2 = (x_1 \cdot 0) + (x_2 \cdot 0) + 0 = 0
$$

No matter what the input is, every neuron in the hidden layer computes exactly the same weighted sum (\( z = 0 \)).

After applying an activation function (like ReLU or Sigmoid), every hidden neuron will output the exact same activation value.

```text
Input [2, 3]
      │
   Weights=0
      │
h1 outputs 'a'
h2 outputs 'a'
```

---

# 4. The Symmetry Problem in Backpropagation

During Forward Propagation, \( h_1 \) and \( h_2 \) did exactly the same amount of "work" (which was nothing). They output identical values.

When we calculate the Loss and perform Backpropagation, the gradients flowing back to \( h_1 \) and \( h_2 \) will also be perfectly identical.

Because the gradients are identical, the weight updates for \( h_1 \) and \( h_2 \) will be identical!

### After 1 Epoch:
- \( h_1 \) weights might become `[0.05, -0.02]`
- \( h_2 \) weights will also become `[0.05, -0.02]`

### After 100 Epochs:
- \( h_1 \) weights might become `[1.2, -0.8]`
- \( h_2 \) weights will also become `[1.2, -0.8]`

Both neurons will always compute the exact same feature. If you have 1,000 neurons in a hidden layer, they will all behave exactly like a single, redundant neuron.

This phenomenon is called **The Symmetry Problem** (or failing to break symmetry).

---

# Interview Questions

## Q1. Why can't we initialize neural network weights to zero?

**Answer**

If weights are initialized to zero, all neurons in a given layer will perform the exact same mathematical operation during Forward Propagation and output the same values. Consequently, they will receive identical gradients during Backpropagation and update their weights identically. The network fails to "break symmetry," meaning a hidden layer with 1,000 neurons will just act like a single neuron, rendering deep learning impossible.

---

## Q2. Can we initialize biases to zero?

**Answer**

Yes, it is perfectly fine to initialize biases to zero, as long as the weights are initialized randomly. Random weights alone are enough to break symmetry, so neurons will still compute different features and receive different gradients even if they start with a zero bias.

---

# Summary

Weight initialization is the crucial first step before training begins. Zero initialization is a fatal mistake because it creates perfect symmetry across the network, forcing every neuron in a layer to learn the exact same feature. To make deep learning work, we must break this symmetry.

---

# Key Takeaways

✔ Zero weight initialization results in all neurons outputting the same values.
✔ Identical outputs lead to identical gradients during Backpropagation.
✔ Identical gradients mean all neurons learn the same exact features.
✔ This is called the Symmetry Problem.
✔ We must break symmetry to allow different neurons to learn different features.

---

## Next Part

**Part 2 – Random, Xavier, and He Initialization**

In the next part, we will explore the correct ways to initialize weights using randomness, and learn mathematically optimized initializations like Xavier and He that prevent gradients from exploding or vanishing at the very beginning of training.
