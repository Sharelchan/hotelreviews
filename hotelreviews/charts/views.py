from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
 
import numpy as np
import pandas as pd
from .models import Data
from .models import wordcloud
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize 
from django.db.models import Avg
from django.http import JsonResponse



def index(request):
    pics=wordcloud.objects.all()
    hotel_name = []
    hotel_location = []
    rating = []
    review = []
    reviews = Data.objects.all()
    for x in reviews:
        hotel_name.append(x.hotel_name)
        hotel_location.append(x.hotel_location)
        rating.append(x.rating)
        review.append(x.review)
    #serialized_data = serialize('json', hotel_name) 
    data = Data.objects.all()   
    # Serialize the values into JSON format    
    serialized_data = serialize('json', data)
        

    return render(request, 'dashboard.html',{
        "pics": pics,
        'Hotel_Name': hotel_name,
        'Hotel_location': hotel_location,
        'Rating': rating,    
        'Review': review,
        'serialized_data': serialized_data
    })


# Create your views here.
