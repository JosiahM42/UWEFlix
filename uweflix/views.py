from django.shortcuts import render
from django.http import *

#Forms 
from uweflix.forms import addFilmForm

#models
from uweflix.models import Film

from django.shortcuts import redirect



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

def studentAccount(request):
    return render(request, "uweflix/studentAccount.html")


def addFilms (request):
    return render(request, "uweflix/addFilms.html")

def allFilms (request):
    return render(request, "uweflix/allFilms.html")


def addFilm(request):
    form = addFilmForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("cinemaAdmin")
    else:
        return render(request, "uweflix/addFilms.html", {"form": form})


# deletes film on request
def deleteFilm(request, id):

     film = Film.objects.get(pk=id)
     film.delete()

     return redirect("allFilms")

# Gets all films in the system to be displayed
def getAllFilms(request):

    filmList = Film.objects.all()

    return render (request, 'uweflix/allFilms.html', {'filmList': filmList})
