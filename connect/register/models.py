from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Person(models.Model):
    
    person_id = IntegerField
    person_name = CharField(max_length=64)
    person_password = CharField(max_length=64)

# for the company

class Company(models.Model):
   
    Com_name = CharField
    com_id = IntegerField
    package_level = IntegerField
    #the pckege level shows the services the company is suscribed to   
   
