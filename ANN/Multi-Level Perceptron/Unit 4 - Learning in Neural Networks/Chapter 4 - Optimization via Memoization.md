# Unit 4 – Learning in Neural Networks

# Chapter 4 – Optimization via Memoization

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Memoization is in the context of computer science.
- Explain why Memoization is critical for Neural Network performance.
- See how caching intermediate results during Forward Propagation saves time during Backpropagation.

---

# 1. Introduction

Training deep neural networks is extremely computationally expensive. Every training step requires calculating Forward Propagation, computing the Loss, and then performing Backpropagation to calculate gradients.

If we naively compute everything from scratch, training would take weeks instead of hours.

To solve this, deep learning frameworks (like TensorFlow and PyTorch) use an optimization technique borrowed from computer science called **Memoization**.

---

# 2. What is Memoization?

Memoization is an optimization technique used to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

Think of it like a student solving a tough math problem:
- The first time, it takes them 10 minutes to calculate the answer.
- They write the answer down on a piece of paper (the cache).
- If someone asks them the same question 5 minutes later, they don't do the math again. They just read the answer from the paper.

In Neural Networks, we apply this concept heavily between Forward Propagation and Backpropagation.

---

# 3. Why Neural Networks Need Memoization

Let's review what happens during a single training step.

### Forward Propagation
During Forward Propagation, the network calculates the weighted sums ($ z $) and activations ($ a $) layer by layer.

$$

z^{[1]} = W^{[1]}x + b^{[1]}

$$

$$
a^{[1]} = f(z^{[1]})

$$

$$

z^{[2]} = W^{[2]}a^{[1]} + b^{[2]}

$$

$$
a^{[2]} = f(z^{[2]})

$$

### Backpropagation
During Backpropagation, we calculate the gradients using the Chain Rule. 
For example, to update $ W^{[2]} $, the gradient requires the derivative of the activation function and the output of the previous layer.

$$

dW^{[2]} = dz^{[2]} \cdot (a^{[1]})^T

$$

Notice that the formula for Backpropagation *requires* variables that were already calculated during Forward Propagation (like $ a^{[1]} $ and $ z^{[2]} $).

---

# 4. The Naive Approach vs Memoization

### The Naive Approach (No Caching)
When it's time to do Backpropagation, the computer realizes it needs $ a^{[1]} $ to compute $ dW^{[2]} $.
If it didn't save $ a^{[1]} $, it has to re-calculate it from scratch:

$$ a^{[1]} = f(W^{[1]}x + b^{[1]}) $$

This wastes an incredible amount of CPU/GPU cycles.

### The Memoization Approach (Caching)
During Forward Propagation, as soon as the network calculates $ z^{[1]} $, $ a^{[1]} $, $ z^{[2]} $, etc., it **stores them in memory (cache)**.

```text
Forward Pass
      ↓
Calculate z[1]  ──> SAVE to Cache
      ↓
Calculate a[1]  ──> SAVE to Cache
      ↓
Calculate z[2]  ──> SAVE to Cache
```

When Backpropagation begins, the network doesn't recompute anything. It simply pulls the values from the cache.

```text
Backward Pass
      ↓
Need a[1]?      <── READ from Cache
      ↓
Compute Gradients instantly!
```

---

# 5. The Memory vs Speed Trade-off

Memoization highlights a classic computer science dilemma: **Memory vs Speed**.

- By saving all intermediate variables ($ z $'s and $ a $'s) in memory, we sacrifice a large amount of RAM (or GPU VRAM).
- In exchange, we gain a massive speed boost, cutting training times down by orders of magnitude.

This is why training deep neural networks requires GPUs with massive amounts of VRAM (e.g., 16GB, 24GB, or even 80GB). The memory is mostly being used to cache these intermediate forward propagation values for the backward pass!

---

# Interview Questions

## Q1. What is Memoization in Deep Learning?

**Answer**

Memoization is the optimization technique of caching the intermediate results (like weighted sums and activations) computed during Forward Propagation. These cached values are stored in memory so they can be instantly reused during Backpropagation to compute gradients, saving immense computational time.

---

## Q2. Why does training a Neural Network require so much GPU memory (VRAM)?

**Answer**

While the weights and biases take up some memory, the vast majority of memory during training is consumed by the "cache" (memoization). The network must store the intermediate activations and weighted sums for every single neuron in every layer, for every image in the batch, so that Backpropagation can be calculated efficiently.

---

# Summary

Memoization is a silent hero in deep learning. While mathematical algorithms like Gradient Descent dictate *how* a network learns, software optimizations like Memoization dictate *how fast* a network learns. By trading memory for computational speed, deep learning frameworks make training massive neural networks feasible.

---

# Key Takeaways

✔ Memoization means storing expensive computational results in a cache for reuse.
✔ Forward Propagation calculates $ z $ and $ a $ values and caches them.
✔ Backpropagation reads these cached values instead of recomputing them.
✔ Memoization is the primary reason why neural network training requires significant amounts of RAM/VRAM.
