# Foundations: Tensors and Matrix Multiplication

In PyTorch, everything revolves around the **Tensor**. A tensor is a generalization of scalars, vectors, and matrices to higher dimensions. It is essentially a grid of numbers. PyTorch tensors are similar to NumPy arrays, but with the added superpower that they can run on GPUs and track gradients.

## 1. Tensors
Here is how we create basic 1D and 2D tensors in PyTorch.

```python
import torch

# 1D Tensor (Vector) - A line of numbers
x = torch.tensor([1.0, 2.0, 3.0])

# 2D Tensor (Matrix) - A grid with rows and columns
y = torch.tensor([[1, 2], 
                  [3, 4]])

print("1D Tensor x:\n", x)
print("2D Tensor y:\n", y)
```

## 2. Tensor Shapes
The `shape` of a tensor is crucial. It tells you exactly how many dimensions exist and how many elements are in each dimension. In Deep Learning, a "Shape Mismatch" is the most common error you will encounter.

```python
# Checking shapes
print("Shape of x:", x.shape) # Output: torch.Size([3]) -> 3 elements in 1 dimension
print("Shape of y:", y.shape) # Output: torch.Size([2, 2]) -> 2 rows, 2 columns

# Reshaping a tensor using .view()
# We take a 1D tensor of 6 elements and reshape it into a 2x3 matrix
z = torch.tensor([1, 2, 3, 4, 5, 6])
z_reshaped = z.view(2, 3) 
print("z reshaped to 2x3:\n", z_reshaped)
```

## 3. Operations
PyTorch tensors support all standard mathematical operations. These operations are performed element-wise by default.

```python
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])

# Element-wise addition and multiplication
print("a + b =", a + b)  # Output: tensor([4., 6.])
print("a * b =", a * b)  # Output: tensor([3., 8.])

# Applying mathematical functions (e.g., ReLU activation)
# ReLU turns negative numbers to 0, and keeps positive numbers unchanged.
print("ReLU([-1.0, 5.0]) =", torch.relu(torch.tensor([-1.0, 5.0])))
```

## 4. Matrix Multiplication
Unlike element-wise multiplication (`*`), Matrix Multiplication (`@` or `torch.matmul()`) computes the dot product of rows and columns.
**The Golden Rule of Shapes:** To multiply Matrix A by Matrix B, the number of columns in A must equal the number of rows in B.
`(M x N) @ (N x P) = Result (M x P)`

```python
# Matrix A is 2x3 (2 rows, 3 columns)
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

# Matrix B is 3x2 (3 rows, 2 columns)
B = torch.tensor([[7, 8],
                  [9, 10],
                  [11, 12]])

# Matrix Multiplication using the @ operator
# We are doing (2x3) @ (3x2), so the result will be (2x2)
C = A @ B

print("Matrix A @ B =\n", C)
print("Shape of result C:", C.shape)
```
