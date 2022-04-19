from django.shortcuts import render
from django.http import *

#Forms
from uweflix.forms import *

#models
from uweflix.models import *

from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.models import

from django.views.generic import *

from django.urls import *

from .models import Account

from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    showingList = Showing.objects.all()

    return render(request, "uweflix/home.html", {'showingList': showingList})


from django.contrib.auth.decorators import login_required, user_passes_test

from django.urls import reverse

def home(request):
    return render(request, "uweflix/home.html")

# def loginRequest(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         attemptedUser = authenticate(request, username=username, password=password)

#         if attemptedUser is not None:
#             login(request, attemptedUser)

#             if attemptedUser.is_club:
#                 return redirect('studentAccount')
#             elif attemptedUser.is_cinema_admin:
#                 return redirect('cinemaAdmin')
#             elif attemptedUser.is_cinema_accounts:
#                 return redirect('accountAdmin')
#         else:
#             messages.info(request, 'The username or password entered is incorrect, please try again')
#             return redirect('login')
        
    

#     return render(request, "uweflix/login.html")

def guestLoginRequest(request):
    guestUser = authenticate(request, username='Guest', password='Customer')
    login(request, guestUser)
    return redirect('home')

def loginRequest(request):
    form = AuthenticationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            attemptedUser = authenticate(username=username, password=password)

            if attemptedUser is not None:
                login(request, attemptedUser)
                messages.info(request, 'Login Sucessful')

                if attemptedUser.is_club:
                    return redirect('studentAccount')
                if attemptedUser.is_cinema_admin:
                    return redirect('cinemaAdmin')
                elif attemptedUser.is_cinema_accounts:
                    return redirect('accountAdmin')
            else:
                messages.info(request, 'The username or password entered is incorrect, please try again')
                return redirect('login')

    return render(request, "uweflix/login.html", context)


def logoutRequest(request):
    logout(request)
    return redirect('login')

def signupRequest(request):
    form = signUpForm()
    context = {'form': form}

    if request.method == 'POST':
        form = signUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            newUser = authenticate(request, username=username, password=password)
            newUser.is_active = False

            newUser.save()

            if newUser is not None:
                messages.success(request, 'New user account has been created {username}')
            else:
                messages.success(request, 'Error found during new user account generation')

            return redirect("home")
        else:
            messages.success(request, 'Password is too short, please enter an 8 mixed character password ')


    return render(request, "uweflix/signup.html", context)


# Club Sign Up

def clubRegistrationRequest(request):
    if request.method == 'POST':
        registrationForm = clubRegistrationForm(request.POST)

        if registrationForm.is_valid():
            registrationForm.save()
            messages.success(request, ('Club has been registered'))
        elif registrationForm.is_valid() == False:
            pass
        return redirect("clubRegister")

    else:
        registrationForm = clubRegistrationForm()

    return render(request, "uweflix/clubRegistration.html", {'clubForm': registrationForm})

def userActivationRequest(request):
    allUsers = Account.objects.filter(is_customer=True).get()
    # clubUsers = allUsers.filter(User.is_club)
    return render(request, "uweflix/activationRequest.html", {"newUser": allUsers})


def tickets(request, id):

    return render(request, "uweflix/tickets.html")

def checkout(request):
    return render(request, "uweflix/checkout.html")

@login_required

@user_passes_test(lambda user: user.groups.filter(name='CinemaAdmin').exists())
def cinemaAdmin(request):
    return render(request, "uweflix/cinemaAdmin.html")

@login_required
@user_passes_test(lambda user: user.groups.filter(name='AccountAdmin').exists())
def accountAdmin(request):
    return render(request, "uweflix/accountAdmin.html")

@login_required
@user_passes_test(lambda user: user.groups.filter(name='ClubRepresentative').exists())
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

def addScreen (request):
    return render(request, "uweflix/addScreen.html")

def allScreen (request):
    return render(request, "uweflix/allScreen.html")


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



# ===== Screen Details CRUD =====
# Add screen from form
def addScreen(request):

    form = addScreenForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("cinemaAdmin")
    else:
        return render(request, "uweflix/addScreen.html", {"form": form})


# deletes screen on request
def deleteScreen(request, screen_id):

    screen = Screen.objects.get(pk=screen_id)
    screen.delete()

    return redirect("allScreen")

# Gets all screens in the system to be displayed
def getAllScreens(request):

    screenList = Screen.objects.all()

    return render(request, 'uweflix/allScreen.html', {'screenList': screenList})

# amend a screens details
def amendScreen(request, screen_id):

    screen = Screen.objects.get(pk=screen_id)

    form = addScreenForm(request.POST or None, instance=screen)

    if form.is_valid():
        form.save()
        return redirect("allScreen")

    else:
        return render(request, "uweflix/amendScreen.html", {"Venue": screen, "form": form})

# ===== Showing Details CRUD =====
# Add screen from form

def addShowing(request):

    form = addShowingForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return render(request, "uweflix/cinemaAdmin.html")
    else:
        return render(request, "uweflix/addShowings.html", {"form": form})


# deletes screen on request
def deleteShowing(request, showing_id):

    showing = Showing.objects.get(pk=showing_id)
    showing.delete()

    return redirect("allShowing")

# Gets all screens in the system to be displayed
def getAllShowing(request):

    showingList = Showing.objects.all()

    return render(request, 'uweflix/allShowing.html', {'showingList': showingList})

# amend a screens details
def amendShowing(request, showing_id):

    showing = Showing.objects.get(pk=showing_id)

    form = addShowingForm(request.POST or None, instance=showing)

    if form.is_valid():
        form.save()
        return redirect("allShowing")

    else:
        return render(request, "uweflix/amendShowing.html", {"Showing": showing, "form": form})




# Drop down box for showings form

class showingListView(ListView):
    model = Showing
    template_name = 'uweflix/addShowings.html'
    context_object_name = 'showingList'

class showingCreateView(CreateView):
    model = Showing
    form_class = addShowingForm
    success_url = reverse_lazy('cinemaAdmin')


class showingUpdateView(UpdateView):
    model = Showing
    form_class = addShowingForm
    success_url = reverse_lazy('cinemaAdmin')


# AJAX Code for showing form
def load_Screens(request):

    venue_id = request.GET.get('venue_id')
    screen_id  = Screen.objects.filter(venue_id=venue_id).all()

    return render(request, 'uweflix/screenDropdownList.html', {'screen_id_list': screen_id})



#tickets
def getTicketFromShowing(request, showing_id):

    user_id = None

    form = purchaseTicketForm(request.POST or None)

    showing = Showing.objects.get(pk=showing_id)



    if request.method == "POST":
        print("temp")
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return render(request, "uweflix/checkout.html")
    else:
        return render(request, "uweflix/tickets.html", {"showing": showing, "form": form})




# User Account Views
# def signUpRequest(request):
#     form = signUpForm()
#     context = {'form': form}
#     return render(request, "uweflix/signup.html", context)
