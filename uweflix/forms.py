from email import message
from django import forms
from uweflix.models import Film

from django.forms import ModelForm, TextInput, EmailInput


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
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Film Title'
                }),
                'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'whats the film about?'
                }),
                # 'age_rating': TextInput(attrs={
                # 'class': "form-control",
                # 'style': 'max-width: 300px;',
                # 'placeholder': 'Am I going to be called a bad uncle for letting my nephew see this film'
                # }),
                'duration': EmailInput(attrs={
                'class': "form-control",
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





