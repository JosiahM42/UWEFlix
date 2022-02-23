from django.urls import path
from EsdGroup import views

urlpatterns = [
    path("", views.home, name="home"),
    path("EsdGroup/<name>", views.hello_there, name="hello_there"),
]