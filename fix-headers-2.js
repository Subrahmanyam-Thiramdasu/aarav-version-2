const fs = require('fs');

const aboutContent = fs.readFileSync('about.html', 'utf8');
const headerMatch = aboutContent.match(/<header class="site-header" id="siteHeader">[\s\S]*?<\/header>/);
if (!headerMatch) { console.error('No header found in about'); process.exit(1); }
const fullHeader = headerMatch[0];

const mobileMenuMatch = aboutContent.match(/<nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation" aria-hidden="true">[\s\S]*?<\/nav>/);
const fullMobileMenu = mobileMenuMatch ? mobileMenuMatch[0] : '';

function fixPage(file, themeClass, isActiveStr) {
  let content = fs.readFileSync(file, 'utf8');
  
  // Custom header with active state
  let customizedHeader = fullHeader.replace(
    '<header class="site-header" id="siteHeader">',
    `<header class="site-header theme-transparent ${themeClass}" id="siteHeader">`
  );
  
  // Clear any existing active links
  customizedHeader = customizedHeader.replace(/class="nav-link is-active"/g, 'class="nav-link"');
  // Set new active link based on isActiveStr (naive implementation)
  if (isActiveStr) {
     customizedHeader = customizedHeader.replace(`">${isActiveStr}</a>`, ` is-active">${isActiveStr}</a>`);
  } else {
     customizedHeader = customizedHeader.replace(`>Services\n`, ` is-active">Services\n`);
  }
  
  if (content.includes('<header class="cinematic-header" id="siteHeader">')) {
     content = content.replace(/<header class="cinematic-header" id="siteHeader">[\s\S]*?<\/header>/, customizedHeader);
  } else if (content.includes('<header class="site-header" id="siteHeader">')) {
     content = content.replace(/<header class="site-header" id="siteHeader">[\s\S]*?<\/header>/, customizedHeader);
  } else if (content.includes('<header class="site-header theme-transparent')) {
     content = content.replace(/<header class="site-header theme-transparent[^>]*>[\s\S]*?<\/header>/, customizedHeader);
  }
  
  if (!content.includes('class="mobile-menu" id="mobileMenu"')) {
     content = content.replace('</header>', '</header>\n\n<!-- Mobile Menu -->\n' + fullMobileMenu);
  }
  
  fs.writeFileSync(file, content);
  console.log('Fixed header in', file);
}

const pagesToFix = [
  { f: 'home-physiotherapy.html', t: 'theme-light' },
  { f: 'post-surgical-rehabilitation.html', t: 'theme-light' },
  { f: 'stroke-rehabilitation.html', t: 'theme-dark' },
  { f: 'index.html', t: 'theme-dark', active: 'Home' },
  { f: 'laser-therapy.html', t: 'theme-dark' },
  { f: 'sports-rehabilitation.html', t: 'theme-dark' },
  { f: 'chiropractic.html', t: 'theme-light' },
  { f: 'physiotherapy.html', t: 'theme-light' }
];

pagesToFix.forEach(p => {
  try { fixPage(p.f, p.t, p.active); } catch (e) { console.log('Error on', p.f, e); }
});
