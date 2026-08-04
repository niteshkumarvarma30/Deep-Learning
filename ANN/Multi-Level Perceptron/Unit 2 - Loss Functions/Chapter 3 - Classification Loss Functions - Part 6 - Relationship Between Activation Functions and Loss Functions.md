# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 6 – Relationship Between Activation Functions and Loss Functions

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what **Logits** are.
- Understand the relationship between **Weighted Sum**, **Raw Output**, **Linear Output**, and **Logits**.
- Learn the formulas of **Sigmoid** and **Softmax**.
- Understand why **Sigmoid is paired with Binary Cross Entropy (BCE)**.
- Understand why **Softmax is paired with Categorical Cross Entropy (CCE)** and **Sparse Categorical Cross Entropy (SCCE)**.
- Understand why incorrect activation-loss combinations are not used.
- Understand the complete classification pipeline.

---

# 1. Why Do We Need Activation Functions?

The last neuron of a neural network **does not directly produce probabilities**.

Instead,

it first computes a mathematical expression called the **Weighted Sum**.

This value can be

- negative,
- positive,
- zero,
- very large,
- or very small.

These values are **not probabilities**.

Therefore,

we use an **activation function** to convert these values into probabilities.

---

# 2. Weighted Sum

Every neuron first computes

$$
\boxed{ z=w^Tx+b }
$$

or equivalently

$$
\boxed{ z=\sum_{i=1}^{n}w_ix_i+b }
$$

where

- \(x_i\) = Input Features
- \(w_i\) = Weights
- \(b\) = Bias
- \(z\) = Weighted Sum

---

## Example

Suppose

$$
x=[2,3]
$$

Weights

$$
w=[0.5,0.8]
$$

Bias

$$
b=1
$$

Then

$$
z=(0.5)(2)+(0.8)(3)+1
$$

$$
=1+2.4+1
$$

$$
=4.4
$$

Therefore,

$$
\boxed{z=4.4}
$$

---

# 3. What is a Logit?

The value

$$
\boxed{z=w^Tx+b}
$$

is known by several different names.

| Name | Meaning |
|-------|---------|
| Weighted Sum | Mathematical linear combination of inputs |
| Linear Output | Output before activation |
| Raw Output | Unprocessed neuron output |
| Logit | Raw output before activation |

All four terms refer to **exactly the same quantity**.

```text
Inputs

↓

Weighted Sum

↓

z = 4.4

↓

Logit

↓

Raw Output

↓

Linear Output
```

Therefore,

$$
\boxed{ \text{Logit} = \text{Weighted Sum} = \text{Raw Output} = \text{Linear Output} = z }
$$

---

# 4. Why Can't We Use Logits Directly?

Suppose

```text
Logit = 8
```

Can we say

```text
Probability = 8
```

No.

A probability must satisfy

$$
0\le P\le1
$$

However,

logits can be

```text
-100

-10

0

5

50

1000
```

Therefore,

they must be converted into probabilities.

---

# 5. Sigmoid Activation Function

Sigmoid is used for **Binary Classification**.

## Formula

$$
\boxed{ \sigma(z) = \frac{1}{1+e^{-z}} }
$$

where

- \(z\) = Logit
- \(\sigma(z)\) = Probability

The Sigmoid function converts any real number into

$$
0\le\sigma(z)\le1
$$

---

## Example 1

Suppose

$$
z=0
$$

Then

$$
\sigma(0) = \frac1{1+e^0} = 0.5
$$

---

## Example 2

Suppose

$$
z=4
$$

Then

$$
\sigma(4) = \frac1{1+e^{-4}} \approx0.982
$$

Very high probability.

---

## Example 3

Suppose

$$
z=-4
$$

Then

$$
\sigma(-4) \approx0.018
$$

Very low probability.

---

# 6. Binary Classification Pipeline

```text
Input Features

↓

Weighted Sum

↓

Logit (z)

↓

Sigmoid

↓

Probability

↓

Binary Cross Entropy (BCE)

↓

Loss

↓

Backpropagation

↓

Gradient Descent
```

---

# 7. Why is Sigmoid Used with BCE?

Binary Cross Entropy expects

- a single probability,
- between 0 and 1,
- representing the probability of Class 1.

Sigmoid produces exactly this.

Therefore,

the correct combination is

```text
Sigmoid

↓

Binary Cross Entropy
```

---

# 8. Softmax Activation Function

Softmax is used for **Multi-Class Classification**.

Suppose there are

$$
C
$$

classes.

For class \(i\),

the Softmax probability is

$$
\boxed{ P_i = \frac{e^{z_i}} {\sum_{j=1}^{C}e^{z_j}} }
$$

where

- \(z_i\) = Logit of Class \(i\)
- \(P_i\) = Probability of Class \(i\)

---

# Properties of Softmax

Softmax guarantees

- Every probability lies between 0 and 1.
- All probabilities add up to 1.

$$
\boxed{ \sum_{i=1}^{C}P_i=1 }
$$

---

# 9. Softmax Example

Suppose the output layer produces three logits.

```text
Cat

↓

2

Dog

↓

1

Horse

↓

0
```

---

## Step 1

Compute exponentials.

$$
e^2=7.39
$$

$$
e^1=2.72
$$

$$
e^0=1
$$

---

## Step 2

Add them.

$$
7.39+2.72+1=11.11
$$

---

## Step 3

Compute probabilities.

Cat

$$
\frac{7.39}{11.11} = 0.665
$$

Dog

$$
\frac{2.72}{11.11} = 0.245
$$

Horse

$$
\frac1{11.11} = 0.090
$$

Final Output

```text
Cat

↓

0.665

Dog

↓

0.245

Horse

↓

0.090
```

Notice

```text
0.665+0.245+0.090=1
```

---

# 10. Multi-Class Classification Pipeline

```text
Input Features

↓

Hidden Layers

↓

Weighted Sum

↓

Logits

↓

Softmax

↓

Probability Distribution

↓

Categorical Cross Entropy (CCE)

or

Sparse Categorical Cross Entropy (SCCE)

↓

Loss

↓

Backpropagation

↓

Gradient Descent
```

---

# 11. Why is Softmax Used with CCE?

Categorical Cross Entropy compares

- the actual probability distribution,
- with the predicted probability distribution.

Therefore,

the predicted probabilities must

- lie between 0 and 1,
- sum to exactly 1.

Softmax guarantees both conditions.

Hence,

the correct combination is

```text
Softmax

↓

Categorical Cross Entropy
```

---

# 12. Why is Softmax Used with SCCE?

Sparse Categorical Cross Entropy differs from CCE only in the **label format**.

The predictions remain

```text
[0.10,0.80,0.10]
```

Therefore,

Softmax is also paired with SCCE.

---

# 13. Why Can't We Use Sigmoid with CCE?

Suppose there are three classes.

Sigmoid outputs

```text
Cat

↓

0.90

Dog

↓

0.80

Horse

↓

0.75
```

Notice

```text
0.90+0.80+0.75=2.45
```

These values **do not form a probability distribution**.

CCE expects probabilities that sum to **1**.

Therefore,

Sigmoid is unsuitable for standard multi-class classification.

---

# 14. Why Can't We Use Softmax with BCE?

Binary Cross Entropy expects

- one probability,
- produced by one output neuron.

Softmax requires

- multiple output neurons,
- probabilities distributed across multiple classes.

Although binary classification can technically be implemented with two Softmax outputs, it is less efficient than using one Sigmoid output.

Therefore,

binary classification almost always uses

```text
Sigmoid

↓

Binary Cross Entropy
```

---

# 15. Correct Pairings

| Problem Type | Activation Function | Loss Function |
|---------------|---------------------|---------------|
| Binary Classification | Sigmoid | Binary Cross Entropy (BCE) |
| Multi-Class Classification (One-Hot Labels) | Softmax | Categorical Cross Entropy (CCE) |
| Multi-Class Classification (Integer Labels) | Softmax | Sparse Categorical Cross Entropy (SCCE) |

---

# 16. Modern Deep Learning Libraries

Modern frameworks improve numerical stability by combining the activation function and the loss function.

Examples

### PyTorch

```python
nn.BCEWithLogitsLoss()

nn.CrossEntropyLoss()
```

---

### TensorFlow

```python
BinaryCrossentropy(from_logits=True)

CategoricalCrossentropy(from_logits=True)
```

These functions accept **raw logits** and internally apply the correct activation function before computing the loss.

---

# 17. Common Mistakes

❌ Using Sigmoid with CCE.

❌ Using Softmax with BCE for ordinary binary classification.

❌ Applying Softmax manually before `CrossEntropyLoss` in PyTorch.

❌ Forgetting whether labels are One-Hot Encoded or Integer Encoded.

---

# 18. Complete Deep Learning Classification Pipeline

## Binary Classification

```text
Input

↓

Weighted Sum

↓

Logit (Raw Output)

↓

Sigmoid

↓

Probability

↓

Binary Cross Entropy

↓

Loss

↓

Backpropagation

↓

Gradient Descent
```

---

## Multi-Class Classification

```text
Input

↓

Hidden Layers

↓

Weighted Sum

↓

Logits

↓

Softmax

↓

Probability Distribution

↓

Categorical Cross Entropy

or

Sparse Categorical Cross Entropy

↓

Loss

↓

Backpropagation

↓

Gradient Descent
```

---

# Interview Questions

## Q1. What is a Logit?

**Answer**

A logit is the raw output (weighted sum) of a neuron before applying the activation function.

---

## Q2. Are Logit, Weighted Sum, Raw Output, and Linear Output different?

**Answer**

No.

They all refer to the same quantity,

$$
z=w^Tx+b
$$

---

## Q3. What is the formula of the Sigmoid function?

$$
\boxed{ \sigma(z) = \frac{1}{1+e^{-z}} }
$$

---

## Q4. What is the formula of the Softmax function?

$$
\boxed{ P_i = \frac{e^{z_i}} {\sum_{j=1}^{C}e^{z_j}} }
$$

---

## Q5. Why is Sigmoid used with BCE?

Because Sigmoid converts a single logit into a probability between 0 and 1, which is exactly what BCE expects.

---

## Q6. Why is Softmax used with CCE?

Because Softmax converts multiple logits into a probability distribution whose probabilities sum to 1.

---

## Q7. What are logits?

They are the raw outputs of the final layer before any activation function is applied.

---

# Summary

The output neuron of a neural network first computes a **weighted sum**

$$
z=w^Tx+b
$$

This value is called the **Weighted Sum**, **Linear Output**, **Raw Output**, or **Logit**.

Since logits are not probabilities, they must be converted using an activation function.

- **Sigmoid** converts a single logit into a probability for **binary classification** and is paired with **Binary Cross Entropy (BCE)**.
- **Softmax** converts multiple logits into a probability distribution for **multi-class classification** and is paired with **Categorical Cross Entropy (CCE)** or **Sparse Categorical Cross Entropy (SCCE)**.

Understanding the relationship between logits, activation functions, and loss functions is fundamental to designing and training neural networks.

---

# Key Takeaways

✔ Logit = Weighted Sum = Raw Output = Linear Output.

✔ Weighted Sum Formula

$$
z=w^Tx+b
$$

✔ Sigmoid Formula

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

✔ Softmax Formula

$$
P_i=\frac{e^{z_i}}{\sum_{j=1}^{C}e^{z_j}}
$$

✔ Sigmoid is used for binary classification.

✔ Softmax is used for multi-class classification.

✔ BCE works with Sigmoid.

✔ CCE and SCCE work with Softmax.

✔ Modern Deep Learning frameworks often accept logits directly and apply the appropriate activation internally for better numerical stability.
