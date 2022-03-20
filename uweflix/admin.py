# Admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Registering user model
admin.site.register(Account, UserAdmin)

admin.site.register(CinemaAdmin)

admin.site.register(AccountAdmin)

admin.site.register(Club)



# Register your models here.