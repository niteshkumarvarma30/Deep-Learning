# Unit 5 – Training Challenges & Solutions

# Chapter 5 – Early Stopping

## Part 4 – How Early Stopping Works

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the complete Early Stopping algorithm.
- Learn how validation performance is monitored.
- Understand the concept of **Patience**.
- Learn how Deep Learning frameworks decide when to stop training.
- Understand why the best model is often saved before training ends.

---

# 1. Introduction

In the previous chapter,

we learned that

- Training Loss usually keeps decreasing.
- Validation Loss eventually starts increasing due to overfitting.

The next question is

> **How does the computer know when to stop training?**

The answer is

**Early Stopping continuously monitors validation performance after every epoch.**

---

# 2. Basic Workflow

The training process looks like

```text
Start Training

↓

Epoch 1

↓

Compute Validation Loss

↓

Epoch 2

↓

Compute Validation Loss

↓

Epoch 3

↓

Compute Validation Loss

↓

...

↓

Stop Training Automatically
```

After every epoch,

the model checks whether the validation performance has improved.

---

# 3. Improvement Check

Suppose the Validation Loss values are

| Epoch | Validation Loss |
|------:|----------------:|
| 1 | 0.85 |
| 2 | 0.70 |
| 3 | 0.58 |
| 4 | 0.49 |
| 5 | 0.44 |

Each epoch produces a lower Validation Loss.

Therefore,

training continues.

---

# 4. When Improvement Stops

Now suppose the losses become

| Epoch | Validation Loss |
|------:|----------------:|
| 6 | 0.44 |
| 7 | 0.45 |
| 8 | 0.46 |
| 9 | 0.47 |

Validation Loss is no longer improving.

Instead,

it is increasing.

This suggests that the model has started overfitting.

---

# 5. Should Training Stop Immediately?

Should we stop immediately after one bad epoch?

Usually,

**No.**

Validation Loss may temporarily increase because of

- Random mini-batches
- Noise
- Small fluctuations

Stopping immediately might terminate training too early.

---

# 6. The Patience Parameter

To solve this problem,

Early Stopping introduces a parameter called

```text
Patience
```

**Patience** is defined as

> **The number of consecutive epochs to wait for an improvement before stopping training.**

Example

```text
Patience = 3
```

The algorithm waits for **3 consecutive epochs** without improvement.

---

# 7. Example of Patience

Suppose

| Epoch | Validation Loss | Improvement? |
|------:|----------------:|--------------|
| 10 | 0.42 | ✅ Yes |
| 11 | 0.43 | ❌ No (1) |
| 12 | 0.44 | ❌ No (2) |
| 13 | 0.45 | ❌ No (3) |

Since the patience value is **3**,

training stops after **Epoch 13**.

---

# 8. What If Improvement Returns?

Suppose

| Epoch | Validation Loss |
|------:|----------------:|
| 10 | 0.42 |
| 11 | 0.43 |
| 12 | 0.41 |

Although Epoch 11 was worse,

Epoch 12 improves again.

The patience counter is reset to zero,

and training continues.

---

# 9. Complete Early Stopping Algorithm

The algorithm works as follows.

```text
Train One Epoch

↓

Compute Validation Loss

↓

Is Validation Loss Better Than Best?

↓

Yes

↓

Save Model

↓

Reset Patience Counter

↓

Continue Training

OR

↓

No

↓

Increase Patience Counter

↓

Has Patience Limit Been Reached?

↓

Yes

↓

Stop Training

↓

No

↓

Continue Training
```

---

# 10. Why Save the Best Model?

Suppose the Validation Loss values are

| Epoch | Validation Loss |
|------:|----------------:|
| 15 | 0.32 |
| 16 | 0.34 |
| 17 | 0.36 |
| 18 | 0.39 |

Training stops at Epoch 18.

However,

the best Validation Loss occurred at

```text
Epoch 15
```

Therefore,

Deep Learning frameworks usually restore the model weights from the best epoch,

not from the final epoch.

---

# 11. Framework Example

A typical Keras implementation looks like

```python
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)
```

Meaning

- Monitor **Validation Loss**
- Wait **3 epochs** without improvement
- Restore the weights from the **best-performing epoch**

---

# 12. Real-Life Analogy

Imagine preparing for a marathon.

Each week,

you record your running time.

```text
Week

↓

Better Time?

↓

Yes

↓

Continue Training

↓

No

↓

Wait a Few Weeks

↓

Still No Improvement?

↓

Stop Training
```

You do not quit after one poor workout.

You wait to see whether performance improves again.

The **Patience** parameter behaves in exactly the same way.

---

# 13. One Important Insight

Many beginners think

> **Early Stopping always stops exactly at the epoch with the lowest Validation Loss.**

This is not entirely correct.

Training usually continues for a few more epochs because of the **Patience** parameter.

Once training stops,

the framework restores the model from the epoch that achieved the **lowest Validation Loss**.

---

# Visual Summary

```text
Train One Epoch

↓

Compute Validation Loss

↓

Improved?

↓

Yes

↓

Save Best Model

↓

Reset Patience

↓

Continue Training

OR

↓

No

↓

Increase Patience Counter

↓

Patience Exceeded?

↓

Yes

↓

Stop Training

↓

Restore Best Model
```

---

# Difference Between Immediate Stopping and Early Stopping with Patience

| Immediate Stopping | Early Stopping with Patience |
|--------------------|------------------------------|
| Stops after first bad epoch | Waits for several bad epochs |
| Sensitive to random fluctuations | Robust to temporary fluctuations |
| May stop too early | Stops only after consistent lack of improvement |
| Does not tolerate noise | Handles noisy validation curves |
| Rarely used | Standard approach in Deep Learning |

---

# Interview Questions

## Q1. What is the purpose of the Patience parameter?

**Answer**

Patience specifies how many consecutive epochs without improvement are allowed before stopping training.

---

## Q2. Why doesn't Early Stopping stop after the first increase in Validation Loss?

**Answer**

Because temporary fluctuations or noise may cause small increases. Patience prevents the model from stopping too early.

---

## Q3. Why is the best model saved during training?

**Answer**

Because the lowest Validation Loss may occur several epochs before training actually stops.

---

## Q4. What does `restore_best_weights=True` do?

**Answer**

It restores the model parameters from the epoch that achieved the best Validation Loss instead of using the weights from the final training epoch.

---

## Q5. Which metric is most commonly monitored in Early Stopping?

**Answer**

Validation Loss (`val_loss`), although Validation Accuracy may also be used for certain tasks.

---

# Summary

Early Stopping works by evaluating Validation Loss after every training epoch.

If Validation Loss improves, the model continues training and saves the new best weights.

If Validation Loss does not improve, a patience counter is increased.

Once the number of consecutive non-improving epochs exceeds the patience value, training stops automatically.

Modern Deep Learning frameworks then restore the model weights from the epoch with the lowest Validation Loss, ensuring the final model achieves the best possible generalization.

---

# Key Takeaways

✔ Early Stopping monitors Validation Loss after every epoch.

✔ The **Patience** parameter prevents premature stopping.

✔ The patience counter resets whenever Validation Loss improves.

✔ Training stops only after the patience limit is exceeded.

✔ The best-performing model is automatically restored.

✔ Early Stopping improves generalization while reducing overfitting.

---

## Next Part

**Part 5 – The Patience Parameter (Deep Dive)**

In the next chapter, we will study the **Patience** parameter in greater detail, understand how different patience values affect training, learn how to choose an appropriate patience value, and examine practical examples from real-world Deep Learning projects.
