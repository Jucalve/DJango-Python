from django.db import models


# Create your models here.
#It's linked to a DB
class Feature(models.Model): # (...) to convert basic class into a model
    #id: int        #Automatically generates an ID
    name = models.CharField(max_length=90,default='example') #%%%%Field for data types
    details = models.CharField(max_length=500,default='example')