# Unsupervised Learning: Fixed-Weight Competitive Networks, Maxnet, and Hamming Networks

## Table of Contents

1. [Fixed-Weight Competitive Networks](#1-fixed-weight-competitive-networks)
2. [Numerical Example: Fixed-Weight Competitive Network](#2-numerical-example-fixed-weight-competitive-network)
3. [Role in Unsupervised Learning](#3-role-in-unsupervised-learning)
4. [Maxnet Neural Network](#4-maxnet-neural-network)
5. [Maxnet Training Algorithm](#5-maxnet-training-algorithm)
6. [Numerical Example: Maxnet](#6-numerical-example-maxnet)
7. [Advantages of Maxnet](#7-advantages-of-maxnet)
8. [Hamming Network](#8-hamming-network)
9. [Numerical Example: Hamming Network](#9-numerical-example-hamming-network)
10. [Comparison of the Three Networks](#10-comparison-of-the-three-networks)
11. [Important Formula Sheet](#11-important-formula-sheet)
12. [Practice Questions](#12-practice-questions)

---

# 1. Fixed-Weight Competitive Networks

## 1.1 What is a fixed-weight competitive network?

A fixed-weight competitive network is a type of neural network used in **unsupervised learning**.

In this network:

- The connection weights are not updated during learning.
- Multiple neurons receive the same input.
- Each neuron calculates its activation.
- Neurons compete with one another.
- The neuron with the highest activation wins.

The winning neuron represents the category or prototype most similar to the input.

### Why is it called fixed-weight?

In ordinary neural network training, weights are adjusted to improve predictions.

In a fixed-weight competitive network, the weights remain constant:

\[
w_{ij}(t+1)=w_{ij}(t)
\]

This means the weight at the next iteration is equal to the weight at the current iteration.

**Important:** Fixed weights do not mean that neuron activations cannot change. Activations depend on the input and can vary even though the connection weights remain unchanged.

## 1.2 Basic working principle

1. **Input presentation:** The input vector is presented to all neurons simultaneously.
2. **Activation calculation:** Each neuron calculates its activation, usually using a similarity measure such as the dot product.
3. **Competition:** The neurons compete based on their calculated activations.
4. **Winner selection:** The neuron with the highest activation wins and represents the category most similar to the input.

## 1.3 Mathematical representation

The activation equation is:

\[
y_j=\sum_i x_iw_{ij}
\]

Where:

| Symbol | Meaning |
|---|---|
| \(x_i\) | Input feature |
| \(w_{ij}\) | Weight connecting input \(i\) to neuron \(j\) |
| \(y_j\) | Activation of neuron \(j\) |
| \(i\) | Input-feature index |
| \(j\) | Neuron index |

This is a dot product between the input vector and the weight vector of a neuron.

The winning neuron is:

\[
j^*=\arg\max_j(y_j)
\]

Here, \(\arg\max\) returns the index of the neuron with the maximum activation.

---

# 2. Numerical Example: Fixed-Weight Competitive Network

Suppose there are three neurons, each having a predefined weight vector.

## Step 1: Define the weight vectors

\[
w_1=(1,0,0)
\]

\[
w_2=(0,1,0)
\]

\[
w_3=(0,0,1)
\]

These weight vectors represent three different prototypes.

## Step 2: Provide an input vector

Suppose the input is:

\[
x=(0.2,0.8,0.1)
\]

All three neurons receive the same input.

## Step 3: Calculate the dot products

### Neuron 1

\[
y_1=x\cdot w_1
\]

\[
y_1=(0.2)(1)+(0.8)(0)+(0.1)(0)
\]

\[
\boxed{y_1=0.2}
\]

### Neuron 2

\[
y_2=x\cdot w_2
\]

\[
y_2=(0.2)(0)+(0.8)(1)+(0.1)(0)
\]

\[
\boxed{y_2=0.8}
\]

### Neuron 3

\[
y_3=x\cdot w_3
\]

\[
y_3=(0.2)(0)+(0.8)(0)+(0.1)(1)
\]

\[
\boxed{y_3=0.1}
\]

## Step 4: Compare the activations

| Neuron | Activation |
|---|---:|
| Neuron 1 | 0.2 |
| Neuron 2 | 0.8 |
| Neuron 3 | 0.1 |

The maximum activation is:

\[
\max(0.2,0.8,0.1)=0.8
\]

Therefore:

\[
\boxed{\text{Winner}=\text{Neuron 2}}
\]

Neuron 2 represents the prototype most similar to the input according to this dot-product comparison.

### What happened?

The network did not modify any weights. It only:

1. Received the input.
2. Calculated three dot products.
3. Compared the activations.
4. Selected the maximum.

This is the central idea behind fixed-weight competitive networks.

---

# 3. Role in Unsupervised Learning

In supervised learning, we provide both an input and its correct target:

\[
(X,t)
\]

Where:

- \(X\) is the input.
- \(t\) is the correct target output.

In the fixed-weight competitive network described here, target labels are not required to select the winning prototype. The network compares the input with predefined prototypes and selects the one with the highest activation.

### Simple interpretation

Imagine three predefined prototypes:

- Prototype 1: Red objects.
- Prototype 2: Blue objects.
- Prototype 3: Green objects.

An input arrives. The network calculates its similarity to all three prototypes and selects the closest one.

The category is determined by the fixed weight vectors.

**Important distinction:** This is unsupervised winner selection, but the categories are predefined through the initial weight vectors. The network is not learning new prototype weights in this particular fixed-weight model.

---

# 4. Maxnet Neural Network

## 4.1 What is Maxnet?

Maxnet is a competitive neural network used to determine the maximum value among a set of input activations.

It follows the **winner-take-all principle** through repeated lateral inhibition.

The main idea is:

- Every neuron initially has an activation value.
- Each neuron inhibits the other neurons.
- The neuron with the largest activation eventually survives.
- Weaker neurons are suppressed to zero.

## 4.2 What is lateral inhibition?

Lateral inhibition means that one neuron suppresses the activations of other neurons.

For example, suppose three neurons have initial activations:

\[
a_1=0.7,\quad a_2=0.4,\quad a_3=0.9
\]

Neuron 3 has the highest activation.

Through repeated inhibition, neurons 1 and 2 gradually become zero, while neuron 3 remains active.

The surviving neuron identifies the maximum input.

## 4.3 Architecture of Maxnet

The Maxnet architecture described in the notes has these properties:

- Each neuron has a self-connection with weight \(+1\).
- Every neuron inhibits every other neuron.
- Each inhibitory connection has weight \(-\epsilon\).
- The weights are predetermined, so no training is involved.

Here:

\[
0<\epsilon<\frac{1}{n}
\]

Where \(n\) is the number of neurons.

### Connection types

| Connection | Weight | Purpose |
|---|---:|---|
| Self-connection | \(+1\) | Preserves the neuron's own activation |
| Other-neuron connection | \(-\epsilon\) | Suppresses competing neurons |

For three neurons, the weight matrix is:

\[
W=
\begin{bmatrix}
1&-\epsilon&-\epsilon\\
-\epsilon&1&-\epsilon\\
-\epsilon&-\epsilon&1
\end{bmatrix}
\]

The diagonal values are \(+1\), while the off-diagonal values are \(-\epsilon\).

This is a recurrent competitive network because the neurons repeatedly interact with one another.

## 4.4 Maxnet mathematical equation

The update equation is:

\[
\boxed{
y_j(k+1)=f\left[y_j(k)-\epsilon
\sum_{i\ne j}y_i(k)\right]
}
\]

Where:

| Symbol | Meaning |
|---|---|
| \(y_j(k)\) | Activation of neuron \(j\) at iteration \(k\) |
| \(y_j(k+1)\) | New activation |
| \(\epsilon\) | Inhibition parameter |
| \(i\ne j\) | All neurons except neuron \(j\) |
| \(f\) | Activation function |

The activation function is:

\[
f(x)=
\begin{cases}
x,&x>0\\
0,&x\leq0
\end{cases}
\]

This function ensures that negative activations become zero.

**Important:** Maxnet does not learn its weights. Its purpose is to find the maximum among the initial activation values.

---

# 5. Maxnet Training Algorithm

The algorithm is:

1. Initialize neurons with the input activation values.
2. Select a small inhibition parameter \(\epsilon\).
3. Calculate the new activation of each neuron.
4. If an activation becomes negative, replace it with zero.
5. Repeat the process.
6. Continue until only one neuron has a nonzero activation.
7. The remaining neuron represents the maximum input.

In mathematical form:

\[
\boxed{
y_j(k+1)=
\max\left(0,\,
y_j(k)-\epsilon\sum_{i\ne j}y_i(k)
\right)
}
\]

All neurons are updated using the activations from the previous iteration. This is called a simultaneous update.

---

# 6. Numerical Example: Maxnet

Consider a Maxnet with four neurons.

Given:

\[
\epsilon=0.2
\]

Initial activations:

\[
a_1(0)=0.3
\]

\[
a_2(0)=0.5
\]

\[
a_3(0)=0.07
\]

\[
a_4(0)=0.09
\]

We need to find which neuron wins.

## Step 1: Check the inhibition parameter

For four neurons:

\[
0<\epsilon<\frac{1}{n}
\]

Substitute:

\[
0<0.2<\frac{1}{4}
\]

\[
0<0.2<0.25
\]

The inhibition parameter is valid.

## Step 2: Calculate the first iteration

Use:

\[
a_j(1)=
\max\left(0,\,
a_j(0)-0.2\sum_{i\ne j}a_i(0)
\right)
\]

### Neuron 1

\[
a_1(1)=
\max(0,0.3-0.2(0.5+0.07+0.09))
\]

\[
=\max(0,0.3-0.132)
\]

\[
\boxed{a_1(1)=0.168}
\]

### Neuron 2

\[
a_2(1)=
\max(0,0.5-0.2(0.3+0.07+0.09))
\]

\[
=\max(0,0.5-0.092)
\]

\[
\boxed{a_2(1)=0.408}
\]

### Neuron 3

\[
a_3(1)=
\max(0,0.07-0.2(0.3+0.5+0.09))
\]

\[
=\max(0,0.07-0.178)
\]

\[
\boxed{a_3(1)=0}
\]

### Neuron 4

\[
a_4(1)=
\max(0,0.09-0.2(0.3+0.5+0.07))
\]

\[
=\max(0,0.09-0.174)
\]

\[
\boxed{a_4(1)=0}
\]

After the first iteration:

\[
\boxed{[0.168,\;0.408,\;0,\;0]}
\]

Neurons 3 and 4 have been suppressed.

## Step 3: Calculate the second iteration

Only neurons 1 and 2 remain active.

### Neuron 1

\[
a_1(2)=\max(0,0.168-0.2(0.408))
\]

\[
\boxed{a_1(2)=0.0864}
\]

### Neuron 2

\[
a_2(2)=\max(0,0.408-0.2(0.168))
\]

\[
\boxed{a_2(2)=0.3744}
\]

New activations:

\[
[0.0864,\;0.3744,\;0,\;0]
\]

## Step 4: Calculate the third iteration

### Neuron 1

\[
a_1(3)=\max(0,0.0864-0.2(0.3744))
\]

\[
\boxed{a_1(3)=0.01152}
\]

### Neuron 2

\[
a_2(3)=\max(0,0.3744-0.2(0.0864))
\]

\[
\boxed{a_2(3)=0.35712}
\]

New activations:

\[
[0.01152,\;0.35712,\;0,\;0]
\]

## Step 5: Calculate the fourth iteration

### Neuron 1

\[
a_1(4)=\max(0,0.01152-0.2(0.35712))
\]

\[
=\max(0,-0.059904)
\]

\[
\boxed{a_1(4)=0}
\]

### Neuron 2

\[
a_2(4)=\max(0,0.35712-0.2(0.01152))
\]

\[
\boxed{a_2(4)=0.354816}
\]

Now:

\[
\boxed{[0,\;0.354816,\;0,\;0]}
\]

**Final result: Neuron 2 wins.**

It had the maximum initial activation:

\[
a_2(0)=0.5
\]

All other neurons have been suppressed to zero.

## 6.1 Complete iteration table

| Iteration | Neuron 1 | Neuron 2 | Neuron 3 | Neuron 4 |
|---|---:|---:|---:|---:|
| Initial | 0.30000 | 0.50000 | 0.07000 | 0.09000 |
| 1 | 0.16800 | 0.40800 | 0 | 0 |
| 2 | 0.08640 | 0.37440 | 0 | 0 |
| 3 | 0.01152 | 0.35712 | 0 | 0 |
| 4 | 0 | 0.354816 | 0 | 0 |

### Understanding the result

Maxnet does not directly calculate the maximum using a simple comparison operation. Instead, it repeatedly suppresses competing neurons through lateral inhibition until the maximum-activation neuron survives.

---

# 7. Advantages of Maxnet

1. **Simple architecture:** The network has a straightforward competitive structure.
2. **No training required:** Weights are predetermined.
3. **Efficient maximum selection:** It identifies the maximum among competing inputs.
4. **Useful in competitive classification:** It can select the strongest candidate.
5. **Part of the Hamming network:** It is used as the winner-selection stage in a Hamming network.

---

# 8. Hamming Network

## 8.1 What is a Hamming Network?

A Hamming network is a competitive neural network used mainly for **pattern classification**.

Its purpose is to identify which stored pattern is most similar to a given input pattern.

The network described in the notes has two layers:

1. Hamming layer.
2. Maxnet competitive layer.

## 8.2 Why is it called a Hamming Network?

The name comes from **Hamming distance**.

Hamming distance measures how many corresponding positions differ between two equal-length patterns.

For example:

\[
A=10110
\]

\[
B=10010
\]

Compare the bits:

| Position | A | B | Different? |
|---|---:|---:|---|
| 1 | 1 | 1 | No |
| 2 | 0 | 0 | No |
| 3 | 1 | 0 | Yes |
| 4 | 1 | 1 | No |
| 5 | 0 | 0 | No |

Only one position differs.

Therefore:

\[
\boxed{d_H(A,B)=1}
\]

A smaller Hamming distance means greater similarity.

## 8.3 Architecture of Hamming Network

The Hamming network has two layers.

### Layer 1: Hamming layer

The Hamming layer compares the input pattern with every stored pattern.

It calculates a similarity score for each stored pattern.

The neuron with the highest similarity score corresponds to the closest stored pattern.

### Layer 2: Maxnet competitive layer

The Maxnet layer receives the similarity scores from the Hamming layer.

It performs winner-take-all competition.

The neuron with the highest similarity score survives.

Therefore:

- **Hamming layer:** Similarity calculation.
- **Maxnet layer:** Winner selection.

---

# 9. Numerical Example: Hamming Network

Suppose a system stores three patterns:

\[
P_1=10110
\]

\[
P_2=11100
\]

\[
P_3=00111
\]

A new input arrives:

\[
X=10010
\]

We want to identify which stored pattern is most similar to the input.

## Step 1: Calculate Hamming distance

Compare the input with each stored pattern.

### Input and Pattern 1

```text
Input:    1 0 0 1 0
Pattern:  1 0 1 1 0
          0 0 1 0 0  <- Differences
```

Only one position differs.

\[
d_H(X,P_1)=1
\]

### Input and Pattern 2

```text
Input:    1 0 0 1 0
Pattern:  1 1 1 0 0
          0 1 1 1 0  <- Differences
```

Three positions differ.

\[
d_H(X,P_2)=3
\]

### Input and Pattern 3

```text
Input:    1 0 0 1 0
Pattern:  0 0 1 1 1
          1 0 1 0 1  <- Differences
```

Three positions differ.

\[
d_H(X,P_3)=3
\]

## Step 2: Convert distance into similarity

For binary patterns of length \(n\):

\[
\boxed{S=n-d_H}
\]

Here:

\[
n=5
\]

For Pattern 1:

\[
S_1=5-1=4
\]

For Pattern 2:

\[
S_2=5-3=2
\]

For Pattern 3:

\[
S_3=5-3=2
\]

## Step 3: Hamming layer output

| Stored pattern | Hamming distance | Similarity |
|---|---:|---:|
| Pattern 1 | 1 | 4 |
| Pattern 2 | 3 | 2 |
| Pattern 3 | 3 | 2 |

The Hamming layer produces:

\[
\boxed{[4,2,2]}
\]

## Step 4: Maxnet competition

The Maxnet layer receives:

\[
[4,2,2]
\]

It performs winner-take-all competition.

The highest activation is:

\[
\max(4,2,2)=4
\]

Therefore:

\[
\boxed{\text{Winner}=\text{Pattern 1}}
\]

The input `10010` is most similar to the stored pattern `10110`.

**Note:** This example illustrates the conceptual Hamming-distance interpretation. An actual Hamming network implements the matching scores using predefined weights and biases in the first layer, followed by Maxnet competition.

---

# 10. Comparison of the Three Networks

| Feature | Fixed-weight competitive network | Maxnet | Hamming network |
|---|---|---|---|
| Main purpose | Select the most similar prototype | Find maximum activation | Identify closest stored pattern |
| Input | Feature vector | Activation values | Binary or bipolar pattern |
| Weight adjustment | No | No | No during recall |
| Main operation | Dot product / similarity | Lateral inhibition | Pattern matching |
| Competition | Winner selection | Repeated suppression | Uses Maxnet |
| Output | Winning category | Maximum-valued neuron | Closest stored pattern |

## 10.1 How are they related?

### Fixed-weight competitive network

Determines which predefined prototype best matches the input.

### Maxnet

Provides a mechanism to select the largest activation through lateral inhibition.

### Hamming network

Uses a Hamming matching layer to calculate similarity and Maxnet to select the winning stored pattern.

---

# 11. Important Formula Sheet

## 11.1 Fixed-weight competitive network

Activation:

\[
y_j=\sum_i x_iw_{ij}
\]

Winner selection:

\[
j^*=\arg\max_j(y_j)
\]

Fixed-weight condition:

\[
w_{ij}(t+1)=w_{ij}(t)
\]

## 11.2 Maxnet

Update equation:

\[
y_j(k+1)=
f\left[y_j(k)-\epsilon
\sum_{i\ne j}y_i(k)\right]
\]

Activation function:

\[
f(x)=
\begin{cases}
x,&x>0\\
0,&x\leq0
\end{cases}
\]

Inhibition condition:

\[
0<\epsilon<\frac{1}{n}
\]

## 11.3 Hamming network

Hamming distance:

\[
d_H(X,P)=\sum_{i=1}^{n}I(x_i\ne p_i)
\]

Here, \(I\) is 1 when the corresponding bits differ and 0 otherwise.

Binary pattern similarity:

\[
S=n-d_H(X,P)
\]

---

# 12. Practice Questions

Try answering these questions to check your understanding.

## Question 1

Why is a fixed-weight competitive network called fixed-weight?

A. Its activations never change.

B. Its connection weights remain constant.

C. It has no input layer.

D. It uses only zero weights.

**Answer:** B

Explanation: Its weights remain unchanged, even though activations vary with the input.

## Question 2

Which activation measure is used in the fixed-weight competitive network example?

A. Mean squared error

B. Dot product

C. Cross entropy

D. Hamming loss only

**Answer:** B

Explanation: The network calculates the dot product between the input and each neuron's weight vector.

## Question 3

What does Maxnet identify?

A. Minimum activation

B. Average activation

C. Maximum activation

D. Sum of activations

**Answer:** C

Explanation: Maxnet suppresses weaker neurons and retains the maximum-activation neuron.

## Question 4

What is the self-connection weight in Maxnet?

A. -1

B. 0

C. +1

D. -epsilon

**Answer:** C

Explanation: Each neuron has a self-connection weight of +1.

## Question 5

For four Maxnet neurons, which epsilon satisfies the stated condition?

A. 0.5

B. 0.3

C. 0.2

D. 0.8

**Answer:** C

Explanation:

\[
0<\epsilon<\frac{1}{4}
\]

Therefore, 0.2 is valid.

## Question 6

What is the purpose of the Hamming layer?

A. Update weights

B. Calculate similarity between input and stored patterns

C. Suppress neurons

D. Calculate gradients

**Answer:** B

Explanation: The Hamming layer calculates pattern similarity.

## Question 7

What is the purpose of the Maxnet layer in a Hamming network?

A. Calculate input features

B. Store training data

C. Select the highest similarity score

D. Change stored patterns

**Answer:** C

Explanation: Maxnet selects the winning neuron based on the highest similarity.

## Question 8

If two binary patterns have a Hamming distance of 2 and length 5, what is their matching-bit count?

A. 2

B. 3

C. 5

D. 7

**Answer:** B

Explanation:

\[
S=n-d_H=5-2=3
\]

---

# Final Revision: What You Must Remember

1. **Fixed-weight competitive network:** Multiple neurons calculate similarity, and the neuron with the highest activation wins.
2. **Maxnet:** Uses lateral inhibition to suppress weaker neurons and retain the maximum-activation neuron.
3. **Hamming network:** Compares an input pattern against stored patterns and identifies the closest match.
4. **Hamming layer:** Calculates similarity.
5. **Maxnet layer:** Selects the winner.

The most important distinction for examinations is:

> A Hamming network calculates similarity, while Maxnet selects the winner. Together, they identify the stored pattern that most closely matches the input.
