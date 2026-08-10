# Phase 2: Artificial Neural Networks (ANN)

In your theoretical notes, you learned that an Artificial Neural Network is built by connecting multiple perceptrons together. In PyTorch, a Perceptron layer is created using `nn.Linear`. A Multi-Layer Perceptron (MLP) is formed by stacking these `nn.Linear` layers with Activation Functions in between.

## 1. Multi-Layer Perceptron Architecture
When we define an MLP in PyTorch, we inherit from `nn.Module`.
We define our layers in the `__init__` function and dictate how data flows through them in the `forward` function.

```python
import torch
import torch.nn as nn

class MultiLayerPerceptron(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        
        # Layer 1: Input to Hidden (Extracts patterns from the input)
        self.hidden_layer = nn.Linear(input_size, hidden_size)
        
        # Layer 2: Hidden to Output (Makes the final prediction)
        self.output_layer = nn.Linear(hidden_size, output_size)
        
        # Activation Function (ReLU adds non-linearity so the network can learn complex patterns)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        # 1. Pass input through hidden layer
        x = self.hidden_layer(x)
        # 2. Apply activation function
        x = self.relu(x)
        # 3. Pass through output layer
        out = self.output_layer(x)
        return out

# Initialize the model with custom sizes
# Here we take 4 inputs, route them through 10 hidden neurons, and output 1 prediction value.
model = MultiLayerPerceptron(input_size=4, hidden_size=10, output_size=1)

print(model)
```

## 2. Viewing the Architecture
If you print the `model`, PyTorch beautifully summarizes the architecture exactly as it was built:

```text
MultiLayerPerceptron(
  (hidden_layer): Linear(in_features=4, out_features=10, bias=True)
  (output_layer): Linear(in_features=10, out_features=1, bias=True)
  (relu): ReLU()
)
```
Notice that `bias=True` is the default. PyTorch automatically adds a bias vector to every `nn.Linear` layer unless you explicitly tell it not to (`bias=False`).

With this architecture and the Training Loop from Phase 1, you have everything you need to train a standard Artificial Neural Network!
