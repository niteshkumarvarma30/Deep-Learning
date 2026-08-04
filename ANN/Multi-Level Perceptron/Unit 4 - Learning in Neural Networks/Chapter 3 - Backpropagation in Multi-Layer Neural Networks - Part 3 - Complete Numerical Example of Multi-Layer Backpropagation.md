# Unit 4 – Learning in Neural Networks

# Chapter 3 – Backpropagation in Multi-Layer Neural Networks

## Part 3 – Complete Numerical Example of Multi-Layer Backpropagation

---

# Learning Objectives

After completing this chapter, you will be able to:

- Perform one complete Forward Propagation manually.
- Compute the prediction error.
- Calculate the output-layer delta.
- Calculate the hidden-layer delta.
- Compute gradients for all weights and biases.
- Perform one Gradient Descent update manually.
- Understand exactly how neural networks learn from data.

---

# 1. Our Neural Network

To understand Backpropagation clearly, we will use the simplest possible multi-layer neural network.

```text
Input (x)

↓

Hidden Neuron

↓

Output Neuron

↓

Prediction (ŷ)

↓

Loss
```

The network contains

- One input neuron
- One hidden neuron
- One output neuron

Although real neural networks contain thousands or millions of neurons, the learning process is exactly the same.

---

# 2. Given Values

## Input

$$
x=2
$$

---

## Actual Target

$$
y=1
$$

---

## Hidden Layer Parameters

Weight

$$
W_1=0.5
$$

Bias

$$
b_1=0.1
$$

---

## Output Layer Parameters

Weight

$$
W_2=0.8
$$

Bias

$$
b_2=0.2
$$

---

## Learning Rate

$$
\eta=0.1
$$

---

## Activation Function

Sigmoid

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

---

## Loss Function

Binary Cross Entropy (BCE)

---

# 3. Step 1 – Forward Propagation

The hidden layer computes

## Hidden Weighted Sum

$$
z_1=W_1x+b_1
$$

Substitute the values

$$
z_1=(0.5)(2)+0.1
$$

$$
z_1=1.1
$$

---

## Hidden Activation

$$
a_1=\sigma(z_1)
$$

$$
a_1=\sigma(1.1)
$$

$$
a_1\approx0.7503
$$

---

## Output Weighted Sum

$$
z_2=W_2a_1+b_2
$$

Substitute

$$
z_2=(0.8)(0.7503)+0.2
$$

$$
z_2=0.8002
$$

---

## Prediction

$$
\hat y=\sigma(z_2)
$$

$$
\hat y=\sigma(0.8002)
$$

$$
\hat y\approx0.6900
$$

The network predicts

```text
69% probability of Class 1
```

---

# 4. Step 2 – Compute the Loss

Actual label

$$
y=1
$$

Since we are using Binary Cross Entropy,

$$
L=-\log(\hat y)
$$

Substitute

$$
L=-\log(0.69)
$$

$$
\boxed{ L\approx0.371 }
$$

This means the prediction is not perfect and the network needs to learn.

---

# 5. Step 3 – Begin Backpropagation

Now the network computes gradients.

Backpropagation always starts from the **output layer**.

---

# 6. Step 4 – Compute Output Layer Delta

For

- Sigmoid activation
- Binary Cross Entropy loss

the derivative simplifies to

$$
\boxed{ \delta_2=\hat y-y }
$$

Substitute

$$
\delta_2=0.69-1
$$

$$
\boxed{ \delta_2=-0.31 }
$$

Interpretation

The prediction is smaller than the target,

so the network needs to increase its output.

---

# 7. Step 5 – Compute Gradient of Output Weight

Formula

$$
\frac{\partial L}{\partial W_2} = \delta_2a_1
$$

Substitute

$$
=(-0.31)(0.7503)
$$

$$
\boxed{ \frac{\partial L}{\partial W_2} =-0.233 }
$$

---

# 8. Step 6 – Compute Gradient of Output Bias

Since

$$
\frac{\partial z_2}{\partial b_2}=1
$$

the gradient is simply

$$
\boxed{ \frac{\partial L}{\partial b_2} = \delta_2 =-0.31 }
$$

---

# 9. Step 7 – Compute Hidden Layer Delta

Formula

$$
\delta_1 = W_2 \delta_2 \sigma'(z_1)
$$

First compute the Sigmoid derivative.

$$
\sigma'(z) = \sigma(z)(1-\sigma(z))
$$

Therefore

$$
\sigma'(1.1) = 0.7503(1-0.7503)
$$

$$
= 0.1874
$$

Now substitute

$$
\delta_1 = (0.8)(-0.31)(0.1874)
$$

$$
\boxed{ \delta_1=-0.0465 }
$$

Notice

The hidden-layer error is smaller because it is scaled by

- the output weight,
- and the derivative of the activation function.

---

# 10. Step 8 – Compute Gradient of Hidden Weight

Formula

$$
\frac{\partial L}{\partial W_1} = \delta_1x
$$

Substitute

$$
=(-0.0465)(2)
$$

$$
\boxed{ \frac{\partial L}{\partial W_1} =-0.093 }
$$

---

# 11. Step 9 – Compute Gradient of Hidden Bias

Since

$$
\frac{\partial z_1}{\partial b_1}=1
$$

we obtain

$$
\boxed{ \frac{\partial L}{\partial b_1} = \delta_1 = -0.0465 }
$$

---

# 12. Step 10 – Gradient Descent Updates

Gradient Descent updates every parameter.

General rule

$$
W=W-\eta\nabla L
$$

---

## Update Hidden Weight

$$
W_1 = 0.5 - 0.1(-0.093)
$$

$$
\boxed{ W_1=0.5093 }
$$

---

## Update Hidden Bias

$$
b_1 = 0.1 - 0.1(-0.0465)
$$

$$
\boxed{ b_1=0.10465 }
$$

---

## Update Output Weight

$$
W_2 = 0.8 - 0.1(-0.233)
$$

$$
\boxed{ W_2=0.8233 }
$$

---

## Update Output Bias

$$
b_2 = 0.2 - 0.1(-0.31)
$$

$$
\boxed{ b_2=0.231 }
$$

---

# 13. Updated Parameters

| Parameter | Before Update | After Update |
|------------|--------------:|-------------:|
| \(W_1\) | 0.5000 | 0.5093 |
| \(b_1\) | 0.1000 | 0.10465 |
| \(W_2\) | 0.8000 | 0.8233 |
| \(b_2\) | 0.2000 | 0.2310 |

Notice

All trainable parameters have moved in a direction that should reduce the loss.

---

# 14. Complete Training Iteration

```text
Input

↓

Forward Propagation

↓

Prediction

↓

Loss

↓

Output Delta

↓

Hidden Delta

↓

Weight Gradients

↓

Bias Gradients

↓

Gradient Descent

↓

Updated Parameters
```

One complete learning iteration is now finished.

---

# 15. What Happens Next?

Training does **not** stop after one iteration.

Instead,

the same process repeats for every training sample or mini-batch.

```text
Epoch 1

↓

Epoch 2

↓

Epoch 3

↓

...

↓

Loss decreases

↓

Model learns
```

With repeated updates,

the prediction gradually becomes closer to the target.

---

# 16. One Important Insight

During **Forward Propagation**, the network performs

- Multiplication
- Addition
- Activation Functions

During **Backpropagation**, the network performs

- Chain Rule
- Local Derivatives
- Delta Computation
- Gradient Computation
- Gradient Descent

There is no hidden magic.

Deep Learning frameworks such as PyTorch and TensorFlow simply automate these mathematical operations for millions of parameters.

---

# Complete Numerical Summary

| Quantity | Value |
|-----------|-------|
| Input \(x\) | 2 |
| Target \(y\) | 1 |
| Hidden Weighted Sum \(z_1\) | 1.1 |
| Hidden Activation \(a_1\) | 0.7503 |
| Output Weighted Sum \(z_2\) | 0.8002 |
| Prediction \(\hat y\) | 0.6900 |
| Loss | 0.371 |
| Output Delta \(\delta_2\) | -0.31 |
| Hidden Delta \(\delta_1\) | -0.0465 |
| Gradient \(W_2\) | -0.233 |
| Gradient \(b_2\) | -0.31 |
| Gradient \(W_1\) | -0.093 |
| Gradient \(b_1\) | -0.0465 |

---

# Interview Questions

## Q1. Why is the output-layer delta computed first?

**Answer**

Because the loss is directly connected to the output layer. Once the output error is known, it can be propagated backward through the hidden layers.

---

## Q2. Why is the hidden-layer delta smaller than the output-layer delta?

**Answer**

Because it is multiplied by the output weight and the derivative of the activation function, causing the error signal to shrink as it propagates backward.

---

## Q3. What is updated during Gradient Descent?

**Answer**

Every trainable parameter, including all weights and biases, is updated using the computed gradients.

---

## Q4. Does one iteration completely train the neural network?

**Answer**

No.

One iteration performs only one parameter update.

Training requires many iterations (epochs) until the loss converges.

---

## Q5. What is the purpose of this numerical example?

**Answer**

It demonstrates the complete learning cycle of a neural network, including Forward Propagation, Loss Computation, Backpropagation, Gradient Computation, and Gradient Descent.

---

# Summary

This chapter demonstrated one complete learning iteration of a two-layer neural network.

Starting from the input,

the network performed Forward Propagation to produce a prediction.

The Binary Cross Entropy loss measured the prediction error.

Backpropagation then computed the output-layer delta, propagated the error to the hidden layer, calculated gradients for every weight and bias, and finally updated all parameters using Gradient Descent.

This complete sequence forms the foundation of how modern neural networks learn from data.

---

# Key Takeaways

✔ Forward Propagation computes predictions.

✔ Binary Cross Entropy measures prediction error.

✔ Backpropagation computes output and hidden-layer deltas.

✔ Gradients are calculated for every weight and bias.

✔ Gradient Descent updates all trainable parameters.

✔ One iteration consists of Forward Pass → Loss → Backpropagation → Parameter Update.

✔ Deep Learning frameworks automate exactly these mathematical operations.

---

## Next Part

**Part 4 – Matrix Form of Backpropagation**

In the next chapter, we will replace individual neurons with **vectors and matrices**, allowing us to derive the scalable Backpropagation equations used in real-world Deep Learning libraries such as **PyTorch**, **TensorFlow**, and **JAX**.
