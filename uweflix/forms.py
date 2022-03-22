from email import message
#from turtle import Screen
from django import forms
from uweflix.models import Film, Venue, Account, Screen
from django.contrib.auth.forms import UserCreationForm

from django.forms import  TextInput, Textarea

class signUpForm(UserCreationForm): 
        #email = forms.EmailField(required=True)

        class Meta:
                model = Account
                # fields = "__all__"
                fields =('username','email', 'password1', 'password2', 'is_club')

                # if email were to be used as the unique identifier
                # fields = ('email', 'password1', 'password2', 'is_club')


        


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



# class addScreenForm(forms.ModelForm):
#         class Meta:
#                 model = Screen
#                 fields = "capacity,"
                
#                 #Styles Form boxes
#                 widgets = {
#                 'name': TextInput(attrs={
#                 'class': "addScreenForm",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Screens capacity'
#                 })
#         }




















class loginForm(forms.Form):
        userName = forms.CharField(max_length=12)
        password = forms.PasswordInput()

class signUpFormForm(forms.Form):
        userName = forms.CharField()
        password = forms.PasswordInput()





