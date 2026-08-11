# Project: End-to-End MNIST Classifier

This folder contains a complete, production-ready script for training a Convolutional Neural Network (CNN) in PyTorch. 

While the previous phases covered the architecture of PyTorch models, this script introduces the missing pieces required to build full AI projects:
1. **Data Loading:** Using `torchvision.datasets` and `DataLoader`.
2. **Validation Loops:** Using `model.eval()` and `torch.no_grad()` to test the model on unseen data.
3. **Model Saving:** Using `torch.save()` to save the trained weights.

## How to Run
Ensure you have PyTorch and Torchvision installed. Then simply run the script:

```bash
python mnist_cnn.py
```

## What the Script Does
1. **Downloads MNIST:** It automatically downloads 60,000 training images and 10,000 testing images of handwritten digits (0-9).
2. **Builds the CNN:** It initializes the exact CNN architecture we learned in Phase 3.
3. **Trains for 3 Epochs:** It loops over the training data 3 times, updating weights using Backpropagation and the Adam Optimizer.
4. **Calculates Accuracy:** After every epoch, it freezes the gradients and tests the model on the 10,000 testing images, printing out the final Accuracy percentage (usually ~98%).
5. **Saves the Model:** It exports the trained weights to `mnist_cnn.pth`.
