from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_http_methods
# Create your views here.


@require_http_methods(['GET', 'POST'])
def signup(request):
    # Q1-1
    # POST 방식
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 유효성 검사
            user = form.save()
            return redirect('accounts:login')
            
    else:  # GET 방식
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)



@require_http_methods(['GET', 'POST'])
def login(request):
    # Q2-1
    # POST 방식
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect('accounts:index')
            return render(request, 'accounts/index.html')
    else:  # GET 방식
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)