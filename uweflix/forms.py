from email import message
from django import forms
from uweflix.models import Film, Venue

from django.forms import  TextInput, Textarea


# venues= [('uwe', 'UWE')
#         ('temp', 'temp')]

# class venueForm(forms.Form):
#    choseVenue = forms.CharField(label='Choose a Venue: ', widget=forms.Select(choices=venues))


class addFilmForm(forms.ModelForm):
        class Meta:
                model = Film
                fields = ("title","description", "age_rating", "duration",) #
                #Styles Form boxes
                widgets = {
                'title': TextInput(attrs={
                'class': "addFilmsForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Film Title'
                }),
                'description': Textarea(attrs={
                'class': "addFilmsForm",
                'style': 'max-width: 300px;',
                'placeholder': 'whats the film about?'
                }),
                'duration': TextInput(attrs={
                'class': "addFilmsForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Eg, 1:30:30'
                })
        }

class addVenueForm(forms.ModelForm):
        class Meta:
                model = Venue
                fields = ("name","street_address", "postcode", "city",) #
                
                #Styles Form boxes
                widgets = {
                'name': TextInput(attrs={
                'class': "addVenueForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Venue name'
                }),
                'street_address': TextInput(attrs={
                'class': "addVenueForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Full address'
                }),'postcode': TextInput(attrs={
                'class': "addVenueForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Eg BS16 1WE'
                }),
                'city': TextInput(attrs={
                'class': "addVenueForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Eg Bristol'
                })
        }
















class loginForm(forms.Form):
        userName = forms.CharField(max_length=12)
        password = forms.PasswordInput()

class signUpFormForm(forms.Form):
        userName = forms.CharField()
        password = forms.PasswordInput()





