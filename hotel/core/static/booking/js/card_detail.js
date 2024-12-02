document.addEventListener('DOMContentLoaded', function() {
    // Находим все карточки по классу
    const cards = document.querySelectorAll('.cust-card');

    // Добавляем обработчик клика для каждой карточки
    cards.forEach(card => {
        card.addEventListener('click', function() {
            // Получаем ID карточки
            const cardId = card.id;

            // Получаем текущие параметры из URL
            const urlParams = new URLSearchParams(window.location.search);

            // Создаем новый URL с добавлением пути и параметров
            const newUrl = `card_detail/${cardId}/?` + urlParams.toString();

            // Выполняем редирект на новый URL
            window.location.href = newUrl;
        });
    });
});
