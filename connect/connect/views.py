from django.http import HttpResponse
from django.shortcuts import render
from register import views
from calculator import views

def register(request):
    return render (request,'register.html')
def log_in(request):
     return render (request,'register/log_in.html')
def sign_up(request):
     return render (request,'register/sign_up.html')
def calculator(request):
    return render (request,'calculator/calculator.html')



  