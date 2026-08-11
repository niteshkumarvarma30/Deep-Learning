# Phase 5: Attention (The Q, K, V Mechanism)

To solve the Information Bottleneck problem of LSTMs, the Attention Mechanism was invented. It allows a neural network to look at every single word in a sentence simultaneously and figure out which words are most relevant to each other.

The core of modern Attention (used in Transformers) relies on the **Query, Key, Value (Q, K, V)** system.
- **Query (Q):** What a word is looking for.
- **Key (K):** What a word has to offer.
- **Value (V):** The actual information or content of the word.

## The Mathematical Core of Attention
Here is how we calculate Attention manually using PyTorch tensor operations.

```python
import torch
import torch.nn.functional as F

# 1. Setup Dummy Data
# 1 sentence, 5 words long, with each word having an embedding size of 8
sequence = torch.randn(1, 5, 8) 

# In a real model, Q, K, and V are created by passing the sequence through nn.Linear layers.
# For this math demonstration, we will just use random tensors of the same size.
Q = torch.randn(1, 5, 8)
K = torch.randn(1, 5, 8)
V = torch.randn(1, 5, 8)

# 2. Calculate the Attention Scores
# We multiply the Queries by the Keys (Q @ K^T) to see how well they "match".
# K.transpose(1, 2) flips the shape of K from [1, 5, 8] to [1, 8, 5] so matrix multiplication works.
attention_scores = Q @ K.transpose(1, 2) 

print("Attention Scores Shape:", attention_scores.shape) 
# Output: torch.Size([1, 5, 5]) 
# This is a 5x5 grid showing how strongly every word relates to every other word!

# 3. Apply Softmax
# We use softmax to turn the raw scores into percentages/probabilities that add up to 1.0 (100%)
attention_weights = F.softmax(attention_scores, dim=-1)

# 4. Generate Final Context-Aware Output
# We multiply our percentage weights by the actual content (Values)
final_output = attention_weights @ V

print("Final Output Shape:", final_output.shape)
# Output: torch.Size([1, 5, 8]) 
# It is exactly the same size as our input, but now every word has been enriched with context from the entire sentence!
```

### Why is this better than an LSTM?
An LSTM processes a sentence sequentially (Word 1 $\rightarrow$ Word 2 $\rightarrow$ Word 3). 
The operation `Q @ K^T` compares *every* word with *every* other word simultaneously in a single mathematical step. This parallel processing is exactly what makes Transformers so incredibly fast to train on GPUs!
