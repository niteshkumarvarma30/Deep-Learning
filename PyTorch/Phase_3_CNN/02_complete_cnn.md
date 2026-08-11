# Phase 3: The Complete CNN Architecture

Now that we understand how Convolutions and Pooling extract features from images, we must connect them to a final classifier (an MLP from Phase 2) to actually make predictions!

## 1. Flattening (`nn.Flatten`)
The output of a convolutional/pooling block is a 3D tensor (e.g., `16 Channels x 15 Height x 15 Width`). 
However, standard linear layers (`nn.Linear`) only accept **1D flat vectors**.

We use `nn.Flatten()` to crush this 3D box of numbers into a single straight line.

```python
import torch.nn as nn
import torch

# Assume pooled_maps is shape [1, 16, 15, 15]
# (1 image, 16 channels, 15x15 pixels)
pooled_maps = torch.randn(1, 16, 15, 15)

flatten = nn.Flatten()
flat_vector = flatten(pooled_maps)

print("Flattened Shape:", flat_vector.shape)
# Output: torch.Size([1, 3600])
# 16 * 15 * 15 = 3600 total numbers!
```

## 2. The Complete CNN Model
A standard CNN architecture always follows this pattern:
**Feature Extraction (Conv $\rightarrow$ ReLU $\rightarrow$ Pool)** $\rightarrow$ **Flatten** $\rightarrow$ **Classification (Linear $\rightarrow$ ReLU $\rightarrow$ Linear)**

Let's build a complete PyTorch model that takes a `3x32x32` color image and predicts which of 10 classes (like digits 0-9) it belongs to.

```python
import torch
import torch.nn as nn

class CompleteCNN(nn.Module):
    def __init__(self):
        super().__init__()
        
        # 1. Feature Extractor (CNN Block)
        # Input: 3x32x32 -> Output: 16x30x30
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
        self.relu = nn.ReLU()
        
        # Input: 16x30x30 -> Output: 16x15x15
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # 2. Flatten Layer
        self.flatten = nn.Flatten()
        
        # 3. Classifier (MLP Block)
        # Because our math told us the output of pool1 is 16*15*15 = 3600
        # The input to the first linear layer MUST be 3600.
        self.fc1 = nn.Linear(in_features=3600, out_features=128) 
        self.fc2 = nn.Linear(in_features=128, out_features=10) # 10 final classes
        
    def forward(self, x):
        # Pass through CNN Feature Extractor
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool1(x)
        
        # Flatten the 3D tensor into a 1D vector
        x = self.flatten(x)
        
        # Pass through the MLP Classifier
        x = self.fc1(x)
        x = self.relu(x)
        out = self.fc2(x)
        
        return out

# Let's test our complete model!
cnn_model = CompleteCNN()
dummy_image = torch.randn(1, 3, 32, 32)
prediction = cnn_model(dummy_image)

print("Final Prediction Shape:", prediction.shape)
# Output: torch.Size([1, 10]) -> 10 probabilities for 10 classes!
```

With this complete model, you can use the exact same Training Loop from Phase 1 to train it on real images!
