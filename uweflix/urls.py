from django.urls import path
from uweflix import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("tickets/", views.tickets, name="tickets"),
    path("checkout/", views.checkout, name="checkout"),

]
