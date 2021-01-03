from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'category', 'image']

class RegisterUserForm(UserCreationForm):
    error_messages = {
        'Error.'
    }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']