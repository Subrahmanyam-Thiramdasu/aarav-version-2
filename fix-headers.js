const fs = require('fs');

const physiocontent = fs.readFileSync('physiotherapy.html', 'utf8');
const headerMatch = physiocontent.match(/<header class="site-header" id="siteHeader">[\s\S]*?<\/header>/);
if (!headerMatch) { console.error('No header found in physio'); process.exit(1); }

const fullHeader = headerMatch[0];
const mobileMenuMatch = physiocontent.match(/<nav class="mobile-menu" id="mobileMenu" aria-label="Mobile navigation" aria-hidden="true">[\s\S]*?<\/nav>/);
const fullMobileMenu = mobileMenuMatch ? mobileMenuMatch[0] : '';

function fixPage(file, themeClass) {
  let content = fs.readFileSync(file, 'utf8');
  
  const headerReplacement = fullHeader.replace(
    '<header class="site-header" id="siteHeader">',
    `<header class="site-header theme-transparent ${themeClass}" id="siteHeader">`
  );
  
  // Replace cinematic-header or site-header
  if (content.includes('<header class="cinematic-header" id="siteHeader">')) {
     content = content.replace(/<header class="cinematic-header" id="siteHeader">[\s\S]*?<\/header>/, headerReplacement);
  } else if (content.includes('<header class="site-header" id="siteHeader">')) {
     content = content.replace(/<header class="site-header" id="siteHeader">[\s\S]*?<\/header>/, headerReplacement);
  }
  
  // Also make sure mobile menu is present and updated if we replaced cinematic header
  if (!content.includes('class="mobile-menu" id="mobileMenu"')) {
     content = content.replace('</header>', '</header>\n\n<!-- Mobile Menu -->\n' + fullMobileMenu);
  }
  
  fs.writeFileSync(file, content);
  console.log('Fixed header in', file);
}

fixPage('home-physiotherapy.html', 'theme-light');
fixPage('post-surgical-rehabilitation.html', 'theme-light');
fixPage('stroke-rehabilitation.html', 'theme-dark');
fixPage('index.html', 'theme-dark');
fixPage('laser-therapy.html', 'theme-dark');
fixPage('sports-rehabilitation.html', 'theme-dark');
fixPage('chiropractic.html', 'theme-light');
