/**
 * Mistral AI Chat Widget - v3.2 with code formatting
 */

class MistralChat {
    constructor() {
        this.isOpen = false;
        this.messages = [];
        this.currentProblemId = null;
        this.init();
    }
    
    init() {
        const chatHTML = `
            <div id="mistral-chat-widget" class="chat-widget">
                <div class="chat-header">
                    <svg class="icon-small" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke-width="2"/>
                    </svg>
                    <span>AI Helper</span>
                    <button id="chat-close" class="chat-close">×</button>
                </div>
                <div id="chat-messages" class="chat-messages"></div>
                <div class="chat-input-container">
                    <input type="text" id="chat-input" placeholder="Ask about this problem..." />
                    <button id="chat-send">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </button>
                </div>
            </div>
            
            <button id="chat-toggle" class="chat-toggle">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke-width="2"/>
                </svg>
                <span class="chat-badge">AI</span>
            </button>
        `;
        
        document.body.insertAdjacentHTML('beforeend', chatHTML);
        
        document.getElementById('chat-toggle').addEventListener('click', () => this.toggle());
        document.getElementById('chat-close').addEventListener('click', () => this.close());
        document.getElementById('chat-send').addEventListener('click', () => this.sendMessage());
        document.getElementById('chat-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
        
        const urlParts = window.location.pathname.split('/');
        if (urlParts[1] === 'problem' && urlParts[2]) {
            this.currentProblemId = parseInt(urlParts[2]);
        }
        
        this.addMessage('assistant', 'Hi! I\'m your AI helper. Ask me anything about this problem! 🤖');
    }
    
    toggle() {
        this.isOpen = !this.isOpen;
        const widget = document.getElementById('mistral-chat-widget');
        widget.classList.toggle('open', this.isOpen);
        
        if (this.isOpen) {
            document.getElementById('chat-input').focus();
            
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'chat_opened',
                    'problem_id': this.currentProblemId
                });
            }
        }
    }
    
    close() {
        this.isOpen = false;
        document.getElementById('mistral-chat-widget').classList.remove('open');
    }
    
    addMessage(role, content) {
        const messagesContainer = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${role}`;
        
        // NEW: Format code blocks
        const formatted = this.formatMessage(content);
        messageDiv.innerHTML = formatted;
        
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        this.messages.push({ role, content });
    }
    
    formatMessage(text) {
        // Detect and format SQL/Python code blocks
        // Look for multi-line code
        if (text.includes('SELECT') || text.includes('FROM') || text.includes('WHERE')) {
            // SQL code detected - format with <pre>
            text = text.replace(/(SELECT[\s\S]*?;)/gi, '<pre class="code-block">$1</pre>');
        }
        
        if (text.includes('import ') || text.includes('def ') || text.includes('print(')) {
            // Python code detected
            text = text.replace(/((?:import|def|class|for|if|while)[\s\S]*?)(?=\n\n|\n[A-Z]|$)/gi, '<pre class="code-block">$1</pre>');
        }
        
        // Convert newlines to <br> for non-code text
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }
    
    async sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        this.addMessage('user', message);
        input.value = '';
        
        const typingDiv = document.createElement('div');
        typingDiv.className = 'chat-message assistant typing';
        typingDiv.textContent = 'Typing...';
        typingDiv.id = 'typing-indicator';
        document.getElementById('chat-messages').appendChild(typingDiv);
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: message,
                    problem_id: this.currentProblemId,
                    lang: window.i18n ? window.i18n.getCurrentLang() : 'en'
                })
            });
            
            const result = await response.json();
            
            const typing = document.getElementById('typing-indicator');
            if (typing) typing.remove();
            
            if (result.success) {
                this.addMessage('assistant', result.reply);
                
                if (window.dataLayer) {
                    window.dataLayer.push({
                        'event': 'chat_message_sent',
                        'problem_id': this.currentProblemId
                    });
                }
            } else {
                this.addMessage('assistant', `Error: ${result.error}`);
            }
        } catch (error) {
            const typing = document.getElementById('typing-indicator');
            if (typing) typing.remove();
            
            this.addMessage('assistant', `Sorry, I couldn't connect. Error: ${error.message}`);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.startsWith('/problem/')) {
        window.mistralChat = new MistralChat();
    }
});
