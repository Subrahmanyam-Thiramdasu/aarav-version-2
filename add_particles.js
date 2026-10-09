const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;
  
  if (!content.includes('bg-animations.css')) {
    content = content.replace('</head>', '  <link rel="stylesheet" href="css/bg-animations.css">\n</head>');
    changed = true;
  }
  if (!content.includes('particle-bg.js')) {
    content = content.replace('</head>', '  <script src="js/particle-bg.js" defer></script>\n</head>');
    changed = true;
  }
  
  let lines = content.split('\n');
  let newLines = [];
  let addedToHero = false;
  
  for (let line of lines) {
    if (!addedToHero && (line.includes('class="page-hero"') || line.includes('class="page-hero ') || line.includes('class="hero ') || line.includes('class="cinematic-hero') || line.includes('class="bg-organic-shape') || line.includes('class="section editorial-about'))) {
      if (!line.includes('particle-canvas-container')) {
        line = line.replace(/class="([^"]*)"/, 'class="$1 particle-canvas-container"');
        changed = true;
      }
      addedToHero = true; // only add to the first hero-like section per page
    }
    
    // Also add to any dark sections independently of the hero
    if (line.includes('glow-dark') && !line.includes('particle-canvas-container')) {
      line = line.replace(/class="([^"]*)"/, 'class="$1 particle-canvas-container"');
      changed = true;
    }
    
    newLines.push(line);
  }
  
  if (changed) {
    content = newLines.join('\n');
    fs.writeFileSync(file, content);
    console.log('Updated ' + file);
  }
});
