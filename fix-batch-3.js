const fs = require('fs');
const files = ['child-development.html', 'pediatric-physiotherapy.html', 'speech-therapy.html'];
const template = fs.readFileSync('physiotherapy.html', 'utf8');
const headerMatch = template.match(/<header class="site-header.*?" id="siteHeader">[\s\S]*?<\/nav>/);
if (!headerMatch) {
    console.error('Header not found in index.html');
    process.exit(1);
}
let fullHeader = headerMatch[0];
// replace theme-transparent with theme-light for these child pages
fullHeader = fullHeader.replace('class="site-header theme-transparent"', 'class="site-header theme-light"');

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  let c = fs.readFileSync(f, 'utf8');
  
  // replace old header + mobile menu with the new standard one
  c = c.replace(/<header class="site-header"[\s\S]*?<\/nav>/, fullHeader);
  
  // Update active links based on filename
  c = c.replace(/class="nav-link is-active"/g, 'class="nav-link"');
  if (f === 'child-development.html') {
      c = c.replace(/<a href="child-development.html" class="nav-link">Child Development<\/a>/g, '<a href="child-development.html" class="nav-link is-active">Child Development</a>');
  }
  
  if (!c.includes('<script>lucide.createIcons();</script>')) {
      c = c.replace('</body>', '<script>lucide.createIcons();</script>\n</body>');
  }
  
  fs.writeFileSync(f, c);
  console.log(`Updated ${f}`);
});
