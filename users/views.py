from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'users/register.html')

def register(request):
    #if request.method == "POST":
    return render(request, 'users/register.html')