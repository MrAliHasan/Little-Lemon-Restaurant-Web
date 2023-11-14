from django.db import models
from django.utils import timezone

# Create your models here.


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    reservation_date = models.DateField(default=timezone.now)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
