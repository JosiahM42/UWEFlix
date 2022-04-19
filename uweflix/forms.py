from email import message
from django import forms
from uweflix.models import Film, Venue, Account, Screen
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from django.forms import  TextInput, Textarea, PasswordInput

class signUpForm(UserCreationForm): 
        #email = forms.EmailField(required=True)
        class Meta:
                model = Account
                # fields = "__all__"
                fields =('username',
                         'first_name',
                         'last_name',
                         'email', 
                         'password1', 
                         'password2', 
                         'is_club')
        def save(self, commit=True):
                Account = super(signUpForm, self).save(commit=False)
                Account.first_name = self.cleaned_data['first_name']
                Account.last_name = self.cleaned_data['last_name']
                Account.email = self.cleaned_data['email']

                if commit:
                        Account.save()

                return Account
                # if email were to be used as the unique identifier
                # fields = ('email', 'password1', 'password2', 'is_club')
#Edit profile                
class EditProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')

# class loginForm(AuthenticationForm):
#         username = forms.CharField(widget=forms.TextInput())
#         password = forms.CharField(widget=forms.PasswordInput())

#         class Meta:
#                 model = Account

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





