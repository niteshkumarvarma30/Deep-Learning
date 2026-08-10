# Foundations: Autograd and Backpropagation

To train a Neural Network, you need to calculate gradients (derivatives) so you know how to update your weights to reduce the error. Calculating derivatives by hand using the Chain Rule is extremely tedious. PyTorch solves this using **Autograd** (Automatic Differentiation).

## 1. Computational Graphs and `requires_grad=True`
When you create a tensor in PyTorch, you can tell PyTorch to "track" it by setting `requires_grad=True`. PyTorch will then silently build a **Computational Graph** in the background, recording every mathematical operation that happens to that tensor.

Usually, you only set `requires_grad=True` for your model's **Weights** and **Biases**, because those are the parameters the network needs to learn and update. Input data does not need gradients.

```python
import torch

# This is our "Weight" tensor. 
# We tell PyTorch: "Track this! We will need its gradient later."
w = torch.tensor([2.0], requires_grad=True)

# This is our Input data (we don't need to track inputs)
x = torch.tensor([3.0])

# Forward Pass: We do some math
# Under the hood, PyTorch builds a graph: x and w multiply to create y.
y = w * x  # y = 2 * 3 = 6
print("Output y:", y)
```

## 2. Backpropagation with `.backward()`
Once you have computed your final output (which in a real scenario would be your Loss or Error), you can calculate the gradients for every single tracked tensor in the entire graph with one command: `.backward()`.

This fires the Chain Rule backwards through the computational graph. It calculates how much each weight contributed to the final output, and stores that gradient inside the weight tensor's `.grad` attribute.

```python
# 1. Trigger Backpropagation
# This calculates dy/dw
y.backward()

# 2. Look at the gradient (derivative) stored inside 'w'
print("Gradient of w (dy/dw):", w.grad) 

# Why is it 3.0?
# The equation is y = w * x
# The derivative of y with respect to w is x.
# Since x = 3.0, the gradient is exactly 3.0!
```

## Summary of a Training Step
When you eventually build a real neural network, the training loop will always follow this exact structure:
1. **Forward pass:** Pass data through the model to calculate the output and Loss.
2. **Backward pass:** Call `loss.backward()` to calculate the gradients for all weights.
3. **Weight Update:** An Optimizer looks at all the `.grad` values and updates the weights slightly to lower the loss.
4. **Zero Gradients:** Clear the gradients for the next loop so they don't add up!
