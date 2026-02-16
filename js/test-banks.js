// ============================================
// Test Banks - Interactive MCQ Functionality
// ============================================

// Sample questions data
// In the future, this will be loaded from a folder/file
const questions = [
    {
        id: 1,
        question: "What does 'Willkommen' mean in English?",
        options: ["Welcome", "Goodbye", "Thank you", "Please"],
        correct: 0
    },
    {
        id: 2,
        question: "How do you say 'Hello' in German?",
        options: ["Hallo", "Tschüss", "Danke", "Bitte"],
        correct: 0
    },
    {
        id: 3,
        question: "What is the German word for 'Learning'?",
        options: ["Lernen", "Lehren", "Lesen", "Lachen"],
        correct: 0
    },
    {
        id: 4,
        question: "Which article is used with 'Haus' (house) in German?",
        options: ["Der", "Die", "Das", "Den"],
        correct: 0
    },
    {
        id: 5,
        question: "What does 'Viel Erfolg' mean?",
        options: ["Good luck", "Thank you", "You're welcome", "See you later"],
        correct: 0
    }
];

let userAnswers = {};
let score = 0;
let totalQuestions = questions.length;

// Initialize the test
document.addEventListener('DOMContentLoaded', function() {
    renderQuestions();
    updateScore();
    
    // Check all answers button
    const checkAllBtn = document.getElementById('checkAllBtn');
    if (checkAllBtn) {
        checkAllBtn.addEventListener('click', checkAllAnswers);
    }
    
    // Reset button
    const resetBtn = document.getElementById('resetBtn');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetTest);
    }
});

// Render all questions
function renderQuestions() {
    const container = document.getElementById('questionsContainer');
    if (!container) return;
    
    container.innerHTML = '';
    
    questions.forEach((q, index) => {
        const questionCard = document.createElement('div');
        questionCard.className = 'question-card';
        questionCard.id = `question-${q.id}`;
        
        questionCard.innerHTML = `
            <div class="question-header">
                <span class="question-number">Question ${index + 1}</span>
            </div>
            <div class="question-text">${q.question}</div>
            <div class="options-container" id="options-${q.id}">
                ${q.options.map((option, optIndex) => `
                    <div class="option-item" data-question="${q.id}" data-option="${optIndex}">
                        <input type="radio" name="question-${q.id}" id="q${q.id}-opt${optIndex}" value="${optIndex}">
                        <label for="q${q.id}-opt${optIndex}">${option}</label>
                    </div>
                `).join('')}
            </div>
            <div class="feedback" id="feedback-${q.id}"></div>
        `;
        
        container.appendChild(questionCard);
    });
    
    // Add event listeners to options
    document.querySelectorAll('.option-item').forEach(item => {
        item.addEventListener('click', function() {
            const questionId = parseInt(this.dataset.question);
            const optionIndex = parseInt(this.dataset.option);
            
            // Uncheck other options
            document.querySelectorAll(`input[name="question-${questionId}"]`).forEach(radio => {
                radio.checked = false;
            });
            
            // Check selected option
            const radio = this.querySelector('input[type="radio"]');
            radio.checked = true;
            
            // Update visual state
            document.querySelectorAll(`#options-${questionId} .option-item`).forEach(opt => {
                opt.classList.remove('selected');
            });
            this.classList.add('selected');
            
            // Store answer
            userAnswers[questionId] = optionIndex;
            
            // Show instant feedback
            showFeedback(questionId, optionIndex);
        });
    });
}

// Show instant feedback for a question
function showFeedback(questionId, selectedOption) {
    const question = questions.find(q => q.id === questionId);
    if (!question) return;
    
    const feedbackDiv = document.getElementById(`feedback-${questionId}`);
    const isCorrect = selectedOption === question.correct;
    
    // Remove previous feedback classes
    feedbackDiv.classList.remove('correct', 'incorrect', 'show');
    
    // Add appropriate class and show
    feedbackDiv.classList.add(isCorrect ? 'correct' : 'incorrect', 'show');
    
    if (isCorrect) {
        feedbackDiv.innerHTML = '<span class="feedback-icon">✅</span> Correct! Well done!';
    } else {
        const correctAnswer = question.options[question.correct];
        feedbackDiv.innerHTML = `<span class="feedback-icon">❌</span> Wrong! The correct answer is: <strong>${correctAnswer}</strong>`;
    }
    
    // Update option styling
    const options = document.querySelectorAll(`#options-${questionId} .option-item`);
    options.forEach((opt, index) => {
        opt.classList.remove('correct', 'incorrect');
        if (index === question.correct) {
            opt.classList.add('correct');
        } else if (index === selectedOption && !isCorrect) {
            opt.classList.add('incorrect');
        }
    });
    
    updateScore();
}

// Check all answers
function checkAllAnswers() {
    questions.forEach(q => {
        const selectedAnswer = userAnswers[q.id];
        if (selectedAnswer !== undefined) {
            showFeedback(q.id, selectedAnswer);
        }
    });
}

// Reset test
function resetTest() {
    userAnswers = {};
    score = 0;
    renderQuestions();
    updateScore();
}

// Update score display
function updateScore() {
    score = 0;
    questions.forEach(q => {
        if (userAnswers[q.id] === q.correct) {
            score++;
        }
    });
    
    const scoreElement = document.getElementById('score');
    const totalElement = document.getElementById('total');
    
    if (scoreElement) scoreElement.textContent = score;
    if (totalElement) totalElement.textContent = totalQuestions;
}
