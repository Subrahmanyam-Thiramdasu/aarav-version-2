import os

files_to_fix = [
    'about.html',
    'blog.html',
    'contact.html',
    'privacy-policy.html',
    'terms.html',
    'blog/back-pain-desk-job.html',
    'blog/child-development-milestones.html',
    'blog/speech-delay.html',
    'blog/stroke-recovery.html'
]

for f in files_to_fix:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace('logo-white.png', 'logo.png" style="filter: brightness(0) invert(1);')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed logo in {f}')
