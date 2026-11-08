# Hebbian Network, Hebb's Learning Rule, and Types of Learning in ANN

## Table of Contents

1.  [Hebbian Network](#part-1-hebbian-network)
2.  [Hebb's Learning Rule](#2-hebbs-learning-rule)
3.  [Bipolar vs. Binary
    Data](#3-why-is-hebbian-learning-more-suitable-for-bipolar-data)
4.  [Hebbian Training
    Algorithm](#part-2-hebbian-network-training-algorithm)
5.  [Complete Numerical
    Example](#6-complete-numerical-example-hebbian-training)
6.  [Types of
    Learning](#part-3-types-of-learning-in-artificial-neural-networks)
7.  [Supervised Learning](#10-supervised-learning)
8.  [Unsupervised and Reinforcement Learning](#12-unsupervised-learning)
9.  [Comparison and
    Revision](#14-difference-between-the-three-learning-types)
10. [Practice Questions](#17-practice-questions)

------------------------------------------------------------------------

# Part 1. Hebbian Network

## 1. What Is a Hebbian Network?

The Hebbian network is based on a learning principle proposed by
**Donald Hebb in 1949**.

The central idea is:

> When two interconnected neurons are activated together repeatedly, the
> connection strength between them increases.

In simple language: **neurons that fire together strengthen their
connection.**

This principle is inspired by biological learning in the human brain. A
biological synapse is the junction through which neurons communicate. In
an artificial neural network, the strength of a connection is
represented by a **weight**.

  Biological neural network   Artificial neural network
  --------------------------- ---------------------------
  Neuron                      Artificial neuron
  Synaptic connection         Connection
  Synaptic strength           Weight
  Strengthening of synapse    Increase in weight

## 2. Hebb's Learning Rule

According to Hebb's rule, the weight vector increases proportionately to
the product of the input and the learning signal. In the training
procedure described in these notes, the learning signal is equal to the
neuron's output.

The weight-update equation is:

$$
w_i(\\text{new}) = w_i(\\text{old}) + x_i y
$$

Where:

-   $w_i(\\text{old})$ = previous weight.
-   $w_i(\\text{new})$ = updated weight.
-   $x_i$ = activation of input neuron $i$.
-   $y$ = output or learning signal.

The weight change is:

$$
\\boxed{\\Delta w_i = x_i y}
$$

### 2.1 Possible combinations for bipolar data

For bipolar values, $x_i,y\\in\\{-1,+1\\}$.

    Input $x_i$   Output $y$   Product $x_i y$ Weight effect
  ------------- ------------ ----------------- ------------------
             +1           +1                +1 Weight increases
             +1           -1                -1 Weight decreases
             -1           +1                -1 Weight decreases
             -1           -1                +1 Weight increases

### 2.2 Numerical example

Suppose $w_{old}=0$, $x=+1$, and $y=+1$.

$$
w_{new}=w_{old}+xy
$$

$$
w_{new}=0+(1)(1)=1
$$

Therefore, $\\boxed{w_{new}=1}$.

Now suppose $x=+1$ and $y=-1$:

$$
w_{new}=0+(1)(-1)=-1
$$

The weight decreases.

## 3. Why Is Hebbian Learning More Suitable for Bipolar Data?

The notes state that Hebb's rule is more suitable for bipolar data than
binary data.

### 3.1 Binary representation

Binary values are $\\{0,1\\}$:

-   ON = 1
-   OFF = 0

The Hebbian update is $\\Delta w=xy$.

**Case 1: Input ON, target OFF**

$$
x=1,\\quad y=0,\\quad \\Delta w=1\\times0=0
$$

**Case 2: Input OFF, target OFF**

$$
x=0,\\quad y=0,\\quad \\Delta w=0\\times0=0
$$

Both conditions produce the same update.

### 3.2 Bipolar representation

Bipolar values are $\\{-1,+1\\}$:

-   ON = +1
-   OFF = -1

**Case 1: Input ON, target OFF**

$$
x=+1,\\quad y=-1,\\quad \\Delta w=(+1)(-1)=-1
$$

**Case 2: Input OFF, target OFF**

$$
x=-1,\\quad y=-1,\\quad \\Delta w=(-1)(-1)=+1
$$

The two conditions now produce different updates.

  Training condition        Binary update   Bipolar update
  ----------------------- --------------- ----------------
  Input ON, target OFF                  0               -1
  Input OFF, target OFF                 0               +1

**Key takeaway:** Bipolar representation allows Hebb's multiplication
rule to distinguish these two conditions.

------------------------------------------------------------------------

# Part 2. Hebbian Network Training Algorithm

## 4. Purpose of the Training Algorithm

The training algorithm calculates and adjusts weights and bias. It
specifies:

1.  How to initialize weights.
2.  How to provide input patterns.
3.  How to provide the learning signal.
4.  How to update weights and bias.

The flow is: start → initialize weights → process each training pair →
activate input units → set output learning signal → update weights and
bias → continue until all pairs are processed.

## 5. Step-by-Step Hebbian Training Algorithm

### Step 0: Initialize weights and bias

Initialize all weights to zero:

$$
w_i=0,\\qquad i=1,2,\\ldots,n
$$

Here, $n$ is the total number of input neurons. Initialize the bias to
zero as well:

$$
b=0
$$

For two input neurons, initially $w_1=0$, $w_2=0$, and $b=0$.

### Step 1: Process each training input-output pair

Steps 2 to 4 are performed for each input training vector and target
output pair.

Example training dataset:

  Pattern   Input vector $X$     Target $t$
  --------- ------------------ ------------
  P1        \[+1, +1\]                   +1
  P2        \[+1, -1\]                   -1
  P3        \[-1, +1\]                   -1

The network processes each pair sequentially and carries the updated
weights forward.

### Step 2: Activate the input units

The input layer generally uses the identity function, so it passes the
supplied input values forward unchanged:

$$
\\boxed{x_i=s_i}
$$

Here, $s_i$ is the supplied input and $x_i$ is the input-neuron
activation.

For $X=[+1,-1]$, we have $x_1=+1$ and $x_2=-1$.

### Step 3: Activate the output unit

In the training procedure shown in the notes, the output-unit activation
is set to the target:

$$
\\boxed{y=t}
$$

Here, $t$ is the desired target output, and $y$ is the learning signal
used by the Hebbian update.

**Important:** In this particular procedure, the target is used directly
as the learning signal. This is not the same as calculating a prediction
and comparing it with the target using a loss function.

### Step 4: Update weights and bias

Weight update:

$$
\\boxed{w_i(\\text{new})=w_i(\\text{old})+x_i y}
$$

Bias update:

$$
\\boxed{b(\\text{new})=b(\\text{old})+y}
$$

Therefore:

$$
\\Delta w_i=x_i y,\\qquad \\Delta b=y
$$

These steps are repeated for every training pair.

## 6. Complete Numerical Example: Hebbian Training

Suppose the network has two input neurons and one output neuron. Use
bipolar inputs, with initial weights and bias equal to zero.

Training dataset:

  Pattern     $x_1$   $x_2$   Target $t$
  --------- ------- ------- ------------
  P1             +1      +1           +1
  P2             +1      -1           -1
  P3             -1      +1           -1

Learning rules:

$$
w_i(\\text{new})=w_i(\\text{old})+x_i y
$$

$$
b(\\text{new})=b(\\text{old})+y,\\qquad y=t
$$

### Initial values

$$
w_1=0,\\quad w_2=0,\\quad b=0
$$

### Pattern 1: $X=[+1,+1]$, target $t=+1$

Set $x_1=+1$, $x_2=+1$, and $y=+1$.

First weight:

$$
w_1(new)=0+(1)(1)=1
$$

Second weight:

$$
w_2(new)=0+(1)(1)=1
$$

Bias:

$$
b(new)=0+1=1
$$

After P1:

$$
\\boxed{w_1=1,\\quad w_2=1,\\quad b=1}
$$

### Pattern 2: $X=[+1,-1]$, target $t=-1$

Use the updated values from P1: $w_1=1$, $w_2=1$, $b=1$.

Set $x_1=+1$, $x_2=-1$, and $y=-1$.

First weight:

$$
w_1(new)=1+(1)(-1)=0
$$

Second weight:

$$
w_2(new)=1+(-1)(-1)=2
$$

Bias:

$$
b(new)=1+(-1)=0
$$

After P2:

$$
\\boxed{w_1=0,\\quad w_2=2,\\quad b=0}
$$

### Pattern 3: $X=[-1,+1]$, target $t=-1$

Use the updated values from P2: $w_1=0$, $w_2=2$, $b=0$.

Set $x_1=-1$, $x_2=+1$, and $y=-1$.

First weight:

$$
w_1(new)=0+(-1)(-1)=1
$$

Second weight:

$$
w_2(new)=2+(1)(-1)=1
$$

Bias:

$$
b(new)=0+(-1)=-1
$$

After P3:

$$
\\boxed{w_1=1,\\quad w_2=1,\\quad b=-1}
$$

### Final weights and bias

$$
\\boxed{\\mathbf{w}=[1,1],\\qquad b=-1}
$$

### Complete update summary

  Pattern     $w_1$ after update   $w_2$ after update   Bias
  --------- -------------------- -------------------- ------
  Initial                      0                    0      0
  P1                           1                    1      1
  P2                           0                    2      0
  P3                           1                    1     -1

**Important:** Weights are updated sequentially. They are not restarted
from zero for each new training pattern.

## 7. Vector-Form Weight Update

For multiple inputs, the weight changes can be written in vector form:

$$
\\boxed{\\Delta\\mathbf{w}=y\\mathbf{x}}
$$

The updated vector is:

$$
\\boxed{\\mathbf{w}(new)=\\mathbf{w}(old)+\\Delta\\mathbf{w}}
$$

Example:

$$
\\mathbf{x}=[1,-1],\\qquad y=1
$$

$$
\\Delta\\mathbf{w}=1[1,-1]=[1,-1]
$$

The first weight increases by 1, and the second weight decreases by 1.

## 8. Applications of Hebbian Learning

Hebbian learning can be used for:

1.  **Pattern association:** Learning relationships between patterns.
2.  **Pattern categorization:** Grouping patterns based on learned
    relationships.
3.  **Pattern classification:** Associating inputs with output
    categories.

The common principle is that connection weights are modified according
to the relationship between input and output activity.

------------------------------------------------------------------------

# Part 3. Types of Learning in Artificial Neural Networks

## 9. What Is Learning?

Learning is a process of acquiring knowledge. In artificial neural
networks, learning means adjusting network parameters based on
information from data or interaction with an environment.

The three broad categories are:

1.  Supervised Learning.
2.  Unsupervised Learning.
3.  Reinforcement Learning.

## 10. Supervised Learning

In supervised learning, the network receives:

-   Input data.
-   Desired output, also called the target.

The network calculates its actual output and compares it with the
desired output.

An analogy is a child learning from parents and teachers: the child
receives guidance and feedback about whether an answer or action is
correct.

### 10.1 How supervised learning works

**Step 1: Provide input**

$$
X=[x_1,x_2,\\ldots,x_n]
$$

**Step 2: Calculate actual output**

$$
\\boxed{\\hat{y}=f(X;W,b)}
$$

Here, $\\hat{y}$ is the predicted output.

**Step 3: Compare actual and desired output**

The target is $y_{target}$. The network compares $y_{target}$ with
$\\hat{y}$.

**Step 4: Generate an error signal**

For a simple example:

$$
y_{target}=1,\\qquad \\hat{y}=0.6
$$

$$
e=y_{target}-\\hat{y}=1-0.6=0.4
$$

**Step 5: Adjust weights**

The error signal is used to adjust weights so that future predictions
become closer to the desired output. This process continues during
training.

### 10.2 Supervised-learning flow

1.  Input data is passed to the neural network.
2.  The network produces a predicted output.
3.  The prediction is compared with the target.
4.  An error or loss is calculated.
5.  The training algorithm updates weights and biases.
6.  The process repeats over training examples.

### 10.3 Numerical example: Cat classification

Suppose a neural network is trained to identify cats.

  Input image     Target
  ------------- --------
  Cat image            1
  Dog image            0
  Cat image            1
  Dog image            0

For a cat image, the target is 1. Suppose the network predicts 0.3. A
loss function measures the difference, and the training algorithm
updates weights to improve future predictions.

**Important:** The actual weight-update method depends on the network.
Modern neural networks typically use backpropagation and gradient-based
optimization.

## 11. Types of Supervised-Learning Models

### 11.1 Perceptron Network

The perceptron is a simple trainable artificial neuron used for binary
classification.

It calculates:

$$
y_{in}=b+\\sum_i x_iw_i
$$

It uses a threshold activation function and updates weights based on
classification errors.

### 11.2 ADALINE (Adaptive Linear Neuron)

ADALINE stands for **Adaptive Linear Neuron**. It uses a linear
activation during learning and adjusts weights using the difference
between the target and the linear output.

A commonly used learning method is the **Least Mean Squares (LMS)
rule**.

### 11.3 MADALINE (Multiple ADALINE)

MADALINE stands for **Multiple Adaptive Linear Neurons**. It combines
multiple ADALINE units to solve more complex classification problems.

### 11.4 Radial Basis Function (RBF) Network

An RBF network uses radial basis functions in its hidden layer. It
measures how close an input is to particular centers in the feature
space.

RBF networks can be used for classification and function approximation.

## 12. Unsupervised Learning

In unsupervised learning, the network receives input data without
corresponding target labels.

The objective is to discover patterns, structures, or groups within the
data.

**Example: Customer segmentation**

An e-commerce company may have customer purchase data without predefined
customer categories. An unsupervised algorithm can group customers based
on purchasing behavior.

Examples:

-   K-Means clustering.
-   Hierarchical clustering.
-   Self-Organizing Maps (SOM).

## 13. Reinforcement Learning

In reinforcement learning, an agent learns by interacting with an
environment.

It receives:

-   Rewards for desirable actions.
-   Penalties for undesirable actions.

The objective is to learn a policy that maximizes cumulative reward.

**Example: Robot navigation**

-   Moving toward the destination: positive reward.
-   Hitting an obstacle: negative reward.
-   Reaching the destination: large positive reward.

Examples include Q-Learning and Deep Q-Networks (DQN).

## 14. Difference Between the Three Learning Types

  -----------------------------------------------------------------------
  Feature           Supervised        Unsupervised      Reinforcement
                    learning          learning          learning
  ----------------- ----------------- ----------------- -----------------
  Training data     Labeled           Unlabeled         Interaction with
                                                        environment

  Target output     Available         Not provided      Rewards guide
                                                        learning

  Feedback          Target and        No direct target  Rewards or
                    prediction        feedback          penalties
                    comparison                          

  Main objective    Learn             Discover hidden   Maximize
                    input-output      patterns          cumulative reward
                    mapping                             

  Example           Classification    Clustering        Robot navigation
  -----------------------------------------------------------------------

## 15. Hebbian Learning vs. Supervised Learning

A common question is:

**If Hebbian learning uses an input-output pair, is it also supervised
learning?**

The answer requires a distinction.

The basic biological Hebbian principle is commonly associated with
unsupervised, correlation-based learning.

However, the specific algorithm in these notes sets the output unit to
the target:

$$
y=t
$$

and updates weights using:

$$
w_i(new)=w_i(old)+x_i t
$$

This is a target-driven Hebbian learning procedure.

  -----------------------------------------------------------------------
  Feature                 Hebbian algorithm in    Modern supervised
                          these notes             learning
  ----------------------- ----------------------- -----------------------
  Input                   Given                   Given

  Target                  Used as learning signal Given

  Output                  Set to target in this   Calculated prediction
                          Hebbian procedure       

  Weight update           $w_i+x_i y$             Gradient-based update

  Loss function           Not required by this    Commonly used
                          Hebbian rule            

  Backpropagation         Not required            Used in standard
                                                  multilayer
                                                  neural-network training
  -----------------------------------------------------------------------

The word "output" can mean different things in different learning
algorithms.

------------------------------------------------------------------------

# 16. Final Revision Sheet

## Hebbian Network

**Main principle:** Neurons that fire together strengthen their
connection.

**Hebbian weight update:**

$$
\\boxed{w_i(new)=w_i(old)+x_i y}
$$

**Hebbian bias update:**

$$
\\boxed{b(new)=b(old)+y}
$$

**Vector form:**

$$
\\boxed{\\Delta\\mathbf{w}=y\\mathbf{x}}
$$

## Hebbian Training Algorithm

1.  Initialize weights and bias to zero.
2.  Activate input units: $x_i=s_i$.
3.  Set output learning signal: $y=t$.
4.  Update weights and bias.
5.  Repeat for every training pair.

## Supervised Learning

$$
\\text{Input}\\rightarrow\\text{Prediction}
$$

$$
\\text{Prediction vs. Target}\\rightarrow\\text{Error}
$$

$$
\\text{Error}\\rightarrow\\text{Parameter updates}
$$

## Three Learning Types

  Learning type   Main idea
  --------------- -------------------------------------
  Supervised      Learn from labeled examples
  Unsupervised    Discover patterns in unlabeled data
  Reinforcement   Learn through rewards and penalties

------------------------------------------------------------------------

# 17. Practice Questions

Try solving these questions after studying the concepts.

### Question 1

According to Hebb's rule, what happens when two interconnected bipolar
neurons are both active (+1)?

A. Weight decreases.

B. Weight increases.

C. Weight becomes zero.

D. Bias is removed.

**Answer: B. Weight increases.**

Explanation:

$$
(+1)\\times(+1)=+1
$$

Therefore, the weight increases.

### Question 2

What is the updated weight if:

$$
x=-1,\\quad y=+1,\\quad w_{old}=3
$$

**Solution:**

$$
w_{new}=w_{old}+xy
$$

$$
w_{new}=3+(-1)(+1)
$$

$$
\\boxed{w_{new}=2}
$$

### Question 3

In the Hebbian training algorithm shown in the notes, what is assigned
to the output unit?

A. The initial weight.

B. The bias.

C. The target value $t$.

D. The prediction error.

**Answer: C. The target value $t$.**

Explanation:

$$
y=t
$$

### Question 4

Which learning method uses rewards and penalties?

A. Supervised learning.

B. Unsupervised learning.

C. Reinforcement learning.

D. Hebbian learning.

**Answer: C. Reinforcement learning.**

### Question 5

Which learning rule is commonly associated with ADALINE?

A. LMS learning rule.

B. K-Means.

C. Q-Learning.

D. Decision tree.

**Answer: A. LMS learning rule.**

------------------------------------------------------------------------

## 18. Key Takeaways

-   Hebbian learning is based on strengthening connections when neurons
    are activated together.
-   The Hebbian weight update depends on the product of input activity
    and output learning signal.
-   Bipolar representation distinguishes ON and OFF states using +1 and
    -1.
-   The Hebbian training procedure in these notes initializes weights
    and bias to zero.
-   Each training pair updates the current weights and bias
    sequentially.
-   The output learning signal is set to the target in the specified
    Hebbian algorithm.
-   Supervised learning uses labeled examples and compares predictions
    with targets.
-   Unsupervised learning discovers patterns without target labels.
-   Reinforcement learning uses rewards and penalties to guide an
    agent's behavior.
-   Perceptron, ADALINE, MADALINE, and RBF networks are examples of
    neural-network models discussed in the supervised-learning section.
