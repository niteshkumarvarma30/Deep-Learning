# PyTorch Practice

This folder contains hands-on PyTorch implementations of the deep learning concepts covered in the theoretical notes.

## Learning Roadmap

`	ext
                          PYTORCH
                            │
                            ▼
              ┌────────────────────────┐
              │ PHASE 1: FOUNDATIONS   │
              └────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Tensors          Tensor Shapes      Operations
          │
          ▼
    Matrix Multiplication
          │
          ▼
       Autograd
          │
          ▼
      Computational
          Graph
          │
          ▼
       Backpropagation
          │
          ▼
       nn.Module
          │
          ▼
       nn.Linear
          │
          ▼
    Activation Functions
          │
          ▼
     Loss Functions
          │
          ▼
       Optimizers
          │
          ▼
    Training Loop
          │
          ▼
══════════════════════════════════════════════════
              PHASE 2: ANN
══════════════════════════════════════════════════
          │
          ▼
       Perceptron
          │
          ▼
   Multi-Layer Perceptron
          │
          ▼
   Forward Propagation
          │
          ▼
    Backpropagation
          │
          ▼
      ANN Training
          │
          ▼
══════════════════════════════════════════════════
              PHASE 3: CNN
══════════════════════════════════════════════════
          │
          ▼
      Image Tensors
          │
          ▼
        Conv2D
          │
          ▼
      Filters / Kernels
          │
          ▼
      Feature Maps
          │
          ▼
        Pooling
          │
          ▼
        Flatten
          │
          ▼
        CNN Model
          │
          ▼
══════════════════════════════════════════════════
              PHASE 4: RNN
══════════════════════════════════════════════════
          │
          ▼
      Sequence Tensors
          │
          ▼
       RNN Cell
          │
          ▼
      Hidden State
          │
          ▼
         RNN
          │
          ▼
        LSTM
          │
          ▼
         GRU
          │
          ▼
   Autoregressive Generation
          │
          ▼
══════════════════════════════════════════════════
          PHASE 5: ATTENTION
══════════════════════════════════════════════════
          │
          ▼
    Encoder–Decoder
          │
          ▼
   Bottleneck Problem
          │
          ▼
      Attention
          │
       ┌──┴──┐
       ▼     ▼
  Bahdanau  Luong
       │     │
       ▼     ▼
 Alignment Scores
       │
       ▼
      αᵢⱼ
       │
       ▼
      Cᵢ
   Context Vector
          │
          ▼
══════════════════════════════════════════════════
        PHASE 6: TRANSFORMERS
══════════════════════════════════════════════════
          │
          ▼
       Tokenization
          │
          ▼
       Embeddings
          │
          ▼
   Positional Encoding
          │
          ▼
       X = E + PE
          │
          ▼
       Query / Key / Value
          │
          ▼
    Q = XWQ
    K = XWK
    V = XWV
          │
          ▼
   QKᵀ / √dₖ
          │
          ▼
       Softmax
          │
          ▼
     Attention Weights
          │
          ▼
       × V
          │
          ▼
    Self-Attention
          │
          ▼
   Multi-Head Attention
          │
          ▼
 Masked Multi-Head Attention
          │
          ▼
    Cross-Attention
          │
          ▼
      Transformer
`
