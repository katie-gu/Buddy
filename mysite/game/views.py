from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return render(request, 'game/home.html')

def profile(request):
    #query(data) 
    return render(request, "game/profile.html")

