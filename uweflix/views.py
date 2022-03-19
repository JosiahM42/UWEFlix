from django.shortcuts import render
from django.http import *

#Forms 
from uweflix.forms import *

#models
from uweflix.models import *

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

def addVenues (request):
    return render(request, "uweflix/addVenues.html")

def allVenues (request):
    return render(request, "uweflix/allVenues.html")


#Film Details CRUD
# Add films from form
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

#
def amendFilm(request, id):

    film = Film.objects.get(pk=id)
    form = addFilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect("allFilms")
    
    else:
        return render(request, "uweflix/amendFilms.html", {"film": film, "form": form})


# Venue Details CRUD
# Add venue from form
def addVenue(request):

    form = addVenueForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("cinemaAdmin")
    else:
        return render(request, "uweflix/addVenues.html", {"form": form})


# deletes venues on request
def deleteVenue(request, venue_id):

    venue = Venue.objects.get(pk=venue_id)
    venue.delete()

    return redirect("allVenues")

# Gets all venues in the system to be displayed
def getAllVenues(request):

    venueList = Venue.objects.all()

    return render(request, 'uweflix/allVenues.html', {'venueList': venueList})

#
def amendVenue(request, venue_id):

    venue = Venue.objects.get(pk=venue_id)
    form = addVenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect("allVenues")
    
    else:
        return render(request, "uweflix/amendVenues.html", {"Venue": venue, "form": form})