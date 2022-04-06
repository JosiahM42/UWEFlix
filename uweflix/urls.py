from django.urls import path
from uweflix import views

urlpatterns = [

    #form url
    # Note!!!!!! all form stuff must got at the top as django looks for each page top to bottom, so form version of page must go above and take priority 
    
    #Films
    path("addFilms/", views.addFilm, name="addFilm"),
    path("allFilms/", views.getAllFilms, name="addFilm"),
    path("deleteFilm/<id>", views.deleteFilm, name="deleteFilm"),
    path("amendFilm/<id>", views.amendFilm, name="amendFilm"),

    #Venues
    path("addVenues/", views.addVenue, name="addVenues"),
    path("allVenues/", views.getAllVenues, name="allVenues"),
    path("deleteVenues/<venue_id>", views.deleteVenue, name="deleteVenues"),
    path("amendVenues/<venue_id>", views.amendVenue, name="amendVenues"),

    #Screens
    path("addScreen/", views.addScreen, name="addScreen"),
    path("allScreen/", views.getAllScreens, name="allScreen"),
    path("deleteScreen/<screen_id>", views.deleteScreen, name="deleteScreen"),
    path("amendScreen/<screen_id>", views.amendScreen, name="amendScreen"),

    #Showing
    path("addShowing/", views.addShowing, name="addShowing"),
    path("allShowing/", views.getAllShowing, name="allShowing"),
    path("deleteShowing/<showing_id>", views.deleteShowing, name="deleteShowing"),
    path("amendShowing/<showing_id>", views.amendShowing, name="amendShowing"), 

    path('ajax/load-screens/', views.load_Screens, name='ajax_screen_branches'),


    #Ticket system 
    path("tickets/<showing_id>", views.tickets, name="tickets"),

    path("", views.home, name="home"),
    path("login/", views.loginRequest, name="login"),
    path("logout/", views.logoutRequest, name="logout"),
    path("signup/", views.signupRequest, name="signup"),
    path("tickets/", views.tickets, name="tickets"),
    path("checkout/", views.checkout, name="checkout"),
    path("cinemaAdmin/", views.cinemaAdmin, name="cinemaAdmin"),
    path("accountAdmin/", views.accountAdmin, name="accountAdmin"),
    path("studentAccount/", views.studentAccount, name="studentAccount"),
    path("addFilms/", views.addFilms, name="addFilms"),
    path("allFilms/", views.allFilms, name="allFilms"),
    path("addVenues/", views.addVenues, name="addVenues"),
    path("allVenues/", views.allVenues, name="allVenues"),
    # path("addScreen/", views.addScreen, name="addScreen"),
    # path("allScreen/", views.allScreen, name="allScreen"),



]
