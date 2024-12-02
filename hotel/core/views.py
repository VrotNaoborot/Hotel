from django.shortcuts import render
from .models import *
from datetime import *
import locale
from pymystem3 import Mystem

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def main(request):
    return render(request, 'index.html')


def booking(request):
    # Получаем параметры запроса
    check_in = request.GET.get('date')  # Дата заезда
    nights = request.GET.get('nights')  # Количество ночей
    adults = request.GET.get('adults')  # Количество взрослых
    child_age = request.GET.get('children-age', '')  # Возраст детей (строка с ;)
    child_ages = child_age.split(';') if child_age else []

    try:
        # Преобразуем параметры в нужный формат
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        nights = int(nights)
        adults = int(adults)
        total_guests = adults + len(child_ages)
        check_out_date = check_in_date + timedelta(days=nights)
    except (ValueError, TypeError):
        error_message = "Неверный формат данных. Убедитесь, что все поля заполнены корректно."
        return render(request, 'booking.html', {'error': error_message})

    res_categories = []
    suitable_categories = CategoryRoom.objects.filter(capacity__gte=total_guests)

    for category in suitable_categories:
        # Получаем все комнаты категории
        rooms = Room.objects.filter(category=category)

        available_rooms = []

        for room in rooms:
            # Проверяем, занята ли комната в указанный период
            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            )

            # Если нет пересечений с бронированиями, значит, комната доступна
            if not overlapping_bookings.exists():
                if hasattr(category, 'min_price'):
                    if category.min_price > room.price:
                        category.min_price = room.price
                else:
                    category.min_price = room.price
                available_rooms.append(room)

        # Если есть хотя бы одна свободная комната в категории, добавляем её в результат
        if available_rooms:
            res_categories.append(category)
    return render(request, 'booking.html', {'categories': res_categories})


def card_detail(request, id):
    category = CategoryRoom.objects.filter(id=id)
    if category:
        rooms = Room.objects.filter(category=category[0])
        check_in = request.GET.get('date')  # Дата заезда
        nights = request.GET.get('nights')  # Количество ночей
        adults = request.GET.get('adults')  # Количество взрослых
        child_age = request.GET.get('children-age', '')  # Возраст детей (строка с ;)
        child_ages = child_age.split(';') if child_age else []

        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        nights = int(nights)
        adults = int(adults)
        check_out_date = check_in_date + timedelta(days=nights)

        available_rooms = []

        for room in rooms:
            # Проверяем, занята ли комната в указанный период
            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            )

            # Если нет пересечений с бронированиями, значит, комната доступна
            if not overlapping_bookings.exists():
                if hasattr(category[0], 'min_price'):
                    if category[0].min_price > room.price:
                        category[0].min_price = room.price
                else:
                    category[0].min_price = room.price
                available_rooms.append(room)

        if available_rooms:
            return render(request, 'card_detail.html', {'count_rooms': len(available_rooms),
                                                        'category': category[0]})


def declension_of_adult(number):
    if 11 <= number % 100 <= 14:
        return f"{number} взрослых"
    elif number % 10 == 1:
        return f"{number} взрослый"
    elif 2 <= number % 10 <= 4:
        return f"{number} взрослых"
    else:
        return f"{number} взрослых"


def declension_of_child(number):
    if 11 <= number % 100 <= 14:
        return f"{number} детей"
    elif number % 10 == 1:
        return f"{number} ребенок"
    elif 2 <= number % 10 <= 4:
        return f"{number} ребенка"
    else:
        return f"{number} детей"


def declension_of_night(number):
    if 11 <= number % 100 <= 14:
        return f"{number} Ночей"
    elif number % 10 == 1:
        return f"{number} Ночь"
    elif 2 <= number % 10 <= 4:
        return f"{number} Ночи"
    else:
        return f"{number} Ночей"


def get_day_of_week(date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]


def order(request, id):
    category = CategoryRoom.objects.filter(id=id)
    if category:
        rooms = Room.objects.filter(category=category[0])
        check_in = request.GET.get('date')  # Дата заезда
        nights = request.GET.get('nights')  # Количество ночей
        adults = request.GET.get('adults')  # Количество взрослых
        child_age = request.GET.get('children-age', '')  # Возраст детей (строка с ;)
        child_ages = child_age.split(';') if child_age else []

        # Преобразуем строку даты в объект datetime
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        nights = int(nights)  # Преобразуем количество ночей в целое число
        adults = int(adults)  # Преобразуем количество взрослых в целое число

        # Рассчитываем дату выезда
        check_out_date = check_in_date + timedelta(days=nights)

        # Получаем день недели для даты заезда и выезда
        check_in_day_of_week = get_day_of_week(check_in_date)
        check_out_day_of_week = get_day_of_week(check_out_date)

        # Форматируем даты в формат "день месяц" (например, 20 ноября)
        check_in_formatted = check_in_date.strftime("%d %B")
        check_out_formatted = check_out_date.strftime("%d %B")

        for room in rooms:
            # Проверяем, занята ли комната в указанный период
            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            )

            # Если нет пересечений с бронированиями, значит, комната доступна
            if not overlapping_bookings.exists():
                if hasattr(category[0], 'min_price'):
                    if category[0].min_price > room.price:
                        category[0].min_price = room.price
                else:
                    category[0].min_price = room.price

        return render(request, 'order.html', {
            'check_in_formatted': check_in_formatted,
            'check_out_formatted': check_out_formatted,
            'check_in_day_of_week': check_in_day_of_week,
            'check_out_day_of_week': check_out_day_of_week,
            'adults_word': declension_of_adult(adults),
            'child_word': declension_of_child(len(child_ages)),
            'category': category[0],
            'nights_word': declension_of_night(nights)
        })
