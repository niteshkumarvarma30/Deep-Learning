# McCulloch--Pitts (M-P) Neuron Model

## 1. Introduction

The **McCulloch--Pitts (M-P) neuron** is an early mathematical model of
an artificial neuron. It receives binary inputs, combines their effects,
and produces a binary output:

-   `1`: the neuron fires.
-   `0`: the neuron does not fire.

The M-P neuron uses a threshold-based activation function and supports
excitatory and inhibitory connections.

## 2. Net Input and Threshold Activation

The net input is the sum of the weighted inputs:

\[ y\_{in} = `\sum`{=tex}\_{i=1}\^{n} x_i w_i \]

where:

-   (x_i) is the value of input (i).
-   (w_i) is the weight of the connection from input (i).
-   \(n\) is the number of inputs.
-   (y\_{in}) is the total net input.

The neuron compares its net input with a threshold, (`\theta`{=tex}):

\[ f(y\_{in}) =

```{=tex}
\begin{cases}
1, & y_{in} \geq \theta \\
0, & y_{in} < \theta
\end{cases}
```
\]

If the net input reaches or exceeds the threshold, the neuron fires.
Otherwise, it does not fire.

## 3. Excitatory and Inhibitory Connections

The M-P model distinguishes between two types of connections.

### 3.1 Excitatory connections

An excitatory connection encourages the neuron to fire. Its weight is
positive:

\[ w \> 0 \]

Example:

\[ x = 1,`\quad`{=tex}w = 2 \]

Its contribution to the net input is:

\[ xw = 1 `\times 2`{=tex} = 2 \]

This increases the net input and makes firing more likely.

### 3.2 Inhibitory connections

An inhibitory connection suppresses the neuron's firing. It is
represented by a negative weight:

\[ w \< 0 \]

Example:

\[ x = 1,`\quad`{=tex}w = -5 \]

Its contribution is:

\[ xw = 1 `\times`{=tex}(-5) = -5 \]

This reduces the net input.

**Important:** In the classical M-P model, an active inhibitory input
has an absolute veto effect. If an inhibitory input is active, the
neuron does not fire, regardless of the excitatory input.

## 4. Absolute Inhibition

**Absolute inhibition** means that an active inhibitory input prevents
the neuron from firing, even when all excitatory inputs are active.

Assume:

-   There are (n) excitatory inputs.
-   Every excitatory connection has weight (+w).
-   The inhibitory connection has weight (-p), where (p \> 0).
-   The firing threshold is (`\theta`{=tex}).

When all excitatory inputs are active, their maximum contribution is:

\[ nw \]

If the inhibitory input is also active, the net input is:

\[ y\_{in} = nw - p \]

For the neuron not to fire, this value must be strictly less than the
threshold:

\[ nw - p \< `\theta`{=tex} \]

Rearranging gives:

\[ `\boxed{\theta > nw - p}`{=tex} \]

This is the absolute-inhibition condition.

### 4.1 Numerical example: Absolute inhibition

Suppose:

-   Number of excitatory inputs: (n = 5)
-   Excitatory weight: (w = 2)
-   Magnitude of inhibitory weight: (p = 12)
-   Threshold: (`\theta`{=tex}= 5)

First, calculate the maximum excitatory contribution:

\[ nw = 5 `\times 2`{=tex} = 10 \]

Now activate the inhibitory input:

\[ y\_{in} = nw - p = 10 - 12 = -2 \]

Compare this with the threshold:

\[ -2 \< 5 \]

Therefore, the neuron does not fire:

\[ `\boxed{y = 0}`{=tex} \]

The absolute-inhibition condition is satisfied:

\[ 5 \> 10 - 12 \]

Even though all five excitatory inputs are active, the inhibitory input
prevents firing.

## 5. Firing with (k) or More Excitatory Inputs

The M-P neuron can be configured to fire only when at least (k)
excitatory inputs are active, provided no inhibitory input is active.

Assume every excitatory connection has the same positive weight (w).

Two conditions must hold.

### Condition 1: (k) active inputs must make the neuron fire

When exactly (k) inputs are active, the net input is:

\[ kw \]

It must reach or exceed the threshold:

\[ kw `\geq`{=tex}`\theta`{=tex} \]

### Condition 2: (k-1) active inputs must not make the neuron fire

When exactly (k-1) inputs are active, the net input is:

\[ (k-1)w \]

It must remain below the threshold:

\[ (k-1)w \< `\theta`{=tex} \]

Combining both conditions:

\[ `\boxed{kw \geq \theta > (k-1)w}`{=tex} \]

### 5.1 Numerical example: At least 3 inputs must be active

Suppose:

-   There are 5 excitatory inputs.
-   Each excitatory weight is (w = 2).
-   The neuron should fire when at least (k = 3) inputs are active.

Using the threshold condition:

\[ kw `\geq`{=tex}`\theta`{=tex}\> (k-1)w \]

Substitute (k = 3) and (w = 2):

\[ 3(2) `\geq`{=tex}`\theta`{=tex}\> (3-1)(2) \]

\[ 6 `\geq`{=tex}`\theta`{=tex}\> 4 \]

A valid threshold is:

\[ `\theta`{=tex}= 5 \]

Test different numbers of active inputs:

    Active excitatory inputs   Net input   Threshold   Output
  -------------------------- ----------- ----------- --------
                           0           0           5        0
                           1           2           5        0
                           2           4           5        0
                           3           6           5        1
                           4           8           5        1
                           5          10           5        1

The neuron fires when three or more excitatory inputs are active.

## 6. Combined Example: Excitation and Absolute Inhibition

Consider a neuron with:

-   Five excitatory inputs, each with weight (+2).
-   One inhibitory input with weight (-12).
-   Threshold (`\theta`{=tex}= 5).
-   Required number of excitatory inputs (k = 3).

Let (x_1,`\ldots`{=tex},x_5) represent the excitatory inputs, and let
(z) represent the inhibitory input. All inputs are binary: `0` means
inactive and `1` means active.

The net input is:

\[ y\_{in} = 2x_1 + 2x_2 + 2x_3 + 2x_4 + 2x_5 - 12z \]

The threshold output is:

\[ y =

```{=tex}
\begin{cases}
1, & y_{in} \geq 5 \\
0, & y_{in} < 5
\end{cases}
```
\]

The inhibitory input has an absolute veto effect.

### Case 1: Only two excitatory inputs are active

\[ y\_{in} = 2 + 2 = 4 \]

Since (4 \< 5):

\[ `\boxed{y = 0}`{=tex} \]

### Case 2: Three excitatory inputs are active

\[ y\_{in} = 2 + 2 + 2 = 6 \]

Since (6 `\geq 5`{=tex}):

\[ `\boxed{y = 1}`{=tex} \]

### Case 3: All five excitatory inputs are active, with no inhibition

\[ y\_{in} = 2 + 2 + 2 + 2 + 2 = 10 \]

Since (10 `\geq 5`{=tex}):

\[ `\boxed{y = 1}`{=tex} \]

### Case 4: All five excitatory inputs and the inhibitory input are active

\[ y\_{in} = 10 - 12 = -2 \]

Since (-2 \< 5):

\[ `\boxed{y = 0}`{=tex} \]

The inhibitory input prevents firing even though all excitatory inputs
are active.

## 7. Why Does the M-P Neuron Have No Particular Training Algorithm?

In the classical M-P model, weights and thresholds are specified
manually. The model does not provide a particular algorithm that
automatically learns these values from training examples.

For example, we can manually choose:

\[ w_1 = w_2 = w_3 = 1 \]

and:

\[ `\theta`{=tex}= 2 \]

The neuron then fires when the sum of its three binary inputs is at
least 2.

The classical M-P model does not learn its weights through:

-   Gradient descent.
-   Backpropagation.
-   Loss minimization.

This distinguishes the original M-P neuron from trainable models such as
the perceptron and modern neural networks.

## 8. M-P Neuron: Key Concepts Summary

  ------------------------------------------------------------------------
  Concept              Meaning              Mathematical condition
  -------------------- -------------------- ------------------------------
  Excitatory           Encourages firing    (w \> 0)
  connection                                

  Inhibitory           Suppresses firing    (w \< 0)
  connection                                

  Threshold activation Determines whether   (y\_{in}
                       the neuron fires     `\geq`{=tex}`\theta`{=tex})

  Absolute inhibition  Active inhibition    (`\theta`{=tex}\> nw-p)
                       prevents firing      

  At least (k) active  Fires with (k) or    (kw
  inputs               more excitatory      `\geq`{=tex}`\theta`{=tex}\>
                       inputs               (k-1)w)

  Training algorithm   Weights and          No particular learning
                       threshold are        algorithm
                       specified manually   
                       in the classical     
                       model                
  ------------------------------------------------------------------------

## 9. Important Formulas for Revision

**Net input:**

\[ `\boxed{y_{in} = \sum_{i=1}^{n} x_iw_i}`{=tex} \]

**Threshold activation:**

\[
`\boxed{ y = \begin{cases} 1, & y_{in} \geq \theta \\ 0, & y_{in} < \theta \end{cases} }`{=tex}
\]

**Absolute inhibition:**

\[ `\boxed{\theta > nw-p}`{=tex} \]

**Firing with at least (k) excitatory inputs:**

\[ `\boxed{kw \geq \theta > (k-1)w}`{=tex} \]

## 10. Final Takeaway

The McCulloch--Pitts neuron is a manually configured binary threshold
neuron.

Remember these three rules:

1.  **Excitatory input:** pushes the neuron toward firing.
2.  **Inhibitory input:** acts as an absolute veto in the classical M-P
    model.
3.  **Threshold:** determines how much excitatory input is required for
    firing.

Unlike modern trainable neural networks, the classical M-P neuron does
not automatically learn its weights through a training algorithm.

## 11. Important Clarification: (n) vs. (`\sum `{=tex}x_i)

A common source of confusion in the absolute-inhibition formula is the
difference between:

-   (n): the **total number of excitatory input neurons**.
-   (`\sum`{=tex}\_{i=1}\^{n} x_i): the **number of active excitatory
    inputs**, when each input is binary (`0` or `1`).

These two quantities are not always equal.

### Example: Five excitatory inputs

Suppose the neuron has five excitatory inputs:

\[ x_1,;x_2,;x_3,;x_4,;x_5 \]

Therefore:

\[ n=5 \]

Assume each input is binary:

\[ x_i `\in `{=tex}{0,1} \]

**Case A: All five inputs are ON**

\[ x_1=x_2=x_3=x_4=x_5=1 \]

The number of active inputs is:

\[ `\sum`{=tex}\_{i=1}\^{5}x_i=1+1+1+1+1=5 \]

If every excitatory connection has weight (w=2), the total excitatory
contribution is:

\[ y\_{`\text{exc}`{=tex}}=`\sum`{=tex}\_{i=1}\^{5}x_iw \]

Since all weights are equal:

\[ y\_{`\text{exc}`{=tex}}=w`\sum`{=tex}\_{i=1}\^{5}x_i \]

\[ y\_{`\text{exc}`{=tex}}=2(5)=10 \]

This is why the maximum excitatory contribution can be written as:

\[ `\boxed{nw=5\times2=10}`{=tex} \]

**Case B: Only three inputs are ON**

For example:

\[
x_1=1,`\quad `{=tex}x_2=1,`\quad `{=tex}x_3=1,`\quad `{=tex}x_4=0,`\quad `{=tex}x_5=0
\]

The total number of excitatory neurons is still:

\[ n=5 \]

However, the number of active inputs is:

\[ `\sum`{=tex}\_{i=1}\^{5}x_i=1+1+1+0+0=3 \]

Therefore, the excitatory contribution is:

\[ y\_{`\text{exc}`{=tex}}=2(3)=6 \]

It is **not** (5`\times2`{=tex}), because only three inputs are active.

### Applying the inhibitory input

Suppose the inhibitory connection has weight (-p=-12), and the threshold
is:

\[ `\theta=5`{=tex} \]

When all five excitatory inputs are ON and the inhibitory input is also
ON:

\[ y\_{in}=nw-p \]

\[ y\_{in}=5(2)-12 \]

\[ y\_{in}=10-12=-2 \]

Since:

\[ -2\<5 \]

the neuron does not fire:

\[ `\boxed{y=0}`{=tex} \]

This confirms absolute inhibition for the given maximum excitatory
input.

### Summary: Do not confuse these quantities

  ------------------------------------------------------------------------
  Symbol or expression  Meaning                                    Example
  --------------------- --------------------- ----------------------------
  \(n\)                 Total number of                                  5
                        excitatory input      
                        neurons               

  (x_i)                 Value of an                                 0 or 1
                        individual input      

  (`\sum `{=tex}x_i)    Number of active       5 if all are ON; 3 if three
                        inputs for binary                           are ON
                        inputs                

  \(w\)                 Weight of each                                   2
                        excitatory connection 

  (nw)                  Maximum excitatory           (5`\times2`{=tex}=10)
                        contribution when all 
                        (n) inputs are ON     

  (w`\sum `{=tex}x_i)   Actual excitatory          (2`\times3`{=tex}=6) if
                        contribution for the                  three are ON
                        current input pattern 
  ------------------------------------------------------------------------

**Remember:**

\[ `\boxed{n=\text{total number of excitatory inputs}}`{=tex} \]

\[
`\boxed{\sum_{i=1}^{n}x_i=\text{number of active excitatory inputs}}`{=tex}
\]

They are equal only when all excitatory inputs are ON. The expression
(nw) represents the maximum excitatory contribution when all (n) inputs
are active.
