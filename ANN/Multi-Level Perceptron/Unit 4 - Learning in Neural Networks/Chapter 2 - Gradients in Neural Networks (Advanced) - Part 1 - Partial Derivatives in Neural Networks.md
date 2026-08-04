# Unit 4 – Learning in Neural Networks

# Chapter 2 – Gradients in Neural Networks (Advanced)

## Part 1 – Partial Derivatives in Neural Networks

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why ordinary derivatives are not sufficient for neural networks.
- Learn what a partial derivative is.
- Understand why deep learning uses **∂** instead of **d**.
- Compute simple partial derivatives.
- Understand the role of partial derivatives in Backpropagation.

---

# 1. Recap: Ordinary Derivative

In the previous chapter, we studied a function with only one variable.

Suppose

$$
L(w)=w^2
$$

where

- \(L\) = Loss
- \(w\) = Weight

The derivative is

$$
\frac{dL}{dw}=2w
$$

Notice something important.

The function depends on **only one variable**.

```text
Loss

↓

Weight (w)
```

Since there is only one independent variable,

an **ordinary derivative** is sufficient.

---

# 2. The Problem in Neural Networks

Real neural networks are much more complex.

Consider a neuron with two inputs.

```text
x₁ ---- W₁

             \

              → Neuron → Output

             /

x₂ ---- W₂

        +

      Bias (b)
```

The output now depends on

- Weight \(W_1\)
- Weight \(W_2\)
- Bias \(b\)

Therefore,

the loss depends on multiple variables.

$$
L=L(W_1,W_2,b)
$$

Now ask yourself

> **If I change only \(W_1\), how will the loss change?**

Or

> **If I change only \(W_2\), what happens to the loss?**

An ordinary derivative cannot answer these questions.

---

# 3. What is a Partial Derivative?

## Definition

A **Partial Derivative** measures how a function changes with respect to **one variable while keeping all other variables constant**.

Instead of writing

$$
\frac{dL}{dw}
$$

we write

$$
\boxed{ \frac{\partial L}{\partial W_1} }
$$

This means

> **How does the loss change if only \(W_1\) changes while all other parameters remain fixed?**

Similarly,

$$
\frac{\partial L}{\partial W_2}
$$

asks

> **How does the loss change if only \(W_2\) changes?**

---

# 4. Why Do We Use the Symbol ∂?

There are two different derivative symbols.

---

## Ordinary Derivative

$$
\frac{d}{dx}
$$

Used when a function depends on **only one variable**.

Example

$$
y=x^2
$$

---

## Partial Derivative

$$
\frac{\partial}{\partial x}
$$

Used when a function depends on **multiple variables**.

Example

$$
L(W_1,W_2,b)
$$

Since neural networks contain many weights and biases,

Deep Learning almost always uses **partial derivatives**.

---

# 5. A Simple Mathematical Example

Suppose

$$
f(x,y)=x^2+3y
$$

This function depends on two variables.

---

## Partial Derivative with Respect to x

Keep \(y\) constant.

Differentiate only the terms containing \(x\).

$$
\frac{\partial f}{\partial x} = 2x
$$

Notice

The term

$$
3y
$$

behaves like a constant because \(y\) is fixed.

---

## Partial Derivative with Respect to y

Now keep \(x\) constant.

Differentiate only the terms containing \(y\).

$$
\frac{\partial f}{\partial y} = 3
$$

Notice

The term

$$
x^2
$$

is treated as a constant because \(x\) is fixed.

---

# 6. Applying Partial Derivatives to Neural Networks

Suppose the loss function is

$$
L=L(W_1,W_2,b)
$$

Backpropagation computes

$$
\frac{\partial L}{\partial W_1}
$$

$$
\frac{\partial L}{\partial W_2}
$$

$$
\frac{\partial L}{\partial b}
$$

Each partial derivative answers the question

> **How sensitive is the loss to this particular parameter?**

---

# 7. Why Compute Every Partial Derivative?

Imagine a neural network containing

```text
1,000,000 Weights
```

Updating every weight randomly would not improve the model.

Instead,

Backpropagation computes a partial derivative for **every weight and every bias**.

These values tell the optimizer exactly

- which parameters should change,
- in which direction,
- and by how much.

---

# 8. Real-Life Analogy

Imagine you are cooking a meal.

The taste depends on

- Salt
- Sugar
- Chili Powder

Suppose the food tastes bad.

You ask

> "What happens if I change only the amount of salt?"

This is similar to computing

$$
\frac{\partial Taste}{\partial Salt}
$$

Next,

you ask

> "What happens if I change only the sugar?"

This is similar to computing

$$
\frac{\partial Taste}{\partial Sugar}
$$

Each ingredient is adjusted one at a time while keeping the others unchanged.

Neural networks perform the same process for their weights and biases.

---

# 9. Partial Derivatives in Backpropagation

Backpropagation does not compute a single derivative.

Instead,

it computes **thousands or even millions of partial derivatives**.

Example

```text
∂L/∂W₁

∂L/∂W₂

∂L/∂W₃

⋮

∂L/∂Wₙ

∂L/∂b₁

∂L/∂b₂

⋮

∂L/∂bₙ
```

These partial derivatives are then passed to the optimizer.

---

# 10. From Partial Derivatives to the Gradient Vector

Once every partial derivative has been computed,

they are combined into a single mathematical object called the **Gradient Vector**.

For example,

$$
\nabla L = \begin{bmatrix} \frac{\partial L}{\partial W_1}\\[6pt] \frac{\partial L}{\partial W_2}\\[6pt] \frac{\partial L}{\partial b} \end{bmatrix}
$$

This vector contains the gradient for every trainable parameter.

The optimizer uses this vector to update all parameters simultaneously.

We will study the Gradient Vector in the next chapter.

---

# 11. One Important Insight

Many beginners think

> **Gradient = One Derivative**

This is only true for functions with one variable.

In neural networks,

the gradient consists of **many partial derivatives**,

one for every weight and bias.

---

# Difference Between Ordinary and Partial Derivatives

| Ordinary Derivative | Partial Derivative |
|---------------------|--------------------|
| Uses symbol **d** | Uses symbol **∂** |
| One independent variable | Multiple independent variables |
| Example: \(y=x^2\) | Example: \(L(W_1,W_2,b)\) |
| One derivative | One derivative per variable |
| Rare in Deep Learning | Used everywhere in Deep Learning |

---

# Interview Questions

## Q1. What is a partial derivative?

**Answer**

A partial derivative measures how a function changes with respect to one variable while keeping all other variables constant.

---

## Q2. Why do neural networks use partial derivatives instead of ordinary derivatives?

**Answer**

Because the loss function depends on many parameters (weights and biases), not just one variable.

---

## Q3. What does

$$
\frac{\partial L}{\partial W_1}
$$

represent?

**Answer**

It measures how the loss changes when only weight \(W_1\) changes while all other parameters remain fixed.

---

## Q4. Why does Backpropagation compute partial derivatives?

**Answer**

To determine how much each weight and bias contributed to the prediction error so that the optimizer can update each parameter correctly.

---

## Q5. What is the difference between an ordinary derivative and a partial derivative?

**Answer**

An ordinary derivative is used for functions with one variable, whereas a partial derivative is used for functions with multiple variables by differentiating one variable at a time while holding the others constant.

---

# Summary

Neural networks contain many trainable parameters, including weights and biases.

Since the loss depends on all of these parameters simultaneously, ordinary derivatives are not sufficient.

Instead, Deep Learning uses **partial derivatives**, which measure how the loss changes when only one parameter changes while all others remain constant.

Backpropagation computes these partial derivatives for every trainable parameter, providing the information needed by optimization algorithms to update the model efficiently.

---

# Key Takeaways

✔ Ordinary derivatives are used for functions with one variable.

✔ Partial derivatives are used for functions with multiple variables.

✔ Neural networks require partial derivatives because they contain many weights and biases.

✔ The notation **∂** represents a partial derivative.

✔ Backpropagation computes one partial derivative for every trainable parameter.

✔ These partial derivatives tell the optimizer how each parameter should be updated.

✔ All partial derivatives together form the **Gradient Vector**, which will be studied next.

---

## Next Part

**Part 2 – Gradient Vector**

In the next chapter, we will learn how all the individual partial derivatives are combined into a single **Gradient Vector**, understand the **∇ (nabla)** notation, and see how optimization algorithms use this vector to update every parameter in a neural network simultaneously.
