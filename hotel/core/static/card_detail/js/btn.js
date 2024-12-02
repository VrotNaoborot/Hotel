document.addEventListener('DOMContentLoaded', function() {
    // Находим кнопку по классу
    const orderButton = document.querySelector('.btn-order');

    // Проверяем, если кнопка существует
    if (orderButton) {
        orderButton.addEventListener('click', function() {
            // Получаем текущий URL
            const currentUrl = window.location.href;

            // Извлекаем ID карточки из URL
            const urlParams = new URLSearchParams(window.location.search);
            const cardId = window.location.pathname.split('/')[2]; // ID будет в части пути URL после card_detail/

            // Если ID не найден, выводим ошибку
            if (!cardId) {
                console.error('ID не найден в URL');
                return;
            }

            // Парсим параметры из URL
            // Формируем новый URL с card_detail и параметрами
            const newUrl = `/card_detail/${cardId}/order?${urlParams.toString()}`;

            // Редирект на новый URL с параметрами
            window.location.href = newUrl;
        });
    }
});
