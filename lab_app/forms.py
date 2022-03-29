from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django import forms

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', label_suffix='', max_length=150,widget=forms.TextInput(attrs={'title':'First Name', 'placeholder':'Enter First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name',label_suffix='', max_length=150,widget=forms.TextInput(attrs={'title':'Last Name', 'placeholder':'Enter Last Name','class':'form-control'}))
    mobile = forms.CharField(label='Mobile No',label_suffix='', max_length=150,widget=forms.NumberInput(attrs={'title':'Mobile Number', 'placeholder':'Enter Mobile Number','class':'form-control'}))
    email = forms.EmailField(label='Email Id',label_suffix='', max_length=150, widget=forms.EmailInput(attrs={'title':'Email Id', 'placeholder':'Enter Email Id','class':'form-control'}))
    password1 = forms.CharField(label='Password',label_suffix='', max_length=150,widget=forms.PasswordInput(attrs={'title':'Password', 'placeholder':'Enter Password','class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',label_suffix='', max_length=150,widget=forms.PasswordInput(attrs={'title':'Confirm Password', 'placeholder':'Confirm Password','class':'form-control'}))
    class Meta:
        model = User
        fields= ('first_name',
                 'last_name',
                 'mobile',
                 'email',
                 'password1',
                 'password2')

class MyAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email Id', max_length=150, label_suffix='',widget=forms.EmailInput(attrs={'title':'Email Id', 'placeholder':'Enter Email Id','class':'form-control'}))
    password = forms.CharField(label="Password", label_suffix='', widget=forms.PasswordInput(attrs={'title':'Password','placeholder':'Enter Password', 'class':'form-control'}),
    )