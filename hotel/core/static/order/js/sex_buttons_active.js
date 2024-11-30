const buttons = document.querySelectorAll('.sex-button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Убираем активный класс с всех кнопок
        buttons.forEach(btn => btn.classList.remove('active'));

        // Добавляем активный класс только для выбранной кнопки
        button.classList.add('active');
    });
});
