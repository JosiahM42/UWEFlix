from email import message
from django import forms
from uweflix.models import *


venues= [('uwe', 'UWE')
        ('temp', 'temp')]

class venueForm(forms.Form):
   choseVenue = forms.CharField(label='Choose a Venue: ', widget=forms.Select(choices=venues))

class loginForm(forms.Form):
        userName = forms.CharField(max_length=12)
        password = forms.PasswordInput(max_length=12)

class signUpFormForm(forms.Form):
        userName = forms.CharField()
        password = forms.PasswordInput()

