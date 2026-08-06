# Unit 4 – Backpropagation and Parameters

# Chapter 1 – Learnable Parameters and Weight Sharing

---

# Learning Objectives

After completing this chapter, you will be able to:

- Calculate the number of parameters in a Convolutional layer.
- Understand the concept of Weight Sharing in CNNs.
- Explain why CNNs are drastically more computationally efficient than fully connected ANNs.

---

# 1. Introduction

In Unit 1, we learned that a standard ANN requires billions of weights to process a high-resolution image because every pixel connects to every neuron in the hidden layer.

Convolutional Neural Networks completely solve this parameter explosion using a brilliant mechanism known as **Weight Sharing**.

---

# 2. What are the Parameters in a CNN?

Unlike an ANN where the weights are long 1D arrays connecting layers, the weights in a CNN are literally the numbers inside the **Filters**.

If a CNN uses a $3 \times 3$filter, there are exactly 9 weights in that filter, plus 1 bias term.
- **Parameters per filter:**$(3 \times 3) + 1 = 10$parameters.

### Calculating Layer Parameters
Suppose a Convolutional layer takes an RGB image (3 channels) and applies 32 filters of size$3 \times 3$.

- Each filter must match the input channels, so the true filter size is$3 \times 3 \times 3 = 27$weights.
- Add 1 bias per filter:$27 + 1 = 28$parameters per filter.
- We have 32 filters total:$28 \times 32 = 896$total parameters.

Even if the input image is$1000 \times 1000 \times 3$, this Convolutional layer *still* only has **896 learnable parameters**. 

Compare this to the **3 Billion parameters** required by an ANN!

---

# 3. Weight Sharing

How can a CNN process a million-pixel image using only 896 weights? 

It achieves this through **Weight Sharing**. 

When a$3 \times 3$filter is applied to the image, it slides across the entire image. The CNN uses the **exact same 9 weights** to calculate the feature map for the top-left corner as it does for the bottom-right corner.

### Why does this make sense?
Because a feature (like a vertical edge) looks exactly the same whether it is in the top-left corner or the bottom-right corner of the image. 

If the network learns a great$3 \times 3$filter for detecting a cat's fur texture, it doesn't need to re-learn that texture for every single pixel location. It learns it once, and then shares those weights across the entire spatial area.

---

# Interview Questions

## Q1. How do you calculate the number of learnable parameters in a Convolutional layer?

**Answer**
You calculate the number of weights in a single filter (Filter Height$\times$Filter Width$\times$Input Channels), add 1 for the bias, and then multiply by the total number of filters in that layer. The size of the input image itself does not affect the number of parameters in a Convolutional layer.

---

## Q2. What is Weight Sharing in a CNN and why is it important?

**Answer**
Weight sharing means that a single filter (a small set of weights) is applied across the entire spatial area of the input image. It is important because it drastically reduces the total number of learnable parameters, making the network computationally efficient and significantly lowering the risk of overfitting.

---

# Summary

Weight Sharing is the secret behind the efficiency of CNNs. By reusing the same small filters across the entire image, CNNs can process massive, high-resolution images using a tiny fraction of the parameters required by a fully connected ANN. 

---

# Key Takeaways

✔ The learnable parameters in a CNN are the numbers inside the Filters.
✔ Parameters =$(\text{Filter Size} \times \text{Input Channels} + 1) \times \text{Number of Filters}$.
✔ The size of the input image does not affect the parameter count of the Conv layer.
✔ Weight sharing allows the network to learn a feature once and detect it everywhere.
