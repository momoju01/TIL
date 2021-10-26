from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


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
    foods = ['족발', 'hamburger', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message_t')
    context = {
        'message_c':message
    }
    return render(request, 'articles/catch.html', context)