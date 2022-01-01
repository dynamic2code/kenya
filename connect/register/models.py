from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Person(models.Model):
    
    person_id = IntegerField
    person_name = CharField(max_length=64)
    person_password = CharField(max_length=64)

    def register(self):
        #accepts the details of the user and stores in the db
        #     
        pass


    def log_in(person_name,person_password):
        if (person_name == person_name):
            if (person_password == person_password):
                #will come as a pop up window and transit to the next page
                print("wellcome")
        else:
            print("wrong details please try again")


            
                        


    def generate_person_id(person_name):
        first_id = 1475
        out_fist_id = "ckps" + str(first_id)
      


# for the company
# 

class Company(models.Model):
   
    Com_name = CharField
    com_id = IntegerField
    package_level = IntegerField
    #the pckege level shows the services the company is suscribed to   


    def log_in_company():
        pass    

    def generate_company_number():
        pass 
    #generates the id for com to show the total number
   

class links:
    def __init__(self):
        pass
    


    # the links to be generated
    def link_generator():
        pass