/**
 * AARAV CLINICS — Reliable Premium GSAP Motion System
 * Resilient, Accessible, High-Performance Motion Engine
 */

(function () {
  'use strict';

  // Universal visibility restoration fallback
  function restoreAllVisibility() {
    const selectors = [
      '.gsap-title-reveal',
      '.gsap-reveal-up',
      '.gsap-reveal-left',
      '.gsap-reveal-right',
      '.gsap-scale-up',
      '.gsap-clip-reveal',
      '.gsap-word-reveal',
      '.gsap-text-progress',
      '.split-word-inner',
      '.split-word'
    ];
    selectors.forEach(sel => {
      document.querySelectorAll(sel).forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.clipPath = 'none';
        el.style.visibility = 'visible';
      });
    });
  }

  // Check prefers-reduced-motion
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Function to initialize animation system
  function initAnimations() {
    if (window.__aaravAnimationsInitialized) return;
    window.__aaravAnimationsInitialized = true;

    // Handle Page Loader if present
    const loader = document.getElementById('pageLoader');
    if (loader) {
      setTimeout(() => {
        loader.style.opacity = '0';
        setTimeout(() => loader.remove(), 400);
      }, 500);
    }

    // If reduced motion is requested or GSAP is unavailable, restore visibility and exit
    if (prefersReducedMotion || typeof window.gsap === 'undefined') {
      restoreAllVisibility();
      return;
    }

    try {
      // Register ScrollTrigger only once
      if (typeof window.ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
      }

      const defaultEase = "power3.out";
      const expoEase = "expo.out";

      /* ── Safe Text Splitter ── */
      const safeSplitWords = (element) => {
        if (!element || element.dataset.splitDone === 'true') return;
        const text = element.textContent.trim();
        if (!text) return;

        // If the element contains complex nested elements, don't destructively wipe
        if (element.children.length > 0 && !element.classList.contains('allow-split-children')) {
          return;
        }

        const words = text.split(/\s+/);
        if (!words.length) return;

        element.innerHTML = words.map(w => 
          `<span class="split-word" style="display:inline-block;overflow:hidden;vertical-align:top;"><span class="split-word-inner" style="display:inline-block;padding-bottom:0.1em;">${w}&nbsp;</span></span>`
        ).join('');
        element.dataset.splitDone = 'true';
      };

      /* ── Sticky Header Progress ── */
      const header = document.getElementById('siteHeader');
      if (header && typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.create({
          start: 'top -50',
          onUpdate: self => {
            if (self.direction === 1) {
              header.classList.add('scrolled');
            } else if (self.progress === 0) {
              header.classList.remove('scrolled');
            }
          }
        });
      }

      /* ── Hero Load Animations ── */
      const heroTl = gsap.timeline({ delay: 0.08 });

      // Animate title lines smoothly without clipping risk
      const titleLines = document.querySelectorAll('.gsap-title-reveal');
      if (titleLines.length) {
        heroTl.fromTo(titleLines,
          { y: 28, opacity: 0 },
          { 
            y: 0, 
            opacity: 1, 
            duration: 0.9, 
            stagger: 0.1, 
            ease: "power3.out",
            clearProps: 'transform,opacity'
          }
        );
      }

      // Hero supporting elements
      const heroReveals = document.querySelectorAll('.cinematic-hero .gsap-reveal-up, .hero .gsap-reveal-up');
      if (heroReveals.length) {
        heroTl.fromTo(heroReveals,
          { opacity: 0, y: 30 },
          { 
            opacity: 1, 
            y: 0, 
            duration: 0.9, 
            stagger: 0.08, 
            ease: defaultEase,
            clearProps: 'transform,opacity'
          },
          "-=0.7"
        );
      }

      /* ── Hero Parallax ── */
      const heroBg = document.querySelector('.hero-parallax-img');
      const heroContainer = document.querySelector('.cinematic-hero, .hero');
      if (heroBg && heroContainer && typeof ScrollTrigger !== 'undefined') {
        gsap.to(heroBg, {
          y: '15%',
          scale: 1.05,
          ease: 'none',
          scrollTrigger: {
            trigger: heroContainer,
            start: 'top top',
            end: 'bottom top',
            scrub: 0.5
          }
        });
      }

      /* ── Advanced Staggered Word Reveal (Section Headings) ── */
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.utils.toArray('.gsap-word-reveal').forEach(el => {
          try {
            safeSplitWords(el);
            const inners = el.querySelectorAll('.split-word-inner');
            if (inners.length) {
              gsap.fromTo(inners,
                { y: '100%', opacity: 0 },
                {
                  scrollTrigger: { 
                    trigger: el, 
                    start: "top 88%",
                    once: true 
                  },
                  y: '0%', 
                  opacity: 1, 
                  duration: 1.0, 
                  stagger: 0.025, 
                  ease: expoEase,
                  clearProps: 'transform,opacity'
                }
              );
            }
          } catch (err) {
            el.style.opacity = '1';
            el.style.transform = 'none';
          }
        });
      }

      /* ── Scroll-Linked Text Progression (Editorial Body Only) ── */
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.utils.toArray('.gsap-text-progress').forEach(el => {
          // If in hero, do NOT scrub fade — ensure it is 100% visible immediately
          if (el.closest('.cinematic-hero, .hero')) {
            el.style.opacity = '1';
            el.style.transform = 'none';
            return;
          }
          try {
            safeSplitWords(el);
            const inners = el.querySelectorAll('.split-word-inner');
            if (inners.length) {
              gsap.fromTo(inners,
                { opacity: 0.3 },
                {
                  opacity: 1,
                  stagger: 0.05,
                  ease: 'none',
                  scrollTrigger: {
                    trigger: el,
                    start: "top 82%",
                    end: "bottom 55%",
                    scrub: 0.4
                  }
                }
              );
            }
          } catch (err) {
            el.style.opacity = '1';
          }
        });
      }

      /* ── Image Clip-Path Reveal ── */
      if (typeof ScrollTrigger !== 'undefined') {
        gsap.utils.toArray('.gsap-clip-reveal').forEach(el => {
          gsap.fromTo(el,
            { clipPath: 'inset(100% 0% 0% 0%)', scale: 1.06 },
            {
              scrollTrigger: { 
                trigger: el, 
                start: "top 86%",
                once: true 
              },
              clipPath: 'inset(0% 0% 0% 0%)',
              scale: 1,
              duration: 1.25,
              ease: expoEase,
              clearProps: 'clipPath,scale'
            }
          );
        });
      }

      /* ── General Scroll Triggered Reveals ── */
      if (typeof ScrollTrigger !== 'undefined') {
        // Reveal Up (Outside hero)
        gsap.utils.toArray('section:not(.cinematic-hero):not(.hero) .gsap-reveal-up').forEach(el => {
          gsap.fromTo(el,
            { opacity: 0, y: 35 },
            {
              scrollTrigger: { 
                trigger: el, 
                start: "top 88%",
                once: true 
              },
              opacity: 1, 
              y: 0, 
              duration: 0.9, 
              ease: defaultEase,
              clearProps: 'opacity,transform'
            }
          );
        });

        // Reveal Left
        gsap.utils.toArray('.gsap-reveal-left').forEach(el => {
          gsap.fromTo(el,
            { opacity: 0, x: -35 },
            {
              scrollTrigger: { 
                trigger: el, 
                start: "top 88%",
                once: true 
              },
              opacity: 1, 
              x: 0, 
              duration: 0.9, 
              ease: defaultEase,
              clearProps: 'opacity,transform'
            }
          );
        });

        // Reveal Right
        gsap.utils.toArray('.gsap-reveal-right').forEach(el => {
          gsap.fromTo(el,
            { opacity: 0, x: 35 },
            {
              scrollTrigger: { 
                trigger: el, 
                start: "top 88%",
                once: true 
              },
              opacity: 1, 
              x: 0, 
              duration: 0.9, 
              ease: defaultEase,
              clearProps: 'opacity,transform'
            }
          );
        });

        // Scale Up
        gsap.utils.toArray('.gsap-scale-up').forEach(el => {
          gsap.fromTo(el,
            { opacity: 0, scale: 0.95 },
            {
              scrollTrigger: { 
                trigger: el, 
                start: "top 88%",
                once: true 
              },
              opacity: 1, 
              scale: 1, 
              duration: 0.9, 
              ease: "back.out(1.2)",
              clearProps: 'opacity,transform'
            }
          );
        });

        // Stagger Groups
        gsap.utils.toArray('.gsap-stagger-group').forEach(group => {
          const items = group.querySelectorAll('.gsap-item, li, .benefit-row, .bento-card');
          if (items.length) {
            gsap.fromTo(items,
              { opacity: 0, y: 30 },
              {
                scrollTrigger: { 
                  trigger: group, 
                  start: "top 86%",
                  once: true 
                },
                opacity: 1, 
                y: 0, 
                duration: 0.8, 
                stagger: 0.08, 
                ease: defaultEase,
                clearProps: 'opacity,transform'
              }
            );
          }
        });
      }

      // Parallax Groups
      const aboutGroup = document.querySelector('.gsap-parallax-group');
      if (aboutGroup && typeof ScrollTrigger !== 'undefined') {
        const fast = aboutGroup.querySelector('.gsap-parallax-fast');
        const slow = aboutGroup.querySelector('.gsap-parallax-slow');
        if (fast) {
          gsap.to(fast, {
            y: -40,
            ease: 'none',
            scrollTrigger: { trigger: aboutGroup, start: 'top bottom', end: 'bottom top', scrub: 0.5 }
          });
        }
        if (slow) {
          gsap.to(slow, {
            y: 40,
            ease: 'none',
            scrollTrigger: { trigger: aboutGroup, start: 'top bottom', end: 'bottom top', scrub: 0.5 }
          });
        }
      }

      // Ambient Slow Spin
      const spinner = document.querySelector('.gsap-spin-slow');
      if (spinner) {
        gsap.to(spinner, {
          rotation: 360,
          duration: 35,
          repeat: -1,
          ease: 'none'
        });
      }

      // Refresh ScrollTrigger once fully loaded and on window resize
      window.addEventListener('load', () => {
        if (typeof ScrollTrigger !== 'undefined') {
          ScrollTrigger.refresh();
        }
      });

      let resizeTimeout;
      window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
          if (typeof ScrollTrigger !== 'undefined') {
            ScrollTrigger.refresh();
          }
        }, 200);
      });

    } catch (err) {
      console.warn('[Animations] Error during initialization, restoring visibility fallback:', err);
      restoreAllVisibility();
    }
  }

  // Fallback safety timer: ensure everything is visible even if DOMContentLoaded hangs or GSAP CDN fails
  setTimeout(() => {
    if (!window.__aaravAnimationsInitialized) {
      initAnimations();
    }
  }, 1200);

  // Ready State check
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnimations);
  } else {
    initAnimations();
  }

})();
