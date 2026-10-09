/**
 * Aarav Clinics - Premium Particle Background
 * A lightweight, responsive canvas particle system.
 */

class ParticleNetwork {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    
    // Check if the parent section is a dark theme
    const isDark = canvas.closest('.glow-dark, .theme-dark, .cinematic-hero') !== null;
    
    this.options = {
      particleColor: isDark ? 'rgba(22, 138, 173, 0.6)' : 'rgba(22, 138, 173, 0.3)',
      lineColor: isDark ? 'rgba(0, 142, 155, 0.2)' : 'rgba(0, 142, 155, 0.1)',
      particleAmount: 40, // Base amount, will scale with width
      defaultRadius: 1.5,
      variantRadius: 2,
      linkRadius: 120, // Distance to connect particles
      velocity: 0.3
    };

    // Respect prefers-reduced-motion
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    this.prefersReducedMotion = mediaQuery.matches;
    
    mediaQuery.addEventListener('change', (e) => {
      this.prefersReducedMotion = e.matches;
      if (this.prefersReducedMotion) {
        this.pause();
        this.draw(); // Draw static frame
      } else {
        this.play();
      }
    });

    this.init();
    
    window.addEventListener('resize', () => {
      this.resize();
    });
    
    // Use intersection observer to pause when not visible
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.play();
        } else {
          this.pause();
        }
      });
    }, { threshold: 0 });
    this.observer.observe(this.canvas);
  }

  init() {
    this.resize();
    this.createParticles();
    this.play();
  }

  resize() {
    // Handle device pixel ratio for crisp rendering
    const dpr = window.devicePixelRatio || 1;
    const rect = this.canvas.parentElement.getBoundingClientRect();
    
    this.canvas.width = rect.width * dpr;
    this.canvas.height = rect.height * dpr;
    this.ctx.scale(dpr, dpr);
    
    this.canvas.style.width = `${rect.width}px`;
    this.canvas.style.height = `${rect.height}px`;

    this.w = rect.width;
    this.h = rect.height;
    
    // Adjust particle count based on screen size
    const area = this.w * this.h;
    this.particleCount = Math.min(
      Math.floor((area / 200000) * this.options.particleAmount),
      150 // max particles to prevent lag
    );
    
    // On mobile, reduce connection distance to improve performance
    if (this.w < 768) {
      this.options.linkRadius = 80;
      this.particleCount = Math.floor(this.particleCount * 0.6);
    }
  }

  createParticles() {
    this.particles = [];
    for (let i = 0; i < this.particleCount; i++) {
      this.particles.push(new Particle(this));
    }
  }

  draw() {
    this.ctx.clearRect(0, 0, this.w, this.h);
    
    for (let i = 0; i < this.particles.length; i++) {
      this.particles[i].draw();
      this.particles[i].update();
    }
    
    // Draw lines
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        this.linkParticles(this.particles[i], this.particles[j]);
      }
    }
  }

  linkParticles(p1, p2) {
    const dx = p1.x - p2.x;
    const dy = p1.y - p2.y;
    const dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < this.options.linkRadius) {
      const opacity = 1 - (dist / this.options.linkRadius);
      this.ctx.beginPath();
      this.ctx.strokeStyle = this.options.lineColor.replace(/[^,]+(?=\))/, opacity.toFixed(2));
      this.ctx.lineWidth = 0.8;
      this.ctx.moveTo(p1.x, p1.y);
      this.ctx.lineTo(p2.x, p2.y);
      this.ctx.stroke();
    }
  }

  animate() {
    if (this.prefersReducedMotion || !this.isPlaying) return;
    this.draw();
    this.animationId = requestAnimationFrame(() => this.animate());
  }

  play() {
    if (this.isPlaying || this.prefersReducedMotion) return;
    this.isPlaying = true;
    this.animate();
  }

  pause() {
    this.isPlaying = false;
    cancelAnimationFrame(this.animationId);
  }
}

class Particle {
  constructor(network) {
    this.network = network;
    this.x = Math.random() * this.network.w;
    this.y = Math.random() * this.network.h;
    
    // Random direction
    const angle = Math.random() * Math.PI * 2;
    const velocity = this.network.options.velocity * (0.5 + Math.random() * 0.5);
    
    this.vx = Math.cos(angle) * velocity;
    this.vy = Math.sin(angle) * velocity;
    
    this.radius = this.network.options.defaultRadius + Math.random() * this.network.options.variantRadius;
    this.color = this.network.options.particleColor;
  }

  update() {
    if (this.network.prefersReducedMotion) return;
    
    this.x += this.vx;
    this.y += this.vy;

    // Wrap around edges for continuous feel
    if (this.x < -this.radius) this.x = this.network.w + this.radius;
    if (this.x > this.network.w + this.radius) this.x = -this.radius;
    if (this.y < -this.radius) this.y = this.network.h + this.radius;
    if (this.y > this.network.h + this.radius) this.y = -this.radius;
  }

  draw() {
    this.network.ctx.beginPath();
    this.network.ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    this.network.ctx.fillStyle = this.color;
    this.network.ctx.fill();
  }
}

// Auto-initialize on designated containers
document.addEventListener('DOMContentLoaded', () => {
  const containers = document.querySelectorAll('.particle-canvas-container');
  containers.forEach(container => {
    // Make sure container has position relative/absolute
    const style = window.getComputedStyle(container);
    if (style.position === 'static') {
      container.style.position = 'relative';
    }
    
    // Create canvas element
    const canvas = document.createElement('canvas');
    canvas.classList.add('particle-canvas');
    
    // Intelligent insertion:
    // If the container has a dedicated background wrapper (like .cinematic-hero-bg), 
    // insert the canvas into that wrapper so it sits above the image but behind the main content.
    const bgWrapper = container.querySelector('.cinematic-hero-bg, .about-hero-bg');
    if (bgWrapper) {
      bgWrapper.appendChild(canvas);
    } else {
      // Otherwise, insert as the first child of the container
      container.insertBefore(canvas, container.firstChild);
      
      // Ensure the direct children (content) stay above the canvas by giving them position relative if they are static
      Array.from(container.children).forEach(child => {
        if (child !== canvas) {
          const childStyle = window.getComputedStyle(child);
          if (childStyle.position === 'static' && child.tagName !== 'SCRIPT' && child.tagName !== 'STYLE') {
            child.style.position = 'relative';
            child.style.zIndex = '1';
          }
        }
      });
    }
    
    // Initialize network
    new ParticleNetwork(canvas);
  });
});
