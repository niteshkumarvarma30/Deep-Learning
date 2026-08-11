# Phase 4: Sequence Data (RNN, LSTM, GRU)

Unlike images which are 2D grids of pixels, sequence data represents information over time (like words in a sentence, or stock prices over a week). To handle time-dependent data, we use Recurrent Neural Networks (RNNs) which maintain a "memory" (Hidden State) as they process the sequence step-by-step.

## 1. Sequence Tensors (B, L, F)
In PyTorch, sequences must follow a strict 3D tensor shape:
`[Batch Size, Sequence Length, Features]`

- **Batch Size:** Number of sequences (e.g., number of sentences) processed at once.
- **Sequence Length ($L$):** The number of time steps (e.g., words in a sentence).
- **Features ($F$):** The size of the numerical representation for each time step (e.g., embedding size of a word).

```python
import torch

# Create a dummy sequence tensor
# 1 sentence, 5 words long, each word represented by 10 features
dummy_sequence = torch.randn(1, 5, 10) 
print("Sequence Shape:", dummy_sequence.shape) 
# Output: torch.Size([1, 5, 10])
```

## 2. Standard RNN (`nn.RNN`)
A standard RNN reads the sequence one step at a time, updating its Hidden State ($h_t$) to remember what it has seen.

```python
import torch.nn as nn

# input_size = 10 (Features per word)
# hidden_size = 20 (The RNN compresses its memory into a 20-number vector)
# batch_first = True (Tells PyTorch our tensor starts with Batch Size)
rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)

# RNNs return two things: 
# 1. 'output': The hidden state at EVERY time step.
# 2. 'final_hidden_state': The hidden state at the VERY LAST time step.
output, final_hidden_state = rnn(dummy_sequence)

print("Output Shape:", output.shape) 
# Output: torch.Size([1, 5, 20]) -> A 20-number memory vector for all 5 words.

print("Final Hidden State Shape:", final_hidden_state.shape) 
# Output: torch.Size([1, 1, 20]) -> The final summary of the entire 5-word sentence.
```

## 3. LSTM (`nn.LSTM`)
Standard RNNs suffer from the **Vanishing Gradient Problem** (they forget early words in long sentences). Long Short-Term Memory (LSTM) networks fix this by introducing a **Cell State** ($c_t$), which acts as a long-term memory conveyor belt regulated by mathematical "gates" (Input, Forget, Output).

In PyTorch, an LSTM returns three pieces of information instead of two.
```python
lstm = nn.LSTM(input_size=10, hidden_size=20, batch_first=True)

# Notice it returns a tuple containing (hidden_state, cell_state)
output, (final_hidden_state, final_cell_state) = lstm(dummy_sequence)

print("LSTM Output Shape:", output.shape)
print("LSTM Final Hidden State Shape:", final_hidden_state.shape)
print("LSTM Final Cell State Shape:", final_cell_state.shape)
```

## 4. GRU (`nn.GRU`)
The Gated Recurrent Unit (GRU) is a simplified, more efficient version of the LSTM. It merges the Hidden State and Cell State into a single memory vector, while still keeping the smart forgetting gates to prevent the vanishing gradient problem.

Because there is no separate cell state, the code looks exactly like a standard RNN!
```python
gru = nn.GRU(input_size=10, hidden_size=20, batch_first=True)

output, final_hidden_state = gru(dummy_sequence)

print("GRU Output Shape:", output.shape)
print("GRU Final Hidden State Shape:", final_hidden_state.shape)
```
