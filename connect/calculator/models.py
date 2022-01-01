from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField

# Create your models here.
# induction being bringing another person on board
# referral being bringing a web to our service
class Account(models.Model):
    
    initial = IntegerField
    final_amount = IntegerField
    incriment = IntegerField
    withdraw = IntegerField
    referral = IntegerField
    induction = IntegerField

#working on theaccount









#class company_statistics():
    #has 
        #sales
        #popularity
        #social media precence
   