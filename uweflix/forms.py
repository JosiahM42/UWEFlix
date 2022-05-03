# from email import message
# #from turtle import Screen
# from django import forms
# from uweflix.models import Film, Venue, Account, Screen, Club
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from django.forms import  TextInput, Textarea, PasswordInput, NumberInput, Select

# from email import message
# from attr import field
#from turtle import Screen
from django import forms
from uweflix.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from django.forms import  *
from django.forms import ModelForm
class signUpForm(UserCreationForm):
        #email = forms.EmailField(required=True)

        class Meta:
                model = Account
                # fields = "__all__"
                fields =('username','email', 'password1', 'password2', 'is_club')

                # if email were to be used as the unique identifier

                # widgets = {
                # 'username': TextInput(attrs={
                # 'class': "signUpForm",
                # 'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:50%',
                # 'placeholder': 'Enter username...' 
                # }),
                # 'email': TextInput(attrs={
                # 'class': "signUpForm",
                # 'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:50%',
                # 'placeholder': 'Enter email...' 
                # }),
                # 'password1': PasswordInput(attrs={
                # 'class': "signUpForm",
                # 'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:50%',
                # 'placeholder': 'Enter password...' 
                # }),
                # 'password2': PasswordInput(attrs={
                # 'class': "signUpForm",
                # 'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:50%',
                # 'placeholder': 'Enter re-enter password...' 
                # }),

                # }


# class loginForm(AuthenticationForm):
#         username = forms.CharField(widget=forms.TextInput())
#         password = forms.CharField(widget=forms.PasswordInput())

#         class Meta:
#                 model = Account
        
class clubRegistrationForm(ModelForm):
        class Meta:
                model = Club
                # fields = "__all__"
                fields =('club_name','street_address', 'postcode', 'city', 'phone', 'account_id')

                def __init__(self, *args,**kwargs):
                        super (signUpForm,self ).__init__(*args,**kwargs)
                        self.fields['account_id'].queryset = Account.objects.filter(is_club=True)

                widgets = {
                'club_name': TextInput(attrs={
                'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:30%',
                'placeholder': 'Enter club name...' 
                }),
                'street_address': TextInput(attrs={
                      'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:30%',
                'placeholder': 'Enter street address...' 
                }),
                'postcode': TextInput(attrs={
                'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:30%',
                'placeholder': 'Enter postcode...' 
                }),
                'city': TextInput(attrs={
                'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:30%',
                'placeholder': 'Enter city...' 
                }),
                'phone': NumberInput(attrs={
                'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:30%',
                'placeholder': 'Enter club phone number...' 
                }),
                'account_id': Select(attrs={
                'class': "clubRegistrationForm",
                'style':'padding:8px;display:block;border:none;border-bottom:1px solid #ccc;width:20%',
                'placeholder': 'Account' 
                }),
                }

class activateCustomerAccounts(ModelForm):
        class Meta:
                model = Account
                fields = ('username','email', 'is_club', 'is_customer', 'is_active')

        # def __init__(self, *args,**kwargs):
        #         super (activateCustomerAccounts,self ).__init__(*args,**kwargs)
        #         self.fields['username'].queryset = Account.objects.filter(is_club=True)

class addFilmForm(ModelForm):
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

class addVenueForm(ModelForm):
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



class addScreenForm(ModelForm):
        class Meta:
                model = Screen
                fields = ("venue_id", "screen_num", "capacity",)

                #Styles Form boxes
                widgets = {
                'screen_num': TextInput(attrs={
                'class': "addScreenForm",
                'style': 'max-width: 300px;',
                'placeholder': 'eg 1'
                }),
                'capacity': TextInput(attrs={
                'class': "addVenueForm",
                'style': 'max-width: 300px;',
                'placeholder': 'Eg 120'
                })

        }




















# class loginForm(forms.Form):
#         userName = forms.CharField(max_length=12)
#         password = forms.PasswordInput()

# class signUpFormForm(forms.Form):
#         userName = forms.CharField()
#         password = forms.PasswordInput()
