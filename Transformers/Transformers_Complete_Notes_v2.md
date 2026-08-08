# Transformers and Attention Mechanisms --- Complete Mathematical Notes

> **Study note based on the provided Encoder--Decoder, Bahdanau
> Attention, Luong Attention, Multi-Head Attention, Masked Multi-Head
> Attention, and Transformer material.**
>
> The purpose of this note is to build the concepts chronologically:
>
> **Encoder--Decoder → Bottleneck → Attention → Bahdanau → Luong →
> Self-Attention → Multi-Head Attention → Masked Attention →
> Cross-Attention → Transformer**

------------------------------------------------------------------------

# Table of Contents

1.  [Sequence-to-Sequence Encoder--Decoder
    Model](#1-sequence-to-sequence-encoderdecoder-model)
2.  [Encoder](#2-encoder)
3.  [Encoder Vector / Context Vector](#3-encoder-vector--context-vector)
4.  [Decoder](#4-decoder)
5.  [Output Layer and Softmax](#5-output-layer-and-softmax)
6.  [LSTM Encoder--Decoder Example](#6-lstm-encoderdecoder-example)
7.  [Teacher Forcing](#7-teacher-forcing)
8.  [Problems with the Classical
    Encoder--Decoder](#8-problems-with-the-classical-encoderdecoder)
9.  [Why Attention Was Introduced](#9-why-attention-was-introduced)
10. [Attention Input $C_i$](#10-attention-input-c_i)
11. [Attention Weights and Alignment
    Scores](#11-attention-weights-and-alignment-scores)
12. [Bahdanau Attention](#12-bahdanau-attention)
13. [Detailed Bahdanau Calculation
    Flow](#13-detailed-bahdanau-calculation-flow)
14. [Bahdanau Attention
    Architecture](#14-bahdanau-attention-architecture)
15. [Luong Attention](#15-luong-attention)
16. [Detailed Luong Calculation
    Flow](#16-detailed-luong-calculation-flow)
17. [Bahdanau vs Luong Attention](#17-bahdanau-vs-luong-attention)
18. [From Attention to Transformers](#18-from-attention-to-transformers)
19. [Tokenization and Embeddings](#19-tokenization-and-embeddings)
20. [Positional Encoding](#20-positional-encoding)
21. [Position-Aware Input Matrix $X$](#21-position-aware-input-matrix-x)
22. [Self-Attention](#22-self-attention)
23. [Query, Key, and Value](#23-query-key-and-value)
24. [Scaled Dot-Product Attention](#24-scaled-dot-product-attention)
25. [Complete Self-Attention Toy
    Example](#25-complete-self-attention-toy-example)
26. [Multi-Head Attention](#26-multi-head-attention)
27. [Transformer Encoder](#27-transformer-encoder)
28. [Transformer Decoder](#28-transformer-decoder)
29. [Masked Multi-Head
    Self-Attention](#29-masked-multi-head-self-attention)
30. [Training vs Inference](#30-training-vs-inference)
31. [Cross-Attention](#31-cross-attention)
32. [Where Do Q, K, and V Come From?](#32-where-do-q-k-and-v-come-from)
33. [What Is the Final Encoder
    Output?](#33-what-is-the-final-encoder-output)
34. [Where Is Cross-Attention in the Original Transformer
    Diagram?](#34-where-is-cross-attention-in-the-original-transformer-diagram)
35. [Complete Transformer Data Flow](#35-complete-transformer-data-flow)
36. [Attention Comparison Table](#36-attention-comparison-table)
37. [Key Mathematical Formulas](#37-key-mathematical-formulas)
38. [Final Mental Model](#38-final-mental-model)
39. [Exam-Ready Summary](#39-exam-ready-summary)

------------------------------------------------------------------------

# 1. Sequence-to-Sequence Encoder--Decoder Model

A classical **sequence-to-sequence (Seq2Seq)** model converts an input
sequence into an output sequence.

The three main conceptual blocks are:

``` text
Input Sequence
      |
      v
   Encoder
      |
      v
Hidden / Context Vector
      |
      v
   Decoder
      |
      v
Output Sequence
```

The encoder converts the input sequence into a representation, and the
decoder uses that representation to generate the output sequence.

The model is trained to maximize the conditional probability of the
target sequence given the input sequence:

$$
P(Y|X)
$$

For a sequence of output tokens:

$$
P(Y|X) = \prod_{t=1}^{T_y} P(y_t|y_{<t},X)
$$

where:

-   $X$ = input sequence
-   $Y$ = target/output sequence
-   $y_t$ = output token at timestep $t$
-   $y_{<t}$ = previously generated target tokens

### Example

``` text
English:
once upon a time

        ↓

Encoder–Decoder

        ↓

French:
il était une fois
```

The provided material describes this as a sequence-to-sequence
translation architecture using an encoder LSTM and decoder LSTM.

------------------------------------------------------------------------

# 2. Encoder

The encoder reads the input sequence **sequentially**.

For a sequence:

``` text
x₁, x₂, x₃, ..., xₜ
```

the encoder produces:

``` text
h₁, h₂, h₃, ..., hₜ
```

At each timestep, the current input and previous hidden state are used
to compute the next hidden state.

For a simplified RNN:

$$
\boxed{ h_t=f(W_{hh}h_{t-1}+W_{hx}x_t) }
$$

where:

-   $x_t$ = current input
-   $h_{t-1}$ = previous hidden state
-   $h_t$ = current hidden state
-   $W_{hh}$ = hidden-to-hidden weights
-   $W_{hx}$ = input-to-hidden weights
-   $f$ = nonlinear activation

The important idea is:

``` text
x₁ → h₁
       ↓
x₂ → h₂
       ↓
x₃ → h₃
       ↓
...
       ↓
xₜ → hₜ
```

The encoder therefore processes the sequence one element at a time.

The provided material also notes that multiple recurrent units can be
stacked and that LSTM/GRU cells can be used instead of a simple RNN.

------------------------------------------------------------------------

# 3. Encoder Vector / Context Vector

After the encoder has processed the entire input, its final hidden state
represents a summary of the input.

For the classical encoder--decoder architecture:

$$
\boxed{ \text{Context Vector}=h_T }
$$

This vector is intended to encapsulate the information needed by the
decoder.

Conceptually:

``` text
Input sequence
     |
     v
h₁ → h₂ → h₃ → ... → hₜ
                       |
                       v
                Context Vector
```

The context vector is also used to initialize the decoder.

------------------------------------------------------------------------

# 4. Decoder

The decoder generates the output sequence one token at a time.

A simplified decoder recurrence is:

$$
\boxed{ h_t=f(W_{hh}h_{t-1}) }
$$

and the output is generated from the current decoder state.

In an LSTM decoder, the hidden state and cell state are maintained:

$$
(h_t,c_t) = LSTM(y_{t-1},h_{t-1},c_{t-1})
$$

The decoder begins with a start token:

``` text
<START>
```

and continues until it predicts:

``` text
<END>
```

Example:

``` text
<START> → il → était → une → fois → <END>
```

At each timestep:

``` text
Previous output
       +
Previous hidden state
       |
       v
    Decoder
       |
       v
Current hidden state
       |
       v
   Linear + Softmax
       |
       v
Next token
```

------------------------------------------------------------------------

# 5. Output Layer and Softmax

The decoder's hidden representation is passed through a linear layer
followed by softmax.

A simplified equation is:

$$
\boxed{ y_t=\text{softmax}(W_Sh_t) }
$$

Softmax converts the output scores into a probability distribution over
the vocabulary.

Example:

``` text
P(il)    = 0.72
P(le)    = 0.15
P(un)    = 0.04
...
```

The model can then select or decode the next token according to the
probability distribution.

------------------------------------------------------------------------

# 6. LSTM Encoder--Decoder Example

Consider:

``` text
Input:
once | upon | a | time
```

Each word is converted into an embedding:

$$
e_{\text{once}},e_{\text{upon}},e_{\text{a}},e_{\text{time}}
$$

The encoder LSTM processes them sequentially:

  Time    Input   Hidden State
  ------- ------- --------------
  (t_1)   once    $h_1$
  (t_2)   upon    $h_2$
  (t_3)   a       $h_3$
  (t_4)   time    $h_4$

For an LSTM:

$$
\boxed{ (h_t,c_t)=LSTM(x_t,h_{t-1},c_{t-1}) }
$$

After the last token:

$$
h_4,c_4
$$

represent the encoder's final state.

The context can therefore be represented as:

$$
\boxed{ C=(h_4,c_4) }
$$

The decoder can be initialized using these final encoder states:

$$
h_0^{dec}=h_4^{enc}
$$

$$
c_0^{dec}=c_4^{enc}
$$

This transfers the encoded sentence information from encoder to decoder.

------------------------------------------------------------------------

# 7. Teacher Forcing

**Teacher forcing** is a training technique in which the decoder
receives the **correct previous target token** rather than its own
previous prediction.

For example, target:

``` text
<START> il était une fois <END>
```

During training:

``` text
Decoder Input:   <START>  il      était   une
Expected Output: il       était   une     fois
```

So:

$$
\boxed{ \text{Training} \rightarrow \text{Ground-truth previous token} }
$$

whereas during inference:

$$
\boxed{ \text{Inference} \rightarrow \text{Model's previous prediction} }
$$

Teacher forcing helps stabilize and accelerate sequence learning.

------------------------------------------------------------------------

# 8. Problems with the Classical Encoder--Decoder

The classical architecture has a major limitation:

> **The entire input sequence is compressed into one fixed-size context
> vector.**

Conceptually:

``` text
Long Input Sequence
        |
        v
   ONE VECTOR
        |
        v
     Decoder
```

This is the **context-vector bottleneck**.

### Main problems

1.  Information loss.
2.  Early words can become difficult to preserve.
3.  Long sequences are harder to model.
4.  The decoder has no explicit word-to-word alignment.
5.  Every output word relies on the same static summary.

The source material describes the problem as especially important for
longer sentences.

------------------------------------------------------------------------

# 9. Why Attention Was Introduced

Suppose the model wants to translate:

``` text
Turn off the lights
```

into:

``` text
light band karo
```

When generating a particular output word, the decoder may only need a
specific part of the input.

For example:

``` text
"band"
   ↑
"turn" + "off"
```

The decoder does not necessarily need the entire sentence equally for
every output word.

The classical architecture instead gives the decoder the same fixed
context representation for every output step.

Attention changes this.

### Without attention

``` text
Encoder
   |
   v
Single Context Vector
   |
   v
Decoder
```

### With attention

``` text
Encoder
   |
   ├── h₁
   ├── h₂
   ├── h₃
   └── h₄
        |
        v
Decoder dynamically selects
the useful information
```

At every decoder timestep, attention asks:

> **Which encoder hidden states are most relevant right now?**

------------------------------------------------------------------------

# 10. Attention Input $C_i$

In the attention architecture, the decoder receives an additional piece
of information called the **attention input** $C_i$.

Without attention, the decoder can be thought of as using:

$$
y_{i-1},S_{i-1}
$$

With attention, it additionally receives:

$$
C_i
$$

So:

$$
\boxed{ \text{Decoder input at timestep }i = (y_{i-1},S_{i-1},C_i) }
$$

The purpose of $C_i$ is to provide the decoder with the encoder
information that is most useful for producing the current output.

------------------------------------------------------------------------

## 10.1 What is $C_i$?

$C_i$ is a **weighted combination of encoder hidden states**.

Suppose the encoder produces:

$$
h_1,h_2,h_3,h_4
$$

and the attention mechanism assigns:

$$
\alpha_{i1},\alpha_{i2},\alpha_{i3},\alpha_{i4}
$$

Then:

$$
\boxed{ C_i = \alpha_{i1}h_1+ \alpha_{i2}h_2+ \alpha_{i3}h_3+ \alpha_{i4}h_4 }
$$

or generally:

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

If the encoder hidden state has dimension $d_h$, then $C_i$ has the same
dimension $d_h$, because it is a weighted sum of vectors of that
dimension.

------------------------------------------------------------------------

# 11. Attention Weights and Alignment Scores

For every decoder timestep $i$, the attention mechanism assigns a weight
to every encoder hidden state.

For example:

``` text
Encoder states:

h₁ → αᵢ₁ = 0.10
h₂ → αᵢ₂ = 0.20
h₃ → αᵢ₃ = 0.60
h₄ → αᵢ₄ = 0.10
```

A larger value means that the corresponding encoder state contributes
more strongly to $C_i$.

The weights are often obtained by first calculating raw
alignment/similarity scores and then normalizing them with softmax.

$$
e_{ij}=\text{alignment score}
$$

$$
\boxed{ \alpha_{ij} = \text{softmax}$e_{ij}$ }
$$

Therefore the complete dependency is:

``` text
Encoder hidden state hⱼ
             +
Decoder state
             |
             v
      Alignment score eᵢⱼ
             |
             v
           Softmax
             |
             v
      Attention weight αᵢⱼ
             |
             v
        Weighted hⱼ
             |
             v
           Cᵢ
```

This distinction is important:

> **The (\alpha_{ij}) values determine $C_i$; $C_i$ does not
> determine the (\alpha_{ij}) values.**

------------------------------------------------------------------------

# 12. Bahdanau Attention

Bahdanau Attention is also called **Additive Attention**.

The key dependency is:

$$
\boxed{ e_{ij}=f(S_{i-1},h_j) }
$$

where:

-   $S_{i-1}$ = previous decoder hidden state
-   $h_j$ = encoder hidden state at position $j$
-   $f$ = learned alignment function

The source material describes this alignment function as an
ANN/alignment model.

------------------------------------------------------------------------

## 12.1 The Critical Bahdanau Dependency Chain

This is one of the most important concepts:

$$
\boxed{ S_{i-1},h_j \rightarrow e_{ij} \rightarrow \alpha_{ij} \rightarrow C_i }
$$

More explicitly:

### Step 1 --- Take decoder's previous hidden state

$$
S_{i-1}
$$

### Step 2 --- Take an encoder hidden state

$$
h_j
$$

### Step 3 --- Pass them to the alignment model

$$
e_{ij}=f(S_{i-1},h_j)
$$

### Step 4 --- Normalize the scores

$$
\alpha_{ij} = \frac{\exp$e_{ij}$}
{\sum_k\exp(e_{ik})}
$$

### Step 5 --- Calculate the attention input

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

So:

``` text
Previous Decoder State Sᵢ₋₁
             +
Encoder State hⱼ
             |
             v
     ANN / Alignment Model
             |
             v
       Score eᵢⱼ
             |
             v
          Softmax
             |
             v
        αᵢⱼ
             |
             v
Weighted Encoder States
             |
             v
           Cᵢ
```

------------------------------------------------------------------------

# 13. Detailed Bahdanau Calculation Flow

Suppose the encoder has:

$$
h_1,h_2,h_3,h_4
$$

and the decoder is generating its $i$-th output.

The decoder's previous state is:

$$
S_{i-1}
$$

We calculate:

$$
e_{i1}=f(S_{i-1},h_1)
$$

$$
e_{i2}=f(S_{i-1},h_2)
$$

$$
e_{i3}=f(S_{i-1},h_3)
$$

$$
e_{i4}=f(S_{i-1},h_4)
$$

Then:

$$
$$
\alpha_{i1},\alpha_{i2},\alpha_{i3},\alpha_{i4}
$$
= \text{softmax} ([e_{i1},e_{i2},e_{i3},e_{i4}])
$$

Finally:

$$
C_i= \alpha_{i1}h_1+ \alpha_{i2}h_2+
\alpha_{i3}h_3+ \alpha_{i4}h_4
$$

The largest (\alpha) causes the corresponding encoder hidden
state to contribute most strongly.

------------------------------------------------------------------------

## 13.1 ANN Alignment Model

In the source material, $S_{i-1}$ and $h_j$ are combined and passed to
an ANN.

Conceptually:

``` text
Sᵢ₋₁ ─────┐
           ├──→ Concatenate → ANN → eᵢⱼ
hⱼ ───────┘
```

The same alignment model is reused across decoder timesteps.

The source describes this ANN as a *_time-distributed fully connected
neural network** and refers to it as the **alignment model**.

------------------------------------------------------------------------

## 13.2 Example of Dimensions

Suppose:

$$
h_j\in\mathbb{R}^{1\times4}
$$

and:

$$
S_{i-1}\in\mathbb{R}^{1\times4}
$$

Concatenating them gives:

$$
[,S_{i-1};h_j,] \in \mathbb{R}^{1\times8}
$$

The source's example then considers an ANN with a hidden layer and
output neuron that produces the alignment score.

------------------------------------------------------------------------

# 14. Bahdanau Attention Architecture

A simplified flow is:

``` text
Input sequence
      |
      v
   Encoder
      |
      ├── h₁
      ├── h₂
      ├── h₃
      └── h₄
           |
           |
Previous decoder state Sᵢ₋₁
           |
           v
   Alignment ANN
           |
           v
   eᵢ₁ eᵢ₂ eᵢ₃ eᵢ₄
           |
           v
        Softmax
           |
           v
 αᵢ₁ αᵢ₂ αᵢ₃ αᵢ₄
           |
           v
Cᵢ = Σ αᵢⱼhⱼ
           |
           v
      Decoder LSTM
           |
           v
        Output
           |
           v
        Softmax
```

The source describes the Bahdanau attention input as being supplied to
the LSTM cell.

After prediction, the output can be compared with the ground truth using
categorical cross-entropy, followed by backpropagation and weight
updates.

------------------------------------------------------------------------

# 15. Luong Attention

Luong Attention differs from Bahdanau Attention in two especially
important ways:

1.  It uses the **current decoder hidden state (S_i)** rather than the
    previous decoder state $S_{i-1}$.
2.  It can calculate similarity using a **dot product** rather than an
    ANN alignment model.

Therefore, according to the provided material:

$$
\boxed{ e_{ij}=S_i^T h_j }
$$

and:

$$
\boxed{ \alpha_{ij} = \text{softmax}$e_{ij}$ }
$$

Then:

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

------------------------------------------------------------------------

# 16. Detailed Luong Calculation Flow

Suppose the encoder produces:

$$
h_1,h_2,h_3,h_4
$$

and the current decoder state is:

$$
S_i
$$

Calculate:

$$
e_{i1}=S_i^Th_1
$$

$$
e_{i2}=S_i^Th_2
$$

$$
e_{i3}=S_i^Th_3
$$

$$
e_{i4}=S_i^Th_4
$$

Then:

$$
$$
\alpha_{i1},\alpha_{i2},\alpha_{i3},\alpha_{i4}
$$
= \text{softmax} ([e_{i1},e_{i2},e_{i3},e_{i4}])
$$

Finally:

$$
C_i= \sum_j\alpha_{ij}h_j
$$

The dot product measures how strongly the current decoder state is
related to each encoder hidden state.

If two vectors are more aligned, their dot product tends to be larger.

------------------------------------------------------------------------

# 17. Bahdanau vs Luong Attention

This distinction is extremely important.

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  Property                Bahdanau                                                       Luong
  ----------------------- -------------------------------------------------------------- --------------------------------------------------------------
  Type                    Additive Attention                                             Dot-Product / Multiplicative-style Attention

  Decoder state used for  Previous $S_{i-1}$                                            Current (S_i)
  alignment                                                                              

  Encoder representation  $h_j$                                                          $h_j$

  Score function          Learned ANN/alignment model                                    Dot product

  Score                   (e_{ij}=f(S_{i-1},h_j))                                      (e_{ij}=S_i^Th_j)

  Attention weights       (\alpha_{ij}=\text{softmax}$e_{ij}$)   (\alpha_{ij}=\text{softmax}$e_{ij}$)

  Context                 (C_i=\sum_j\alpha_{ij}h_j)                     (C_i=\sum_j\alpha_{ij}h_j)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

### The most important difference

$$
\boxed{ \text{Bahdanau: } S_{i-1},h_j \rightarrow \alpha_{ij} }
$$

$$
\boxed{ \text{Luong: } S_i,h_j \rightarrow \alpha_{ij} }
$$

Then in both:

$$
\boxed{ \alpha_{ij} \rightarrow C_i }
$$

------------------------------------------------------------------------

## 17.1 Why Luong Uses the Current State

The provided material explains that using (S_i) gives the attention
mechanism access to the decoder's updated information.

Therefore the model can dynamically adjust its attention based on the
current decoder state.

------------------------------------------------------------------------

## 17.2 Why Dot Product?

The dot product is computationally simpler than using an ANN alignment
model.

If two vectors are similar:

$$
S_i^Th_j
$$

tends to be larger.

If they are very different, the dot product tends to be smaller.

The resulting scores are passed through softmax to obtain normalized
attention weights.

------------------------------------------------------------------------

## 17.3 Location of $C_i$

The source also highlights an architectural difference:

### Bahdanau

The attention input $C_i$ is supplied to the LSTM cell.

### Luong

The attention input $C_i$ is combined with the LSTM output, then the
combined representation is passed through a feed-forward network and
softmax.

Conceptually:

### Bahdanau

``` text
Sᵢ₋₁ + yᵢ₋₁ + Cᵢ
          |
          v
       LSTM
          |
          v
       Output
```

### Luong

``` text
Previous decoder information
          |
          v
        LSTM
          |
          v
       hᵢ / output
          +
          Cᵢ
          |
          v
    Concatenate
          |
          v
Feed-Forward Network
          |
          v
       Softmax
```

------------------------------------------------------------------------

# 18. From Attention to Transformers

Attention solved the fixed context-vector problem.

The next major step was to use attention without relying on recurrent
processing.

The Transformer architecture is based on attention mechanisms rather
than recurrence.

Conceptually:

``` text
RNN/LSTM Encoder–Decoder
          |
          v
     Bottleneck
          |
          v
      Attention
          |
          v
   Transformer
```

The Transformer can process sequence positions in parallel during
training because it does not require an RNN to process each token
sequentially.

------------------------------------------------------------------------

# 19. Tokenization and Embeddings

Before attention, text is converted into tokens.

Example:

``` text
"I love cats"
```

may become:

``` text
["I", "love", "cats"]
```

Each token receives an embedding vector.

Conceptually:

``` text
"I"       → [0.2, 0.7, ...]
"love"    → [0.8, 0.1, ...]
"cats"    → [0.4, 0.6, ...]
```

Collectively, these form the input embedding matrix:

$$
E
$$

------------------------------------------------------------------------

# 20. Positional Encoding

Unlike an RNN, self-attention does not inherently impose sequential
order.

For example:

``` text
Dog bites man
```

and:

``` text
Man bites dog
```

contain the same words but have different meanings.

Therefore, position information is added to the embeddings.

The original Transformer uses sinusoidal positional encoding.

For even dimensions:

$$
\boxed{ PE_{(pos,2i)} = \sin \left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right) }
$$

For odd dimensions:

$$
\boxed{ PE_{(pos,2i+1)} = \cos \left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right) }
$$

where:

-   $pos$ = token position
-   $i$ = dimension index
-   (d_{\text{model}}) = model dimension

------------------------------------------------------------------------

# 21. Position-Aware Input Matrix $X$

The input to the attention layer is not positional encoding alone.

It is:

$$
\boxed{ X=E+PE }
$$

where:

-   $E$ = input embeddings
-   (PE) = positional encodings
-   $X$ = position-aware input representation

The flow is:

``` text
Tokens
  |
  v
Embeddings E
  +
Positional Encoding PE
  |
  v
X = E + PE
  |
  v
Attention
```

This distinction is important:

> **$X$ is the combination of the embedding matrix and positional
> encoding matrix.**

------------------------------------------------------------------------

# 22. Self-Attention

Self-attention allows tokens within the same sequence to interact.

Example:

> Money in the bank

The representation of `"bank"` can use information from `"money"` and
the surrounding words.

In self-attention:

$$
Q,K,V
$$

are generated from the **same input source**.

If the source is $X$:

$$
Q=XW_Q
$$

$$
K=XW_K
$$

$$
V=XW_V
$$

Conceptually:

``` text
                 Same X
               /   |   \
              /    |    \
            WQ     WK    WV
             |      |     |
             Q      K     V
```

------------------------------------------------------------------------

# 23. Query, Key, and Value

The three projections have different roles.

## Query

$$
Q
$$

represents what a token is looking for.

> **What information do I need?**

## Key

$$
K
$$

represents what a token can be matched by.

> **What characteristics do I provide for matching?**

## Value

$$
V
$$

contains the information that is actually aggregated.

> **What information should I provide?**

Mathematically:

$$
\boxed{ Q=XW_Q }
$$

$$
\boxed{ K=XW_K }
$$

$$
\boxed{ V=XW_V }
$$

The matrices (W_Q,W_K,W_V) are learned during training.

------------------------------------------------------------------------

# 24. Scaled Dot-Product Attention

The central Transformer attention equation is:

$$
\boxed{ \text{Attention}(Q,K,V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right)V }
$$

There are four conceptual steps.

``` text
QKᵀ
 |
 v
Raw similarity scores
 |
 v
Divide by √dₖ
 |
 v
Softmax
 |
 v
Attention weights
 |
 v
Multiply by V
 |
 v
Context-aware output
```

------------------------------------------------------------------------

## 24.1 Step 1 --- (QK^T)

$$
QK^T
$$

computes pairwise similarity between Queries and Keys.

Each row corresponds to a Query.

Each column corresponds to a Key.

------------------------------------------------------------------------

## 24.2 Step 2 --- Scaling

$$
\frac{QK^T}{\sqrt{d_k}}
$$

The scaling factor helps prevent dot-product values from becoming
excessively large, which can make softmax too sharp and hurt gradient
behavior.

------------------------------------------------------------------------

## 24.3 Step 3 --- Softmax

For a vector (x):

$$
\boxed{ \text{softmax}(x_i) = \frac{e^{x_i}} {\sum_j e^{x_j}} }
$$

Softmax converts the scores into normalized weights.

Each row sums to 1.

------------------------------------------------------------------------

## 24.4 Step 4 --- Multiply by V

The attention weights are multiplied by (V):

$$
\boxed{ Output=AttentionWeights\times V }
$$

This produces a weighted aggregation of the Value vectors.

It is better to think of this as a **weighted mixture/aggregation**
rather than a hard deletion of irrelevant information.

------------------------------------------------------------------------

# 25. Complete Self-Attention Toy Example

Assume a two-token sequence and:

$$
d_k=2
$$

------------------------------------------------------------------------

## Step 1 --- Input Embeddings

Let:

$$
E=
```{=tex}
\begin{bmatrix}
0.9&0.1\\
0.1&0.9
\end{bmatrix}
```
$$

and:

$$
PE=
```{=tex}
\begin{bmatrix}
0.1&-0.1\\
-0.1&0.1
\end{bmatrix}
```
$$

Then:

$$
X=E+PE
$$

$$
X=
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

The identity matrix is intentionally chosen to simplify the
calculations.

------------------------------------------------------------------------

## Step 2 --- Calculate Q, K, V

Let:

$$
W_Q=
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

$$
W_K=
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

$$
W_V=
```{=tex}
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
```
$$

Then:

$$
Q=XW_Q =
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

$$
K=XW_K =
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

and:

$$
V=XW_V =
```{=tex}
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
```
$$

------------------------------------------------------------------------

## Step 3 --- Calculate (QK^T)

$$
QK^T =
```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

# [

```{=tex}
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
```
$$

------------------------------------------------------------------------

## Step 4 --- Scale

Since:

$$
d_k=2
$$

$$
\sqrt{d_k}=\sqrt2\approx1.414
$$

Therefore:

$$
\frac{QK^T}{\sqrt{d_k}} \approx
```{=tex}
\begin{bmatrix}
0.707&0\\
0&0.707
\end{bmatrix}
```
$$

------------------------------------------------------------------------

## Step 5 --- Softmax

For the first row:

$$
[0.707,0]
$$

we obtain approximately:

$$
[0.67,0.33]
$$

For the second row:

$$
[0,0.707]
$$

we obtain:

$$
[0.33,0.67]
$$

Therefore:

$$
\boxed{ A= \begin{bmatrix} 0.67&0.33\\ 0.33&0.67 \end{bmatrix} }
$$

This is the attention-weight matrix.

------------------------------------------------------------------------

## Step 6 --- Multiply by V

$$
Output=AV
$$

# [

```{=tex}
\begin{bmatrix}
0.67&0.33\\
0.33&0.67
\end{bmatrix}
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
```
$$

First row:

$$
[1.66,2.66]
$$

Second row:

$$
[2.34,3.34]
$$

Therefore:

$$
\boxed{ Output= \begin{bmatrix} 1.66&2.66\\ 2.34&3.34 \end{bmatrix} }
$$

This output contains representations formed by mixing information
according to the learned attention weights.

------------------------------------------------------------------------

# 26. Multi-Head Attention

Instead of calculating attention only once, the Transformer performs
attention through multiple heads.

Each head has different learned projections and can capture different
relationships.

For head $i$:

$$
\boxed{ head_i = \text{Attention} (QW_i^Q,KW_i^K,VW_i^V) }
$$

Then:

$$
\boxed{ \text{MultiHead}(Q,K,V) = \text{Concat} (head_1,\ldots,head_h)W^O }
$$

Conceptually:

``` text
                     X
                     |
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      Head 1       Head 2       Head 3 ...
        ↓            ↓            ↓
    Attention    Attention    Attention
        ↓            ↓            ↓
        └────────────┼────────────┘
                     ↓
                Concatenate
                     ↓
                 Linear Wᴼ
                     ↓
                   Output
```

Different heads can learn different types of relationships.

------------------------------------------------------------------------

# 27. Transformer Encoder

A Transformer encoder consists of a stack of encoder blocks.

One encoder block contains:

1.  Multi-Head Self-Attention
2.  Add & Norm
3.  Feed-Forward Network
4.  Add & Norm

Conceptually:

``` text
Input X
   |
   v
Multi-Head Self-Attention
   |
   v
Residual + LayerNorm
   |
   v
Feed-Forward Network
   |
   v
Residual + LayerNorm
   |
   v
Output
```

This block is repeated (N) times.

------------------------------------------------------------------------

## 27.1 Encoder Input

The initial input is:

$$
X=E+PE
$$

This is passed to the first encoder block.

------------------------------------------------------------------------

## 27.2 Attention Output

The multi-head self-attention layer creates contextual representations.

------------------------------------------------------------------------

## 27.3 Add & Norm

The attention output is combined with its input using a residual
connection and normalized.

A simplified expression is:

$$
Z= \text{LayerNorm} \left(
X+\text{MHA}$X$ \right)
$$

------------------------------------------------------------------------

## 27.4 Feed-Forward Network

A position-wise feed-forward network then processes the representation:

$$
FFN(x)=\sigma(xW_1+b_1)W_2+b_2
$$

------------------------------------------------------------------------

## 27.5 Second Add & Norm

The result is again combined with its input and normalized:

$$
Output= \text{LayerNorm} \left( Z+FFN(Z)
\right)
$$

The output is then passed to the next encoder block.

------------------------------------------------------------------------

# 28. Transformer Decoder

A Transformer decoder block contains:

1.  Masked Multi-Head Self-Attention
2.  Add & Norm
3.  Cross-Attention
4.  Add & Norm
5.  Feed-Forward Network
6.  Add & Norm

Conceptually:

``` text
Target Embeddings
       |
       v
Masked Multi-Head
Self-Attention
       |
       v
    Add & Norm
       |
       v
Cross-Attention <----- Encoder Output
       |
       v
    Add & Norm
       |
       v
Feed-Forward Network
       |
       v
    Add & Norm
       |
       v
Linear
       |
       v
Softmax
       |
       v
Output probabilities
```

------------------------------------------------------------------------

# 29. Masked Multi-Head Self-Attention

The decoder must not see future target tokens.

Suppose the target is:

``` text
I love cats
```

The allowed attention pattern is:

``` text
             I     love     cats

I            ✓      ✗        ✗

love         ✓      ✓        ✗

cats         ✓      ✓        ✓
```

So:

-   Position 1 can only see itself.
-   Position 2 can see positions 1 and 2.
-   Position 3 can see positions 1, 2, and 3.

------------------------------------------------------------------------

## 29.1 Causal Mask

A conceptual mask is:

$$
M=
```{=tex}
\begin{bmatrix}
0&-\infty&-\infty\\
0&0&-\infty\\
0&0&0
\end{bmatrix}
```
$$

The attention becomes:

$$
\boxed{ \text{Attention} = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}}+M \right)V }
$$

Because:

$$
e^{-\infty}=0
$$

future positions receive zero attention probability.

This prevents data leakage.

------------------------------------------------------------------------

# 30. Training vs Inference

## Training

During training, the correct target sequence is known.

The decoder can receive the shifted-right target:

``` text
<START> I love cats
```

and learn:

``` text
I love cats <END>
```

The causal mask prevents each position from seeing its future answer.

Therefore the positions can be processed in parallel.

------------------------------------------------------------------------

## Inference

During inference, the future output is unknown.

The decoder generates autoregressively:

``` text
<START>
   |
   v
I
   |
   v
I love
   |
   v
I love cats
   |
   v
<END>
```

Therefore:

$$
\boxed{ \text{Training → parallelized} }
$$

$$
\boxed{ \text{Inference → autoregressive} }
$$

------------------------------------------------------------------------

# 31. Cross-Attention

Cross-attention connects the decoder to the encoder.

This is where the Q/K/V source changes.

In cross-attention:

$$
\boxed{ Q=X_{\text{decoder}}W_Q }
$$

$$
\boxed{ K=X_{\text{encoder}}W_K }
$$

$$
\boxed{ V=X_{\text{encoder}}W_V }
$$

Therefore:

``` text
Decoder
   |
   v
   Q
   |
   v
Cross-Attention
   ^
   |
 K + V
   ^
   |
Encoder
```

The decoder is effectively asking:

> **Which information from the encoded input do I need for the output I
> am currently generating?**

------------------------------------------------------------------------

# 32. Where Do Q, K, and V Come From?

This is one of the most important concepts in the entire architecture.

The answer depends on the attention layer.

------------------------------------------------------------------------

## 32.1 Encoder Self-Attention

The encoder has:

$$
X_{\text{encoder}}
$$

Then:

$$
Q=X_{\text{encoder}}W_Q
$$

$$
K=X_{\text{encoder}}W_K
$$

$$
V=X_{\text{encoder}}W_V
$$

So:

``` text
Same Encoder X
   ├── Q
   ├── K
   └── V
```

This is **self-attention**.

------------------------------------------------------------------------

## 32.2 Decoder Masked Self-Attention

The decoder has its own representation:

$$
X_{\text{decoder}}
$$

Then:

$$
Q=X_{\text{decoder}}W_Q
$$

$$
K=X_{\text{decoder}}W_K
$$

$$
V=X_{\text{decoder}}W_V
$$

All three still come from the same source.

The difference is the causal mask.

``` text
Same Decoder X
   ├── Q
   ├── K
   └── V

       +
    Causal Mask
```

------------------------------------------------------------------------

## 32.3 Decoder Cross-Attention

Now two different sources are involved.

### Query

$$
\boxed{ Q=X_{\text{decoder}}W_Q }
$$

### Key

$$
\boxed{ K=X_{\text{encoder}}W_K }
$$

### Value

$$
\boxed{ V=X_{\text{encoder}}W_V }
$$

Therefore:

``` text
Decoder X ──→ Q
                \
                 \
                  → Cross-Attention
                 /
Encoder X ──→ K,V
```

This is the most important Q/K/V distinction.

------------------------------------------------------------------------

# 33. What Is the Final Encoder Output?

A common confusion is:

> "Is (X_{\text{encoder}}) simply the output of Attention
> Weights × V?"

Not exactly.

The expression:

$$
\text{softmax} \left(
\frac{QK^T}{\sqrt{d_k}} \right)V
$$

is the output of an attention operation.

The final encoder representation is produced after passing through the
complete stack of encoder blocks.

Conceptually:

``` text
E + PE
  |
  v
Encoder Block 1
  |
  v
Encoder Block 2
  |
  v
...
  |
  v
Encoder Block N
  |
  v
Final Encoder Output
```

Within each block:

``` text
Input
  |
  v
Multi-Head Self-Attention
  |
  v
Add & Norm
  |
  v
Feed-Forward Network
  |
  v
Add & Norm
  |
  v
Block Output
```

The final encoder representation is what is supplied to the decoder's
cross-attention layer.

It becomes the source from which the decoder creates:

$$
K
$$

and:

$$
V
$$

for cross-attention.

------------------------------------------------------------------------

# 34. Where Is Cross-Attention in the Original Transformer Diagram?

The original Transformer architecture diagram labels the relevant block
simply as:

> **Multi-Head Attention**

It does not necessarily write the words "Cross-Attention."

Inside the decoder, however, there are two different attention blocks:

``` text
Decoder
   |
   v
Masked Multi-Head Attention
   |
   v
Add & Norm
   |
   v
Multi-Head Attention
   ^
   |
Encoder Output
   |
   v
Add & Norm
   |
   v
Feed-Forward
```

The **second Multi-Head Attention block** is what is commonly called
**Cross-Attention**.

Why?

Because its inputs come from two different streams:

``` text
Decoder → Q

Encoder → K
Encoder → V
```

So although the original diagram labels it "Multi-Head Attention," its
functional role is cross-attention.

------------------------------------------------------------------------

# 35. Complete Transformer Data Flow

## 35.1 Encoder

``` text
Input Tokens
     |
     v
Token Embeddings
     |
     +
Positional Encoding
     |
     v
X_encoder_initial
     |
     v
Multi-Head Self-Attention
     |
     v
Add & Norm
     |
     v
Feed-Forward
     |
     v
Add & Norm
     |
     v
Repeat N times
     |
     v
Final Encoder Output
```

Denote the final output as:

$$
X_{\text{encoder}}
$$

------------------------------------------------------------------------

## 35.2 Decoder

During training:

``` text
Target Tokens
     |
     v
Target Embeddings
     |
     +
Positional Encoding
     |
     v
Masked Multi-Head
Self-Attention
     |
     v
Add & Norm
     |
     v
Cross-Attention
     ^
     |
Encoder Output
     |
     v
Add & Norm
     |
     v
Feed-Forward
     |
     v
Add & Norm
     |
     v
Linear
     |
     v
Softmax
     |
     v
Next-token probabilities
```

------------------------------------------------------------------------

# 36. Attention Comparison Table

  ------------------------------------------------------------------------------------
  Attention         Q source    K source    V source    Mask        Main purpose
  ----------------- ----------- ----------- ----------- ----------- ------------------
  Encoder           Encoder     Encoder     Encoder     No causal   Understand
  Self-Attention                                        mask        input-token
                                                                    relationships

  Decoder Masked    Decoder     Decoder     Decoder     Yes         Understand
  Self-Attention                                                    previous/current
                                                                    target context

  Decoder           Decoder     Encoder     Encoder     No causal   Connect output
  Cross-Attention                                       target mask generation to
                                                                    input information

  Bahdanau          Decoder     ---         Encoder     ---         Dynamic alignment
  Attention         previous                hidden                  
                    state +                 states                  
                    encoder                                         
                    state used                                      
                    to                                              
                    calculate                                       
                    score                                           

  Luong Attention   Decoder     ---         Encoder     ---         Dynamic alignment
                    current                 hidden                  using simpler
                    state +                 states                  similarity
                    encoder                                         
                    state used                                      
                    to                                              
                    calculate                                       
                    score                                           
  ------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 37. Key Mathematical Formulas

## Classical Encoder

$$
\boxed{ h_t=f(W_{hh}h_{t-1}+W_{hx}x_t) }
$$

## LSTM Encoder

$$
\boxed{ (h_t,c_t)=LSTM(x_t,h_{t-1},c_{t-1}) }
$$

## Decoder Output

$$
\boxed{ y_t=\text{softmax}(W_Sh_t) }
$$

## Attention Context

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

## Bahdanau Alignment

$$
\boxed{ e_{ij}=f(S_{i-1},h_j) }
$$

$$
\boxed{ \alpha_{ij} = \text{softmax}$e_{ij}$ }
$$

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

## Luong Alignment

$$
\boxed{ e_{ij}=S_i^Th_j }
$$

$$
\boxed{ \alpha_{ij} = \text{softmax}$e_{ij}$ }
$$

$$
\boxed{ C_i=\sum_j\alpha_{ij}h_j }
$$

## Input Representation

$$
\boxed{ X=E+PE }
$$

## Self-Attention Projections

$$
\boxed{ Q=XW_Q }
$$

$$
\boxed{ K=XW_K }
$$

$$
\boxed{ V=XW_V }
$$

## Scaled Dot-Product Attention

$$
\boxed{ \text{Attention}(Q,K,V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right)V }
$$

## Multi-Head Attention

$$
\boxed{ head_i= \text{Attention} (QW_i^Q,KW_i^K,VW_i^V) }
$$

$$
\boxed{ \text{MultiHead} = \text{Concat} (head_1,\ldots,head_h)W^O }
$$

## Masked Attention

$$
\boxed{ \text{Attention} = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}}+M \right)V }
$$

## Cross-Attention

$$
\boxed{ Q=X_{\text{decoder}}W_Q }
$$

$$
\boxed{ K=X_{\text{encoder}}W_K }
$$

$$
\boxed{ V=X_{\text{encoder}}W_V }
$$

------------------------------------------------------------------------

# 38. Final Mental Model

The entire evolution can be remembered as:

``` text
                    RNN / LSTM
                 Encoder–Decoder
                       |
                       v
             Fixed Context Vector
                       |
                       v
                Bottleneck Problem
                       |
                       v
                    Attention
                       |
          ┌────────────┴────────────┐
          v                         v
      Bahdanau                    Luong
      Attention                  Attention
          |                         |
          |                         |
          └────────────┬────────────┘
                       v
                  Transformer
                       |
        ┌──────────────┼──────────────┐
        v              v              v
   Self-Attention   Multi-Head    Masked Attention
                       |
                       v
                Cross-Attention
                       |
                       v
                   Decoder
                       |
                       v
                  Prediction
```

------------------------------------------------------------------------

# 39. Exam-Ready Summary

## 39.1 Classical Encoder--Decoder

The encoder reads the input sequentially and compresses it into a fixed
context vector. The decoder uses this representation to generate the
output sequence one token at a time.

------------------------------------------------------------------------

## 39.2 Bottleneck Problem

A single fixed-size context vector must represent the entire input
sequence. For long sequences, information can be lost and there is no
explicit word-to-word alignment.

------------------------------------------------------------------------

## 39.3 Attention

Attention allows the decoder to access all encoder hidden states and
dynamically determine which ones are important for the current output.

$$
C_i=\sum_j\alpha_{ij}h_j
$$

------------------------------------------------------------------------

## 39.4 Bahdanau Attention

The alignment score depends on the **previous decoder hidden state** and
the encoder hidden state:

$$
\boxed{ e_{ij}=f(S_{i-1},h_j) }
$$

The score is calculated using a learned ANN/alignment model.

Then:

$$
e_{ij} \rightarrow \alpha_{ij} \rightarrow
C_i
$$

where:

$$
C_i=\sum_j\alpha_{ij}h_j
$$

------------------------------------------------------------------------

## 39.5 Luong Attention

The alignment score depends on the **current decoder hidden state** and
encoder hidden state:

$$
\boxed{ e_{ij}=S_i^Th_j }
$$

The dot product provides the similarity score.

Then:

$$
e_{ij} \rightarrow \alpha_{ij} \rightarrow
C_i
$$

------------------------------------------------------------------------

## 39.6 Transformer Self-Attention

In self-attention:

$$
Q,K,V
$$

come from the same input source:

$$
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
$$

------------------------------------------------------------------------

## 39.7 Masked Self-Attention

In decoder masked self-attention:

$$
Q,K,V
$$

all come from the decoder, but future tokens are masked.

------------------------------------------------------------------------

## 39.8 Cross-Attention

In decoder cross-attention:

$$
\boxed{ Q\leftarrow Decoder }
$$

$$
\boxed{ K,V\leftarrow Encoder }
$$

This is how the decoder accesses the encoder's representation of the
input sequence.

------------------------------------------------------------------------

# The Three Most Important Chains

If you remember only three things, remember these.

## Bahdanau

$$
\boxed{ S_{i-1},h_j \rightarrow e_{ij} \rightarrow \alpha_{ij} \rightarrow C_i }
$$

with:

$$
e_{ij}=f(S_{i-1},h_j)
$$

------------------------------------------------------------------------

## Luong

$$
\boxed{ S_i,h_j \rightarrow e_{ij} \rightarrow \alpha_{ij} \rightarrow C_i }
$$

with:

$$
e_{ij}=S_i^Th_j
$$

------------------------------------------------------------------------

## Transformer Self-Attention

$$
\boxed{ X \rightarrow Q,K,V \rightarrow QK^T \rightarrow \frac{QK^T}{\sqrt{d_k}} \rightarrow Softmax \rightarrow Attention\ Weights \rightarrow V \rightarrow Output }
$$

And for Transformer cross-attention:

$$
\boxed{ X_{\text{decoder}}\rightarrow Q }
$$

$$
\boxed{ X_{\text{encoder}}\rightarrow K,V }
$$

These distinctions form the conceptual bridge from classical
sequence-to-sequence models to modern Transformer architectures.
