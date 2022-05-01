from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('verification/', views.verification, name='verification'),
    path('error/', views.error, name='error'),
    path('vacinas/', views.vacMain, name='vacinas'),
    path('schedule/', views.appointment, name='schedule'),
] 
