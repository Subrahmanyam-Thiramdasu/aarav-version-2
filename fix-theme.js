const fs = require('fs');
['pediatric-physiotherapy.html', 'speech-therapy.html'].forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    c = c.replace(/class="site-header theme-light"/, 'class="site-header theme-dark"');
    fs.writeFileSync(f, c);
});
console.log('done');
