from django import forms
from django.forms import ModelForm, fields
from register.models import Person
from register.models import Company

class PersonForm(ModelForm):
    class Meta:
        model= Person
        fields = ('person_name','person_password')