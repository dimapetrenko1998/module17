from django.shortcuts import render


def home(request):
    return render(request, 'third_task/home.html')


def shop(request):
    items = {
        'item1': 'Game 1',
        'item2': 'Game 2',
        'item3': 'Game 3'
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
