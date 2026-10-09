import os
import re
from bs4 import BeautifulSoup

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
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    title = soup.find('title')
    title_text = title.text.strip() if title else None
    
    desc = soup.find('meta', attrs={'name': 'description'})
    desc_text = desc.get('content').strip() if desc and desc.get('content') else None
    
    h1s = soup.find_all('h1')
    
    if not title_text:
        issues.append(f"{f}: Missing <title>")
    else:
        if title_text in titles:
            issues.append(f"{f}: Duplicate <title> '{title_text}'")
        titles.add(title_text)
        
    if not desc_text:
        issues.append(f"{f}: Missing meta description")
    else:
        if desc_text in descriptions:
            issues.append(f"{f}: Duplicate meta description '{desc_text}'")
        descriptions.add(desc_text)
        
    if len(h1s) == 0:
        issues.append(f"{f}: Missing <h1>")
    elif len(h1s) > 1:
        issues.append(f"{f}: Multiple <h1> tags found ({len(h1s)})")

if issues:
    print("SEO Issues Found:")
    for i in issues:
        print(i)
else:
    print("No critical SEO issues found.")
