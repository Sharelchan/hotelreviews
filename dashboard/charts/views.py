from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
 
import numpy as np
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'users/dashboard.html')



# class Api(TemplateView):
#     # Create your views here.
#     def getData(request):
#         samp = np.random.randint(100,600,size=(4,5)) #size means the array size
#         df = pd.DataFrame(samp, index=['alex','danny','lina','david'],columns=['Jan','Feb','Mar','Apr','May'])
#         return HttpResponse(df.to_html(classes='table table-bordered'))
    
 

# Create your views here.
