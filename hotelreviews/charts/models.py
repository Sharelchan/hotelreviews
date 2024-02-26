from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    hotel_name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    rating = models.CharField(max_length=50)
    review = models.CharField(max_length=50000000)


    def __str__(self):
        return self.hotel_name

class wordcloud(models.Model):
     image = models.ImageField(null=True, blank=True, upload_to="images/")

     def __str__(self):
        return f"Wordcloud - {self.image.name}"

# Create your models here.
