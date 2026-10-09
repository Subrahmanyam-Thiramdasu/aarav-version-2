import json
import sys

def parse_lh(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    categories = data.get('categories', {})
    
    perf = categories.get('performance', {}).get('score', 0) * 100
    a11y = categories.get('accessibility', {}).get('score', 0) * 100
    bp = categories.get('best-practices', {}).get('score', 0) * 100
    seo = categories.get('seo', {}).get('score', 0) * 100
    
    audits = data.get('audits', {})
    lcp = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
    cls = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')
    tbt = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
    
    print(f"Performance: {perf:.0f}")
    print(f"Accessibility: {a11y:.0f}")
    print(f"Best Practices: {bp:.0f}")
    print(f"SEO: {seo:.0f}")
    print(f"LCP: {lcp}")
    print(f"CLS: {cls}")
    print(f"TBT: {tbt}")

if __name__ == '__main__':
    parse_lh(sys.argv[1])
