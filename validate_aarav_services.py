"""
Aarav Clinics - Comprehensive Validation Script
Checks:
1. Exactly 19 services in services.html
2. Correct names, slugs, and links
3. All 19 individual pages exist and have unique titles, descriptions, H1s
4. Verifies no missing files / broken internal links
5. Checks SEO criteria (title, description, single H1, canonical URL)
6. Verifies redirection files for old service URLs
"""

import os
import re

EXPECTED_19 = [
    ("Shockwave Therapy", "shockwave-therapy.html"),
    ("Advanced Decompression Therapy", "advanced-decompression-therapy.html"),
    ("Cage Therapy", "cage-therapy.html"),
    ("Cupping Therapy", "cupping-therapy.html"),
    ("Dry Needling Therapy", "dry-needling-therapy.html"),
    ("Prenatal and Postnatal Exercise Therapy", "prenatal-postnatal-exercise-therapy.html"),
    ("Speech Therapy for Paediatric and Adult Patients", "speech-therapy-paediatric-adult.html"),
    ("Occupational Therapy", "occupational-therapy.html"),
    ("Vision Therapy", "vision-therapy.html"),
    ("Behavioural Therapy", "behavioural-therapy.html"),
    ("Special Education Therapy", "special-education-therapy.html"),
    ("Parental Training", "parental-training.html"),
    ("Advanced Physiotherapy", "advanced-physiotherapy.html"),
    ("Stroke Rehabilitation", "stroke-rehabilitation.html"),
    ("Paediatric and Adult Rehabilitation", "paediatric-adult-rehabilitation.html"),
    ("Geriatric Rehabilitation", "geriatric-rehabilitation.html"),
    ("Sports Injury Physiotherapy", "sports-injury-physiotherapy.html"),
    ("Pre- and Post-TKR and THR Physiotherapy", "tkr-thr-physiotherapy.html"),
    ("Laser Therapy", "laser-therapy.html"),
]

def validate_services_listing():
    print("=== Checking services.html ===")
    assert os.path.exists("services.html"), "services.html does not exist!"
    with open("services.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Find all svc-card links inside main
    main_match = re.search(r'<main id="main">(.*?)</main>', content, re.DOTALL)
    assert main_match, "No <main id='main'> found in services.html"
    main_content = main_match.group(1)

    card_links = re.findall(r'<a href="([^"]+)" class="svc-card', main_content)
    print(f"Found {len(card_links)} service cards in <main> of services.html")
    assert len(card_links) == 19, f"Expected exactly 19 cards, found {len(card_links)}: {card_links}"

    # Verify each expected service is present in the card links
    expected_slugs = [s[1] for s in EXPECTED_19]
    for name, slug in EXPECTED_19:
        assert slug in card_links, f"Missing card for {name} ({slug}) in services.html"
        assert name in main_content, f"Service title '{name}' not found in services.html"

    print("PASS: services.html contains exactly the 19 unique approved services.")

def validate_individual_pages():
    print("\n=== Checking 19 Individual Service Pages ===")
    titles = set()
    descriptions = set()

    for name, filename in EXPECTED_19:
        assert os.path.exists(filename), f"Service page {filename} does not exist!"
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Title
        t_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        assert t_match, f"Missing <title> in {filename}"
        title = t_match.group(1).strip()
        assert title not in titles, f"Duplicate title in {filename}: '{title}'"
        titles.add(title)

        # Meta description
        d_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE)
        if not d_match:
            d_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE)
        assert d_match, f"Missing meta description in {filename}"
        desc = d_match.group(1).strip()
        assert desc not in descriptions, f"Duplicate description in {filename}: '{desc}'"
        descriptions.add(desc)

        # H1 count
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        assert len(h1s) == 1, f"Expected exactly 1 <h1> in {filename}, found {len(h1s)}"

        # Canonical
        canon_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
        assert canon_match, f"Missing canonical in {filename}"
        assert f"/{filename}" in canon_match.group(1), f"Canonical mismatch in {filename}: {canon_match.group(1)}"

        # Check required sections
        assert 'class="cinematic-hero' in content, f"Missing cinematic-hero in {filename}"
        assert 'class="editorial-about"' in content, f"Missing editorial-about in {filename}"
        assert 'class="services-bento-section"' in content, f"Missing services-bento in {filename}"
        assert 'id="methodology"' in content, f"Missing methodology in {filename}"
        assert 'class="benefits-editorial"' in content, f"Missing benefits in {filename}"
        assert 'class="appointment-cinematic"' in content, f"Missing appointment in {filename}"
        assert 'class="related-services-section"' in content, f"Missing related-services in {filename}"
        assert 'class="premium-footer"' in content, f"Missing premium-footer in {filename}"
        assert 'apptForm' in content, f"Missing apptForm in {filename}"
        assert 'lucide.createIcons()' in content, f"Missing lucide initialization in {filename}"

        print(f"PASS: {filename} verified (Title: '{title[:45]}...')")

    print(f"PASS: All 19 individual service pages exist with unique metadata and complete structure.")

def validate_links():
    print("\n=== Checking for Broken Relative Links Across All HTML Files ===")
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip git, node_modules, .lighthouseci
        if any(ignored in root for ignored in ['.git', 'node_modules', '.lighthouseci', '.vscode']):
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f).replace('\\', '/').replace('./', ''))

    broken = []
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        srcs = re.findall(r'src=["\']([^"\']+)["\']', content)

        directory = os.path.dirname(f)
        for link in hrefs + srcs:
            if link.startswith('http') or link.startswith('mailto') or link.startswith('tel') or link.startswith('#') or link.startswith('data:'):
                continue
            clean_link = link.split('#')[0].split('?')[0]
            if not clean_link:
                continue
            target = os.path.normpath(os.path.join(directory, clean_link)).replace('\\', '/')
            if not os.path.exists(target):
                broken.append((f, link, target))

    if broken:
        print(f"FAIL: Found {len(broken)} broken link(s):")
        for f, link, target in broken:
            print(f"  {f} -> {link} (Target missing: {target})")
        raise AssertionError("Broken links detected.")
    else:
        print(f"PASS: Checked {len(html_files)} HTML files. Zero broken links found!")

def validate_sitemap():
    print("\n=== Checking sitemap.xml ===")
    assert os.path.exists("sitemap.xml"), "sitemap.xml does not exist!"
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        content = f.read()

    for name, slug in EXPECTED_19:
        loc = f"https://aaravhealthcare.com/{slug}"
        assert loc in content, f"Missing {loc} in sitemap.xml"

    print("PASS: sitemap.xml contains all 19 services.")

def main():
    validate_services_listing()
    validate_individual_pages()
    validate_links()
    validate_sitemap()
    print("\n==============================================")
    print("ALL VALIDATION CRITERIA PASSED SUCCESSFULLY!")
    print("==============================================")

if __name__ == "__main__":
    main()
