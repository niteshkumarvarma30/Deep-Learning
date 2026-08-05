# Unit 5 – Training Challenges & Solutions

# Chapter 7 – Weight Initialization

## Part 2 – Random, Xavier, and He Initialization

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why Random Initialization breaks symmetry.
- Explain the problems with Naive Random Initialization (vanishing/exploding gradients).
- Understand Xavier (Glorot) Initialization and when to use it.
- Understand He Initialization and when to use it.

---

# 1. Random Initialization

To solve the Symmetry Problem (discussed in Part 1), we must initialize weights with random numbers.

If every weight starts as a different random number:
- Every neuron will compute a slightly different weighted sum.
- Every neuron will output a different activation.
- During Backpropagation, the gradients will differ.
- Neurons will learn different features. Symmetry is broken!

```text
Weights = Random values close to 0

W[1] = [[ 0.01, -0.05 ],
        [ 0.03,  0.02 ]]
```

## The Problem with Naive Random Initialization
If we simply generate random numbers from a standard Gaussian (Normal) distribution without any mathematical scaling, we encounter a huge problem in deep networks.

### Scenario A: Weights are initialized too small
If weights are initialized with very small random numbers (e.g., multiplying random numbers by `0.01`):
As we multiply through many layers during Forward Propagation, the activations become smaller and smaller until they vanish to zero.
- **Result:** Vanishing Gradient Problem.

### Scenario B: Weights are initialized too large
If weights are initialized with large random numbers:
As we multiply through many layers, the activations grow exponentially until they overflow.
- **Result:** Exploding Gradient Problem.

---

# 2. The Goal of Proper Initialization

To prevent the activations from exploding or vanishing, we need the **variance of the outputs of a layer to be roughly equal to the variance of its inputs**.

This keeps the signal stable as it flows through the network.

To achieve this, researchers discovered that we must scale the random weights based on the **number of input connections to the neuron (Fan-in)** or the **number of output connections (Fan-out)**.

---

# 3. Xavier / Glorot Initialization

Introduced by Xavier Glorot, this initialization technique ensures that the variance remains the same across layers.

It scales the random weights by drawing them from a distribution with a specific variance.

## The Formula
For a Normal distribution, weights are drawn with mean = 0 and variance = `1 / Fan-in`.

Sometimes, it is defined using both Fan-in and Fan-out:
$$
\text{Variance} = \frac{2}{\text{Fan-in} + \text{Fan-out}}
$$

## When to use Xavier Initialization?
Xavier initialization was mathematically derived assuming the activation function is linear. Therefore, it works perfectly for:
- **Sigmoid**
- **Tanh**
- **Softmax**

---

# 4. He Initialization

Introduced by Kaiming He, this technique modifies Xavier Initialization specifically to work with ReLU.

ReLU zeroes out half of the inputs (all the negative ones). Because half the signal is destroyed, the variance is essentially cut in half. To compensate for this, He Initialization doubles the variance.

## The Formula
For a Normal distribution, weights are drawn with mean = 0 and variance = `2 / Fan-in`.

$$
\text{Variance} = \frac{2}{\text{Fan-in}}
$$

## When to use He Initialization?
He Initialization is mathematically optimized for:
- **ReLU**
- **Leaky ReLU**
- **PReLU**

---

# Interview Questions

## Q1. What happens if you initialize weights too small or too large?

**Answer**

If initialized too small, the activations and gradients shrink as they pass through the layers, causing the Vanishing Gradient problem. If initialized too large, the activations and gradients grow exponentially, causing the Exploding Gradient problem.

---

## Q2. When should you use Xavier vs He initialization?

**Answer**

Xavier initialization should be used when the network uses Sigmoid or Tanh activation functions. He initialization should be used when the network uses ReLU or its variants (like Leaky ReLU), because it mathematically compensates for the fact that ReLU zeroes out half of the input space.

---

# Summary

Random initialization is necessary to break symmetry. However, naive random numbers can cause exploding or vanishing gradients before training even starts. By using mathematically derived scaling factors based on the number of input connections, **Xavier** (for Sigmoid/Tanh) and **He** (for ReLU) initializations keep the network perfectly stabilized at the start of training.

---

# Key Takeaways

✔ Random initialization breaks symmetry.
✔ Naive randomness causes Vanishing/Exploding gradients.
✔ The goal of initialization is to keep the variance of the signal stable across layers.
✔ **Xavier Initialization:** Use with Sigmoid / Tanh.
✔ **He Initialization:** Use with ReLU / Leaky ReLU.
