# Unit 5 – Training Challenges & Solutions

# Chapter 5 – Early Stopping

## Part 6 – Model Checkpointing

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what Model Checkpointing is.
- Learn why saving the best model is important.
- Understand how Model Checkpointing works with Early Stopping.
- Learn how modern Deep Learning frameworks implement checkpointing.
- Understand best practices for saving models during training.

---

# 1. Introduction

Suppose you train a neural network for

```text
100 Epochs
```

The best Validation Loss occurs at

```text
Epoch 42
```

Training continues until

```text
Epoch 55
```

where Early Stopping finally terminates training.

A natural question arises.

> **Which model should we keep?**

- Model from Epoch 42?
- Model from Epoch 55?

The correct answer is

> **The model from Epoch 42**, because it achieved the best Validation Loss.

This is exactly why **Model Checkpointing** is used.

---

# 2. What is Model Checkpointing?

Model Checkpointing is a technique that

> **Automatically saves the model whenever its validation performance improves.**

Instead of saving only the final model,

the framework continuously saves the **best-performing model** during training.

---

# 3. Why Is Model Checkpointing Needed?

Suppose Validation Loss changes as follows.

| Epoch | Validation Loss |
|------:|----------------:|
| 40 | 0.34 |
| 41 | 0.32 |
| 42 | 0.29 |
| 43 | 0.30 |
| 44 | 0.31 |
| 45 | 0.33 |

The best model occurs at

```text
Epoch 42
```

If training finishes at Epoch 45,

the final model is **not** the best model.

Without Model Checkpointing,

the best-performing weights would be lost.

---

# 4. How Model Checkpointing Works

The workflow is

```text
Train One Epoch

↓

Compute Validation Loss

↓

Better Than Previous Best?

↓

Yes

↓

Save Model

↓

Continue Training

OR

↓

No

↓

Continue Training
```

Every time Validation Loss improves,

the current model replaces the previous checkpoint.

---

# 5. Relationship Between Early Stopping and Model Checkpointing

These two techniques work together.

```text
Training

↓

Validation Improves

↓

Save Checkpoint

↓

Continue Training

↓

Validation Stops Improving

↓

Early Stopping

↓

Restore Best Checkpoint
```

Notice the difference.

- **Model Checkpointing** saves the best model.
- **Early Stopping** decides when to stop training.

Together,

they provide both

- Good generalization
- Best-performing model

---

# 6. Example

Suppose

| Epoch | Validation Loss | Action |
|------:|----------------:|--------|
| 1 | 0.80 | Save |
| 2 | 0.70 | Save |
| 3 | 0.61 | Save |
| 4 | 0.59 | Save |
| 5 | 0.60 | No Save |
| 6 | 0.62 | No Save |
| 7 | 0.64 | Early Stop |

Training stops at Epoch 7.

However,

the model used for deployment is

```text
Epoch 4
```

because it achieved the **lowest Validation Loss**.

---

# 7. What Does a Checkpoint Contain?

A checkpoint typically stores

- Model weights
- Optimizer state (optional)
- Current epoch
- Learning rate
- Training progress

This information allows

- Restoring the best model
- Continuing interrupted training
- Reproducing experiments

---

# 8. Framework Example

## TensorFlow / Keras

```python
from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    filepath="best_model.keras",
    monitor="val_loss",
    save_best_only=True,
    mode="min"
)
```

Meaning

- Monitor Validation Loss
- Save only the best model
- Lower Validation Loss is considered better

---

## PyTorch

PyTorch commonly saves checkpoints using

```python
torch.save(model.state_dict(), "best_model.pth")
```

whenever Validation Loss improves.

---

# 9. Why Not Save Every Epoch?

Suppose training lasts

```text
200 Epochs
```

Saving every epoch creates

```text
200 Model Files
```

Most of these files are unnecessary.

Saving only the best model

- Saves disk space
- Simplifies deployment
- Keeps only the highest-quality model

---

# 10. Real-Life Analogy

Imagine running a marathon.

Every kilometer,

your coach records your **best running time**.

Even if your speed decreases later,

your best performance has already been recorded.

Model Checkpointing works in exactly the same way.

---

# 11. Best Practices

Always

- Monitor Validation Loss (or Validation Accuracy when appropriate).
- Save only the best-performing model.
- Use Model Checkpointing together with Early Stopping.
- Restore the best checkpoint before deployment.
- Keep backup checkpoints for long-running training jobs if necessary.

---

# 12. One Important Insight

Many beginners believe

> **The model from the final training epoch is always the best model.**

This is incorrect.

Training often continues **after** the best Validation Loss has already been achieved.

Therefore,

the final model is not always the optimal one.

Model Checkpointing ensures that the best model is preserved.

---

# Visual Summary

```text
Train One Epoch

↓

Compute Validation Loss

↓

Validation Improved?

↓

Yes

↓

Save Checkpoint

↓

Continue Training

OR

↓

No

↓

Continue Training

↓

Early Stopping

↓

Restore Best Checkpoint

↓

Deployment
```

---

# Difference Between Early Stopping and Model Checkpointing

| Early Stopping | Model Checkpointing |
|----------------|---------------------|
| Decides when to stop training | Saves the best model |
| Prevents overfitting | Prevents losing the best-performing model |
| Uses Validation Loss to stop training | Uses Validation Loss to save models |
| Uses Patience | Uses save-best logic |
| Controls training duration | Controls model storage |

---

# Interview Questions

## Q1. What is Model Checkpointing?

**Answer**

Model Checkpointing is a technique that automatically saves the model whenever its validation performance improves.

---

## Q2. Why is Model Checkpointing important?

**Answer**

Because the best-performing model may occur before the final training epoch, and checkpointing preserves those optimal weights.

---

## Q3. Can Early Stopping work without Model Checkpointing?

**Answer**

Yes.

However, it is not recommended because the best model weights may be lost if training continues after the optimal epoch.

---

## Q4. What does `save_best_only=True` mean?

**Answer**

It instructs the framework to save the model only when validation performance improves over the previously saved best model.

---

## Q5. Which metric is most commonly monitored for Model Checkpointing?

**Answer**

Validation Loss (`val_loss`) is the most commonly monitored metric, although Validation Accuracy may also be used depending on the problem.

---

# Summary

Model Checkpointing is a technique that automatically saves the model whenever validation performance improves.

It ensures that the best-performing model is preserved even if later epochs lead to overfitting.

When combined with Early Stopping, Model Checkpointing forms a complete training strategy: Early Stopping determines when to terminate training, while Model Checkpointing ensures that the model with the best validation performance is available for deployment.

---

# Key Takeaways

✔ Model Checkpointing automatically saves the best-performing model.

✔ It usually monitors Validation Loss.

✔ It prevents losing the optimal model during training.

✔ It works together with Early Stopping.

✔ Only the best checkpoint is typically saved.

✔ Modern Deep Learning frameworks provide built-in support for Model Checkpointing.

---

# Next Part

## **Part 7 – Advantages and Limitations of Early Stopping**

In the next chapter, we will evaluate **Early Stopping** as a regularization technique, discuss its strengths and weaknesses, compare it with methods such as **Dropout** and **L2 Regularization**, and learn when Early Stopping should and should not be used.
