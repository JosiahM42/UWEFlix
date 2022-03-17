from email import message
from django import forms
from uweflix.models import Film

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
















class loginForm(forms.Form):
        userName = forms.CharField(max_length=12)
        password = forms.PasswordInput()

class signUpFormForm(forms.Form):
        userName = forms.CharField()
        password = forms.PasswordInput()





