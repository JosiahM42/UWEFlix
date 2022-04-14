from email import message
#from turtle import Screen
from django import forms
from uweflix.models import * # Film, Venue, Account, Screen, Showing
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import  TextInput, Textarea, DateTimeInput


class signUpForm(UserCreationForm):
        #email = forms.EmailField(required=True)

        class Meta:
                model = Account
                # fields = "__all__"
                fields =('username','email', 'password1', 'password2', 'is_club')

                # if email were to be used as the unique identifier
                # fields = ('email', 'password1', 'password2', 'is_club')


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



class addScreenForm(forms.ModelForm):
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



class addShowingForm(forms.ModelForm):
        class Meta:
                model = Showing
                fields = ("showing_time","showing_date","film_id", "venue_id" , "screen_id",)
                
                #Styles Form boxes

        # Code to get the relevent screen IDs for the selected venue ID and display it in the dropdown menu so be selected from (not working)


        def __init__(self, *args, **kwargs):
                # Overrides default and set the screens id drop down box as empty
                super().__init__(*args, **kwargs)
                self.fields['screen_id'].queryset = Screen.objects.none()

                if 'venue_id' in self.data:
                        #print("running")
                        try:
                               # print("running2")
                                venue_id = self.data.get('venue_id')
                               # print("running3")
                                self.fields['screen_id'].queryset = Screen.objects.filter(venue_id=venue_id).order_by('screen_num')
                                #print("running4")
                        except (ValueError, TypeError):
                                #print("running5")
                                pass  # invalid input from the client; ignore and fallback to empty screen queryset
                 
                        
                # elif self.instance.pk:
                #         self.fields['screen_id'].queryset = Screen.objects.filter(venue_id=self.instance.venue_id)     

                # if 'country' in self.data:
                #         try:
                #                 country_id = int(self.data.get('country'))
                #                 self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                #         except (ValueError, TypeError):
                  
                #                 pass  # invalid input from the client; ignore and fallback to empty City queryset
                # elif self.instance.pk:
                #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')




# class loginForm(forms.Form):
#         userName = forms.CharField(max_length=12)
#         password = forms.PasswordInput()

# class signUpFormForm(forms.Form):
#         userName = forms.CharField()
#         password = forms.PasswordInput()
