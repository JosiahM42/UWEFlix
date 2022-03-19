from django.urls import path
from uweflix import views

urlpatterns = [

    #form url
    # Note!!!!!! all form stuff must got at the top as django looks for each page top to bottom, so form version of page must go above and take priority 
    path("addFilms/", views.addFilm, name="addFilm"),
    path("allFilms/", views.getAllFilms, name="addFilm"),
    path("deleteFilm/<id>", views.deleteFilm, name="deleteFilm"),
    path("amendFilm/<id>", views.amendFilm, name="amendFilm"),


    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("tickets/", views.tickets, name="tickets"),
    path("checkout/", views.checkout, name="checkout"),
    path("cinemaAdmin/", views.cinemaAdmin, name="cinemaAdmin"),
    path("accountAdmin/", views.accountAdmin, name="accountAdmin"),
    path("studentAccount/", views.studentAccount, name="studentAccount"),
    path("addFilms/", views.addFilms, name="addFilms"),
    path("allFilms/", views.allFilms, name="allFilms"),
    path("addVenues/", views.addVenues, name="addVenues"),
    path("allVenues/", views.allVenues, name="allVenues"),



]
