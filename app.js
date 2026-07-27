document.addEventListener('DOMContentLoaded', () => {
    const header = document.getElementById('header');
    const contactForm = document.getElementById('contactForm');
    const navLinks = document.querySelectorAll('.nav-link');

    // 1. Scroll effect for header
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 2. Smooth scrolling for nav links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            if (targetId === '#') return;

            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                const headerHeight = header.offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 3. Contact Form Submission Handler
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Fetch field values
            const name = document.getElementById('formName').value;
            const email = document.getElementById('formEmail').value;
            const org = document.getElementById('formOrg').value;
            const message = document.getElementById('formMessage').value;

            // Submit Button loading animation
            const btnSubmit = document.getElementById('btnSubmit');
            const originalText = btnSubmit.textContent;
            btnSubmit.disabled = true;
            btnSubmit.textContent = 'Sending Request...';

            // Simulate form submission to backend
            setTimeout(() => {
                const formCard = document.querySelector('.contact-form-card');
                formCard.style.transition = 'all 0.3s ease';
                formCard.style.opacity = '0';

                setTimeout(() => {
                    formCard.innerHTML = `
                        <div style="text-align: center; padding: 2rem 0; animation: fadeIn 0.5s ease forwards;">
                            <div style="font-size: 4rem; color: #1e8e3e; margin-bottom: 1.5rem;">🎉</div>
                            <h3 style="font-size: 1.5rem; margin-bottom: 0.75rem; color: #202124;">Thank you, ${name}!</h3>
                            <p style="color: #5f6368; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">
                                Your demo request for <strong>${org}</strong> has been logged successfully. 
                                A clinical systems specialist will contact you at <strong>${email}</strong> within 24 hours.
                            </p>
                            <button class="btn btn-outline" onclick="window.location.reload();">Send Another Message</button>
                        </div>
                    `;
                    formCard.style.opacity = '1';
                }, 300);
            }, 1200);
        });
    }
});
