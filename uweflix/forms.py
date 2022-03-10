from email import message
from django import forms
from uweflix.models import *


venues= [('uwe', 'UWE')
        ('temp', 'temp')]

class venueForm(forms.Form):
   choseVenue = forms.CharField(label='Choose a Venue: ', widget=forms.Select(choices=venues))

