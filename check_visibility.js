const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const directoryPath = path.join(__dirname);
const htmlFiles = fs.readdirSync(directoryPath).filter(file => file.endsWith('.html'));

(async () => {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });

    const report = {};

    for (const file of htmlFiles) {
        console.log(`Testing ${file}...`);
        await page.goto(`http://localhost:8000/${file}`, { waitUntil: 'networkidle2' });
        
        // Scroll down to trigger ScrollTriggers
        await page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    const scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight - window.innerHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 50);
            });
        });

        // Wait a bit for animations to finish
        await new Promise(r => setTimeout(r, 1000));

        // Evaluate visibility of all sections
        const suspiciousSections = await page.evaluate(() => {
            const sections = document.querySelectorAll('section, .section, header, footer');
            const issues = [];
            
            sections.forEach((sec, index) => {
                const rect = sec.getBoundingClientRect();
                const style = window.getComputedStyle(sec);
                
                // If section takes up space
                if (rect.height > 200) {
                    // Check if it's completely invisible
                    if (style.opacity === '0' || style.visibility === 'hidden' || style.display === 'none') {
                        issues.push(`Section ${index} (height ${rect.height}px) is hidden (opacity: ${style.opacity}, visibility: ${style.visibility})`);
                    } else {
                        // Check if it has any visible text or image content
                        const text = sec.innerText.trim();
                        const images = sec.querySelectorAll('img');
                        let hasVisibleImages = false;
                        images.forEach(img => {
                            const imgRect = img.getBoundingClientRect();
                            if (imgRect.width > 0 && imgRect.height > 0 && window.getComputedStyle(img).opacity !== '0') {
                                hasVisibleImages = true;
                            }
                        });
                        
                        if (text.length === 0 && !hasVisibleImages) {
                            issues.push(`Section ${index} (height ${rect.height}px) has no visible text or images.`);
                        }
                    }
                }
            });
            return issues;
        });

        if (suspiciousSections.length > 0) {
            report[file] = suspiciousSections;
            console.log(`Found issues in ${file}:`, suspiciousSections);
        }
    }

    await browser.close();

    fs.writeFileSync('visibility_report.json', JSON.stringify(report, null, 2));
    console.log("Visibility report saved to visibility_report.json");

})();
