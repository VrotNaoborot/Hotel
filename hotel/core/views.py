from django.shortcuts import render


# Create your views here.


def main(request):
    return render(request, 'index.html')


def booking(request):
    return render(request, 'booking.html')


def card_detail(request):
    return render(request, 'card_detail.html')


def order(request):
    return render(request, 'order.html')
