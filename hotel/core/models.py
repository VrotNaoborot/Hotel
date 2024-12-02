from django.db import models


# Create your models here.

class CategoryRoom(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    capacity = models.IntegerField(verbose_name="Вместимость")
    space = models.IntegerField(verbose_name="Площадь")
    count_room = models.IntegerField(verbose_name="Кол-во комнат")
    amenities = models.JSONField(verbose_name="Удобства", default=list)
    img1 = models.ImageField(verbose_name="Изображение 1")
    img2 = models.ImageField(verbose_name="Изображение 2")
    img3 = models.ImageField(verbose_name="Изображение 3")
    img4 = models.ImageField(verbose_name="Изображение 4")
    img5 = models.ImageField(verbose_name="Изображение 5")

    class Meta:
        verbose_name = "Категория комнаты"
        verbose_name_plural = "Категории комнат"

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField(primary_key=True, verbose_name="Номер комнаты")
    category = models.ForeignKey(CategoryRoom, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена комнаты")

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    number = models.CharField(max_length=30, verbose_name="Номер телефона")
    mail = models.CharField(max_length=100, verbose_name="Почта")
    total_price = models.IntegerField(verbose_name="Итоговая цена")
    check_in_date = models.DateField(verbose_name="Дата заезда")
    check_out_date = models.DateField(verbose_name="Дата выезда")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
