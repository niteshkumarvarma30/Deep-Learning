# Foundations: `nn.Module` and The Training Loop

In the previous sections, we did math manually. However, real neural networks have thousands or millions of parameters (weights and biases). PyTorch provides a dedicated Neural Network library called `torch.nn` to handle this automatically.

## 1. Building a Model with `nn.Module`
`nn.Module` is the base class for all neural network modules in PyTorch. Whenever you build a neural network, you must inherit from this class.

Instead of creating raw weight tensors, we use layers like `nn.Linear`. A Linear layer (also called a Dense or Fully Connected layer) automatically creates and manages the Weight matrix and Bias vector for you.

```python
import torch
import torch.nn as nn

# 1. We create a class that inherits from nn.Module
class SimpleNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        # 2. Define our layers
        # nn.Linear(input_features, output_features)
        # This automatically creates W and b for us!
        self.layer1 = nn.Linear(in_features=2, out_features=1)
        
    def forward(self, x):
        # 3. Define the Forward Pass
        # Pass the input x through the linear layer
        return self.layer1(x)

# Create an instance of our model
model = SimpleNetwork()

# Let's pass some dummy data through it!
dummy_input = torch.tensor([2.0, 3.0])
prediction = model(dummy_input)
print("Model Prediction:", prediction.item())
```

## 2. The Full Training Loop
To actually train a model so it learns, you need three components:
1. **The Model** (which we just built).
2. **A Loss Function** (e.g., `nn.MSELoss()`) to calculate the error between the prediction and the true answer.
3. **An Optimizer** (e.g., `torch.optim.SGD`) to update the weights based on the gradients.

A PyTorch training step **always** follows 5 specific steps.

```python
import torch.optim as optim

# 1. Define Loss and Optimizer
criterion = nn.MSELoss()  
# SGD = Stochastic Gradient Descent, lr = Learning Rate
optimizer = optim.SGD(model.parameters(), lr=0.01) 

# Let's pretend the correct answer is 10.0
target = torch.tensor([10.0]) 

# --- THE 5 STEPS OF TRAINING ---

# Step 1: Forward Pass (Make a prediction)
prediction = model(dummy_input)

# Step 2: Calculate the Loss (How wrong is the prediction?)
loss = criterion(prediction, target)
print("Loss before training:", loss.item())

# Step 3: Zero the Gradients 
# (PyTorch accumulates gradients by default, so we must clear them before every new pass)
optimizer.zero_grad()

# Step 4: Backward Pass (Calculate new gradients via Autograd)
loss.backward()

# Step 5: Update the Weights using the Optimizer
optimizer.step()

# ---
# If we test the model again, the loss will be slightly lower!
new_prediction = model(dummy_input)
new_loss = criterion(new_prediction, target)
print("Loss after 1 step of training:", new_loss.item())
```

If you wrap those 5 steps in a `for` loop (e.g., `for epoch in range(100):`), the network will rapidly learn and the loss will drop to nearly zero!
