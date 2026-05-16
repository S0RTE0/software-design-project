from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Cinema(models.Model):
    name = models.CharField(max_length=100, verbose_name="Cinema Name")
    description = models.TextField(blank=True, verbose_name="Description")
    location = models.CharField(max_length=255, default="Main Street, 1", verbose_name="Location")
    contacts = models.CharField(max_length=100, default="+380 (44) 123-45-67", verbose_name="Contacts")
    working_hours = models.CharField(max_length=100, default="10:00 - 22:00", verbose_name="Working Hours")

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name="Hall Name")
    seats_count = models.IntegerField(verbose_name="Number of seats")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls')

    def __str__(self):
        return f"Hall {self.name} ({self.cinema.name})"

class Session(models.Model):
    name = models.CharField(max_length=150, verbose_name="Movie Name")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ticket Price")
    is_available = models.BooleanField(default=True, verbose_name="Is Available")
    start_time = models.DateTimeField(default=timezone.now, verbose_name="Start Time")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='sessions')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='sessions', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price} uah"

class Ticket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tickets')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='tickets')
    seat_number = models.IntegerField(verbose_name="Seat Number")
    purchased_at = models.DateTimeField(auto_now_add=True, verbose_name="Purchased At")

    def __str__(self):
        return f"Ticket: {self.user.username} - {self.session.name} (Seat {self.seat_number})"
