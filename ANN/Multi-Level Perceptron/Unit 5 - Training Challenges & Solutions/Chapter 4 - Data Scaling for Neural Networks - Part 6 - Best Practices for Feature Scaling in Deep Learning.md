# Unit 5 – Training Challenges & Solutions

# Chapter 4 – Data Scaling for Neural Networks

## Part 6 – Best Practices for Feature Scaling in Deep Learning

---

# Learning Objectives

After completing this chapter, you will be able to:

- Learn the best practices for Feature Scaling.
- Understand when to use Normalization and Standardization.
- Learn how to correctly scale training and test datasets.
- Avoid common mistakes made during preprocessing.
- Understand how Feature Scaling is performed in real-world Machine Learning and Deep Learning projects.

---

# 1. Introduction

Feature Scaling is one of the most important preprocessing steps in Machine Learning and Deep Learning.

However,

many beginners apply scaling incorrectly.

Incorrect scaling can

- Reduce model performance
- Cause data leakage
- Produce misleading evaluation results

Therefore,

following proper scaling practices is essential.

---

# 2. Always Scale Numerical Features

Feature Scaling should generally be applied only to **numerical features**.

Examples

```text
Age

Salary

Height

Weight
```

These numerical features often have different ranges.

Scaling makes them comparable.

---

### Do Not Scale Categorical Features

Categorical values represent labels rather than numerical quantities.

Example

```text
Color

Red

Blue

Green
```

or

```text
Country

India

Japan

USA
```

These should first be encoded using techniques such as

- One-Hot Encoding
- Label Encoding

Feature Scaling is usually **not applied directly** to raw categorical variables.

---

# 3. Split the Dataset Before Scaling

One of the biggest mistakes is

```text
Scale Entire Dataset

↓

Split into Train and Test
```

This is incorrect.

Instead,

always follow this sequence.

```text
Original Dataset

↓

Train-Test Split

↓

Fit Scaler on Training Data

↓

Transform Training Data

↓

Transform Test Data
```

---

# 4. Why Should We Fit Only on Training Data?

Suppose we compute

- Mean
- Standard Deviation
- Minimum
- Maximum

using the entire dataset.

Then,

information from the test set leaks into training.

This is called

> **Data Leakage**

Data leakage makes evaluation unrealistically optimistic.

---

# 5. Correct Scaling Workflow

The proper workflow is

```text
Training Data

↓

Fit Scaler

↓

Learn Scaling Parameters

↓

Transform Training Data

↓

Transform Test Data
```

Notice

The scaler **learns parameters only from the training set**.

The test set is only transformed,

never used to compute scaling parameters.

---

# 6. Normalization vs Standardization

Choose the scaler based on the problem.

### Use Normalization When

- Inputs have fixed bounds.
- Pixel values are used.
- Features naturally lie within a limited range.

Examples

- Images
- Computer Vision
- Autoencoders

---

### Use Standardization When

- Data is approximately normally distributed.
- Features have different units.
- Statistical learning algorithms are used.

Examples

- Neural Networks
- Logistic Regression
- Linear Regression
- Support Vector Machines (SVM)
- PCA

---

# 7. Scaling During Inference

Suppose the model has already been trained.

A new sample arrives.

```text
New Customer

↓

Scale Using Existing Scaler

↓

Prediction
```

Never compute a new scaler for every new sample.

Always reuse the scaler learned from the training data.

---

# 8. Saving the Scaler

In real-world deployment,

the scaler is saved together with the trained model.

```text
Training

↓

Fit Scaler

↓

Train Model

↓

Save Both
```

During prediction

```text
Load Scaler

↓

Scale New Data

↓

Load Model

↓

Prediction
```

Without the original scaler,

predictions may become incorrect.

---

# 9. Common Mistakes

### Mistake 1

Scaling before Train-Test Split

❌ Wrong

---

### Mistake 2

Using different scalers for training and testing

❌ Wrong

---

### Mistake 3

Scaling categorical variables directly

❌ Wrong

---

### Mistake 4

Forgetting to scale new prediction data

❌ Wrong

---

### Mistake 5

Refitting the scaler during inference

❌ Wrong

---

# 10. Best Practice Pipeline

A typical Machine Learning pipeline looks like

```text
Collect Data

↓

Clean Data

↓

Train-Test Split

↓

Feature Scaling

↓

Train Model

↓

Evaluate Model

↓

Save Model

↓

Deploy Model

↓

Scale New Inputs

↓

Prediction
```

This workflow is followed in most production systems.

---

# 11. Real-Life Analogy

Imagine measuring students.

Before comparing them,

you create a grading scale.

```text
Training Students

↓

Create Grading Scale
```

Later,

a new student joins.

You **do not create a new grading scale**.

Instead,

you evaluate the new student using the existing grading scale.

Feature Scaling works in exactly the same way.

---

# 12. One Important Insight

Many beginners think

> **The scaler is useful only during training.**

This is incorrect.

The same scaler must be used during

- Validation
- Testing
- Deployment
- Real-time prediction

Otherwise,

the model receives data in a different format than it was trained on.

---

# Visual Summary

```text
Raw Data

↓

Train-Test Split

↓

Fit Scaler (Training Only)

↓

Transform Train Data

↓

Transform Test Data

↓

Train Model

↓

Save Model + Scaler

↓

Deploy

↓

Scale New Data

↓

Prediction
```

---

# Best Practices Checklist

| Best Practice | Recommendation |
|--------------|----------------|
| Scale numerical features | ✅ Yes |
| Scale categorical features directly | ❌ No |
| Split before scaling | ✅ Yes |
| Fit scaler only on training data | ✅ Yes |
| Transform test data using same scaler | ✅ Yes |
| Save scaler with trained model | ✅ Yes |
| Reuse scaler during deployment | ✅ Yes |

---

# Interview Questions

## Q1. Should Feature Scaling be performed before or after the Train-Test Split?

**Answer**

After the Train-Test Split.

The scaler should be fitted only on the training data.

---

## Q2. Why should the scaler be fitted only on the training set?

**Answer**

To prevent **Data Leakage**, where information from the test set influences model training.

---

## Q3. Should new prediction data be scaled?

**Answer**

Yes.

Every new input must be transformed using the same scaler that was fitted on the training data.

---

## Q4. Why should the scaler be saved with the trained model?

**Answer**

Because future data must be transformed in exactly the same way as the training data.

---

## Q5. Should categorical features be scaled directly?

**Answer**

No.

Categorical features should first be encoded using techniques such as One-Hot Encoding or Label Encoding.

---

# Summary

Feature Scaling is a critical preprocessing step that must be applied carefully.

The correct workflow is to split the dataset first, fit the scaler only on the training data, and then transform both the training and test sets using the same scaler.

The scaler should be saved with the trained model and reused during deployment to ensure consistent preprocessing.

Following these best practices prevents data leakage, improves model reliability, and ensures that the model receives data in the same format during both training and inference.

---

# Key Takeaways

✔ Scale only numerical features.

✔ Split the dataset before scaling.

✔ Fit the scaler only on the training data.

✔ Transform both training and test data using the same scaler.

✔ Save the scaler along with the trained model.

✔ Use the same scaler during deployment and prediction.

✔ Avoid data leakage by never using test data to compute scaling parameters.

---

# ✅ Chapter 4 Completed

You have now completed:

- ✅ Part 1 – Why Neural Networks Need Feature Scaling
- ✅ Part 2 – Normalization (Min-Max Scaling)
- ✅ Part 3 – Standardization (Z-Score Scaling)
- ✅ Part 4 – Normalization vs Standardization
- ✅ Part 5 – Effect of Feature Scaling on Gradient Descent
- ✅ Part 6 – Best Practices for Feature Scaling

---

# Next Chapter

## **Chapter 5 – Regularization in Deep Learning**

We will now begin one of the most important topics in modern Deep Learning:

1. What is Regularization?
2. Why Neural Networks Overfit
3. L1 Regularization (Lasso)
4. L2 Regularization (Ridge / Weight Decay)
5. Elastic Net Regularization
6. Early Stopping
7. Dropout Regularization
8. Comparison of Regularization Techniques
9. Best Practices

This chapter forms the foundation for building neural networks that generalize well to unseen data.
