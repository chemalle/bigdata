from django import forms

from .models import Stocks, Input

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm




class stocksFORM(ModelForm):
     class Meta:
         model = Stocks
         fields = '__all__'


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
