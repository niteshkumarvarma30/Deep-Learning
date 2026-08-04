# Unit 4 – Learning in Neural Networks

# Chapter 2 – Gradients in Neural Networks (Advanced)

## Part 3 – Jacobian Matrix

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why the Gradient Vector is not always sufficient.
- Learn what a Jacobian Matrix is.
- Understand the relationship between the Gradient Vector and the Jacobian Matrix.
- Learn where Jacobians are used in Deep Learning.
- Understand when a Jacobian Matrix is required.

---

# 1. Recap

In the previous chapter, we learned about the **Gradient Vector**.

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

These partial derivatives are combined into

$$
\nabla L = \begin{bmatrix} \frac{\partial L}{\partial W_1}\\[6pt] \frac{\partial L}{\partial W_2}\\[6pt] \frac{\partial L}{\partial b} \end{bmatrix}
$$

This works perfectly because

- there are **multiple inputs (parameters)**,
- but **only one output (the loss)**.

---

# 2. The Limitation of the Gradient Vector

Now suppose our function produces **multiple outputs**.

For example,

$$
\begin{aligned} y_1 &= x_1+x_2\\ y_2 &= x_1x_2 \end{aligned}
$$

Here

- Inputs = 2
- Outputs = 2

Now ask

> **How does every output change with respect to every input?**

A single Gradient Vector is no longer sufficient.

We need a mathematical object that stores **all partial derivatives**.

This object is called the **Jacobian Matrix**.

---

# 3. What is the Jacobian Matrix?

## Definition

The **Jacobian Matrix** stores the partial derivatives of **every output** with respect to **every input**.

Suppose

$$
\mathbf{x} = \begin{bmatrix} x_1\\ x_2 \end{bmatrix}
$$

and

$$
\mathbf{y} = \begin{bmatrix} y_1\\ y_2 \end{bmatrix}
$$

The Jacobian Matrix is

$$
\boxed{ J = \begin{bmatrix} \frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} \\[10pt] \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} \end{bmatrix} }
$$

Notice

- **Rows represent outputs.**
- **Columns represent inputs.**

---

# 4. A Numerical Example

Suppose

$$
\begin{aligned} y_1 &= x_1+x_2\\ y_2 &= x_1x_2 \end{aligned}
$$

Compute every partial derivative.

---

## First Output

### With respect to \(x_1\)

$$
\frac{\partial y_1}{\partial x_1}=1
$$

---

### With respect to \(x_2\)

$$
\frac{\partial y_1}{\partial x_2}=1
$$

---

## Second Output

### With respect to \(x_1\)

$$
\frac{\partial y_2}{\partial x_1}=x_2
$$

---

### With respect to \(x_2\)

$$
\frac{\partial y_2}{\partial x_2}=x_1
$$

---

Therefore,

the Jacobian Matrix becomes

$$
\boxed{ J= \begin{bmatrix} 1 & 1\\[6pt] x_2 & x_1 \end{bmatrix} }
$$

Every element answers one specific question about how one output changes when one input changes.

---

# 5. Interpreting the Jacobian Matrix

Consider the element

$$
\frac{\partial y_2}{\partial x_1}
$$

It answers

> **How does output \(y_2\) change when only input \(x_1\) changes?**

Similarly,

$$
\frac{\partial y_1}{\partial x_2}
$$

answers

> **How does output \(y_1\) change when only input \(x_2\) changes?**

Each element of the Jacobian describes one input-output relationship.

---

# 6. Gradient Vector vs Jacobian Matrix

### Case 1

One output

```text
Inputs

↓

Loss
```

Use

```text
Gradient Vector
```

---

### Case 2

Multiple outputs

```text
Inputs

↓

Multiple Outputs
```

Use

```text
Jacobian Matrix
```

---

# 7. Relationship Between Gradient Vector and Jacobian Matrix

The Gradient Vector is actually a **special case** of the Jacobian Matrix.

Suppose

$$
L=L(W_1,W_2,b)
$$

The Jacobian becomes

$$
\begin{bmatrix} \frac{\partial L}{\partial W_1} & \frac{\partial L}{\partial W_2} & \frac{\partial L}{\partial b} \end{bmatrix}
$$

Since there is only **one output (the loss)**,

the Jacobian has only one row.

This is essentially the Gradient Vector (up to row-vector or column-vector convention).

---

# 8. Why Is the Jacobian Important?

Modern Deep Learning frameworks such as

- PyTorch
- TensorFlow
- JAX

internally compute Jacobians during **Automatic Differentiation**.

Although developers rarely compute Jacobians manually,

the underlying mathematics relies on them.

---

# 9. Jacobian Matrix in Neural Networks

Consider one layer of a neural network.

```text
Input Vector

↓

Linear Layer

↓

Output Vector
```

The input is a vector.

The output is also a vector.

The relationship between these vectors is mathematically described using a Jacobian Matrix.

---

# 10. Real-Life Analogy

Imagine a classroom.

Inputs

```text
Study Hours

Sleep

Attendance
```

Outputs

```text
Mathematics Marks

Physics Marks

Chemistry Marks
```

Now ask

- How do study hours affect Mathematics?
- How does attendance affect Physics?
- How does sleep affect Chemistry?

The Jacobian Matrix stores all of these relationships in one table.

---

# 11. Do We Compute Jacobians Manually?

Usually,

**No.**

For deep neural networks,

the Jacobian Matrix can become extremely large.

Automatic Differentiation libraries compute it efficiently whenever required.

Understanding the concept is much more important than manually calculating large Jacobians.

---

# 12. Difference Between Gradient Vector and Jacobian Matrix

| Gradient Vector | Jacobian Matrix |
|-----------------|-----------------|
| One output | Multiple outputs |
| Many inputs | Many inputs |
| Vector | Matrix |
| One partial derivative per parameter | One partial derivative for every output-input pair |
| Used for scalar-valued functions | Used for vector-valued functions |

---

# 13. One Important Insight

Many beginners think

```text
Gradient Vector

↓

Jacobian Matrix

↓

Exactly the Same
```

This is **not completely correct**.

The Gradient Vector applies to

```text
Many Inputs

↓

One Output
```

The Jacobian Matrix applies to

```text
Many Inputs

↓

Many Outputs
```

Therefore,

the Gradient Vector is simply a **special case** of the Jacobian Matrix.

---

# Visual Summary

```text
Scalar Function

Many Inputs

↓

One Output

↓

Gradient Vector (∇L)
```

```text
Vector Function

Many Inputs

↓

Many Outputs

↓

Jacobian Matrix (J)
```

---

# Interview Questions

## Q1. What is a Jacobian Matrix?

**Answer**

A Jacobian Matrix contains the partial derivatives of every output with respect to every input of a vector-valued function.

---

## Q2. When do we use a Gradient Vector?

**Answer**

When a function has many inputs but only one output.

---

## Q3. When do we use a Jacobian Matrix?

**Answer**

When a function has multiple inputs and multiple outputs.

---

## Q4. Is the Gradient Vector related to the Jacobian Matrix?

**Answer**

Yes.

The Gradient Vector is a special case of the Jacobian Matrix for functions with a single output.

---

## Q5. Do Deep Learning frameworks compute Jacobians?

**Answer**

Yes.

Frameworks such as PyTorch, TensorFlow, and JAX compute Jacobians internally using Automatic Differentiation when required.

---

# Summary

The **Jacobian Matrix** extends the concept of the Gradient Vector to functions with multiple outputs.

While the Gradient Vector stores one partial derivative for every parameter of a scalar-valued function, the Jacobian Matrix stores every output-input partial derivative of a vector-valued function.

Although most Deep Learning practitioners rarely compute Jacobians manually, they play an essential role in Automatic Differentiation and form an important mathematical foundation for modern neural network libraries.

---

# Key Takeaways

✔ A Jacobian Matrix stores every output-input partial derivative.

✔ Rows correspond to outputs.

✔ Columns correspond to inputs.

✔ The Gradient Vector is a special case of the Jacobian Matrix.

✔ Jacobians are used for vector-valued functions.

✔ Automatic Differentiation frameworks compute Jacobians internally.

✔ Jacobians provide the mathematical foundation for many advanced Deep Learning operations.

---

## Next Part

**Part 4 – Hessian Matrix**

In the next chapter, we will study the **Hessian Matrix**, which contains **second-order derivatives**, understand how it describes the **curvature of the loss surface**, and learn why most modern optimizers use only first-order gradients while some advanced optimization methods make use of the Hessian.
