document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".cust-card");

    console.log('!!!!!!!!!! Cards');

    cards.forEach((card) => {
        const images = card.querySelectorAll(".cust-card-first");
        const blocks = card.querySelectorAll(".block");
        const cardTop = card.querySelector(".cust-card-top");

        // Убедимся, что по умолчанию первый блок и изображение активны
        if (images.length > 0 && blocks.length > 0) {
            images[0].classList.add("active");
            blocks[0].classList.add("active");
        }

        // Добавляем событие на наведение для каждого блока
        blocks.forEach((block) => {
            block.addEventListener("mouseenter", () => {
                const target = block.dataset.target;

                // Убираем "active" у всех изображений и блоков внутри текущей карточки
                images.forEach((img) => img.classList.remove("active"));
                blocks.forEach((blk) => blk.classList.remove("active"));

                // Добавляем "active" к текущему блоку и соответствующему изображению
                const targetImage = card.querySelector(`.image-${target}`);
                if (targetImage) {
                    targetImage.classList.add("active");
                }
                block.classList.add("active");
            });
        });

        // Событие при уходе курсора с карточки
        cardTop.addEventListener("mouseleave", () => {
            // Убираем "active" у всех изображений и блоков внутри текущей карточки
            images.forEach((img) => img.classList.remove("active"));
            blocks.forEach((blk) => blk.classList.remove("active"));

            // Возвращаем "active" к первому блоку и изображению
            images[0].classList.add("active");
            blocks[0].classList.add("active");
        });
    });
});
