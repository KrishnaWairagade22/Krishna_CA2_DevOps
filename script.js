// ========== Form Validation - Student Feedback Registration Form ==========
// Sub Task 3: JavaScript Validation

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('feedbackForm');
    const wordCounter = document.getElementById('wordCounter');

    // Helper: show error
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        const group = field.closest('.form-group');
        const errorEl = document.getElementById(fieldId + 'Error');
        group.classList.add('error');
        errorEl.textContent = message;
        errorEl.classList.add('visible');
    }

    // Helper: clear error
    function clearError(fieldId) {
        const field = document.getElementById(fieldId);
        const group = field.closest('.form-group');
        const errorEl = document.getElementById(fieldId + 'Error');
        group.classList.remove('error');
        errorEl.classList.remove('visible');
    }

    // Helper: clear gender error (special case - uses genderGroup)
    function clearGenderError() {
        const group = document.getElementById('genderGroup');
        const errorEl = document.getElementById('genderError');
        group.classList.remove('error');
        errorEl.classList.remove('visible');
    }

    // Helper: show gender error
    function showGenderError(message) {
        const group = document.getElementById('genderGroup');
        const errorEl = document.getElementById('genderError');
        group.classList.add('error');
        errorEl.textContent = message;
        errorEl.classList.add('visible');
    }

    // Helper: count words in text
    function countWords(text) {
        const trimmed = text.trim();
        if (trimmed === '') return 0;
        return trimmed.split(/\s+/).length;
    }

    // Clear errors on input for text fields
    ['studentName', 'emailId', 'mobileNumber', 'department', 'feedbackComments'].forEach(function (id) {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('input', function () {
                clearError(id);
            });
            el.addEventListener('change', function () {
                clearError(id);
            });
        }
    });

    // Clear gender error on change
    document.querySelectorAll('input[name="gender"]').forEach(function (radio) {
        radio.addEventListener('change', function () {
            clearGenderError();
        });
    });

    // Word counter for feedback comments
    const feedbackField = document.getElementById('feedbackComments');
    if (feedbackField) {
        feedbackField.addEventListener('input', function () {
            const words = countWords(this.value);
            wordCounter.textContent = words + ' word' + (words !== 1 ? 's' : '');
            if (words >= 10) {
                wordCounter.style.color = '#4ade80';
            } else {
                wordCounter.style.color = 'rgba(255, 255, 255, 0.4)';
            }
        });
    }

    // ===== Form Submission & Validation =====
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        let isValid = true;

        // 1. Student Name validation — should not be empty
        const studentName = document.getElementById('studentName').value.trim();
        if (studentName === '') {
            showError('studentName', 'Please enter your full name.');
            isValid = false;
        } else if (studentName.length < 2) {
            showError('studentName', 'Name must be at least 2 characters long.');
            isValid = false;
        } else {
            clearError('studentName');
        }

        // 2. Email validation — should be in proper format
        const email = document.getElementById('emailId').value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email === '') {
            showError('emailId', 'Please enter your email address.');
            isValid = false;
        } else if (!emailRegex.test(email)) {
            showError('emailId', 'Please enter a valid email address.');
            isValid = false;
        } else {
            clearError('emailId');
        }

        // 3. Mobile Number validation — should contain valid digits only
        const mobile = document.getElementById('mobileNumber').value.trim();
        const mobileRegex = /^[0-9]{10}$/;
        if (mobile === '') {
            showError('mobileNumber', 'Please enter your mobile number.');
            isValid = false;
        } else if (!mobileRegex.test(mobile)) {
            showError('mobileNumber', 'Please enter a valid 10-digit mobile number.');
            isValid = false;
        } else {
            clearError('mobileNumber');
        }

        // 4. Department validation — should be selected
        const department = document.getElementById('department').value;
        if (department === '') {
            showError('department', 'Please select a department.');
            isValid = false;
        } else {
            clearError('department');
        }

        // 5. Gender validation — at least one option should be selected
        const genderChecked = document.querySelectorAll('input[name="gender"]:checked');
        if (genderChecked.length === 0) {
            showGenderError('Please select your gender.');
            isValid = false;
        } else {
            clearGenderError();
        }

        // 6. Feedback Comments validation — should not be blank, minimum 10 words
        const feedback = document.getElementById('feedbackComments').value.trim();
        const feedbackWords = countWords(feedback);
        if (feedback === '') {
            showError('feedbackComments', 'Please enter your feedback comments.');
            isValid = false;
        } else if (feedbackWords < 10) {
            showError('feedbackComments', 'Feedback must contain at least 10 words. Currently: ' + feedbackWords + ' word(s).');
            isValid = false;
        } else {
            clearError('feedbackComments');
        }

        // If all valid, show success overlay
        if (isValid) {
            const overlay = document.getElementById('successOverlay');
            overlay.classList.add('visible');
        }
    });

    // Reset button — clear all errors when form is reset
    form.addEventListener('reset', function () {
        ['studentName', 'emailId', 'mobileNumber', 'department', 'feedbackComments'].forEach(function (id) {
            clearError(id);
        });
        clearGenderError();
        wordCounter.textContent = '0 words';
        wordCounter.style.color = 'rgba(255, 255, 255, 0.4)';
    });

    // Close success overlay
    document.getElementById('closeSuccessBtn').addEventListener('click', function () {
        const overlay = document.getElementById('successOverlay');
        overlay.classList.remove('visible');
        form.reset();
    });

    // Also close overlay if clicking outside the box
    document.getElementById('successOverlay').addEventListener('click', function (e) {
        if (e.target === this) {
            this.classList.remove('visible');
            form.reset();
        }
    });
});
