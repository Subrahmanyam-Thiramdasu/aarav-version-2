import os
import re

def normalize_hero_styles():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Remove inline font-size, line-height, letter-spacing from hero-giant-title
        content = re.sub(
            r'(<h1[^>]*class="[^"]*hero-giant-title[^"]*"[^>]*style="[^"]*)(font-size:[^;]+;?\s*|line-height:[^;]+;?\s*|letter-spacing:[^;]+;?\s*)+([^"]*")',
            r'\1\3',
            content
        )
        # Clean up empty style attributes if any
        content = re.sub(r'style="\s*"', '', content)

        # Remove inline max-width, font-size from hero paragraphs (typically .gsap-reveal-up right after title)
        # It's tricky to target exactly without parser, let's just leave max-width as it defines composition, 
        # but normalize font-sizes
        content = re.sub(
            r'(<p[^>]*class="[^"]*gsap-reveal-up[^"]*"[^>]*style="[^"]*)(font-size:[^;]+;?\s*|line-height:[^;]+;?\s*)+([^"]*")',
            r'\1\3',
            content
        )
        content = re.sub(r'style="\s*"', '', content)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Normalized inline font styles in {file}")

if __name__ == "__main__":
    normalize_hero_styles()
