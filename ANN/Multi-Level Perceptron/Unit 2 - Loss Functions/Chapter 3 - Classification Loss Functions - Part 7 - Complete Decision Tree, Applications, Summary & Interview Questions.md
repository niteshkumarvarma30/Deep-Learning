# Unit 2 – Loss Functions

# Chapter 3 – Classification Loss Functions

## Part 7 – Complete Decision Tree, Applications, Summary & Interview Questions

---

# Learning Objectives

After completing this part, you will be able to:

- Select the correct activation function and loss function for any classification problem.
- Understand the complete classification pipeline.
- Revise all concepts learned in Chapter 3.
- Answer interview questions confidently.

---

# 1. Complete Decision Tree

Whenever you encounter a classification problem, follow this decision tree.

```text
Classification Problem

↓

How many classes?

↓

Exactly Two?

├── Yes
│
│   ↓
│
│ One Output Neuron
│
│   ↓
│
│ Sigmoid
│
│   ↓
│
│ Binary Cross Entropy (BCE)
│
└── No
     ↓
More than Two Classes
     ↓
One-Hot Labels?
     │
     ├── Yes
     │
     │   ↓
     │
     │ Softmax
     │
     │   ↓
     │
     │ Categorical Cross Entropy (CCE)
     │
     └── No
          ↓
Integer Labels
          ↓
Softmax
          ↓
Sparse Categorical Cross Entropy (SCCE)
```

---

# 2. Complete Deep Learning Classification Pipeline

## Binary Classification

```text
Input

↓

Hidden Layers

↓

Weighted Sum

↓

Logit (Raw Output)

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

↓

Updated Weights
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

Categorical Cross Entropy (CCE)

or

Sparse Categorical Cross Entropy (SCCE)

↓

Loss

↓

Backpropagation

↓

Gradient Descent

↓

Updated Weights
```

---

# 3. Complete Revision Table

| Problem Type | Activation Function | Loss Function | Label Format |
|---------------|---------------------|---------------|--------------|
| Binary Classification | Sigmoid | Binary Cross Entropy (BCE) | 0 or 1 |
| Multi-Class (One-Hot Labels) | Softmax | Categorical Cross Entropy (CCE) | One-Hot Encoding |
| Multi-Class (Integer Labels) | Softmax | Sparse Categorical Cross Entropy (SCCE) | Integer Labels |

---

# 4. Complete Formula Sheet

## Weighted Sum (Logit)

Every neuron first computes

$$
\boxed{ z=w^Tx+b }
$$

where

- \(w\) = Weight Vector
- \(x\) = Input Features
- \(b\) = Bias
- \(z\) = Logit (Raw Output)

---

## Sigmoid Function

Used for Binary Classification.

$$
\boxed{ \sigma(z)=\frac1{1+e^{-z}} }
$$

Output Range

$$
0\le\sigma(z)\le1
$$

---

## Softmax Function

Used for Multi-Class Classification.

$$
\boxed{ P_i = \frac{e^{z_i}} {\sum_{j=1}^{C}e^{z_j}} }
$$

Properties

- Every probability lies between 0 and 1.
- The sum of all probabilities equals 1.

$$
\sum_{i=1}^{C}P_i=1
$$

---

## Binary Cross Entropy (BCE)

$$
\boxed{ L = - \left[ y\log(\hat y) + (1-y)\log(1-\hat y) \right] }
$$

---

## Categorical Cross Entropy (CCE)

$$
\boxed{ L = - \sum_{i=1}^{C} y_i \log(\hat y_i) }
$$

---

## Sparse Categorical Cross Entropy (SCCE)

Conceptually,

$$
\boxed{ L = - \log(\hat y_{\text{correct class}}) }
$$

It produces exactly the same mathematical loss as CCE.

---

# 5. Real-World Applications

| Application | Recommended Loss Function |
|--------------|--------------------------|
| Spam Detection | BCE |
| Email Classification | BCE |
| Disease Detection | BCE |
| Fraud Detection | BCE |
| Sentiment Analysis | BCE |
| Animal Classification | CCE / SCCE |
| Flower Classification | CCE / SCCE |
| MNIST Digit Recognition | SCCE |
| Face Recognition | SCCE |
| Image Classification | CCE / SCCE |
| Language Identification | SCCE |

---

# 6. Common Mistakes

❌ Using Mean Squared Error (MSE) for classification.

❌ Using Sigmoid with Categorical Cross Entropy.

❌ Using Softmax with Binary Cross Entropy for ordinary binary classification.

❌ Using Categorical Cross Entropy with integer labels.

❌ Using Sparse Categorical Cross Entropy with One-Hot Encoded labels.

❌ Forgetting that logits are the outputs **before** activation.

❌ Applying Softmax manually before `CrossEntropyLoss` in PyTorch.

---

# 7. Interview Questions

## Q1. What is a Logit?

**Answer**

A logit is the raw output (weighted sum) of the final neuron before applying an activation function.

---

## Q2. Which activation function is used for binary classification?

**Answer**

Sigmoid.

---

## Q3. Which loss function is paired with Sigmoid?

**Answer**

Binary Cross Entropy (BCE).

---

## Q4. Which activation function is used for multi-class classification?

**Answer**

Softmax.

---

## Q5. Which loss function is paired with Softmax?

**Answer**

Categorical Cross Entropy (CCE) or Sparse Categorical Cross Entropy (SCCE).

---

## Q6. What is the difference between CCE and SCCE?

**Answer**

CCE requires **One-Hot Encoded labels**,

whereas SCCE uses **integer class labels**.

---

## Q7. What is the relationship between BCE and Logistic Regression?

**Answer**

Binary Cross Entropy (BCE) is the **Negative Log-Likelihood (NLL)** derived from **Maximum Likelihood Estimation (MLE)** in Logistic Regression.

---

## Q8. Why can't Mean Squared Error (MSE) be used for classification?

**Answer**

Because MSE measures numerical error instead of probability error and does not appropriately penalize incorrect probability predictions.

---

## Q9. Which loss function should be used for the MNIST dataset?

**Answer**

Usually **Sparse Categorical Cross Entropy (SCCE)**,

because MNIST labels are stored as integer values (0–9).

---

## Q10. What is the difference between Logits and Probabilities?

**Answer**

**Logits**

- Raw outputs of the neuron.
- Can be any real number.
- Produced before activation.

**Probabilities**

- Produced after Sigmoid or Softmax.
- Always lie between 0 and 1.

---

## Q11. Which activation-loss combinations are correct?

| Activation Function | Loss Function |
|---------------------|---------------|
| Sigmoid | Binary Cross Entropy |
| Softmax | Categorical Cross Entropy |
| Softmax | Sparse Categorical Cross Entropy |

---

# 8. Chapter Summary

In this chapter, we studied the complete set of classification loss functions used in Deep Learning.

We learned that classification models predict **probabilities**, not continuous numerical values.

Therefore, regression loss functions such as MSE, MAE, and Huber Loss are not suitable for classification.

Instead,

- **Binary Cross Entropy (BCE)** is used for binary classification together with the **Sigmoid** activation function.
- **Categorical Cross Entropy (CCE)** is used for multi-class classification with **One-Hot Encoded labels** and **Softmax**.
- **Sparse Categorical Cross Entropy (SCCE)** is mathematically identical to CCE but accepts **integer labels**.

We also learned that every neuron first computes

$$
z=w^Tx+b
$$

which is called the **Weighted Sum**, **Raw Output**, **Linear Output**, or **Logit**.

Activation functions convert logits into probabilities, and the corresponding loss functions measure how well those probabilities match the true labels.

---

# 9. Complete Classification Cheat Sheet

```text
Classification Problem

↓

Number of Classes?

↓

2 Classes
    │
    ├── Output Neuron
    │
    ├── Logit (z)
    │
    ├── Sigmoid
    │
    ├── Probability
    │
    └── Binary Cross Entropy (BCE)

-------------------------------------------------

More than 2 Classes
    │
    ├── Output Neurons
    │
    ├── Logits
    │
    ├── Softmax
    │
    ├── Probability Distribution
    │
    ├── One-Hot Labels → CCE
    │
    └── Integer Labels → SCCE
```

---

# Key Takeaways

✔ Classification models predict probabilities, not continuous values.

✔ The final neuron first computes the weighted sum

$$
z=w^Tx+b
$$

✔ The weighted sum is also called

- Logit
- Raw Output
- Linear Output

✔ Sigmoid converts one logit into one probability.

✔ Softmax converts multiple logits into a probability distribution.

✔ BCE is used with Sigmoid.

✔ CCE is used with Softmax and One-Hot labels.

✔ SCCE is used with Softmax and Integer labels.

✔ BCE is mathematically the Negative Log-Likelihood (NLL) derived from Maximum Likelihood Estimation (MLE).

✔ Choosing the correct activation function and loss function is essential for successful Deep Learning classification models.
