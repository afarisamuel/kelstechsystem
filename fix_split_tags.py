import os
import re

TEMPLATE_DIR = 'e:/development/kelstechsystems/templates'

def fix_split_tags(content):
    # Pattern to find {% ... %} that are split across lines
    # We look for {% then anything that doesn't contain %} including newlines then %}
    # Use re.DOTALL to let . match newlines
    
    def join_tag(match):
        tag = match.group(0)
        # Collapse multiple spaces and newlines into a single space
        return re.sub(r'\s+', ' ', tag)

    # First, let's fix the specific testimonial rating if/else which is very nested
    # It's better to just join anything starting with {% and ending with %}
    
    new_content = re.sub(r'\{%[^%]*%\}', join_tag, content, flags=re.DOTALL)
    
    # Also fix split {{ ... }}
    new_content = re.sub(r'\{\{[^}]*\}\}', join_tag, new_content, flags=re.DOTALL)
    
    return new_content

def main():
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                print(f"Processing {file}...")
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fixed_content = fix_split_tags(content)
                
                if fixed_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    print(f"  Fixed split tags in {file}")

if __name__ == '__main__':
    main()
