from django.forms.forms import Form
from django.http import HttpResponse
from django.shortcuts import render
from connect.forms import PersonForm

def log_in(request):
     return render (request,'register/log_in.html')

def sign_up(request):
     return render (request,'register/sign_up.html',{})


def register(self):
        #accepts the details of the user and stores in the db
        #     
     pass

def verification(request):
     #if correct take to the cite
     pass





    #def log_in(person_name,person_password):
     #   if (person_name == person_name):
      #      if (person_password == person_password):
                #will come as a pop up window and transit to the next page
       #         print("wellcome")
        #else:
         #   print("wrong details please try again")
    #def log_in_company():
     #   pass    

    #def generate_company_number():
     #   pass 

            
# Create your views here
