from django.db import models
from django.contrib.auth.models import User



class Data(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_location = models.CharField(max_length=20,default='Unknown')
    rating = models.FloatField()
    review = models.CharField(max_length=50000000)


    def __str__(self):
        return self.hotel_name

class wordcloud(models.Model):
     caption=models.CharField(max_length=50,default='Unknown')
     image = models.ImageField(null=True, blank=True, upload_to="images/")

     def __str__(self):
        return self.caption

# Create your models here.
     
