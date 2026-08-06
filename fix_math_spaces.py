import os
import re

target_dir = r"c:\AI\Deep Learning\CNN\CNN CampusX"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find $ followed by space(s), some content, space(s), and $
    # It replaces it by removing the leading and trailing spaces inside the $...$
    new_content = re.sub(r'\$\s+([^$]+?)\s+\$', r'$\1$', content)
    
    # Also handle cases where there is space only on one side:
    # e.g., `$ p = 1$` -> `$p = 1$`
    new_content = re.sub(r'\$\s+([^$]+?)\$', r'$\1$', new_content)
    # e.g., `$p = 1 $` -> `$p = 1$`
    new_content = re.sub(r'\$([^$]+?)\s+\$', r'$\1$', new_content)

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.md'):
            process_file(os.path.join(root, file))

print("Math spacing fix complete.")
