from django.db import models

# These are temporary testing models only using strings

'''class Agency(models.Model):
   agency_id = models.CharField(max_length=10) # ex. HSR
   agency_name = models.CharField(max_length=100)
   agency_url = models.CharField(max_length=100)
   agency_timezone = models.CharField(max_length=25)
   agency_lang = models.CharField(max_length=10)
   agency_phone = models.CharField(max_length=10)

class Calendar(models.Model):
   end_date = models.CharField(max_length=10)
   monday = models.CharField(max_length=10)
   tuesday = models.CharField(max_length=10)   
   friday = models.CharField(max_length=10)   
   wednesday = models.CharField(max_length=10)   
   thursday = models.CharField(max_length=10)   
   saturday = models.CharField(max_length=10)   
   sunday = models.CharField(max_length=10)
   service_id = models.CharField(max_length=10)
   start_date = models.CharField(max_length=10)
'''
# The Field types/attributes are subject to change in the near future   
class Route(models.Model):
   route_long_name = models.CharField(max_length=40)
   route_short_name = models.CharField(max_length=4)

class Trip(models.Model):
   direction_id = models.CharField(max_length=3)
   route = models.ForeignKey(Route)

class StopTime(models.Model):
   arrival_time = models.CharField(max_length=15)
   trip = models.ManyToManyField(Trip)
