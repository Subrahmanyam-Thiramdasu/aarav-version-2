import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f).replace('\\', '/').replace('./', ''))

print(f'Found {len(html_files)} HTML files.')

links = {}
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
        links[f] = hrefs + srcs

broken = []
for f, file_links in links.items():
    directory = os.path.dirname(f)
    for link in file_links:
        if link.startswith('http') or link.startswith('mailto') or link.startswith('tel') or link.startswith('#'):
            continue
        # strip hash and query
        link_clean = link.split('#')[0].split('?')[0]
        if not link_clean: continue
        
        target = os.path.normpath(os.path.join(directory, link_clean)).replace('\\', '/')
        if not os.path.exists(target):
            broken.append((f, link, target))

for f, link, target in broken:
    print(f'{f}: Broken link -> {link}')
if not broken:
    print('No broken links found!')
