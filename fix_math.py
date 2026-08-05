import os
import re

directories = [
    r"ANN\Multi-Level Perceptron\Unit 1 - Introduction to Neural Networks",
    r"ANN\Multi-Level Perceptron\Unit 4 - Learning in Neural Networks",
    r"ANN\Multi-Level Perceptron\Unit 5 - Training Challenges & Solutions"
]

files_to_fix = [
    "Chapter 5 - Activation Functions - Part 1 - Introduction to Activation Functions.md",
    "Chapter 5 - Activation Functions - Part 2 - Sigmoid and Tanh.md",
    "Chapter 5 - Activation Functions - Part 3 - ReLU and its Variants.md",
    "Chapter 5 - Activation Functions - Part 4 - The Dying ReLU Problem.md",
    "Chapter 5 - Activation Functions - Part 5 - Softmax Activation Function.md",
    "Chapter 4 - Optimization via Memoization.md",
    "Chapter 7 - Weight Initialization - Part 1 - Zero Initialization and its Failures.md",
    "Chapter 7 - Weight Initialization - Part 2 - Random, Xavier, and He Initialization.md",
    "Chapter 8 - Batch Normalization - Part 1 - Internal Covariate Shift and Batch Normalization.md",
    "Chapter 9 - Regularization - Part 1 - Generalization (Overfitting and Underfitting).md",
    "Chapter 9 - Regularization - Part 2 - Mathematical Regularization (L1 and L2).md",
    "Chapter 9 - Regularization - Part 3 - Dropout Layers.md"
]

# Create a set of basenames for quick lookup
target_files = set(files_to_fix)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace inline math \( ... \) with $ ... $
    content = content.replace(r'\(', '$')
    content = content.replace(r'\)', '$')

    # 2. Fix $$ block spacing
    # Ensure empty line before $$
    content = re.sub(r'([^\n])\n\$\$', r'\1\n\n$$', content)
    # Ensure empty line after $$
    content = re.sub(r'\$\$\n([^\n])', r'$$\n\n\1', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for d in directories:
    dir_path = os.path.join(r"c:\AI\Deep Learning", d)
    if not os.path.exists(dir_path):
        continue
    for f in os.listdir(dir_path):
        if f in target_files:
            process_file(os.path.join(dir_path, f))

print("Fixed math formatting in all files.")
