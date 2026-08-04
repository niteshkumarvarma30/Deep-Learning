# Unit 4 – Learning in Neural Networks

# Chapter 1 – Introduction to Learning in Neural Networks

## Part 4 – Computational Graph and the Chain Rule

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a Computational Graph is.
- Learn why neural networks are represented using computational graphs.
- Understand the Chain Rule from calculus.
- Learn how Backpropagation uses the Chain Rule.
- Build the mathematical foundation required for Backpropagation.

---

# 1. The Problem

Suppose we have the following mathematical expression.

$$
y=(3x+2)^2
$$

Suppose

```text
x = 2
```

We can easily calculate the output.

First,

$$
3(2)+2=8
$$

Then,

$$
8^2=64
$$

Computing the output is easy.

Now suppose someone asks

> **How does the output change if x changes slightly?**

Mathematically,

$$
\frac{dy}{dx}
$$

For a simple equation,

this derivative is easy to compute.

However,

a neural network is not one simple equation.

Instead, it consists of thousands or even millions of small mathematical operations.

For example,

```text
Input

↓

Multiply

↓

Add Bias

↓

Activation

↓

Multiply

↓

Add Bias

↓

Loss Function
```

How do we compute gradients efficiently through such a large computation?

---

# 2. Breaking a Large Problem into Small Steps

Instead of solving one large equation,

we divide it into smaller computations.

For

$$
y=(3x+2)^2
$$

we introduce intermediate variables.

$$
a=3x
$$

$$
b=a+2
$$

$$
y=b^2
$$

Instead of one complicated equation,

we now have three simple equations.

This idea is the foundation of Computational Graphs.

---

# 3. What is a Computational Graph?

## Definition

A **Computational Graph** is a graphical representation of a mathematical computation.

It represents

- variables,
- mathematical operations,
- and the flow of information between them.

Each node represents either

- a variable, or
- an operation.

Each edge represents the flow of data.

---

## Example

For

$$
y=(3x+2)^2
$$

the computational graph becomes

```text
x

↓

×3

↓

a

↓

+2

↓

b

↓

Square

↓

y
```

Instead of viewing the computation as one large equation,

we see it as a sequence of simple operations.

---

# 4. Why Do Neural Networks Use Computational Graphs?

A neural network performs thousands of mathematical operations.

For example,

```text
Input

↓

Weighted Sum

↓

Activation

↓

Weighted Sum

↓

Activation

↓

Loss
```

Each step depends on the previous step.

Representing the computation as a graph allows us to

- organize the computation,
- compute outputs efficiently,
- compute gradients efficiently.

---

# 5. Forward Pass on the Computational Graph

Suppose

```text
x = 2
```

The computation proceeds step by step.

```text
x = 2

↓

a = 3×2 = 6

↓

b = 6 + 2 = 8

↓

y = 8² = 64
```

Notice

Every value is computed from left to right.

This is exactly what happens during **Forward Propagation** in a neural network.

---

# 6. Backward Pass

Suppose we now want

$$
\frac{dy}{dx}
$$

Instead of differentiating the entire equation directly,

we move backward through the graph.

```text
y

↓

b

↓

a

↓

x
```

This backward traversal is the foundation of **Backpropagation**.

---

# 7. The Chain Rule

The **Chain Rule** is one of the most important rules in calculus.

It states

> **The derivative of a composite function is equal to the product of the derivatives of its intermediate functions.**

Suppose

$$
y=f(g(x))
$$

Then

$$
\boxed{ \frac{dy}{dx} = \frac{dy}{dg} \times \frac{dg}{dx} }
$$

Instead of differentiating one large function,

we differentiate each small function separately and multiply the results.

---

# 8. Applying the Chain Rule

Recall

$$
a=3x
$$

$$
b=a+2
$$

$$
y=b^2
$$

Now compute the derivatives.

---

## Step 1

$$
\frac{dy}{db}=2b
$$

Since

```text
b = 8
```

$$
\frac{dy}{db}=16
$$

---

## Step 2

$$
\frac{db}{da}=1
$$

---

## Step 3

$$
\frac{da}{dx}=3
$$

---

## Step 4

Apply the Chain Rule.

$$
\frac{dy}{dx} = \frac{dy}{db} \times \frac{db}{da} \times \frac{da}{dx}
$$

Substituting the values

$$
16 \times 1 \times 3 = 48
$$

Therefore,

$$
\boxed{ \frac{dy}{dx}=48 }
$$

Notice

We never differentiated the complete equation directly.

Instead,

we differentiated each small step and multiplied the results.

---

# 9. Why is the Chain Rule Important?

Imagine a deep neural network.

```text
Input

↓

Layer 1

↓

Layer 2

↓

Layer 3

↓

Layer 4

↓

Loss
```

Each layer is another mathematical function.

Backpropagation repeatedly applies the Chain Rule to compute gradients from the output layer back to the input layer.

Without the Chain Rule,

computing gradients for deep neural networks would be practically impossible.

---

# 10. Computational Graph in Neural Networks

A simplified neural network can be represented as

```text
Input

↓

Weighted Sum (z)

↓

Activation Function (a)

↓

Loss Function

↓

Loss
```

Every operation becomes a node in the computational graph.

During Backpropagation,

the algorithm computes the derivative at every node and combines them using the Chain Rule.

---

# 11. Why Does the Chain Rule Make Backpropagation Efficient?

Without the Chain Rule,

we would need to differentiate one enormous equation.

For a network with millions of parameters,

this would be computationally infeasible.

Instead,

the Chain Rule allows us to

- break the computation into small operations,
- compute local derivatives,
- multiply them together,
- efficiently compute the final gradients.

This makes training modern deep neural networks possible.

---

# 12. Forward Pass vs Backward Pass

## Forward Pass

```text
Input

↓

Intermediate Computations

↓

Prediction

↓

Loss
```

Purpose

Compute the output and the loss.

---

## Backward Pass

```text
Loss

↓

Local Derivatives

↓

Chain Rule

↓

Gradients
```

Purpose

Compute gradients for every parameter.

---

# 13. Real-Life Analogy

Imagine a relay race.

```text
Runner 1

↓

Runner 2

↓

Runner 3

↓

Finish Line
```

Each runner contributes to the final finishing time.

If we want to understand why the final time was slow,

we trace the race backward,

examining each runner's contribution.

Similarly,

Backpropagation traces the computation backward,

and the Chain Rule combines the contribution of every operation to the final loss.

---

# 14. One Important Insight

Many beginners believe Backpropagation is a single complicated formula.

It is not.

Backpropagation is simply

1. Build a Computational Graph.
2. Perform the Forward Pass.
3. Traverse the graph backward.
4. Apply the Chain Rule at every node.
5. Compute the gradients.

Everything else is repeated application of these steps.

---

# Interview Questions

## Q1. What is a Computational Graph?

**Answer**

A Computational Graph is a graphical representation of a computation where nodes represent variables or operations and edges represent the flow of data.

---

## Q2. Why are Computational Graphs used in Deep Learning?

**Answer**

They divide complex computations into smaller operations, making gradient computation efficient.

---

## Q3. What is the Chain Rule?

**Answer**

The Chain Rule states that the derivative of a composite function is the product of the derivatives of its intermediate functions.

---

## Q4. Why is the Chain Rule important in Backpropagation?

**Answer**

Backpropagation computes gradients by repeatedly applying the Chain Rule while traversing the computational graph backward.

---

## Q5. What is the difference between the Forward Pass and the Backward Pass?

**Answer**

The Forward Pass computes predictions and the loss, whereas the Backward Pass computes gradients using the Chain Rule.

---

# Summary

A **Computational Graph** represents a computation as a sequence of simple mathematical operations connected together.

Instead of differentiating one large equation,

Backpropagation traverses this graph backward and applies the **Chain Rule** at every operation.

This allows neural networks containing millions of parameters to compute gradients efficiently.

The combination of the Computational Graph and the Chain Rule forms the mathematical foundation of Backpropagation.

---

# Key Takeaways

✔ A Computational Graph breaks complex computations into simple operations.

✔ Nodes represent variables or mathematical operations.

✔ Edges represent the flow of information.

✔ The Forward Pass computes outputs.

✔ The Backward Pass computes gradients.

✔ The Chain Rule computes derivatives by multiplying local derivatives.

✔ Backpropagation repeatedly applies the Chain Rule throughout the computational graph.

✔ Computational Graphs and the Chain Rule make training deep neural networks computationally efficient.

---

## Next Part

**Part 5 – Complete Numerical Example of Backpropagation**

In the next chapter, we will manually perform

- Forward Propagation,
- Loss Calculation,
- Computational Graph construction,
- Chain Rule application,
- Gradient computation,
- and Weight Updates,

to understand the complete Backpropagation algorithm step by step.
