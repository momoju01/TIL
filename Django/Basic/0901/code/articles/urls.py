
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit')
    path('index/', views.index),
    path('', views.index),  # 기본 주소 -> 지금은 http://127.0.0.1:8000/articles/
]