// פונקציות תמיכה כלליות
document.addEventListener('DOMContentLoaded', function() {
    console.log('האתר נטען בהצלחה');

    // הוספת טיפול לטופסי תמיכה
    const supportForms = document.querySelectorAll('.support-form');
    supportForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            // כאן תוכל להוסיף לוגיקה לשליחת טופס תמיכה
            console.log('נשלח טופס תמיכה');
        });
    });

    // פונקציה לטיפול בהודעות
    function showMessage(message, type = 'info') {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('message', type);
        messageContainer.textContent = message;
        document.body.appendChild(messageContainer);

        setTimeout(() => {
            messageContainer.remove();
        }, 3000);
    }
});
