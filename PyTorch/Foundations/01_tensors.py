import torch

print("=== 1. TENSORS ===")
# 1D Tensor (Vector)
x = torch.tensor([1.0, 2.0, 3.0])
# 2D Tensor (Matrix)
y = torch.tensor([[1, 2], 
                  [3, 4]])
print("1D Tensor x:\n", x)
print("2D Tensor y:\n", y)


print("\n=== 2. TENSOR SHAPES ===")
# Checking shapes
print("Shape of x:", x.shape) # Output: torch.Size([3])
print("Shape of y:", y.shape) # Output: torch.Size([2, 2])

# Reshaping a tensor using .view()
z = torch.tensor([1, 2, 3, 4, 5, 6])
z_reshaped = z.view(2, 3) 
print("z reshaped to 2x3:\n", z_reshaped)


print("\n=== 3. OPERATIONS ===")
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])

# Element-wise addition and multiplication
print("a + b =", a + b)
print("a * b =", a * b)

# Using mathematical functions (e.g., ReLU)
print("ReLU([-1.0, 5.0]) =", torch.relu(torch.tensor([-1.0, 5.0])))


print("\n=== 4. MATRIX MULTIPLICATION ===")
# Matrix A is 2x3 (2 rows, 3 columns)
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

# Matrix B is 3x2 (3 rows, 2 columns)
B = torch.tensor([[7, 8],
                  [9, 10],
                  [11, 12]])

# Matrix Multiplication using the @ operator
# (2x3) @ (3x2) -> Result should be (2x2)
C = A @ B

print("Matrix A @ B =\n", C)
print("Shape of result C:", C.shape)
