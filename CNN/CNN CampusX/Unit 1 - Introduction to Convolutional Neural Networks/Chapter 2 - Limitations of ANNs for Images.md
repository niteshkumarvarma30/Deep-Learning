# Unit 1 – Introduction to Convolutional Neural Networks

# Chapter 2 – Limitations of ANNs for Images

---

# Learning Objectives

After completing this chapter, you will be able to:

- Explain how images are represented digitally.
- Understand how a traditional ANN processes an image via flattening.
- Identify the three massive limitations of using traditional ANNs for image processing.

---

# 1. Introduction

Before Convolutional Neural Networks (CNNs) became popular, researchers tried to use standard Artificial Neural Networks (Multi-Layer Perceptrons) to classify images.

However, they quickly realized that ANNs are fundamentally flawed when it comes to image processing. To understand why, we first need to understand how images are passed into an ANN.

---

# 2. How Images are Processed in an ANN

An image is just a grid of numbers (pixels).
- A $28 \times 28$grayscale image has 784 pixels.
- A standard ANN only accepts a 1D column vector as input.

Therefore, to feed an image into an ANN, we must take the 2D grid and stretch it out into a single, long 1D line of pixels. This process is called **Flattening**.

```text
2D Image (3x3)
[ 1, 2, 3 ]
[ 4, 5, 6 ]  ── Flatten ──>  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
[ 7, 8, 9 ]
```

Once flattened, this 1D array is fed into the input layer of the ANN.

---

# 3. The Three Major Limitations

Flattening the image and using a fully connected ANN causes three catastrophic problems.

## Limitation 1: Loss of Spatial Information
In an image, a pixel is highly related to the pixels immediately surrounding it (above, below, left, right). These neighboring pixels form edges and shapes.

When we flatten the 2D image into a 1D array, we destroy the spatial arrangement. Pixel #4 is no longer "below" Pixel #1; it is just somewhere else in the line.

Because the ANN treats every input as an independent variable, it completely loses the ability to recognize 2D spatial patterns.

## Limitation 2: Massive Computational Cost
In a fully connected ANN, every input neuron must connect to every neuron in the first hidden layer.

Suppose we have a modern RGB image of size$1000 \times 1000 \times 3$(1 million pixels per color channel).
- **Total inputs:**$3,000,000$If our first hidden layer has just$1,000$neurons:
- **Number of weights required:**$3,000,000 \times 1,000 = 3,000,000,000$ (3 Billion weights!)

And that is just for the *first* layer. The computational cost and memory required to train billions of parameters for a simple image is impossible for standard hardware.

## Limitation 3: High Risk of Overfitting
Because a fully connected ANN requires billions of learnable parameters (weights) to process an image, the model's complexity becomes astronomically high.

As we learned in our previous units on Regularization, the more parameters a model has, the higher the risk of **Overfitting**. The ANN will easily memorize the exact training images, but will fail completely when tested on new, unseen images.

---

# Interview Questions

## Q1. Why is flattening an image bad for neural networks?

**Answer**
Flattening an image transforms a 2D spatial grid into a 1D array. This destroys the spatial relationships between neighboring pixels, which are essential for recognizing shapes, edges, and objects. The network loses all local spatial context.

---

## Q2. Why are standard ANNs computationally inefficient for image processing?

**Answer**
Standard ANNs are fully connected, meaning every input pixel must have a dedicated weight connecting it to every neuron in the first hidden layer. For even moderately sized images, this results in billions of weights, requiring massive memory and computational power, while simultaneously making the model highly prone to overfitting.

---

# Summary

While ANNs are excellent for tabular data, they fail at computer vision tasks. By flattening images, ANNs destroy crucial spatial patterns. Furthermore, their fully connected architecture leads to an unmanageable explosion in the number of parameters, causing severe overfitting and computational bottlenecks.

CNNs were explicitly designed to solve these three problems.

---

# Key Takeaways

✔ Images must be flattened into a 1D array to enter an ANN.
✔ Flattening destroys 2D spatial information.
✔ ANNs require billions of parameters for high-resolution images.
✔ High parameter counts lead to extreme overfitting.

---

## Next Unit

**Unit 2 – Core Convolutional Operations**

In the next unit, we will learn how CNNs solve the spatial and parameter problems using a mathematical operation called Convolution.
