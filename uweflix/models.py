from django.db import models
from django.utils import timezone

class Film(models.Model):
    # film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    age_rating =  models.CharField(max_length=4)
    duration = models.TimeField()

class Venue(models.Model):
    name =  models.CharField(max_length=25)
    street_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    city = models.CharField(max_length=20)

class Screen(models.Model):
    capacity = models.IntegerField()
    is_full = models.BooleanField()
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    #seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)

class Seat(models.Model):
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=50)


class Showing(models.Model):
    # showing_id = models.AutoField(primary_key=True)
    showing_datetime = models.DateTimeField("date logged")
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)

class Ticket(models.Model):
    # ticket_id = models.AutoField(primary_key=True)
    ticket_price = models.FloatField()
    ticket_type = models.CharField(max_length=10)
    showing_id = models.ForeignKey(Showing, on_delete=models.CASCADE)

class Account(models.Model):
    username =  models.CharField(max_length=12)
    password = models.CharField(max_length=12)

class CinemaAdmin(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_social_distancing = models.BooleanField()

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    email =  models.CharField(max_length=50)
    card_number =  models.IntegerField()
    expiry_date = models.DateField()

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    # representative_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    city = models.CharField(max_length=20)
    phone = models.IntegerField()
    landline = models.IntegerField()
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

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
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    club_discount = models.BooleanField(False)







    