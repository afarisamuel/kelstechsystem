// Kelstech Systems — Main JavaScript

document.addEventListener('DOMContentLoaded', function () {

    // ---- Hero Swiper Initialization ----
    const heroSwiper = new Swiper('.hero-swiper', {
        loop: true,
        parallax: true,
        speed: 1000,
        autoplay: {
            delay: 6000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
        on: {
            slideChangeTransitionStart: function () {
                // You can add content animations here if needed
                const activeSlide = this.slides[this.activeIndex];
                const contents = activeSlide.querySelectorAll('.slide-content > *');
                contents.forEach((el, i) => {
                    el.style.opacity = '0';
                    el.style.transform = 'translateY(20px)';
                });
            },
            slideChangeTransitionEnd: function () {
                const activeSlide = this.slides[this.activeIndex];
                const contents = activeSlide.querySelectorAll('.slide-content > *');
                contents.forEach((el, i) => {
                    setTimeout(() => {
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0)';
                        el.style.transition = 'all 0.6s ease-out';
                    }, i * 150);
                });
            }
        }
    });

    // ---- Navbar scroll effect ----
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // ---- Mobile menu toggle ----
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
            if (mobileMenu.classList.contains('hidden')) {
                menuIcon.className = 'fa-solid fa-bars text-xl';
            } else {
                menuIcon.className = 'fa-solid fa-xmark text-xl';
            }
        });
    }

    // ---- Counter animation ----
    const counters = document.querySelectorAll('[data-counter]');
    const counterSpeed = 50;

    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-counter'));
        let current = 0;
        const increment = Math.ceil(target / counterSpeed);

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = current.toLocaleString() + '+';
        }, 30);
    };

    // Use Intersection Observer for counters
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    // ---- Scroll animations ----
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                scrollObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    animatedElements.forEach(el => scrollObserver.observe(el));

    // ---- Auto-dismiss messages after 5 seconds ----
    const messages = document.querySelectorAll('.message-toast');
    messages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(100px)';
            msg.style.transition = 'all 0.4s ease-out';
            setTimeout(() => msg.remove(), 400);
        }, 5000);
    });

    // ---- Theme Toggle ----
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');

    // Update icon state
    function updateThemeIcon() {
        if (document.documentElement.classList.contains('dark')) {
            themeIcon.className = 'fa-solid fa-sun text-lg w-5 h-5 flex items-center justify-center';
        } else {
            themeIcon.className = 'fa-solid fa-moon text-lg w-5 h-5 flex items-center justify-center';
        }
    }

    if (themeToggle) {
        // Initial icon state
        updateThemeIcon();

        themeToggle.addEventListener('click', function () {
            // Toggle theme class
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
            } else {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
            }
            updateThemeIcon();
        });
    }

    // ---- Active nav link highlighting ----
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('text-primary-400');
            link.classList.remove('text-gray-300', 'text-gray-600');
        }
    });
});
