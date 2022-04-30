from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('verification/', views.verification, name='verification'),
    path('error/', views.error, name='error'),
    path('vacinas/', views.vacMain, name='vacinas'),
] 
