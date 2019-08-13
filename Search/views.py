""" making this for the sake of it """
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import api_data
import pandas as pd
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'Search/index.html')

def results(request):
    query = request.GET.get('q')
    if query:
        datasets = api_data.objects.filter(Q(datasets_available__icontains=query))
        context = {
            'datasets': datasets,
        }
    
    return render(request, 'Search/results.html', context)

def prompt(request):
    return render(request, 'Search/prompt.html')