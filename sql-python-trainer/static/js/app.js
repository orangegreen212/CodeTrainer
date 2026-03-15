// Progress Tracking with localStorage

// Get completed problems from localStorage
function getCompletedProblems() {
    const completed = localStorage.getItem('completed_problems');
    return completed ? JSON.parse(completed) : [];
}

// Mark problem as completed
function markAsCompleted(problemId) {
    let completed = getCompletedProblems();
    if (!completed.includes(problemId)) {
        completed.push(problemId);
        localStorage.setItem('completed_problems', JSON.stringify(completed));
        updateProblemStatus(problemId, true);
        
        // Track in GTM
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'task_completed',
                'problem_id': problemId
            });
        }
    }
}

// Mark problem as incomplete
function markAsIncomplete(problemId) {
    let completed = getCompletedProblems();
    completed = completed.filter(id => id !== problemId);
    localStorage.setItem('completed_problems', JSON.stringify(completed));
    updateProblemStatus(problemId, false);
    
    // Track in GTM
    if (window.dataLayer) {
        window.dataLayer.push({
            'event': 'task_uncompleted',
            'problem_id': problemId
        });
    }
}

// Check if problem is completed
function isCompleted(problemId) {
    return getCompletedProblems().includes(problemId);
}

// Update UI for problem status
function updateProblemStatus(problemId, completed) {
    const statusBadge = document.querySelector(`.problem-row[data-id="${problemId}"] .status-badge`);
    if (statusBadge) {
        if (completed) {
            statusBadge.classList.add('completed');
            statusBadge.textContent = window.i18n.t('problems.status.completed');
        } else {
            statusBadge.classList.remove('completed');
            statusBadge.textContent = window.i18n.t('problems.status.not_started');
        }
    }
    
    // Update checkbox if on problem page
    const checkbox = document.getElementById('complete-checkbox');
    if (checkbox) {
        checkbox.checked = completed;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Update all problem statuses on problems list page
    const problemRows = document.querySelectorAll('.problem-row');
    problemRows.forEach(row => {
        const problemId = parseInt(row.dataset.id);
        if (isCompleted(problemId)) {
            updateProblemStatus(problemId, true);
        }
    });
    
    // Handle complete checkbox on problem page
    const checkbox = document.getElementById('complete-checkbox');
    if (checkbox) {
        const problemId = parseInt(checkbox.dataset.problemId);
        checkbox.checked = isCompleted(problemId);
        
        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                markAsCompleted(problemId);
            } else {
                markAsIncomplete(problemId);
            }
        });
    }
});

// Export for global use
window.progress = {
    markAsCompleted,
    markAsIncomplete,
    isCompleted,
    getCompletedProblems
};
