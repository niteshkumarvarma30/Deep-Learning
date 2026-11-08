# McCulloch–Pitts (M-P) Neuron Model

## 1. Introduction

The **McCulloch–Pitts (M-P) neuron** is an early mathematical model of an artificial neuron. It receives binary inputs, combines their effects, and produces a binary output:

- `1`: the neuron fires.
- `0`: the neuron does not fire.

The M-P neuron uses a threshold-based activation function and supports excitatory and inhibitory connections.

## 2. Net Input and Threshold Activation

The net input is the sum of the weighted inputs:

$$
y_{in} = \sum_{i=1}^{n} x_i w_i
$$

Where:

- $x_i$ is the value of input $i$.
- $w_i$ is the weight of the connection from input $i$.
- $n$ is the total number of input neurons.
- $y_{in}$ is the total net input.

The neuron compares its net input with a threshold, $\theta$:

$$
f(y_{in}) =
\begin{cases}
1, & y_{in} \geq \theta \\
0, & y_{in} < \theta
\end{cases}
$$

If the net input reaches or exceeds the threshold, the neuron fires. Otherwise, it does not fire.

## 3. Excitatory and Inhibitory Connections

The M-P model distinguishes between two types of connections.

### 3.1 Excitatory connections

An excitatory connection encourages the neuron to fire. Its weight is positive:

$$
w > 0
$$

**Example**

Suppose an input is active and its weight is $+2$:

$$
x = 1,\qquad w = 2
$$

Its contribution to the net input is:

$$
xw = 1 \times 2 = 2
$$

This increases the net input and makes firing more likely.

### 3.2 Inhibitory connections

An inhibitory connection suppresses the neuron's firing. It is represented by a negative weight:

$$
w < 0
$$

**Example**

Suppose an input is active and its weight is $-5$:

$$
x = 1,\qquad w = -5
$$

Its contribution is:

$$
xw = 1 \times (-5) = -5
$$

This reduces the net input.

**Important:** In the classical M-P model, an active inhibitory input has an absolute veto effect. If an inhibitory input is active, the neuron does not fire, regardless of the excitatory input.

## 4. Absolute Inhibition

**Absolute inhibition** means that an active inhibitory input prevents the neuron from firing, even when all excitatory inputs are active.

Assume:

- There are $n$ excitatory input neurons.
- Every excitatory connection has weight $+w$.
- The inhibitory connection has weight $-p$, where $p > 0$.
- The firing threshold is $\theta$.

When all excitatory inputs are active, their maximum contribution is:

$$
nw
$$

If the inhibitory input is also active, the net input is:

$$
y_{in} = nw - p
$$

For the neuron not to fire, this value must be strictly less than the threshold:

$$
nw - p < \theta
$$

Rearranging gives the absolute-inhibition condition:

$$
\boxed{\theta > nw - p}
$$

### 4.1 Numerical example: Absolute inhibition

Suppose:

- Number of excitatory input neurons: $n = 5$.
- Excitatory weight: $w = 2$.
- Magnitude of inhibitory weight: $p = 12$.
- Threshold: $\theta = 5$.

First, calculate the maximum excitatory contribution:

$$
nw = 5 \times 2 = 10
$$

Now activate the inhibitory input:

$$
y_{in} = nw - p = 10 - 12 = -2
$$

Compare this with the threshold:

$$
-2 < 5
$$

Therefore, the neuron does not fire:

$$
\boxed{y = 0}
$$

The absolute-inhibition condition is satisfied:

$$
5 > 10 - 12
$$

Even though all five excitatory inputs are active, the inhibitory input prevents firing.

## 5. Firing with $k$ or More Excitatory Inputs

The M-P neuron can be configured to fire only when at least $k$ excitatory inputs are active, provided no inhibitory input is active.

Assume every excitatory connection has the same positive weight $w$.

Two conditions must hold.

### Condition 1: $k$ active inputs must make the neuron fire

When exactly $k$ inputs are active, the net input is:

$$
kw
$$

It must reach or exceed the threshold:

$$
kw \geq \theta
$$

### Condition 2: $k-1$ active inputs must not make the neuron fire

When exactly $k-1$ inputs are active, the net input is:

$$
(k-1)w
$$

It must remain below the threshold:

$$
(k-1)w < \theta
$$

Combining both conditions:

$$
\boxed{kw \geq \theta > (k-1)w}
$$

### 5.1 Numerical example: At least 3 inputs must be active

Suppose:

- There are 5 excitatory input neurons.
- Each excitatory weight is $w = 2$.
- The neuron should fire when at least $k = 3$ inputs are active.

Using the threshold condition:

$$
kw \geq \theta > (k-1)w
$$

Substitute $k = 3$ and $w = 2$:

$$
3(2) \geq \theta > (3-1)(2)
$$

$$
6 \geq \theta > 4
$$

A valid threshold is:

$$
\theta = 5
$$

Test different numbers of active inputs:

| Active excitatory inputs | Net input | Threshold | Output |
|---:|---:|---:|---:|
| 0 | 0 | 5 | 0 |
| 1 | 2 | 5 | 0 |
| 2 | 4 | 5 | 0 |
| 3 | 6 | 5 | 1 |
| 4 | 8 | 5 | 1 |
| 5 | 10 | 5 | 1 |

The neuron fires when three or more excitatory inputs are active.

## 6. Combined Example: Excitation and Absolute Inhibition

Consider a neuron with:

- Five excitatory inputs, each with weight $+2$.
- One inhibitory input with weight $-12$.
- Threshold $\theta = 5$.
- Required number of excitatory inputs $k = 3$.

Let $x_1, x_2, x_3, x_4, x_5$ represent the excitatory inputs, and let $z$ represent the inhibitory input. All inputs are binary: `0` means inactive and `1` means active.

The net input is:

$$
y_{in} = 2x_1 + 2x_2 + 2x_3 + 2x_4 + 2x_5 - 12z
$$

The threshold output is:

$$
y =
\begin{cases}
1, & y_{in} \geq 5 \\
0, & y_{in} < 5
\end{cases}
$$

The inhibitory input has an absolute veto effect.

### Case 1: Only two excitatory inputs are active

$$
y_{in} = 2 + 2 = 4
$$

Since $4 < 5$:

$$
\boxed{y = 0}
$$

### Case 2: Three excitatory inputs are active

$$
y_{in} = 2 + 2 + 2 = 6
$$

Since $6 \geq 5$:

$$
\boxed{y = 1}
$$

### Case 3: All five excitatory inputs are active, with no inhibition

$$
y_{in} = 2 + 2 + 2 + 2 + 2 = 10
$$

Since $10 \geq 5$:

$$
\boxed{y = 1}
$$

### Case 4: All five excitatory inputs and the inhibitory input are active

$$
y_{in} = 10 - 12 = -2
$$

Since $-2 < 5$:

$$
\boxed{y = 0}
$$

The inhibitory input prevents firing even though all excitatory inputs are active.

## 7. Why Does the M-P Neuron Have No Particular Training Algorithm?

In the classical M-P model, weights and thresholds are specified manually. The model does not provide a particular algorithm that automatically learns these values from training examples.

For example, we can manually choose:

$$
w_1 = w_2 = w_3 = 1
$$

and:

$$
\theta = 2
$$

The neuron then fires when the sum of its three binary inputs is at least 2.

The classical M-P model does not learn its weights through:

- Gradient descent.
- Backpropagation.
- Loss minimization.

This distinguishes the original M-P neuron from trainable models such as the perceptron and modern neural networks.

## 8. M-P Neuron: Key Concepts Summary

| Concept | Meaning | Mathematical condition |
|---|---|---|
| Excitatory connection | Encourages firing | $w > 0$ |
| Inhibitory connection | Suppresses firing | $w < 0$ |
| Threshold activation | Determines whether the neuron fires | $y_{in} \geq \theta$ |
| Absolute inhibition | Active inhibition prevents firing | $\theta > nw - p$ |
| At least $k$ active inputs | Fires with $k$ or more excitatory inputs | $kw \geq \theta > (k-1)w$ |
| Training algorithm | Weights and threshold are specified manually in the classical model | No particular learning algorithm |

## 9. Important Formulas for Revision

**Net input:**

$$
\boxed{y_{in} = \sum_{i=1}^{n} x_i w_i}
$$

**Threshold activation:**

$$
\boxed{
y =
\begin{cases}
1, & y_{in} \geq \theta \\
0, & y_{in} < \theta
\end{cases}
}
$$

**Absolute inhibition:**

$$
\boxed{\theta > nw - p}
$$

**Firing with at least $k$ excitatory inputs:**

$$
\boxed{kw \geq \theta > (k-1)w}
$$

## 10. Important Clarification: $n$ vs. $\sum x_i$

A common source of confusion in the absolute-inhibition formula is the difference between:

- $n$: the **total number of excitatory input neurons**.
- $\sum_{i=1}^{n} x_i$: the **number of active excitatory inputs**, when each input is binary (`0` or `1`).

These two quantities are not always equal.

### Example: Five excitatory inputs

Suppose the neuron has five excitatory inputs:

$$
x_1, x_2, x_3, x_4, x_5
$$

Therefore:

$$
n = 5
$$

Assume each input is binary:

$$
x_i \in \{0,1\}
$$

### Case A: All five inputs are ON

$$
x_1 = x_2 = x_3 = x_4 = x_5 = 1
$$

The number of active inputs is:

$$
\sum_{i=1}^{5} x_i = 1+1+1+1+1 = 5
$$

If every excitatory connection has weight $w = 2$, the total excitatory contribution is:

$$
y_{\text{exc}} = \sum_{i=1}^{5} x_i w
$$

Since all weights are equal:

$$
y_{\text{exc}} = w \sum_{i=1}^{5} x_i
$$

$$
y_{\text{exc}} = 2(5) = 10
$$

This is why the maximum excitatory contribution can be written as:

$$
\boxed{nw = 5 \times 2 = 10}
$$

### Case B: Only three inputs are ON

For example:

$$
x_1 = 1,\quad x_2 = 1,\quad x_3 = 1,\quad x_4 = 0,\quad x_5 = 0
$$

The total number of excitatory input neurons is still:

$$
n = 5
$$

However, the number of active inputs is:

$$
\sum_{i=1}^{5} x_i = 1+1+1+0+0 = 3
$$

Therefore, the excitatory contribution is:

$$
y_{\text{exc}} = 2(3) = 6
$$

It is **not** $5 \times 2$, because only three inputs are active.

### Applying the inhibitory input

Suppose the inhibitory connection has weight $-p = -12$, and the threshold is:

$$
\theta = 5
$$

When all five excitatory inputs are ON and the inhibitory input is also ON:

$$
y_{in} = nw - p
$$

$$
y_{in} = 5(2) - 12
$$

$$
y_{in} = 10 - 12 = -2
$$

Since:

$$
-2 < 5
$$

the neuron does not fire:

$$
\boxed{y = 0}
$$

This confirms absolute inhibition for the given maximum excitatory input.

### Summary: Do Not Confuse These Quantities

| Symbol or expression | Meaning | Example |
|---|---|---|
| $n$ | Total number of excitatory input neurons | 5 |
| $x_i$ | Value of an individual input | 0 or 1 |
| $\sum_{i=1}^{n} x_i$ | Number of active inputs for binary inputs | 5 if all are ON; 3 if three are ON |
| $w$ | Weight of each excitatory connection | 2 |
| $nw$ | Maximum excitatory contribution when all $n$ inputs are ON | $5 \times 2 = 10$ |
| $w\sum_{i=1}^{n}x_i$ | Actual excitatory contribution for the current input pattern | $2 \times 3 = 6$ if three are ON |

**Remember:**

$$
\boxed{n = \text{total number of excitatory inputs}}
$$

$$
\boxed{\sum_{i=1}^{n}x_i = \text{number of active excitatory inputs}}
$$

They are equal only when all excitatory inputs are ON. The expression $nw$ represents the maximum excitatory contribution when all $n$ inputs are active.
