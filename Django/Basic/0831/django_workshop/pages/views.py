from django.shortcuts import render

# Create your views here.
def dinner(request, menus, persons):
    context = {
        'menus': menus,
        'persons': persons,
    }
    return render(request, 'dinner.html', context)