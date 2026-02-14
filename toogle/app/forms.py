from django import forms
from .models import Toogle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ToogleForm(forms.ModelForm):

    class Meta:
        model = Toogle
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
