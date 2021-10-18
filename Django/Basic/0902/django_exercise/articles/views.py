from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Alice'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    menus = ['pizza', 'chicken', 'susi', 'ramen']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
    }
    return render(request, 'articles/dinner.html', context)


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)
