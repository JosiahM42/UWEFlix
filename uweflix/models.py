from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Used if email were to be used as a user's unique identifier
# from django.utils.translation import ugettext_lazy as _

from django.conf import settings

import uuid


Age_rating_UK= [
    ('U','U'),
    ('PG','PG'),
    ('12A','12A'),
    ('12','12'),
    ('15','15'),
    ('18','18'),
    ]

class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    age_rating =  models.CharField(max_length=3, choices=Age_rating_UK)
    duration = models.DurationField(max_length=8)

class Venue(models.Model):
    venue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name =  models.CharField(max_length=25)
    street_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=8)
    city = models.CharField(max_length=20)

    def __str__(self):
	    return self.name


class Screen(models.Model):
    screen_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    screen_num = models.IntegerField(max_length=2)
    capacity = models.IntegerField(max_length=3)
    is_full = models.BooleanField(default=False)
    

class Seat(models.Model):
    seat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    
class Showing(models.Model):
    showing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    showing_datetime = models.DateTimeField("date logged")
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    ticket_price = models.FloatField()
    ticket_type = models.CharField(max_length=10)
    showing_id = models.ForeignKey(Showing, on_delete=models.CASCADE)

class Account(AbstractUser):

    # if username was removed and email was used as the unique identifier
    # username = None
    # email = models.EmailField(_('email address'), unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    is_cinema_admin = models.BooleanField(default=False)
    is_cinema_accounts = models.BooleanField(default=False)
    is_club = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    # pass
    

class CinemaAdmin(models.Model):
    account_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_social_distancing = models.BooleanField()

class Token(models.Model):
    quantity = models.IntegerField(default=0)
    purchased_datetime =  models.DateTimeField("date logged")

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    email =  models.CharField(max_length=50)
    account_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    tokenID = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, blank=True)

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    # representative_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    city = models.CharField(max_length=20)
    phone = models.IntegerField()
    landline = models.IntegerField(null=True, blank=True)
    account_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Booking(models.Model):
    # booking_id = models.AutoField(primary_key=True)
    booking_datetime =  models.DateTimeField("date logged")
    ticket_quantity = models.IntegerField(default=0)
    is_club_booking = models.BooleanField(False)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, models.SET_NULL, null=True)
    club_id = models.ForeignKey(Club, models.SET_NULL, null=True)

class Statements(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class AccountAdmin(models.Model):
    account_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club_discount = models.BooleanField(False)

