"""
This forms.py has been created for adding extra fields
"""

from django import forms
from django.contrib.auth.models import User # built in model in django
from django.contrib.auth.forms import UserCreationForm # since UserCreationForm has only default fields [username, password1, password2] so we create UserRegisterForm and inherit UserCreationForm to add email
from . models import Profile

class UserRegisterForm(UserCreationForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']