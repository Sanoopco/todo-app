from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email",'password1','password2']
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control mt-2"}),
            "last_name":forms.TextInput(attrs={"class":"form-control mt-2"}),
            "username":forms.TextInput(attrs={"class":"form-control mt-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control mt-2"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class TaskForm(forms.Form):
    taskname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-2"}))

class ChangePassswordForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-2"}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-2"}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-2"}))
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        