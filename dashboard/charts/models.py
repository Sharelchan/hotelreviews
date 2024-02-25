from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    hotel_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    rating = models.CharField(max_length=50)
    review = models.CharField(max_length=50)

    def __str__(self):
        return self.hotel_name

# Create your models here.
