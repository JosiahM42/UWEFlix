# Admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rsa import sign
from .models import *
from .forms import signUpForm

class UserAdministrator(UserAdmin):
    model = Account
    add_form = signUpForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_cinema_admin',
                    'is_cinema_accounts',
                    'is_club',
                )
            }
        )
    )

# Registering user model
admin.site.register(Account, UserAdministrator)

admin.site.register(CinemaAdmin)

admin.site.register(AccountAdmin)

admin.site.register(Club)



# Register your models here.