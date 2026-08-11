# Phase 5: Scaled Dot-Product and Multi-Head Attention

In the previous section, we calculated raw Attention Scores by multiplying Queries by Keys ($Q @ K^T$). While mathematically correct, this has a flaw when scaled up to real-world dimensions.

## 1. Scaled Dot-Product Attention
If the embedding size (which we call $d_k$) is very large (e.g., 512 numbers per word), the result of $Q @ K^T$ produces massive numbers. When these massive numbers are passed into the Softmax function, the gradients vanish (become near zero), and the network stops learning.

To fix this, the original Transformer paper ("Attention Is All You Need") scales the scores down by dividing them by the square root of $d_k$.

```python
import torch
import torch.nn.functional as F
import math

# Sequence: 1 sentence, 5 words, embedding size 8
Q = torch.randn(1, 5, 8)
K = torch.randn(1, 5, 8)
V = torch.randn(1, 5, 8)

d_k = 8 # Our embedding size

# We scale the scores down by the square root of d_k BEFORE applying softmax!
attention_scores = (Q @ K.transpose(1, 2)) / math.sqrt(d_k)
attention_weights = F.softmax(attention_scores, dim=-1)

final_output = attention_weights @ V
```

## 2. Multi-Head Attention (`nn.MultiheadAttention`)
If we only use one set of $Q$, $K$, and $V$ vectors, the network can only pay attention to one "type" of context (e.g., grammatical structure). 

But in a complex sentence, we want the network to simultaneously analyze grammar, tone, emotion, and context. To do this, we split the math into multiple parallel "Heads". It is like having multiple brains reading the sentence at the same time, each looking for something different.

PyTorch provides a built-in module that handles all the complex math (linear projections, QKV splitting, scaled dot-product, and merging heads) for us.

```python
import torch.nn as nn

# embed_dim = 8 (The size of our word vectors)
# num_heads = 2 (We want 2 parallel attention 'brains')
# batch_first = True (Because our tensor starts with Batch Size)
multihead_attn = nn.MultiheadAttention(embed_dim=8, num_heads=2, batch_first=True)

# For Self-Attention, we pass the EXACT SAME sequence in as the Query, Key, and Value!
# PyTorch will automatically calculate Q, K, and V internally and perform the math.
sequence = torch.randn(1, 5, 8) 
attn_output, attn_weights = multihead_attn(query=sequence, key=sequence, value=sequence)

print("Multi-Head Attention Output Shape:", attn_output.shape)
# Output: torch.Size([1, 5, 8])
```

By connecting `nn.MultiheadAttention` blocks together with standard `nn.Linear` layers, you create a complete **Transformer**!
