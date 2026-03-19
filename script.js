// =============================================
// The Gathering Porch — Script
// =============================================

document.addEventListener('DOMContentLoaded', () => {

  // --- Navbar scroll behavior ---
  const navbar = document.getElementById('navbar');
  const handleScroll = () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // --- Mobile menu toggle ---
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');

  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
    navbar.classList.toggle('menu-open');
    document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
  });

  navMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navMenu.classList.remove('active');
      navbar.classList.remove('menu-open');
      document.body.style.overflow = '';
    });
  });

  // --- Hero animations ---
  const heroElements = document.querySelectorAll('.hero-content [data-animate]');
  const heroTitle = document.querySelector('.hero-title');

  setTimeout(() => {
    heroElements.forEach(el => el.classList.add('animated'));
    if (heroTitle) heroTitle.classList.add('animated');
  }, 300);

  // --- Floating particles ---
  const particlesContainer = document.getElementById('heroParticles');
  if (particlesContainer) {
    for (let i = 0; i < 300; i++) {
      const particle = document.createElement('div');
      particle.className = 'hero-particle';
      const size = Math.random() * 7 + 1;
      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.left = Math.random() * 100 + '%';
      particle.style.animationDuration = (Math.random() * 14 + 6) + 's';
      particle.style.animationDelay = (Math.random() * 8) + 's';
      particle.style.opacity = Math.random() * 0.7 + 0.15;
      particlesContainer.appendChild(particle);
    }
  }

  // --- Scroll-triggered animations ---
  const animatedElements = document.querySelectorAll('[data-animate]:not(.hero-content [data-animate])');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.getAttribute('data-delay') || 0;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, parseInt(delay));
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  });

  animatedElements.forEach(el => observer.observe(el));

  // --- Active nav link on scroll ---
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

  const highlightNav = () => {
    const scrollY = window.scrollY + 200;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      if (scrollY >= top && scrollY < top + height) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', highlightNav, { passive: true });

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // --- Contact form handling ---
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const btn = this.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      // Simulate form submission (replace with actual endpoint)
      setTimeout(() => {
        btn.textContent = 'Message Sent!';
        btn.style.background = '#4CAF50';
        this.reset();
        setTimeout(() => {
          btn.textContent = originalText;
          btn.style.background = '';
          btn.disabled = false;
        }, 3000);
      }, 1000);
    });
  }

  // --- Parallax effect on quote section ---
  const parallaxSection = document.querySelector('.parallax-quote');
  if (parallaxSection) {
    window.addEventListener('scroll', () => {
      const rect = parallaxSection.getBoundingClientRect();
      const speed = 0.3;
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        const yPos = (rect.top - window.innerHeight) * speed;
        parallaxSection.style.backgroundPositionY = yPos + 'px';
      }
    }, { passive: true });
  }

});
