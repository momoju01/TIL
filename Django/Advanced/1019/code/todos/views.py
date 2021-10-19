from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    # 이 코드의 문제 : 서로의 toto를 볼 수 있음
    # todos = Todo.objects.all()   
    todos = request.user.todo_set.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context )

@login_required
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)