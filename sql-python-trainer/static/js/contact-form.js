/**
 * Contact Form Modal
 * Allows users to send messages to developer without showing email publicly
 */

class ContactForm {
    constructor() {
        this.init();
    }
    
    init() {
        // Create modal HTML
        const modalHTML = `
            <div id="contact-modal" class="modal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3>
                            <svg class="icon-medium" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                <path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke-width="2"/>
                            </svg>
                            <span data-i18n="contact.title">Write to Developer</span>
                        </h3>
                        <button class="modal-close" id="contact-close">×</button>
                    </div>
                    
                    <form id="contact-form" class="contact-form">
                        <div class="form-group">
                            <label data-i18n="contact.name">Your Name</label>
                            <input type="text" name="name" required placeholder="John Doe">
                        </div>
                        
                        <div class="form-group">
                            <label data-i18n="contact.email">Your Email</label>
                            <input type="email" name="email" required placeholder="john@example.com">
                        </div>
                        
                        <div class="form-group">
                            <label data-i18n="contact.message">Message</label>
                            <textarea name="message" required rows="5" placeholder="Your message here..."></textarea>
                        </div>
                        
                        <button type="submit" class="btn-primary" data-i18n="contact.send">Send Message</button>
                    </form>
                    
                    <div id="contact-message" class="contact-message" style="display: none;"></div>
                </div>
            </div>
            
            <button id="contact-button" class="contact-button">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke-width="2"/>
                </svg>
                <span data-i18n="contact.button">Contact</span>
            </button>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        // Event listeners
        document.getElementById('contact-button').addEventListener('click', () => this.open());
        document.getElementById('contact-close').addEventListener('click', () => this.close());
        document.getElementById('contact-modal').addEventListener('click', (e) => {
            if (e.target.id === 'contact-modal') this.close();
        });
        
        document.getElementById('contact-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.sendMessage(e.target);
        });
    }
    
    open() {
        document.getElementById('contact-modal').classList.add('open');
        
        // Track in GTM
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'contact_form_opened'
            });
        }
    }
    
    close() {
        document.getElementById('contact-modal').classList.remove('open');
    }
    
    async sendMessage(form) {
        const formData = new FormData(form);
        const messageDiv = document.getElementById('contact-message');
        const submitBtn = form.querySelector('button[type="submit"]');
        
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
        
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (result.success) {
                messageDiv.className = 'contact-message success';
                messageDiv.textContent = result.message;
                messageDiv.style.display = 'block';
                form.reset();
                
                // Track in GTM
                if (window.dataLayer) {
                    window.dataLayer.push({
                        'event': 'contact_form_sent'
                    });
                }
                
                setTimeout(() => {
                    this.close();
                    messageDiv.style.display = 'none';
                }, 3000);
            } else {
                messageDiv.className = 'contact-message error';
                messageDiv.textContent = result.error;
                messageDiv.style.display = 'block';
            }
        } catch (error) {
            messageDiv.className = 'contact-message error';
            messageDiv.textContent = `Error: ${error.message}`;
            messageDiv.style.display = 'block';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Send Message';
        }
    }
}

// Initialize contact form when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.contactForm = new ContactForm();
});
