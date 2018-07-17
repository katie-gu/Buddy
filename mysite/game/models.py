from django.db import models

# Create your models here.
class Challenge(models.Model):
    description = models.TextField(max_length=500, default="")
    #begin_date = models.DateTimeField()
    #end_date = models.DateTimeField()
    #completed = models.BooleanField(default=False)
    xp = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class AppUser(models.Model):
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")
    challenges_completed = models.ManyToManyField(Challenge)

    def __str__(self):
        return self.name