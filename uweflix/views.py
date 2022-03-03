from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "uweflix/home.html")

def login(request):
    return render(request, "uweflix/login.html")

def signup(request):
    return render(request, "uweflix/signup.html")

def tickets(request):
    return render(request, "uweflix/tickets.html")

def checkout(request):
    return render(request, "uweflix/checkout.html")

def cinemaAdmin(request):
    return render(request, "uweflix/cinemaAdmin.html")

def accountAdmin(request):
    return render(request, "uweflix/accountAdmin.html")
