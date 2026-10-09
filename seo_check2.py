import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f).replace('\\', '/').replace('./', ''))

issues = []
titles = set()
descriptions = set()

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Title
    t_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if not t_match:
        issues.append(f"{f}: Missing <title>")
    else:
        t = t_match.group(1).strip()
        if t in titles:
            issues.append(f"{f}: Duplicate <title> '{t}'")
        titles.add(t)
        
    # Description
    d_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not d_match:
        # Check alternative attribute order
        d_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
        
    if not d_match:
        issues.append(f"{f}: Missing meta description")
    else:
        d = d_match.group(1).strip()
        if d in descriptions:
            issues.append(f"{f}: Duplicate meta description '{d}'")
        descriptions.add(d)
        
    # H1
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1_matches) == 0:
        issues.append(f"{f}: Missing <h1>")
    elif len(h1_matches) > 1:
        issues.append(f"{f}: Multiple <h1> tags found ({len(h1_matches)})")

if issues:
    print("SEO Issues Found:")
    for i in issues:
        print(i)
else:
    print("No critical SEO issues found.")
