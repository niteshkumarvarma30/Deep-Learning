# Chapter 9: Learning Rate (η)

> **Course:** Machine Learning & Deep Learning Foundations
>
> **Chapter Goal:**
> Understand what the Learning Rate is, why it is important, how it affects the Perceptron Learning Algorithm, and how different learning rates influence convergence.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Define the Learning Rate.
- Explain why the Learning Rate is required.
- Understand the role of η in the Perceptron update rule.
- Compare small and large learning rates.
- Understand overshooting and slow convergence.
- Choose an appropriate learning rate.

---

# 1. Recap

In the previous chapter we learned the Perceptron Learning Rule

$$
w_{new}=w_{old}+\eta(y-\hat y)x
$$

One symbol in this equation has not yet been studied.

That symbol is

$$
\eta
$$

called the **Learning Rate**.

---

# 2. What is the Learning Rate?

The **Learning Rate** determines

> **How much should the weights change after every incorrect prediction?**

Think of it as the **step size** during learning.

Instead of making huge corrections,

the Perceptron usually makes **small controlled corrections**.

---

# Definition

The **Learning Rate (η)** is a positive constant that controls the magnitude of weight and bias updates during training.

---

# 3. Why Do We Need a Learning Rate?

Suppose the Perceptron predicts

```
Cat
```

instead of

```
Dog
```

It needs to correct its mistake.

But an important question arises.

Should it change the weights

```
A little?
```

or

```
A lot?
```

The Learning Rate answers this question.

---

# 4. Real-Life Analogy

Imagine you are walking toward a door.

### Small Steps

```
🚶

↓

↓

↓

Door
```

You eventually reach the door,

but it takes many steps.

---

### Huge Steps

```
🏃

↓

↓

↓

Door

↓

Oops!

You crossed the door.
```

You now have to walk back.

The same thing happens in machine learning.

---

# 5. Learning Rate in the Update Rule

Recall

$$
w_{new}=w_{old}+\eta(y-\hat y)x
$$

Notice

η multiplies the entire update.

This means

```
Large η

↓

Large Weight Change
```

```
Small η

↓

Small Weight Change
```

---

# 6. Numerical Example

Suppose

```
Current Weight = 4

Input = 3

Error = 1
```

Without Learning Rate

```
Weight Update

=

4 + 3

=

7
```

---

Now suppose

$$
\eta=0.1
$$

Weight Update

$$
4+0.1(1)(3)
$$

$$
4+0.3
$$

$$
4.3
$$

The correction is much smaller.

---

# 7. Small Learning Rate

Example

$$
\eta=0.001
$$

Weight Updates

```
4.000

↓

4.001

↓

4.002

↓

4.003
```

Advantages

✔ Stable learning

✔ Less chance of overshooting

Disadvantages

✘ Training is slow

✘ Requires many epochs

---

# 8. Large Learning Rate

Example

$$
\eta=5
$$

Weight Updates

```
4

↓

19

↓

-12

↓

38

↓

-7
```

The weights jump wildly.

Advantages

✔ Faster updates

Disadvantages

✘ Unstable learning

✘ May never converge

---

# 9. Comparing Learning Rates

| Small η | Large η |
|----------|----------|
| Slow learning | Fast learning |
| Stable | Unstable |
| More epochs | Fewer epochs (if stable) |
| Less overshooting | More overshooting |

---

# 10. What is Overshooting?

Suppose the best weight is

```
10
```

Current Weight

```
5
```

Small Learning Rate

```
5

↓

7

↓

8

↓

9

↓

10
```

Perfect.

---

Large Learning Rate

```
5

↓

20

↓

-5

↓

18

↓

2

↓

15
```

The algorithm keeps jumping around the correct solution.

This is called **Overshooting**.

---

# 11. Effect on the Decision Boundary

Remember

Weights determine the Decision Boundary.

Small Learning Rate

```
Boundary

↓

Small Movement

↓

Small Movement

↓

Correct Position
```

---

Large Learning Rate

```
Boundary

↓

Huge Jump

↓

Huge Jump

↓

Huge Jump
```

The boundary may never settle in the correct position.

---

# 12. Choosing a Good Learning Rate

There is no universal best value.

Common choices are

```
0.1

0.01

0.001
```

The best value depends on

- Dataset
- Number of features
- Complexity of the problem
- Model

---

# 13. Does the Learning Rate Change During Training?

### Original Perceptron

Usually

```
Constant Learning Rate
```

Example

```
η = 0.1

for all epochs
```

---

### Modern Deep Learning

The Learning Rate often changes automatically.

Examples

- Learning Rate Decay
- Step Decay
- Cosine Annealing
- Adam Optimizer

These techniques are used to improve convergence.

---

# 14. Why Not Always Use a Very Small Learning Rate?

Very small learning rates make learning extremely slow.

Imagine reading one page of a book every week.

Eventually,

you will finish,

but it will take a very long time.

---

# 15. Why Not Always Use a Very Large Learning Rate?

Very large learning rates may never allow the model to converge.

Imagine trying to park a car.

Instead of moving slowly,

you drive forward

then backward

then forward

then backward.

You never stop at the correct position.

---

# Common Misconceptions

### Mistake 1

Thinking a larger Learning Rate always learns faster.

❌ Incorrect.

It may prevent convergence.

---

### Mistake 2

Thinking the Learning Rate changes the dataset.

❌ Incorrect.

It only controls the size of the parameter updates.

---

### Mistake 3

Thinking η must always be 1.

❌ Incorrect.

The Learning Rate is a hyperparameter chosen by the user.

---

# Chapter Summary

The Learning Rate determines how much the Perceptron changes its weights after an incorrect prediction.

It appears in the update rule

$$
w_{new}=w_{old}+\eta(y-\hat y)x
$$

A small Learning Rate results in slow but stable learning.

A large Learning Rate results in faster but potentially unstable learning.

Choosing an appropriate Learning Rate is essential for successful training.

---

# Key Takeaways

✔ Learning Rate is represented by

$$
\eta
$$

✔ It controls the size of weight updates.

✔ Small η

↓

Slow but stable learning.

✔ Large η

↓

Fast but unstable learning.

✔ The Learning Rate is a hyperparameter.

✔ The original Perceptron usually uses a constant Learning Rate.

---

# Interview Questions

### Q1. What is the Learning Rate?

**Answer:**

The Learning Rate controls the size of the weight update after each incorrect prediction.

---

### Q2. Where does the Learning Rate appear?

**Answer:**

In the Perceptron Learning Rule

$$
w_{new}=w_{old}+\eta(y-\hat y)x
$$

---

### Q3. What happens if the Learning Rate is too small?

**Answer:**

Training becomes very slow.

---

### Q4. What happens if the Learning Rate is too large?

**Answer:**

The model may overshoot the optimal solution and fail to converge.

---

# Practice Questions

## Conceptual

1. Explain the purpose of the Learning Rate.
2. Differentiate between small and large Learning Rates.
3. What is overshooting?
4. Why is choosing the correct Learning Rate important?

---

## Numerical

### Question 1

Given

```
Weight = 5

Input = 4

η = 0.2

Error = 1
```

Find the updated weight.

---

### Question 2

Repeat the above problem using

```
η = 2
```

Compare the results.

---

## MCQs

### 1. The Learning Rate controls

A. Number of features

B. Dataset size

C. Size of weight updates

D. Number of classes

**Answer:** C

---

### 2. A very small Learning Rate generally leads to

A. Fast convergence

B. Slow learning

C. Data loss

D. Overfitting

**Answer:** B

---

### 3. A very large Learning Rate may cause

A. Better accuracy

B. Overshooting

C. More features

D. Underfitting

**Answer:** B

---

# What's Next?

In **Chapter 10**, we will study the **Error and Loss Function**.

Topics include:

- What is Error?
- What is a Loss Function?
- Difference between Error and Loss
- Perceptron Error Signal
- Why Modern Machine Learning Uses Loss Functions
- Introduction to Optimization
