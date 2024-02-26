from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
 
import numpy as np
import pandas as pd
from .models import Data
from .models import wordcloud
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    pics=wordcloud.objects.all()
    hotel_name = []
    price = []
    rating = []
    review = []
    reviews = Data.objects.all()
    for x in reviews:
        hotel_name.append(x.hotel_name)
        price.append(x.price)
        rating.append(x.rating)
        review.append(x.review)

    return render(request, 'dashboard.html',{
        "pics": pics,
        'Hotel_Name': hotel_name,
        'Price': price,
        'Rating': rating,    
        'Review': review
    })

# Create your views here.
