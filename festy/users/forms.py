from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # pname = forms.CharField()

    class Meta:
        fields = ['username','email', 'password1', 'password2']#,'pname']
        model = get_user_model()
    
    # def save(self, *args, **kwargs):
    #     # Let the UserCreationForm handle the user creation
    #     user = super().save(*args, **kwargs)
    #     # With the user create a Member
    #     Participant.objects.create(user=user)#, pname=self.cleaned_data.get("pname"))