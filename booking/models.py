from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    agency_name = models.CharField(max_length=100,null=True, blank=True)
    agency_id = models.CharField(max_length=100,null=True, blank=True)
    source = models.CharField(max_length=100,null=True, blank=True)  
    destination = models.CharField(max_length=100,null=True, blank=True)
    source_date = models.DateField(null=True, blank=True)
    source_time = models.TimeField(null=True, blank=True)
    destination_date = models.DateField(null=True, blank=True)
    destination_time = models.TimeField(null=True, blank=True)
    total_seats = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.bus_number} - {self.source} to {self.destination}"

class SeatBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    passenger_name = models.CharField(max_length=10,null=True, blank=True)
    contact_number = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.user.username} - Bus {self.bus.bus_number} - Seat {self.seat_number}"

class Agency(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    pincode = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=100,null=True, blank=True)
    username = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name
