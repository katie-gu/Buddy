from django.shortcuts import render
from django.http import HttpResponse
from . import models
from game.models import Challenge

def home(request):
    return render(request, 'game/home.html')

def profile(request):
    Challenge.objects.create(description="Make a new friend.", xp=50)
    Challenge.objects.create(description="Go for a walk.", xp=100)
    challenge1 = Challenge.objects.get(description="Make a new friend.", xp=50)
    challenge2 = Challenge.objects.get(description="Go for a walk.", xp=100)
    return render(request, "game/profile.html", {'challenge1': challenge1, 'challenge2' : challenge2})

