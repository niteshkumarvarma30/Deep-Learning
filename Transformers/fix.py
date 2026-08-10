import re

with open(r'c:\AI\Deep Learning\Transformers\Transformers_Complete_Notes_v2.md', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to find block math that has an opening $$ but is missing a closing $$.
# Because my previous script deleted trailing $$ by mistake (PowerShell ate the $$ in the string).
# Specifically, any line that starts with $$ and opens a block, the end of the block should be closed.
# Wait, it's easier to just run the flawless fix.py again from scratch on orig.md, 
# and then apply the `< t}` fix safely inside a python script!

import subprocess
out = subprocess.check_output(['git', 'show', '6e7344e:Transformers/Transformers_Complete_Notes_v2.md'], shell=False)
text = out.decode('utf-8')

# 1. Strip `...`{=tex} wrappers
text = re.sub(r'`([^`]+)`\{=tex\}', r'\1', text)
text = re.sub(r'\{=tex\}', '', text)

# 2. Block math \[ \]
text = re.sub(r'^\\\[\s*', '$$\n', text, flags=re.MULTILINE)
# For \], it can be at the end of a line, so we replace \s*\]$ with \n$$
text = re.sub(r'\s*\\\]$', '\n$$', text, flags=re.MULTILINE)

# Some might be inline block math like `\[ \alpha \]`
text = re.sub(r'\\\[', '$$', text)
text = re.sub(r'\\\]', '$$', text)

# Now, collapse nested `$$` which happen when pandoc has `\[ \[ \alpha \] \]`
text = re.sub(r'\$\$\s*\$\$', '$$', text)

# 3. Inline math \( \) -> $
text = text.replace(r'\(', '$')
text = text.replace(r'\)', '$')

# 4. Remove escaping for other symbols
text = text.replace(r'\|', '|')
text = text.replace(r'\_', '_')
text = text.replace(r'\^', '^')
text = text.replace(r'\<', '<')
text = text.replace(r'\>', '>')

# 5. Fix pandoc turning _ into * inside math
text = re.sub(r'\*\{([^}]+)\}', r'_{\1}', text)
text = text.replace(r'y*{', r'y_{')
text = text.replace(r'*k', r'_k') 
text = text.replace(r'*i', r'_i') 
text = text.replace(r'*j', r'_j')
text = text.replace(r'*t', r'_t')

# 6. Change \operatorname{...} to \text{...}
text = re.sub(r'\\operatorname\{([^}]+)\}', r'\\text{\1}', text)

# 7. Remove newlines inside \boxed{ ... }
def process_boxes(t):
    out_chars = []
    i = 0
    while i < len(t):
        if t[i:i+7] == r'\boxed{':
            out_chars.append(r'\boxed{')
            i += 7
            depth = 1
            while i < len(t) and depth > 0:
                if t[i] == '{': depth += 1
                elif t[i] == '}': depth -= 1
                
                # Replace newline with space inside boxed
                if t[i] == '\n':
                    out_chars.append(' ')
                else:
                    out_chars.append(t[i])
                i += 1
        else:
            out_chars.append(t[i])
            i += 1
    return "".join(out_chars)

text = process_boxes(text)

# 8. Wrap known loose variables in parenthesis
math_vars = [
    r'X', r'Y', r'y_t', r't', r'y_{<t}', r'x_t', r'h_t', r'h_{t-1}',
    r'W_{hh}', r'W_{hx}', r'f', r'C_i', r'd_h', r'S_{i-1}', r'h_j',
    r'e_{ij}', r'j', r'h_T', r'h_1', r'h_2', r'h_3', r'h_4',
    r'h_0^{dec}', r'h_4^{enc}', r'c_0^{dec}', r'c_4^{enc}', r'c_t', r'c_{t-1}',
    r'i', r'pos', r'd_{\text{model}}'
]
for var in math_vars:
    escaped_var_match = var.replace('{', r'\{').replace('}', r'\}').replace('<', r'\<').replace('^', r'\^')
    text = re.sub(r'(?<!\$)\(' + escaped_var_match + r'\)(?!\$)', f'${var}$', text)

# 9. Fix <t issue causing unclosed braces in KaTeX/MathJax by adding a space: `< t`
text = text.replace('<t}', '< t}')

with open(r'c:\AI\Deep Learning\Transformers\Transformers_Complete_Notes_v2.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Final flawless fix applied!")
