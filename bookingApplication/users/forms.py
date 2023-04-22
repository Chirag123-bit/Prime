from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username","password1", "password2"]






class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ["profile_pic"]