from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=100, verbose_name="Cinema Name")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=150, verbose_name="Movie Name")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ticket Price")
    is_available = models.BooleanField(default=True, verbose_name="Is Available")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='sessions')

    def __str__(self):
        return f"{self.name} - {self.price} uah"

class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name="Hall Name")
    seats_count = models.IntegerField(verbose_name="Number of seats")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls')

    def __str__(self):
        return f"Hall {self.name} ({self.cinema.name})"
