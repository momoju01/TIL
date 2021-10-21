from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name='profile'),  # 이거 맨 마지막에 가야됨! update위에 있으면 username을 update인 사람 있다고 인식할 수도
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
