from django.shortcuts import render


# Create your views here.


def main(request):
    return render(request, 'index.html')


def booking(request):
    return render(request, 'booking.html')
