from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "uweflix/home.html")

def login(request):
    return render(request, "uweflix/login.html")

def signup(request):
    return render(request, "uweflix/signup.html")
