import os
import re

# Directory containing the templates
TEMPLATE_DIR = 'e:/development/kelstechsystems/templates'

def convert_classes(content):
    """
    Converts hardcoded dark classes to handle both light and dark modes.
    e.g., bg-dark-900 -> bg-slate-50 dark:bg-dark-900
    e.g., text-white -> text-slate-900 dark:text-white
    e.g., text-gray-300 -> text-gray-600 dark:text-gray-300
    """
    
    # 1. Background colors
    # Use negative lookbehind to avoid double-processing already dark: prefixed classes
    # Also handle opacities FIRST to avoid base classes matching them
    
    # Background with opacity (handling these first)
    content = re.sub(r'(?<!dark:)\bbg-dark-950/(\d+)\b', r'bg-slate-200/\1 dark:bg-dark-950/\1', content)
    content = re.sub(r'(?<!dark:)\bbg-dark-900/(\d+)\b', r'bg-white/\1 dark:bg-dark-900/\1', content)
    content = re.sub(r'(?<!dark:)\bbg-dark-800/(\d+)\b', r'bg-slate-50/\1 dark:bg-dark-800/\1', content)

    # Base backgrounds (using negative lookahead for / to avoid matching opacity variants twice)
    content = re.sub(r'(?<!dark:)\bbg-dark-950(?!/)\b', 'bg-slate-100 dark:bg-dark-950', content)
    content = re.sub(r'(?<!dark:)\bbg-dark-900(?!/)\b', 'bg-white dark:bg-dark-900', content)
    content = re.sub(r'(?<!dark:)\bbg-dark-800(?!/)\b', 'bg-white dark:bg-dark-900', content) # User wanted darker backgrounds
    
    # Gradients
    content = re.sub(r'(?<!dark:)\bfrom-dark-950\b', 'from-slate-100 dark:from-dark-950', content)
    content = re.sub(r'(?<!dark:)\bto-dark-950\b', 'to-slate-100 dark:to-dark-950', content)
    content = re.sub(r'(?<!dark:)\bfrom-dark-900\b', 'from-white dark:from-dark-900', content)
    content = re.sub(r'(?<!dark:)\bvia-dark-900\b', 'via-white dark:via-dark-900', content)
    content = re.sub(r'(?<!dark:)\bto-dark-900\b', 'to-white dark:to-dark-900', content)
    content = re.sub(r'(?<!dark:)\bfrom-dark-800\b', 'from-white dark:from-dark-900', content)
    content = re.sub(r'(?<!dark:)\bto-dark-800\b', 'to-white dark:to-dark-900', content)

    # 2. Text colors
    content = re.sub(r'(?<!dark:)\btext-white\b', 'text-slate-900 dark:text-white', content)
    content = re.sub(r'(?<!dark:)\btext-gray-300\b', 'text-gray-600 dark:text-gray-300', content)
    content = re.sub(r'(?<!dark:)\btext-gray-400\b', 'text-gray-500 dark:text-gray-400', content)
    
    # 3. Border colors - REMOVE WHITE BORDERS for Dark Mode
    # Replace light borders with transparent or very subtle dark borders in dark mode
    content = re.sub(r'(?<!dark:)\bborder-gray-200\b', 'border-gray-200 dark:border-transparent', content)
    content = re.sub(r'(?<!dark:)\bborder-gray-300\b', 'border-gray-300 dark:border-gray-800', content)
    content = re.sub(r'(?<!dark:)\bborder-white/(\d+)\b', r'border-gray-200/\1 dark:border-transparent', content)
    content = re.sub(r'(?<!dark:)\bborder-slate-200\b', 'border-slate-200 dark:border-transparent', content)
    
    # Cleanup: Fix accidental double dark prefixes or incorrect light classes inside dark:
    content = re.sub(r'dark:bg-(white|slate-\d+)(/\d+)?\b', '', content)
    content = re.sub(r'dark:text-(slate-\d+|gray-\d+)(/\d+)?\b', '', content)
    content = re.sub(r'dark:border-(slate-\d+|gray-\d+|white|gray|slate)(/\d+)?\b', '', content)
    
    # Clean up double dark prefixes like dark:dark:
    content = re.sub(r'dark:dark:', 'dark:', content)
    
    # Fix semi-transparent dark backgrounds on sections/divs that should be solid
    # This addresses the "grey" issue reported by the user
    content = re.sub(r'\bdark:bg-dark-900/50\b', 'dark:bg-dark-900', content)
    content = re.sub(r'\bdark:bg-dark-800/50\b', 'dark:bg-dark-800', content)
    
    # 4. Prose colors (Typography plugin)
    # Ensure dark:prose-invert is present if prose is present
    if 'prose' in content and 'dark:prose-invert' not in content:
        content = re.sub(r'\bprose\b', 'prose dark:prose-invert', content)
    
    return content

def process_templates():
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                new_content = convert_classes(content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file}")

if __name__ == '__main__':
    print("Starting template conversion for light/dark mode...")
    process_templates()
    print("Conversion complete.")
