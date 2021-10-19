# 장고가 만든 것
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# 우리가 만든 것
from .forms import CustomUserCreationForm


# Create your views here.
def signup(request):
    if request.method == "POST":  # 사용자가 값을 입력했을 때, 
        form = CustomUserCreationForm(request.POST)  # 종이와 데이터 합치기
        if form.is_valid():
            form.save()                              # 사용자가 입력한 값 db에 저장
            return redirect('accounts:login')

    else:  # GET일 때 -> URL에 접속했을 때
        form = CustomUserCreationForm()  # 얘는 modelform이라서 custom 만듦: Usercreationform이랑 Userchangeform만 modelfrom임(db랑 연동되는form)
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # form에서 어떤 유저인지 가져오고
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()  # 얘는 왜 커스텀 안 하는가? (modelform 아니라서)

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('todos:index')