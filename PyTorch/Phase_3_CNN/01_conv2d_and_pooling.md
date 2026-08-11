# Phase 3: Convolutional Neural Networks (CNN)

While Artificial Neural Networks (ANNs) process 1D vectors of data, Convolutional Neural Networks (CNNs) are specifically designed to process 2D spatial data like Images. 

## 1. Image Tensors (B, C, H, W)
In PyTorch, images must always be formatted in a specific 4D tensor shape:
`[Batch Size, Channels, Height, Width]`

- **Batch Size:** How many images are being processed simultaneously.
- **Channels:** The color depth (1 for Grayscale, 3 for RGB Color).
- **Height & Width:** The pixel dimensions of the image.

```python
import torch

# Create a dummy image tensor
# 1 Image, 3 Color Channels (RGB), 32x32 pixels
dummy_image = torch.randn(1, 3, 32, 32)
print("Image Shape:", dummy_image.shape)
```

## 2. The Convolutional Layer (`nn.Conv2d`)
A convolutional layer acts like a "flashlight" scanning over the image. This flashlight is called a **Filter** (or Kernel). 
- It slides across the image to look for specific patterns (like horizontal edges, corners, or colors).
- If we use 16 different filters, the layer outputs 16 "Feature Maps" showing exactly where in the image those 16 patterns were found.

```python
import torch.nn as nn

# in_channels = 3 (Because our input is RGB)
# out_channels = 16 (We want to apply 16 different filters)
# kernel_size = 3 (Our flashlight is a 3x3 pixel grid)
conv_layer = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)

# Pass the image through the layer
feature_maps = conv_layer(dummy_image)

print("Feature Maps Shape:", feature_maps.shape)
# Output: torch.Size([1, 16, 30, 30])
```
*Note: The spatial size shrank from 32x32 to 30x30 because a 3x3 filter cannot center on the very edge pixels without spilling off the image.*

## 3. Pooling (`nn.MaxPool2d`)
Pooling shrinks (downsamples) the feature maps to save memory and force the network to keep only the strongest, most dominant features. 
Max Pooling looks at a small window of pixels, keeps the highest number, and throws the rest away.

```python
# kernel_size = 2 (The pooling window is 2x2 pixels)
# stride = 2 (The window jumps 2 pixels at a time, so it never overlaps)
pool_layer = nn.MaxPool2d(kernel_size=2, stride=2)

pooled_maps = pool_layer(feature_maps)

print("Pooled Shape:", pooled_maps.shape)
# Output: torch.Size([1, 16, 15, 15])
```
*Note: The 30x30 spatial dimensions were cut exactly in half to 15x15.*

---

## The Dimension Formula
When designing CNNs, you constantly need to calculate what the output dimensions (Height and Width) will be after passing through a Convolutional or Pooling layer.

The universal formula to calculate the output dimension $O$ for a given dimension $W$ (Width or Height) is:

$$ O = \lfloor \frac{n - f + 2p}{s} \rfloor + 1 $$

Where:
- $n$ = Input Size (Width or Height)
- $f$ = Filter / Kernel Size (`kernel_size`)
- $p$ = Padding (`padding`, default is 0)
- $s$ = Stride (`stride`, default is 1 for Conv2d, and equal to Kernel Size for MaxPool)
- $\lfloor \dots \rfloor$ means "round down to the nearest integer"

### Example Calculation for Conv2d:
For our `dummy_image` (n = 32):
- $f = 3$
- $p = 0$
- $s = 1$

$$
O = \lfloor \frac{32 - 3 + 2(0)}{1} \rfloor + 1 = 29 + 1 = 30
$$

Output: **30x30**

### Example Calculation for MaxPool2d:
For our `feature_maps` (n = 30):
- $f = 2$
- $p = 0$
- $s = 2$

$$
O = \lfloor \frac{30 - 2 + 2(0)}{2} \rfloor + 1 = \lfloor \frac{28}{2} \rfloor + 1 = 14 + 1 = 15
$$

Output: **15x15**
