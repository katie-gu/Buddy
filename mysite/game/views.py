from django.shortcuts import render
from django.http import HttpResponse
from . import models
from game.models import Challenge
from game.models import appUser

def home(request):
    return render(request, 'game/home.html')

#Challenge.objects.create(description="Make a new friend.", xp=50)
#Challenge.objects.create(description="Go for a walk.", xp=100)

def profile(request):
    challenge1 = Challenge.objects.get(description="Make a new friend.", xp=50)
    challenge2 = Challenge.objects.get(description="Go for a walk.", xp=100)
    challenge3 = Challenge.objects.get(description="High five a stranger", xp=80)
    challenge4 = Challenge.objects.get(description="Go outside the house and do 1 pushup", xp=40)
    challenge5 = Challenge.objects.get(description="Say out loud that you are beautiful", xp=30)

    eric =  appUser.objects.all()[0]

    #last argument is a dict that maps HTML NAME to DB ENTRY
    return render(request, "game/profile.html", {
        'challenge1': challenge1,
        'challenge2' : challenge2,
        'challenge3' : challenge3,
        'challenge4' : challenge4,
        'challenge5' : challenge5,
        'eric' : eric})

