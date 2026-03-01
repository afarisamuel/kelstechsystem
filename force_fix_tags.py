import os
import re

TEMPLATE_DIR = 'e:/development/kelstechsystems/templates'

def force_join_tags(content):
    # Join {{ ... }}
    # Match {{ followed by any whitespace including newlines, then non-braces, then any whitespace including newlines, then }}
    def join_match(match):
        return re.sub(r'\s+', ' ', match.group(0))

    content = re.sub(r'\{\{.*?\}\}', join_match, content, flags=re.DOTALL)
    content = re.sub(r'\{%.*?%\}', join_match, content, flags=re.DOTALL)
    return content

def main():
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = force_join_tags(content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8', newline='\n') as f:
                        f.write(new_content)
                    print(f"Fixed {file}")

if __name__ == '__main__':
    main()
