from django.urls import path

from polls import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dayoff/', views.dayoff, name='dayoff'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]