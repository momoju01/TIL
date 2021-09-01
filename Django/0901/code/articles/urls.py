
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),  # 기본 주소 -> 지금은 http://127.0.0.1:8000/articles/
]