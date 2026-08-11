import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ==========================================
# 1. DATA PREPARATION (Datasets & DataLoaders)
# ==========================================

# Transforms convert raw images into PyTorch Tensors and normalize pixel values (0 to 1)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)) # Mean and Std deviation for MNIST
])

# Download and load the Training Data
print("Loading Training Data...")
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Download and load the Testing (Validation) Data
print("Loading Testing Data...")
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# ==========================================
# 2. MODEL ARCHITECTURE (The CNN)
# ==========================================

class MNISTClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        # MNIST images are Grayscale (1 channel) and 28x28 pixels
        # Input: [Batch, 1, 28, 28]
        
        # Convolutional Block
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3) # Output: 16x26x26
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2) # Output: 16x13x13
        
        # Flattening
        self.flatten = nn.Flatten()
        
        # Fully Connected (Linear) Block
        # 16 channels * 13 height * 13 width = 2704
        self.fc1 = nn.Linear(in_features=2704, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=10) # 10 classes for digits 0-9
        
    def forward(self, x):
        # Feature Extraction
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        
        # Classification
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        out = self.fc2(x)
        return out

# Initialize model, loss function, and optimizer
model = MNISTClassifier()
criterion = nn.CrossEntropyLoss() # Used for multi-class classification
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ==========================================
# 3. TRAINING AND VALIDATION LOOP
# ==========================================

epochs = 3

for epoch in range(epochs):
    # --- TRAINING PHASE ---
    model.train() # Set model to training mode
    total_train_loss = 0
    
    for batch_idx, (images, labels) in enumerate(train_loader):
        # 1. Forward Pass
        predictions = model(images)
        loss = criterion(predictions, labels)
        
        # 2. Backward Pass & Optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_train_loss += loss.item()
        
        if batch_idx % 200 == 0:
            print(f"Epoch {epoch+1}/{epochs} | Batch {batch_idx}/{len(train_loader)} | Loss: {loss.item():.4f}")
            
    avg_train_loss = total_train_loss / len(train_loader)
    print(f"--- Epoch {epoch+1} Complete. Avg Train Loss: {avg_train_loss:.4f} ---")
    
    # --- VALIDATION PHASE ---
    # We test the model on unseen data to see how accurate it is!
    model.eval() # Set model to evaluation mode (turns off dropout/batchnorm updates)
    correct_predictions = 0
    total_samples = 0
    
    # torch.no_grad() disables Autograd. We don't need gradients for testing, saving memory!
    with torch.no_grad():
        for images, labels in test_loader:
            predictions = model(images)
            
            # Get the index of the highest probability (the predicted digit)
            _, predicted_classes = torch.max(predictions, dim=1)
            
            # Count how many predictions match the true labels
            total_samples += labels.size(0)
            correct_predictions += (predicted_classes == labels).sum().item()
            
    accuracy = (correct_predictions / total_samples) * 100
    print(f">>> Validation Accuracy: {accuracy:.2f}% <<<\n")

# ==========================================
# 4. SAVING THE MODEL
# ==========================================
# Save the trained weights to a file so we can load it later without retraining
torch.save(model.state_dict(), "mnist_cnn.pth")
print("Model saved successfully as 'mnist_cnn.pth'!")
