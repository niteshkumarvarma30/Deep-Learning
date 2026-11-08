# Linear Separability and Decision Boundary

## 1. Introduction

**Linear separability** describes whether two classes of data can be
separated by a single linear decision boundary.

For two input features, the boundary is a straight line. For three input
features, it is a plane. In higher-dimensional spaces, it is called a
hyperplane.

## 2. Linearly Separable Data

A dataset is linearly separable when a straight line can divide the two
classes without classification errors.

![Linearly separable data](images/linear_separable.png)

-   Points on one side belong to one class.
-   Points on the other side belong to the other class.
-   The straight line is the decision boundary.

## 3. Non-Linearly Separable Data: XOR

Consider the XOR dataset:

    x1   x2   Target
  ---- ---- --------
     0    0        0
     0    1        1
     1    0        1
     1    1        0

The positive points lie diagonally opposite each other. A single
straight line cannot separate the two classes.

![XOR pattern](images/xor_not_separable.png)

A network with an appropriate hidden layer and nonlinear activation can
represent the XOR function. A single linear decision boundary cannot.

## 4. Decision Boundary

A **decision boundary** separates regions of the input space that
receive different predictions.

For a neuron with input features x1 through xn, weights w1 through wn,
and bias b, the net input is:

$$
y_{in} = b + \sum_{i=1}^{n} x_i w_i
$$

The bias can be represented as an additional constant input:

$$
x_0 = 1,\qquad w_0 = b
$$

Therefore:

$$
y_{in} = x_0w_0 + x_1w_1 + \cdots + x_nw_n
$$

### Single-neuron diagram

![Single neuron with bias and weighted
inputs](images/single_neuron_bias.png)

For two input features:

$$
y_{in} = b + x_1w_1 + x_2w_2
$$

## 5. Bipolar Step Activation

The notes use a bipolar step activation function:

$$
f(y_{in}) =
\begin{cases}
+1, & y_{in} \geq 0 \\
-1, & y_{in} < 0
\end{cases}
$$

Thus:

-   If the net input is non-negative, the output is +1.
-   If the net input is negative, the output is -1.

The decision boundary is where the net input equals zero:

$$
y_{in} = 0
$$

For two input features:

$$
b + x_1w_1 + x_2w_2 = 0
$$

This equation represents a straight line.

## 6. Numerical Example: Find the Decision Boundary

Suppose:

$$
w_1 = 2,\qquad w_2 = 1,\qquad b = -4
$$

The net input is:

$$
y_{in} = -4 + 2x_1 + x_2
$$

### Step 1: Set the net input to zero

$$
-4 + 2x_1 + x_2 = 0
$$

Rearrange:

$$
x_2 = 4 - 2x_1
$$

This is the decision boundary.

### Step 2: Find the positive response region

For a positive response:

$$
y_{in} \geq 0
$$

Therefore:

$$
-4 + 2x_1 + x_2 \geq 0
$$

$$
x_2 \geq 4 - 2x_1
$$

### Step 3: Find the negative response region

For a negative response:

$$
y_{in} < 0
$$

Therefore:

$$
-4 + 2x_1 + x_2 < 0
$$

$$
x_2 < 4 - 2x_1
$$

![Decision boundary and positive and negative response
regions](images/decision_boundary_regions.png)

### Step 4: Test input points

    x1   x2   Net input   Bipolar output
  ---- ---- ----------- ----------------
     1    1          -1               -1
     1    3           1               +1
     2    1           1               +1
     2    0           0               +1
     0    2          -2               -1

For example, when x1 = 1 and x2 = 3:

$$
y_{in} = -4 + 2(1) + 3 = 1
$$

Since 1 is greater than or equal to zero, the output is +1.

**Boundary convention:** The activation function in these notes assigns
points exactly on the boundary (net input equal to zero) to the +1
class.

## 7. Decision Boundary: Line, Plane, and Hyperplane

The geometric form depends on the number of input features.

![Decision boundaries in one, two, and three
dimensions](images/boundary_dimensions.png)

-   **One input feature:** the boundary is a point on a number line.
-   **Two input features:** the boundary is a straight line.
-   **Three input features:** the boundary is a plane.
-   **More than three input features:** the boundary is a hyperplane.

The general equation is:

$$
b + \sum_{i=1}^{n} x_iw_i = 0
$$

## 8. Binary and Bipolar Data Representation

The notes distinguish between binary and bipolar representations.

### Binary representation

Binary values are:

$$
\{0,1\}
$$

-   0 represents OFF.
-   1 represents ON.

Example:

$$
X = [1,0,1]
$$

### Bipolar representation

Bipolar values are:

$$
\{-1,+1\}
$$

-   -1 represents OFF.
-   +1 represents ON.

The same pattern in bipolar form is:

$$
X = [+1,-1,+1]
$$

![Binary to bipolar representation](images/binary_bipolar.png)

### Why use bipolar representation?

The notes highlight that bipolar representation can distinguish an OFF
value from a missing or unknown value:

  Meaning                Binary representation   Bipolar representation
  -------------------- ----------------------- ------------------------
  ON                                         1                       +1
  OFF                                        0                       -1
  Missing or unknown         No separate value        0 can be reserved

**Practical note:** Using zero to mark missing data is a convention, not
a universal rule. In real machine-learning pipelines, missing values
need an explicit handling strategy.

## 9. How the Concepts Fit Together

1.  Input features are supplied to the neuron.
2.  Each feature is multiplied by its corresponding weight.
3.  The weighted inputs and bias are added.
4.  The activation function converts the net input into a class
    response.
5.  The decision boundary separates the positive and negative response
    regions.

The complete calculation is:

$$
y_{in} = b + \sum_{i=1}^{n} x_iw_i
$$

For the bipolar step activation:

$$
f(y_{in}) =
\begin{cases}
+1, & y_{in} \geq 0 \\
-1, & y_{in} < 0
\end{cases}
$$

## 10. Formula Sheet

  Concept                         Formula
  ------------------------------- -----------------------------
  Net input                       `y_in = b + sum(x_i * w_i)`
  Bias as an additional input     `x_0 = 1`, `w_0 = b`
  Decision boundary               `y_in = 0`
  Two-feature decision boundary   `b + x_1*w_1 + x_2*w_2 = 0`
  Positive response region        `y_in >= 0`
  Negative response region        `y_in < 0`
  Binary representation           `{0, 1}`
  Bipolar representation          `{-1, +1}`

## 11. Key Takeaways

-   Linear separability means that classes can be separated by one
    linear boundary.
-   XOR is not linearly separable.
-   A neuron's net input is the weighted sum plus bias.
-   The decision boundary occurs where the net input is zero.
-   In two dimensions, the boundary is a line; in three dimensions, it
    is a plane.
-   Binary data uses 0 and 1; bipolar data uses -1 and +1.
-   The bipolar step function shown here assigns a zero net input to the
    +1 class.
