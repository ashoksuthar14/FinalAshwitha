// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Initialize GSAP animations if ScrollTrigger is available
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        // Hero section animations
        gsap.from('.hero-title', {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.hero-subtitle', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.3
        });

        gsap.from('.hero-buttons', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.6
        });

        gsap.from('.hero-image', {
            duration: 1.2,
            scale: 0.8,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.3
        });

        // Floating elements animation
        gsap.to('.floating-element', {
            y: 20,
            duration: 2,
            ease: 'power1.inOut',
            repeat: -1,
            yoyo: true
        });

        // Scroll animations for sections
        const sections = [
            '.features-overview',
            '.how-it-works',
            '.benefits-section',
            '.our-story',
            '.our-mission',
            '.our-values',
            '.our-team',
            '.main-features',
            '.technology-section',
            '.use-cases',
            '.faq-section'
        ];

        sections.forEach(section => {
            const elements = document.querySelector(section);
            if (elements) {
                // Animate section headers
                const header = elements.querySelector('.section-header');
                if (header) {
                    ScrollTrigger.create({
                        trigger: header,
                        start: 'top 80%',
                        onEnter: () => {
                            gsap.from(header, {
                                duration: 0.8,
                                y: 50,
                                opacity: 0,
                                ease: 'power3.out'
                            });
                        },
                        once: true
                    });
                }

                // Animate cards with stagger effect
                const cards = elements.querySelectorAll('.feature-card, .step-card, .benefit-card, .value-card, .team-member, .feature-card-large, .technology-card, .use-case-card');
                if (cards.length > 0) {
                    ScrollTrigger.create({
                        trigger: elements,
                        start: 'top 70%',
                        onEnter: () => {
                            gsap.from(cards, {
                                duration: 0.8,
                                y: 50,
                                opacity: 0,
                                stagger: 0.1,
                                ease: 'power3.out'
                            });
                        },
                        once: true
                    });
                }
            }
        });

        // CTA section animation
        const ctaSection = document.querySelector('.cta-section');
        if (ctaSection) {
            ScrollTrigger.create({
                trigger: ctaSection,
                start: 'top 80%',
                onEnter: () => {
                    gsap.from('.cta-content', {
                        duration: 0.8,
                        scale: 0.9,
                        opacity: 0,
                        ease: 'power3.out'
                    });
                },
                once: true
            });
        }
    }

    // Accordion functionality for FAQ
    const accordionButtons = document.querySelectorAll('.accordion-button');
    
    accordionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const isCollapsed = this.classList.contains('collapsed');
            
            if (!isCollapsed) {
                gsap.from(this.nextElementSibling, {
                    height: 0,
                    duration: 0.5,
                    ease: 'power2.out'
                });
            }
        });
    });
});
