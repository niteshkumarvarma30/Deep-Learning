# Perceptron Networks --- Complete Study Notes

> GitHub-ready notes covering perceptron architecture, activation
> functions, learning rules, training algorithm, multiple-output
> networks, forward propagation, and decision boundaries.

## Table of Contents

1.  [Introduction to Perceptron
    Networks](#1-introduction-to-perceptron-networks)
2.  [Perceptron Architecture](#2-perceptron-architecture)
3.  [Mathematical Model of a
    Perceptron](#3-mathematical-model-of-a-perceptron)
4.  [Perceptron Activation Function](#4-perceptron-activation-function)
5.  [Perceptron Learning Rule](#5-perceptron-learning-rule)
6.  [Numerical Example: Perceptron
    Learning](#6-numerical-example-perceptron-learning)
7.  [Perceptron Training Algorithm](#7-perceptron-training-algorithm)
8.  [Multiple-Output Perceptron
    Network](#8-multiple-output-perceptron-network)
9.  [Forward Propagation: Numerical
    Example](#9-forward-propagation-numerical-example)
10. [Perceptron vs. Sigmoid Neural
    Network](#10-perceptron-vs-sigmoid-neural-network)
11. [Decision Boundary and Linear
    Separability](#11-decision-boundary-and-linear-separability)
12. [Other Machine Learning
    Algorithms](#12-other-machine-learning-algorithms)
13. [Important Formula Sheet](#13-important-formula-sheet)
14. [Practice Questions](#14-practice-questions)

------------------------------------------------------------------------

## 1. Introduction to Perceptron Networks

A **perceptron** is one of the earliest artificial neural network
models. It was introduced by Frank Rosenblatt in the late 1950s.

A perceptron is a basic computational model commonly used for
classification. It receives input features, multiplies them by weights,
adds a bias, and applies an activation function to produce an output.

### Example: Email spam classification

Possible input features include:

-   Number of suspicious words.
-   Number of external links.
-   Whether the sender is unknown.

The perceptron combines these features and produces a classification.

### Single-layer feed-forward network

A classic single-layer perceptron is a feed-forward network because
information moves in one direction:

``` text
Input features  --->  Output neuron  --->  Prediction
```

There are no feedback connections or cycles.

The term *single-layer* refers to the trainable layer of connections
leading to the output units. It does not mean that every historical
perceptron architecture has only one group of units. The classical
sensory-associator-response description is explained next.

------------------------------------------------------------------------

## 2. Perceptron Architecture

The classical architecture described in the lecture notes contains three
types of units:

1.  Sensory units (input units).
2.  Associator units (intermediate or hidden units).
3.  Response units (output units).

### Architecture diagram

``` mermaid
flowchart TD
    A["Sensory units<br/>Receive input features"] -->|"Fixed connections<br/>Weights: -1, 0, +1"| B["Associator units<br/>Process input signals"]
    B -->|"Trainable connections"| C["Response units<br/>Produce output"]
```

### 2.1 Sensory units (input units)

Sensory units receive information from the outside world.

For example, an input vector may be:

$$
X = [x_1, x_2, x_3]
$$

The sensory units represent the input data and pass the signals to the
associator units.

### 2.2 Associator units

Associator units receive signals from sensory units.

According to the architecture in the notes:

-   Sensory units are connected to associator units.
-   These connections have fixed weights.
-   The weights may be assigned values from the set `{-1, 0, +1}`.
-   These fixed sensory-to-associator weights are not adjusted by the
    response-layer perceptron learning rule described below.

The associator units process incoming signals and produce activations.

### 2.3 Response units (output units)

Response units receive signals from associator units and generate the
network output.

The response can take one of three values:

$$
y \in \{-1, 0, +1\}
$$

    Output Interpretation
  -------- --------------------------------
      `+1` Positive response
       `0` No response / neutral response
      `-1` Negative response

The exact meaning of each class depends on the application.

### 2.4 What is trainable?

In this classical three-stage description, the important trainable
connections are those between the associator units and the response
units. The sensory-to-associator connections are described as fixed.

------------------------------------------------------------------------

## 3. Mathematical Model of a Perceptron

A simple perceptron can be represented using:

-   Input features.
-   A weight for each input.
-   A bias.
-   An output neuron.

### Net-input equation

$$
y_{in} = b + \sum_{i=1}^{n} x_i w_i
$$

Expanded form:

$$
y_{in} = b + x_1w_1 + x_2w_2 + \cdots + x_nw_n
$$

  Symbol     Meaning
  ---------- ------------------------------------
  $x_i$      Input feature
  $w_i$      Weight associated with input $x_i$
  $b$        Bias
  $n$        Number of input features
  $y_{in}$   Net input before activation

### 3.1 Role of weights

A weight determines how strongly an input feature contributes to the
neuron's net input.

-   A positive weight increases the net input when its feature is
    positive.
-   A negative weight decreases the net input when its feature is
    positive.
-   A zero weight means that the corresponding feature contributes
    nothing to the weighted sum.

### 3.2 Role of bias

Bias shifts the decision boundary.

Without bias:

$$
y_{in} = x_1w_1 + x_2w_2
$$

With bias:

$$
y_{in} = x_1w_1 + x_2w_2 + b
$$

The bias allows the decision boundary to move away from the origin.

### 3.3 Numerical example: calculating net input

Given:

$$
x_1 = 2, \qquad x_2 = 3
$$

$$
w_1 = 0.5, \qquad w_2 = 0.2
$$

$$
b = 0.1
$$

Use:

$$
y_{in} = b + x_1w_1 + x_2w_2
$$

Substitute:

$$
y_{in} = 0.1 + (2)(0.5) + (3)(0.2)
$$

$$
y_{in} = 0.1 + 1 + 0.6
$$

Therefore:

$$
\boxed{y_{in} = 1.7}
$$

The activation function is applied to this value to obtain the final
output.

------------------------------------------------------------------------

## 4. Perceptron Activation Function

The lecture notes describe a ternary threshold activation function:

$$
f(y_{in}) =
\begin{cases}
+1, & y_{in} > \theta \\\\
0, & -\theta \leq y_{in} \leq \theta \\\\
-1, & y_{in} < -\theta
\end{cases}
$$

Here, `θ` (theta) is the threshold.

The function produces three possible outputs: `+1`, `0`, and `-1`.

### 4.1 Example with a threshold of 2

Let:

$$
\theta = 2
$$

    Net input   Output Reason
  ----------- -------- -----------------------
          `4`     `+1` Greater than `+2`
        `2.5`     `+1` Greater than `+2`
          `1`      `0` Between `-2` and `+2`
          `0`      `0` Between `-2` and `+2`
       `-1.5`      `0` Between `-2` and `+2`
         `-3`     `-1` Less than `-2`

### 4.2 Numerical example

Suppose:

$$
\theta = 2, \qquad y_{in} = 1.7
$$

Since:

$$
-2 \leq 1.7 \leq 2
$$

The output is:

$$
\boxed{y = 0}
$$

If instead:

$$
y_{in} = 3
$$

then `3 > 2`, so:

$$
\boxed{y = +1}
$$

> **Important distinction:** The lecture notes also refer to binary
> activation in the sensory and associator units. Do not confuse that
> with the ternary activation used for the response unit in this model.

------------------------------------------------------------------------

## 5. Perceptron Learning Rule

The perceptron learning rule adjusts weights and bias when the predicted
output differs from the target output.

The learning rule written in the lecture notes is:

### Weight update

$$
\boxed{w_i(new) = w_i(old) + \\alpha t x_i}
$$

### Bias update

$$
\boxed{b(new) = b(old) + \\alpha t}
$$

Where:

  Symbol       Meaning
  ------------ ------------------
  $w_i(new)$   Updated weight
  $w_i(old)$   Previous weight
  $\\alpha$    Learning rate
  $t$          Target output
  $x_i$        Input activation
  $b$          Bias

The target is bipolar:

$$
t \in \{-1, +1\}
$$

The learning rate is selected such that:

$$
0 < \\alpha \\leq 1
$$

### 5.1 What is a learning rate?

The learning rate controls the size of parameter updates.

-   A smaller learning rate produces smaller updates.
-   A larger learning rate produces larger updates.

For example, `α = 0.1` produces smaller updates than `α = 1`, for the
same input and target.

### 5.2 When are weights updated?

According to the notes:

-   Calculate the actual output.
-   Compare the actual output with the target.
-   If an error occurs, update weights and bias.
-   If there is no error, do not update them.

In symbols:

$$
y \\neq t \\quad \\Rightarrow \\quad \\text{Update}
$$

$$
y = t \\quad \\Rightarrow \\quad \\text{No update}
$$

For the particular rule in the notes:

$$
\\Delta w_i = \\alpha t x_i
$$

$$
\\Delta b = \\alpha t
$$

If an input activation is zero, its corresponding weight update is zero
under this rule.

### 5.3 Why can a weight increase or decrease?

If:

$$
x_i = +1, \\qquad t = +1, \\qquad \\alpha = 0.1
$$

then:

$$
\\Delta w_i = 0.1(+1)(+1) = +0.1
$$

The weight increases by `0.1`.

If:

$$
x_i = +1, \\qquad t = -1, \\qquad \\alpha = 0.1
$$

then:

$$
\\Delta w_i = 0.1(+1)(-1) = -0.1
$$

The weight decreases by `0.1`.

------------------------------------------------------------------------

## 6. Numerical Example: Perceptron Learning

Consider a perceptron with two input features and one output neuron.

### Given values

Initial weights:

$$
w_1 = 0.2, \\qquad w_2 = -0.1
$$

Initial bias:

$$
b = 0.05
$$

Learning rate:

$$
\\alpha = 0.1
$$

Threshold:

$$
\\theta = 0.5
$$

Training pattern:

$$
x_1 = 1, \\qquad x_2 = 0
$$

Target:

$$
t = +1
$$

### Step 1: Calculate net input

$$
y_{in} = b + x_1w_1 + x_2w_2
$$

Substitute:

$$
y_{in} = 0.05 + (1)(0.2) + (0)(-0.1)
$$

$$
\\boxed{y_{in} = 0.25}
$$

### Step 2: Apply the activation function

Since:

$$
-0.5 \\leq 0.25 \\leq 0.5
$$

the actual output is:

$$
\\boxed{y = 0}
$$

### Step 3: Compare actual output and target

Actual output:

$$
y = 0
$$

Target output:

$$
t = +1
$$

Since `y` is not equal to `t`, an update is required.

### Step 4: Update the first weight

$$
w_1(new) = w_1(old) + \\alpha t x_1
$$

$$
w_1(new) = 0.2 + (0.1)(1)(1)
$$

$$
\\boxed{w_1(new) = 0.3}
$$

### Step 5: Update the second weight

$$
w_2(new) = w_2(old) + \\alpha t x_2
$$

$$
w_2(new) = -0.1 + (0.1)(1)(0)
$$

$$
\\boxed{w_2(new) = -0.1}
$$

The second input is zero, so its weight does not change.

### Step 6: Update the bias

$$
b(new) = b(old) + \\alpha t
$$

$$
b(new) = 0.05 + (0.1)(1)
$$

$$
\\boxed{b(new) = 0.15}
$$

### Parameter comparison

  Parameter     Before update   After update
  ----------- --------------- --------------
  $w_1$                   0.2            0.3
  $w_2$                  -0.1           -0.1
  $b$                    0.05           0.15

### Step 7: Recalculate the output

Using the updated parameters:

$$
y_{in} = 0.15 + (1)(0.3) + (0)(-0.1)
$$

$$
y_{in} = 0.45
$$

Since:

$$
-0.5 \\leq 0.45 \\leq 0.5
$$

the output is still:

$$
y = 0
$$

It still does not match the target `+1`. Another update is needed when
this pattern is processed again.

> **Note about learning-rule conventions:** This numerical example
> follows the update formula written in the lecture notes: `Δwᵢ = αtxᵢ`
> and `Δb = αt`. A commonly used conventional perceptron correction is
> `Δwᵢ = α(t − y)xᵢ` and `Δb = α(t − y)`. These are different update
> conventions. Use the formula prescribed by your course when solving
> its numerical problems.

------------------------------------------------------------------------

## 7. Perceptron Training Algorithm

The training algorithm repeatedly processes training input-target pairs
and adjusts parameters when required.

### Training flowchart

``` mermaid
flowchart TD
    A([Start]) --> B["Initialize weights and bias"]
    B --> C["Set learning rate α"]
    C --> D{"For each training pair"}
    D -->|Yes| E["Activate input units"]
    E --> F["Calculate net input"]
    F --> G["Apply activation function"]
    G --> H{"Actual output equals target?"}
    H -->|No| I["Update weights and bias"]
    H -->|Yes| J["Keep parameters unchanged"]
    I --> K["Process next training pair"]
    J --> K
    K --> D
    D -->|No more pairs| L{"Any parameter changes in the pass?"}
    L -->|Yes| D
    L -->|No| M([Stop])
```

### Step 0: Initialize weights and learning rate

Initialize weights to zero:

$$
w_i = 0
$$

Initialize bias:

$$
b = 0
$$

Select a learning rate:

$$
0 < \\alpha \\leq 1
$$

The lecture notes use `α = 1` for simplicity.

### Step 1: Repeat the training process

Repeat the training steps until the stopping condition is satisfied.

### Step 2: Select a training pair

The training dataset contains pairs:

$$
(s, t)
$$

Where:

-   `s` is the training input.
-   `t` is the target output.

Example:

  Input        Target
  ---------- --------
  `[1, 0]`       `+1`
  `[0, 1]`       `-1`
  `[1, 1]`       `+1`

Each training pair is processed.

### Step 3: Activate the input layer

The input layer uses the identity activation function:

$$
x_i = s_i
$$

The input values are passed without modification.

### Step 4: Calculate the network output

First calculate the net input:

$$
y_{in} = b + \\sum_{i=1}^{n} w_i x_i
$$

Then apply the activation function:

$$
y = f(y_{in})
$$

For the ternary activation function:

$$
f(y_{in}) =
\\begin{cases}
+1, & y_{in} > \\theta \\\\
0, & -\\theta \\leq y_{in} \\leq \\theta \\\\
-1, & y_{in} < -\\theta
\\end{cases}
$$

### Step 5: Compare actual and target outputs

If:

$$
y \\neq t
$$

update:

$$
w_i(new) = w_i(old) + \\alpha t x_i
$$

$$
b(new) = b(old) + \\alpha t
$$

Otherwise, keep the parameters unchanged:

$$
w_i(new) = w_i(old)
$$

$$
b(new) = b(old)
$$

### Step 6: Check the stopping condition

The lecture notes state that training continues until there is no weight
change.

In practical terms, this means completing a full pass through the
training dataset without making any parameter updates.

If parameter changes occur, training continues.

**Convergence note:** The classic perceptron convergence guarantee
applies to linearly separable data under the standard perceptron update
rule. A perceptron may not converge on non-linearly separable data.

------------------------------------------------------------------------

## 8. Multiple-Output Perceptron Network

A perceptron can have multiple output neurons when a classification task
contains multiple classes.

For example, an image classifier may distinguish:

1.  Cat.
2.  Dog.
3.  Horse.

It can use three output neurons:

  Output neuron   Class
  --------------- -------
  $y_1$           Cat
  $y_2$           Dog
  $y_3$           Horse

An example output vector is:

$$
[y_1, y_2, y_3] = [+1, -1, -1]
$$

This indicates that the first output class is selected.

### Net input for output neuron j

$$
y_{in,j} = b_j + \\sum_{i=1}^{n} x_i w_{ij}
$$

Where:

-   `j` identifies the output neuron.
-   `i` identifies the input feature.
-   `wᵢⱼ` is the weight from input `i` to output `j`.
-   `bⱼ` is the bias of output neuron `j`.

Each response unit has its own weights and bias.

The target outputs can be represented as:

$$
y_1 \\rightarrow t_1
$$

$$
y_2 \\rightarrow t_2
$$

$$
\\vdots
$$

$$
y_m \\rightarrow t_m
$$

------------------------------------------------------------------------

## 9. Forward Propagation: Numerical Example

Forward propagation is the process of passing input data through a
neural network to calculate its output.

The numerical example in the lecture notes contains:

-   Three input features.
-   One hidden-layer neuron.
-   One output-layer neuron.
-   Sigmoid activation functions.

### Network architecture

``` mermaid
flowchart LR
    X1["x₁ = 95"] --> H["Hidden neuron"]
    X2["x₂ = 4"] --> H
    X3["x₃ = 4"] --> H
    H --> O["Output neuron"]
    O --> Y["Final prediction"]
```

### 9.1 Given input and hidden-layer parameters

Input features:

$$
x_1 = 95, \\qquad x_2 = 4, \\qquad x_3 = 4
$$

Weights:

$$
w_1 = 0.01, \\qquad w_2 = 0.02, \\qquad w_3 = 0.03
$$

Hidden-layer bias:

$$
b_1 = 0.001
$$

### 9.2 Step 1: Calculate the hidden neuron's weighted sum

The equation is:

$$
z_1 = x_1w_1 + x_2w_2 + x_3w_3 + b_1
$$

Substitute:

$$
z_1 = (95)(0.01) + (4)(0.02) + (4)(0.03) + 0.001
$$

Calculate each multiplication:

$$
95 \\times 0.01 = 0.95
$$

$$
4 \\times 0.02 = 0.08
$$

$$
4 \\times 0.03 = 0.12
$$

Add the values:

$$
z_1 = 0.95 + 0.08 + 0.12 + 0.001
$$

$$
\\boxed{z_1 = 1.151}
$$

### 9.3 Step 2: Apply sigmoid activation to the hidden neuron

The sigmoid function is:

$$
\\boxed{\\sigma(z) = \\frac{1}{1 + e^{-z}}}
$$

Substitute:

$$
a_1 = \\frac{1}{1 + e^{-1.151}}
$$

Therefore:

$$
\\boxed{a_1 \\approx 0.7595}
$$

This is the activation produced by the hidden neuron.

**Important:** `0.7595` is not the final network prediction. It is the
hidden neuron's output, which is passed to the output neuron.

### 9.4 Step 3: Pass the hidden output to the output neuron

The lecture notes give:

$$
w_{h2} = 0.02
$$

$$
b_2 = 0.001
$$

The hidden-neuron output is:

$$
a_1 = 0.7595
$$

The output neuron's weighted input is:

$$
z_2 = a_1w_{h2} + b_2
$$

Substitute:

$$
z_2 = (0.7595)(0.02) + 0.001
$$

$$
z_2 = 0.01519 + 0.001
$$

Therefore:

$$
\\boxed{z_2 = 0.01619}
$$

> **Arithmetic clarification:** The handwritten notes appear to show
> `0.04518` for this calculation. With the displayed weight `0.02`,
> hidden activation `0.7595`, and bias `0.001`, the correct result is
> approximately `0.01619`.

### 9.5 Step 4: Apply sigmoid to the output neuron

The final output is:

$$
\\hat{y} = \\sigma(z_2)
$$

Substitute:

$$
\\hat{y} = \\frac{1}{1 + e^{-0.01619}}
$$

Therefore:

$$
\\boxed{\\hat{y} \\approx 0.5040}
$$

This is the final output of the network.

### 9.6 Complete forward propagation summary

  -------------------------------------------------------------------------------------------
  Stage                 Calculation                                                    Result
  --------------------- ---------------------------------------- ----------------------------
  Input                 `95, 4, 4`                                                      Given

  Hidden weighted sum   `95(0.01) + 4(0.02) + 4(0.03) + 0.001`                        `1.151`

  Hidden activation     `σ(1.151)`                                                   `0.7595`

  Output weighted sum   `0.7595(0.02) + 0.001`                                      `0.01619`

  Final activation      `σ(0.01619)`                                                 `0.5040`
  -------------------------------------------------------------------------------------------

### Forward propagation concept

$$
\\boxed{
\\text{Input}
\\rightarrow
\\text{Weighted Sum}
\\rightarrow
\\text{Activation}
\\rightarrow
\\text{Next Layer}
}
$$

The network calculates its final prediction by processing the input
through its layers.

------------------------------------------------------------------------

## 10. Perceptron vs. Sigmoid Neural Network

The perceptron activation function in the earlier section produces:

$$
y \\in \\{-1, 0, +1\\}
$$

The sigmoid forward-propagation example produces:

$$
0 < \\sigma(z) < 1
$$

These are different activation functions and different network examples.

  -----------------------------------------------------------------------
  Feature                 Perceptron in the notes Sigmoid neural network
  ----------------------- ----------------------- -----------------------
  Activation              Threshold function      Sigmoid

  Output                  `-1`, `0`, `+1`         Between `0` and `1`

  Typical use             Classification          Classification and
                                                  probability-like
                                                  outputs

  Training                Perceptron learning     Commonly
                          rule                    backpropagation

  Parameter updates       Perceptron correction   Gradient-based
                                                  optimization
  -----------------------------------------------------------------------

### Sigmoid function

$$
\\sigma(z) = \\frac{1}{1 + e^{-z}}
$$

Its output lies strictly between zero and one.

For binary classification, a threshold such as `0.5` can be used to
convert the sigmoid output into a predicted class. The threshold is a
classification decision rule; it is not part of the sigmoid function
itself.

------------------------------------------------------------------------

## 11. Decision Boundary and Linear Separability

A decision boundary separates different classes in the input feature
space.

For a standard binary perceptron, the decision boundary is:

$$
\\boxed{w_1x_1 + w_2x_2 + b = 0}
$$

For two input features, this equation represents a straight line.

For three input features, it represents a plane.

For higher-dimensional input spaces, it is called a hyperplane.

### 11.1 Numerical example

Suppose:

$$
w_1 = 2, \\qquad w_2 = 1, \\qquad b = -4
$$

The decision boundary is:

$$
2x_1 + x_2 - 4 = 0
$$

Rearrange:

$$
\\boxed{x_2 = 4 - 2x_1}
$$

The line divides the input feature space into two regions:

-   Positive region: `2x₁ + x₂ - 4 > 0`.
-   Negative region: `2x₁ + x₂ - 4 < 0`.

### 11.2 Three regions with a ternary threshold

For the ternary activation function, the two threshold boundaries are:

$$
w_1x_1 + w_2x_2 + b = \\theta
$$

and:

$$
w_1x_1 + w_2x_2 + b = -\\theta
$$

These boundaries create three regions:

-   Positive response region.
-   Neutral response region.
-   Negative response region.

### 11.3 Linear separability

A dataset is linearly separable if a straight line, plane, or hyperplane
can separate its classes without classification errors.

A classic single-layer perceptron cannot represent every possible
classification boundary.

For example, the XOR problem is not linearly separable. A single linear
perceptron cannot correctly classify all XOR patterns.

------------------------------------------------------------------------

## 12. Other Machine Learning Algorithms

The lecture notes also list several machine learning algorithms. These
are separate algorithms, not different types of perceptrons.

  -----------------------------------------------------------------------
  Algorithm                           Main purpose
  ----------------------------------- -----------------------------------
  Linear Regression                   Predict continuous numerical values

  Logistic Regression                 Classification

  Decision Tree                       Classification and regression using
                                      decision rules

  Random Forest                       Ensemble of decision trees

  Support Vector Machine (SVM)        Classification using decision
                                      boundaries

  K-Nearest Neighbours (KNN)          Classification or regression using
                                      nearest neighbours

  Gradient Boosting                   Sequentially combine weak learners

  Naive Bayes                         Probabilistic classification using
                                      Bayes' theorem
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 13. Important Formula Sheet

### 1. Net input

$$
y_{in} = b + \\sum_{i=1}^{n} w_i x_i
$$

### 2. Ternary activation

$$
f(y_{in}) =
\\begin{cases}
+1, & y_{in} > \\theta \\\\
0, & -\\theta \\leq y_{in} \\leq \\theta \\\\
-1, & y_{in} < -\\theta
\\end{cases}
$$

### 3. Perceptron weight update from the lecture notes

$$
w_i(new) = w_i(old) + \\alpha t x_i
$$

### 4. Perceptron bias update from the lecture notes

$$
b(new) = b(old) + \\alpha t
$$

### 5. Sigmoid activation

$$
\\sigma(z) = \\frac{1}{1 + e^{-z}}
$$

### 6. Forward propagation

$$
z = \\mathbf{w}^{T}\\mathbf{x} + b
$$

$$
a = \\sigma(z)
$$

### 7. Standard binary decision boundary

$$
\\mathbf{w}^{T}\\mathbf{x} + b = 0
$$

------------------------------------------------------------------------

## 14. Practice Questions

Try solving these questions before checking the answers.

### Question 1: Perceptron architecture

Which units form the three-stage perceptron architecture described in
the notes?

A. Input, hidden, output only\
B. Sensory, associator, response\
C. Encoder, decoder, output\
D. Input, memory, feedback

### Question 2: Net-input calculation

What is the net input if:

$$
x_1 = 2, \\quad x_2 = 3
$$

$$
w_1 = 0.5, \\quad w_2 = 0.2, \\quad b = 0.1
$$

A. `1.5`\
B. `1.7`\
C. `2.0`\
D. `0.7`

### Question 3: Ternary activation

For `θ = 2`, what is the activation output when:

$$
y_{in} = -3
$$

A. `+1`\
B. `0`\
C. `-1`\
D. `+2`

### Question 4: Perceptron learning

When does the perceptron update its parameters according to the notes?

A. Whenever an input is supplied\
B. Only when actual output differs from target\
C. Only when target is zero\
D. Never

### Question 5: Sigmoid activation

What range of values can the sigmoid function produce?

A. Only `-1` and `+1`\
B. Values strictly between `0` and `1`\
C. Only integers\
D. All real numbers

### Question 6: Linear separability

Can a classic single-layer perceptron solve XOR?

A. Yes, always\
B. No, because XOR is not linearly separable\
C. Only with zero bias\
D. Only with binary weights

### Question 7: Forward propagation

In the forward-pass example, what is the approximate hidden-neuron
activation?

A. `1.151`\
B. `0.7595`\
C. `0.01619`\
D. `0.5040`

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Click to reveal the answers and
explanations`</strong>`{=html}
```{=html}
</summary>
```
  --------------------------------------------------------------------------------------
  Question                Correct answer          Explanation
  ----------------------- ----------------------- --------------------------------------
  1                       B                       The three-stage architecture uses
                                                  sensory, associator, and response
                                                  units.

  2                       B                       `0.1 + (2 × 0.5) + (3 × 0.2) = 1.7`.

  3                       C                       `-3` is less than `-2`, so the output
                                                  is `-1`.

  4                       B                       An update occurs when the actual
                                                  output does not equal the target.

  5                       B                       Sigmoid outputs values strictly
                                                  between zero and one.

  6                       B                       XOR requires a nonlinear decision
                                                  boundary.

  7                       B                       `σ(1.151)` is approximately `0.7595`.
  --------------------------------------------------------------------------------------

```{=html}
</details>
```

------------------------------------------------------------------------

## Final Revision: Recommended Learning Order

Study these topics in the following sequence:

1.  Understand the perceptron architecture.
2.  Learn the role of sensory, associator, and response units.
3.  Practise net-input calculations.
4.  Understand the ternary activation function.
5.  Learn the perceptron weight and bias update rules.
6.  Solve numerical problems involving weight updates.
7.  Understand the complete training algorithm and its stopping
    condition.
8.  Study multiple-output perceptrons.
9.  Practise forward propagation with sigmoid activation.
10. Understand decision boundaries and linear separability.

These concepts form the foundation for understanding multilayer neural
networks, gradient-based optimization, and backpropagation.
