# Transformer Encoder–Decoder: Complete Training and Inference Flow

## 1. Overview

A Transformer Encoder–Decoder model consists of two major parts:

```text
                    ENCODER
                       │
                       │ Encoder representations
                       ▼
                    DECODER
                       │
                       ▼
                 Output tokens
```

The most important difference between **training** and **inference** is:

> **During training, the complete target sequence is already known, so the decoder can process the entire shifted target sequence in one forward pass.**

> **During inference, the target sequence is unknown, so the decoder must generate one token at a time and feed the generated tokens back into itself.**

The architecture uses three important attention mechanisms:

1. **Encoder Self-Attention**
2. **Decoder Masked Self-Attention**
3. **Decoder Cross-Attention**

---

# 2. Example

Suppose we are building an English → French translation model.

### Source

```text
I love cats
```

### Target

```text
J'aime les chats
```

During training, both source and target are available.

During inference, only the source is available:

```text
I love cats
```

The model must generate:

```text
J'aime les chats
```

---

# 3. Complete Transformer Encoder–Decoder Architecture

```text
                         ENCODER

Source tokens
      ↓
Token Embedding
      ↓
Positional Encoding
      ↓
Multi-Head Self-Attention
      ↓
Add & LayerNorm
      ↓
Feed-Forward Network
      ↓
Add & LayerNorm
      ↓
Repeat N times
      ↓
Encoder Output H
      │
      │
      │ Used as K,V
      ▼

                         DECODER

Target tokens
      ↓
Token Embedding
      ↓
Positional Encoding
      ↓
Masked Multi-Head Self-Attention
      ↓
Add & LayerNorm
      ↓
Multi-Head Cross-Attention
      │
      │ Q ← Decoder
      │ K,V ← Encoder
      ↓
Add & LayerNorm
      ↓
Feed-Forward Network
      ↓
Add & LayerNorm
      ↓
Repeat N times
      ↓
Linear Projection
      ↓
Logits
      ↓
Softmax
      ↓
Token probabilities
```

---

# 4. The Three Attention Mechanisms

Understanding these three mechanisms is essential.

---

## 4.1 Encoder Self-Attention

In encoder self-attention:

```text
Q ← Encoder
K ← Encoder
V ← Encoder
```

All three come from the same sequence.

For:

```text
I love cats
```

the tokens can attend to one another.

Conceptually:

```text
I      love      cats
│        │         │
└────────┼─────────┘
         │
    Self-Attention
```

Purpose:

> Understand relationships between tokens in the source sentence.

---

# 5. Decoder Masked Self-Attention

In decoder self-attention:

```text
Q ← Decoder
K ← Decoder
V ← Decoder
```

However, the decoder uses a **causal mask**.

The decoder is not allowed to look at future target tokens.

For:

```text
<START> J'aime les chats
```

the mask looks conceptually like:

```text
             <START>  J'aime  les  chats

<START>         ✓       ✗      ✗      ✗

J'aime          ✓       ✓      ✗      ✗

les             ✓       ✓      ✓      ✗

chats           ✓       ✓      ✓      ✓
```

Therefore:

```text
J'aime
```

can see:

```text
<START>
J'aime
```

but cannot see:

```text
les
chats
```

Purpose:

> Allow the decoder to use previously generated/available target tokens without seeing future tokens.

---

# 6. Decoder Cross-Attention

Cross-attention connects the decoder with the encoder.

Here:

```text
Q ← Decoder

K ← Encoder

V ← Encoder
```

This is one of the most important facts about the Transformer Encoder–Decoder architecture.

```text
                    ENCODER
                       │
                       │ H
                 ┌─────┴─────┐
                 ▼           ▼
                 K           V
                 │           │
                 └─────┬─────┘
                       │
                       ▼
                CROSS-ATTENTION
                       ▲
                       │
                       Q
                       │
                    DECODER
```

The decoder is essentially asking:

> "Which information from the source sentence is relevant to what I am generating now?"

---

# 7. Q, K and V

The basic attention equation is:

\[
Attention(Q,K,V) = softmax \left( \frac{QK^T}{\sqrt{d_k}} \right)V
\]

Where:

* (Q) = Query
* (K) = Key
* (V) = Value
* (d_k) = dimension of the key

A useful mental model is:

```text
Query  → What am I looking for?

Key    → What information do I contain?

Value  → What information should I return?
```

---

# 8. Q, K and V in the Three Attention Types

This table is extremely important.

| Attention                     | Q comes from | K comes from | V comes from |
| ----------------------------- | ------------ | ------------ | ------------ |
| Encoder Self-Attention        | Encoder      | Encoder      | Encoder      |
| Decoder Masked Self-Attention | Decoder      | Decoder      | Decoder      |
| Decoder Cross-Attention       | Decoder      | Encoder      | Encoder      |

Therefore:

\[
\boxed{
Q_{encoder},K_{encoder},V_{encoder}
}
\]

for encoder self-attention.

\[
\boxed{
Q_{decoder},K_{decoder},V_{decoder}
}
\]

for decoder masked self-attention.

And:

\[
\boxed{
Q_{decoder},K_{encoder},V_{encoder}
}
\]

for decoder cross-attention.

---

# 9. What Does the Encoder Actually Produce?

Suppose the source is:

```text
I love cats
```

The encoder does not simply output the original text again.

It produces contextual hidden representations:

\[
H=[h_1,h_2,h_3]
\]

Conceptually:

```text
I       love       cats
│         │          │
▼         ▼          ▼
h₁        h₂         h₃
```

These representations contain contextual information learned through encoder self-attention.

The final encoder output is:

\[
H
\]

---

# 10. How Encoder Information Reaches the Decoder

In decoder cross-attention, the encoder output is projected into Keys and Values:

\[
K=HW_K
\]

\[
V=HW_V
\]

The decoder creates the Query:

\[
Q=YW_Q
\]

where (Y) is the decoder's current representation.

Therefore:

```text
                    ENCODER
                       │
                       │ H
                 ┌─────┴─────┐
                 ▼           ▼
              H W_K        H W_V
                 │           │
                 ▼           ▼
                 K           V
                 │           │
                 └─────┬─────┘
                       │
                       ▼
                Cross-Attention
                       ▲
                       │
                       Q
                       │
                    Decoder
```

So yes:

> **In cross-attention, the encoder supplies K and V, while the decoder supplies Q.**

---

# 11. Why Does the Encoder Not Supply Q in Cross-Attention?

Because the decoder is the component asking the question.

The decoder's Query represents:

> "What information do I need from the source right now?"

The encoder's Keys represent:

> "Where is potentially relevant information?"

The encoder's Values represent:

> "Here is the actual information."

Therefore:

```text
Decoder → Q
Encoder → K,V
```

---

# 12. Multi-Head Attention

Multi-Head Attention performs multiple attention operations in parallel.

For head (i):

\[
head_i = Attention(QW_i^Q,KW_i^K,VW_i^V)
\]

Then the heads are concatenated:

\[
MultiHead(Q,K,V) = Concat(head_1,\dots,head_h)W_O
\]

Conceptually:

```text
                 Input
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
     Head 1      Head 2      Head 3
       │           │           │
       └───────────┼───────────┘
                   ▼
              Concatenate
                   │
                   ▼
              Linear layer
                   │
                   ▼
                 Output
```

Multi-head attention allows different heads to learn different relationships.

---

# 13. Training

Now we can understand the complete training process.

Suppose:

```text
SOURCE:

I love cats
```

Target:

```text
J'aime les chats
```

During training, the model knows both.

---

# 14. Training Step 1 — Source Enters Encoder

The source sentence:

```text
I love cats
```

is tokenized.

Then:

```text
Tokens
  ↓
Token Embeddings
  ↓
Positional Encoding
```

The resulting representation enters the encoder.

---

# 15. Training Step 2 — Encoder Self-Attention

The encoder performs self-attention.

```text
I love cats
     │
     ▼
Self-Attention
     │
     ▼
Contextual representations
```

The encoder computes:

\[
Q=XW_Q
\]

\[
K=XW_K
\]

\[
V=XW_V
\]

Then:

\[
Attention(Q,K,V) = softmax \left( \frac{QK^T}{\sqrt{d_k}} \right)V
\]

This allows each source token to interact with the other source tokens.

---

# 16. Training Step 3 — Encoder Feed-Forward Network

After self-attention:

```text
Self-Attention
      ↓
Add & LayerNorm
      ↓
Feed-Forward Network
      ↓
Add & LayerNorm
```

The Feed-Forward Network is typically:

\[
FFN(x) = W_2\sigma(W_1x+b_1)+b_2
\]

This completes one encoder layer.

The architecture contains multiple encoder layers.

```text
Encoder Layer 1
      ↓
Encoder Layer 2
      ↓
Encoder Layer 3
      ↓
...
      ↓
Encoder Layer N
```

---

# 17. Training Step 4 — Encoder Output

After all encoder layers:

\[
H=[h_1,h_2,\dots,h_n]
\]

For our example:

```text
I       love       cats
│         │          │
▼         ▼          ▼
h₁        h₂         h₃
```

This is the encoder's final output.

---

# 18. Training Step 5 — Encoder Provides K and V

For decoder cross-attention:

\[
K=HW_K
\]

\[
V=HW_V
\]

Conceptually:

```text
                    ENCODER
                       │
                       ▼
                       H
                  ┌────┴────┐
                  ▼         ▼
                  K         V
                  │         │
                  └────┬────┘
                       │
                       ▼
                Decoder Cross-
                  Attention
```

These encoder representations are available to the decoder.

---

# 19. Training Step 6 — Prepare Decoder Input

The target is:

```text
J'aime les chats <END>
```

During training, we shift it right.

### Decoder input

```text
<START> J'aime les chats
```

### Expected output

```text
J'aime les chats <END>
```

So:

```text
Decoder input                 Target

<START>             ───────►  J'aime

<START> J'aime      ───────►  les

<START> J'aime les  ───────►  chats

<START> J'aime les chats ──►  <END>
```

This is called **teacher forcing** or, more precisely in Transformer training, the use of the shifted ground-truth target sequence.

---

# 20. Why Is the Target Shifted?

Because the model is learning:

\[
P(y_t|y_{<t},x)
\]

For example:

\[
P(J'aime|<START>,x)
\]

\[
P(les|<START>,J'aime,x)
\]

\[
P(chats|<START>,J'aime,les,x)
\]

\[
P(<END>|<START>,J'aime,les,chats,x)
\]

The decoder therefore receives the previous target tokens and learns to predict the next token.

---

# 21. Training Step 7 — Decoder Masked Self-Attention

The decoder input is:

```text
<START> J'aime les chats
```

The decoder performs masked self-attention.

Here:

\[
Q=YW_Q
\]

\[
K=YW_K
\]

\[
V=YW_V
\]

All come from the decoder.

But the causal mask prevents future information.

```text
             <START>  J'aime  les  chats

<START>         ✓       ✗      ✗      ✗

J'aime          ✓       ✓      ✗      ✗

les             ✓       ✓      ✓      ✗

chats           ✓       ✓      ✓      ✓
```

---

# 22. Important: The Entire Target Is Present During Training

This is where training differs from inference.

During training, the decoder physically receives:

```text
<START> J'aime les chats
```

all at once.

But the mask makes the model behave as if it only knows the past.

Therefore:

```text
<START>              → J'aime
<START> J'aime       → les
<START> J'aime les   → chats
<START> J'aime les chats → <END>
```

can be calculated in parallel.

---

# 23. Training Step 8 — Decoder Cross-Attention

After masked self-attention, the decoder performs cross-attention.

The decoder creates Queries:

\[
Q=YW_Q
\]

The encoder provides Keys and Values:

\[
K=HW_K
\]

\[
V=HW_V
\]

Therefore:

```text
                    ENCODER
                       │
                       H
                  ┌────┴────┐
                  ▼         ▼
                  K         V
                  │         │
                  └────┬────┘
                       │
                       ▼
                CROSS-ATTENTION
                       ▲
                       │
                    Decoder
                       │
                       Q
```

---

# 24. Multiple Queries During Training

The decoder has multiple positions:

```text
<START>  → Q₁
J'aime   → Q₂
les      → Q₃
chats    → Q₄
```

Therefore cross-attention can conceptually calculate:

```text
Q₁ → prediction for J'aime
Q₂ → prediction for les
Q₃ → prediction for chats
Q₄ → prediction for <END>
```

All these positions use the same encoder source representation (H), transformed into K and V for that decoder cross-attention layer.

---

# 25. Training Step 9 — Feed-Forward Network

After cross-attention:

```text
Cross-Attention
      ↓
Add & LayerNorm
      ↓
Feed-Forward Network
      ↓
Add & LayerNorm
```

Then the decoder layer is complete.

Multiple decoder layers are stacked:

```text
Decoder Layer 1
      ↓
Decoder Layer 2
      ↓
Decoder Layer 3
      ↓
...
      ↓
Decoder Layer N
```

---

# 26. Training Step 10 — Linear Projection

The final decoder representations are passed through a linear projection:

```text
Decoder output
      ↓
Linear layer
      ↓
Vocabulary logits
```

Suppose the vocabulary contains:

```text
J'aime
les
chats
je
suis
...
```

The model generates a logit for every vocabulary token at every target position.

---

# 27. Training Step 11 — Softmax

Softmax converts logits into probabilities:

\[
P(y_t|y_{<t},x) = softmax(logits)
\]

For example:

```text
Position: predicting token 2

J'aime   → 0.01
les      → 0.72
chats    → 0.05
...
```

The correct target is:

```text
les
```

---

# 28. Training Step 12 — Loss

The model's predictions are compared with the ground-truth target:

```text
Predictions:

J'aime
les
chats
<END>

        vs.

Ground truth:

J'aime
les
chats
<END>
```

Usually cross-entropy loss is used.

\[
Loss=CrossEntropy(prediction,target)
\]

The losses across target positions are combined.

---

# 29. Training Step 13 — Backpropagation

The loss is propagated backward through the entire model.

```text
Loss
 ↓
Output Projection
 ↓
Decoder
 ↓
Cross-Attention
 ↓
Decoder Self-Attention
 ↓
Encoder
 ↓
Encoder Self-Attention
```

Therefore **both the encoder and decoder are trained together**.

The encoder is not permanently trained first and then left untouched.

Parameters are updated through backpropagation.

---

# 30. What Gets Updated?

The model can update:

### Encoder

```text
Token embeddings
Positional-related parameters if learnable
WQ
WK
WV
Output projections
FFN weights
LayerNorm parameters
```

### Decoder

```text
Token embeddings
WQ
WK
WV
Output projections
FFN weights
LayerNorm parameters
```

### Output

```text
Final linear projection
```

Therefore:

```text
Encoder + Decoder
       ↓
   Prediction
       ↓
      Loss
       ↓
Backpropagation
       ↓
Update parameters
```

---

# 31. Complete Training Flow

```text
                         TRAINING

SOURCE
"I love cats"
     │
     ▼
Tokenization
     │
     ▼
Embedding + Positional Encoding
     │
     ▼
┌─────────────────────────────┐
│          ENCODER            │
│                             │
│ Multi-Head Self-Attention   │
│          ↓                  │
│ Add & LayerNorm             │
│          ↓                  │
│ Feed Forward                │
│          ↓                  │
│ Add & LayerNorm             │
│          ↓                  │
│ Repeat N layers             │
└──────────────┬──────────────┘
               │
               ▼
         Encoder Output H
               │
          ┌────┴────┐
          ▼         ▼
          K         V
          │         │
          │         │
          ▼         ▼
┌─────────────────────────────┐
│          DECODER            │
│                             │
│ Input:                      │
│ <START> J'aime les chats    │
│          ↓                  │
│ Masked Multi-Head           │
│ Self-Attention              │
│          ↓                  │
│ Add & LayerNorm             │
│          ↓                  │
│ Multi-Head Cross-Attention  │
│                             │
│ Q ← Decoder                 │
│ K,V ← Encoder               │
│          ↓                  │
│ Add & LayerNorm             │
│          ↓                  │
│ Feed Forward                │
│          ↓                  │
│ Add & LayerNorm             │
│          ↓                  │
│ Repeat N layers             │
└──────────────┬──────────────┘
               │
               ▼
        Linear Projection
               │
               ▼
             Logits
               │
               ▼
            Softmax
               │
               ▼
          Predictions
               │
               ▼
      Compare with target
               │
               ▼
              Loss
               │
               ▼
       Backpropagation
               │
               ▼
        Update parameters
```

---

# 32. Does the Decoder Generate One Token at a Time During Training?

**No.**

This is one of the most important concepts.

During training:

```text
Decoder input:

<START> J'aime les chats
```

The model can produce:

```text
J'aime
les
chats
<END>
```

for all positions in one forward pass.

The causal mask ensures that the model cannot cheat.

Therefore training is approximately:

```text
One Encoder Forward Pass
             +
One Decoder Forward Pass
             +
Loss
             +
Backpropagation
```

for a training example/batch.

---

# 33. Inference

Now suppose the model has already been trained.

We provide:

```text
I love cats
```

The target:

```text
J'aime les chats
```

is unknown.

---

# 34. Inference Step 1 — Encoder

The source is passed through the encoder:

```text
I love cats
     │
     ▼
Embedding
     ↓
Positional Encoding
     ↓
Encoder Self-Attention
     ↓
Add & LayerNorm
     ↓
Feed Forward
     ↓
Add & LayerNorm
     ↓
Repeat N layers
     ↓
Encoder Output H
```

The encoder runs once for this input.

---

# 35. Encoder Output During Inference

The encoder output:

\[
H
\]

is used for decoder cross-attention.

Conceptually:

```text
Encoder Output H
       │
       ├────► K
       │
       └────► V
```

The encoder does not need to process the source again for every generated token.

---

# 36. Inference Step 1 — Decoder Starts

The decoder starts with:

```text
<START>
```

It passes through:

```text
Embedding
     ↓
Positional Encoding
     ↓
Masked Self-Attention
     ↓
Cross-Attention
     ↓
Feed Forward
     ↓
Linear
     ↓
Softmax
```

The model predicts:

```text
J'aime
```

---

# 37. Inference Step 2

The newly generated token is appended.

Decoder input becomes:

```text
<START> J'aime
```

The decoder processes the current sequence and predicts:

```text
les
```

Now:

```text
<START> J'aime les
```

---

# 38. Inference Step 3

Decoder input:

```text
<START> J'aime les
```

The model predicts:

```text
chats
```

Now:

```text
<START> J'aime les chats
```

---

# 39. Inference Step 4

Decoder input:

```text
<START> J'aime les chats
```

The model predicts:

```text
<END>
```

Generation stops.

Final output:

```text
J'aime les chats
```

---

# 40. Complete Inference Flow

```text
                         INFERENCE

SOURCE
"I love cats"
     │
     ▼
   ENCODER
     │
     ▼
Encoder Output H
     │
     │
     ├──────── K
     │
     └──────── V
                │
                ▼
             DECODER
                │
                ▼
             <START>
                │
                ▼
      Masked Self-Attention
                │
                ▼
         Cross-Attention
          Q = Decoder
          K,V = Encoder
                │
                ▼
             Softmax
                │
                ▼
             J'aime
                │
                ▼
        <START> J'aime
                │
                ▼
      Masked Self-Attention
                │
                ▼
         Cross-Attention
                │
                ▼
             Softmax
                │
                ▼
               les
                │
                ▼
       <START> J'aime les
                │
                ▼
      Masked Self-Attention
                │
                ▼
         Cross-Attention
                │
                ▼
             Softmax
                │
                ▼
              chats
                │
                ▼
     <START> J'aime les chats
                │
                ▼
              <END>
```

---

# 41. Why Does the Decoder Run Multiple Times During Inference?

Because the target is unknown.

At the beginning:

```text
<START>
```

The model does not know the next token.

It predicts:

```text
J'aime
```

Now it knows one more token.

It predicts:

```text
les
```

Then:

```text
chats
```

Then:

```text
<END>
```

Therefore:

```text
<START>
   ↓
J'aime
   ↓
les
   ↓
chats
   ↓
<END>
```

This is called **autoregressive generation**.

---

# 42. Training vs Inference — Core Difference

| Property              | Training                                   | Inference                   |
| --------------------- | ------------------------------------------ | --------------------------- |
| Source known?         | Yes                                        | Yes                         |
| Target known?         | Yes                                        | No                          |
| Encoder               | One forward pass                           | One forward pass            |
| Decoder               | One forward pass over whole shifted target | Repeated/autoregressive     |
| Decoder input         | Ground-truth shifted target                | Previously generated tokens |
| Masked self-attention | Yes                                        | Yes                         |
| Cross-attention       | Yes                                        | Yes                         |
| Q in cross-attention  | Decoder                                    | Decoder                     |
| K in cross-attention  | Encoder                                    | Encoder                     |
| V in cross-attention  | Encoder                                    | Encoder                     |
| Loss                  | Yes                                        | Usually no                  |
| Backpropagation       | Yes                                        | No                          |
| Parameter updates     | Yes                                        | No                          |
| Generation            | Parallel across target positions           | One token at a time         |

---

# 43. The Most Important Difference

### Training

The target is known:

```text
Target:
J'aime les chats <END>
```

Therefore:

```text
<START> J'aime les chats
```

can be given to the decoder.

The decoder predicts:

```text
J'aime
les
chats
<END>
```

in parallel.

---

### Inference

The target is unknown.

So:

```text
<START>
```

must produce:

```text
J'aime
```

Then:

```text
<START> J'aime
```

must produce:

```text
les
```

Then:

```text
<START> J'aime les
```

must produce:

```text
chats
```

Then:

```text
<START> J'aime les chats
```

must produce:

```text
<END>
```

---

# 44. The Key Difference in One Diagram

## Training

```text
                 SOURCE
                    │
                    ▼
                 ENCODER
                    │
                    ▼
                    H
                  K,V
                    │
                    ▼
        <START> J'aime les chats
                    │
                    ▼
          Masked Self-Attention
                    │
                    ▼
             Cross-Attention
              Q = Decoder
              K,V = Encoder
                    │
                    ▼
              Predictions
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    J'aime         les          chats
       │            │            │
       ▼            ▼            ▼
    Target        Target       Target
    J'aime         les          chats
       │            │            │
       └────────────┼────────────┘
                    ▼
                   Loss
                    │
                    ▼
             Backpropagation
```

---

# 45. Inference

```text
                 SOURCE
                    │
                    ▼
                 ENCODER
                    │
                    ▼
                    H
                  K,V
                    │
                    ▼
                 <START>
                    │
                    ▼
                Decoder
                    │
                    ▼
                  J'aime
                    │
                    ▼
            <START> J'aime
                    │
                    ▼
                Decoder
                    │
                    ▼
                   les
                    │
                    ▼
          <START> J'aime les
                    │
                    ▼
                Decoder
                    │
                    ▼
                  chats
                    │
                    ▼
        <START> J'aime les chats
                    │
                    ▼
                Decoder
                    │
                    ▼
                  <END>
```

---

# 46. Encoder Runs Once vs Decoder Runs Repeatedly

This is the mental model to remember.

## Training

```text
SOURCE
  │
  ▼
ENCODER
  │
  ▼
H
  │
  │ K,V
  ▼
DECODER
  │
  │ Whole shifted target
  ▼
Predictions for all positions
  │
  ▼
Loss
```

Therefore:

> **Encoder: once**

> **Decoder: one forward pass over the complete shifted target sequence**

---

## Inference

```text
SOURCE
  │
  ▼
ENCODER
  │
  ▼
H
  │
  │ K,V
  ▼
DECODER
  │
  ▼
Token 1
  │
  ▼
DECODER
  │
  ▼
Token 2
  │
  ▼
DECODER
  │
  ▼
Token 3
  │
  ▼
...
```

Therefore:

> **Encoder: once**

> **Decoder: repeated autoregressively**

---

# 47. Why Does the Encoder Not Need to Repeat?

The source sentence does not change.

For:

```text
I love cats
```

the encoder creates:

\[
H
\]

Once (H) has been produced, it can be reused by the decoder's cross-attention.

Conceptually:

```text
                    ENCODER
                       │
                       ▼
                       H
                    K,V
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Decoder         Decoder        Decoder
      Step 1          Step 2         Step 3
```

The decoder's Query changes at each generation step, but the source remains the same.

---

# 48. What Changes During Decoder Inference?

The Query changes.

### Step 1

```text
Q₁ = representation of <START>
```

### Step 2

```text
Q₂ = representation of <START> J'aime
```

### Step 3

```text
Q₃ = representation of <START> J'aime les
```

Therefore:

```text
                 Encoder
                   │
                  K,V
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
       Step 1     Step 2     Step 3
        ▲          ▲          ▲
        │          │          │
       Q₁         Q₂         Q₃
```

Each query asks a different question of the encoder.

---

# 49. What Happens to K and V During Inference?

The encoder output is reused.

For a particular decoder cross-attention layer:

\[
K=HW_K
\]

\[
V=HW_V
\]

These represent the encoder information that the decoder can attend to.

The decoder creates:

\[
Q=YW_Q
\]

Then:

\[
Attention(Q,K,V) = softmax \left( \frac{QK^T}{\sqrt{d_k}} \right)V
\]

The result is passed through the rest of the decoder.

---

# 50. KV Cache During Inference

There is another optimization used in practical Transformer implementations: **KV caching**.

During autoregressive generation, previously calculated decoder Keys and Values can be cached.

Conceptually:

```text
Previous decoder tokens
          │
          ▼
       Cached K,V
          │
          ├─────────────┐
          │             │
          ▼             ▼
    Previous K,V      New K,V
          │             │
          └──────┬──────┘
                 ▼
             Attention
                 ▲
                 │
              New Q
```

This avoids recomputing all previous decoder K and V representations from scratch at every generation step.

KV caching is particularly important for efficient inference.

---

# 51. Important Clarification About "The Encoder Is Trained Once"

It is incorrect to think:

> "First the encoder gets trained once, and then the decoder gets trained."

Instead, during model training:

```text
Encoder
   ↓
Decoder
   ↓
Prediction
   ↓
Loss
   ↓
Backpropagation
   ↓
Encoder weights updated
Decoder weights updated
```

Both are trained together.

For every training batch, the encoder performs a forward computation, the decoder performs a forward computation, and gradients update the entire network.

---

# 52. Full Training Loop

For many training batches:

```text
FOR each training batch:

    Source
       ↓
    Encoder
       ↓
    Encoder output H
       ↓
    Create K,V for cross-attention
       ↓
    Shift target right
       ↓
    Decoder
       ↓
    Masked Self-Attention
       ↓
    Cross-Attention
       ↓
    Feed Forward
       ↓
    Linear
       ↓
    Logits
       ↓
    Cross-Entropy Loss
       ↓
    Backpropagation
       ↓
    Update parameters

REPEAT for many batches
```

Over many iterations, the model learns the parameters necessary to translate the source into the target.

---

# 53. Full Inference Loop

After training is complete:

```text
Source
  ↓
Encoder
  ↓
Encoder output H
  ↓
Create/reuse encoder K,V
  ↓
Decoder starts with <START>
  ↓
Predict next token
  ↓
Append token
  ↓
Decoder again
  ↓
Predict next token
  ↓
Append token
  ↓
Repeat
  ↓
<END>
  ↓
Final text
```

Pseudo-process:

```text
generated = [<START>]

while last_token != <END>:

    output = decoder(generated, encoder_output)

    next_token = select_token(output)

    generated.append(next_token)

return generated
```

---

# 54. The Most Important Three Lines

For **Encoder Self-Attention**:

\[
\boxed{Q,K,V \leftarrow Encoder}
\]

For **Decoder Masked Self-Attention**:

\[
\boxed{Q,K,V \leftarrow Decoder}
\]

For **Decoder Cross-Attention**:

\[
\boxed{Q \leftarrow Decoder,\quad K,V \leftarrow Encoder}
\]

These three relationships should be memorized.

---

# 55. Final Mental Model

Think of the encoder as the component that **understands the source**:

```text
"I love cats"
     ↓
ENCODER
     ↓
Contextual representation H
```

The decoder is the component that **generates the target**.

During training:

```text
Target is known

<START> J'aime les chats
          │
          ▼
       DECODER
          │
          ▼
J'aime les chats <END>

All positions can be computed in parallel
because of the causal mask.
```

During inference:

```text
Target is unknown

<START>
   ↓
J'aime
   ↓
<START> J'aime
   ↓
les
   ↓
<START> J'aime les
   ↓
chats
   ↓
<START> J'aime les chats
   ↓
<END>
```

Therefore:

\[
\boxed{
\text{Training: Encoder once + Decoder one parallel forward pass}
}
\]

\[
\boxed{
\text{Inference: Encoder once + Decoder autoregressively}
}
\]

And in both cases:

\[
\boxed{
\text{Cross-Attention: }Q_{\text{Decoder}},K_{\text{Encoder}},V_{\text{Encoder}}
}
\]

The fundamental reason for the difference is simple:

> **During training, the correct target sequence is already available. During inference, it is not, so the decoder has to create the target sequence step by step.**
