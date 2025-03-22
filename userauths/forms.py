from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ImageField, FileInput, DateInput

from .models import User , KYC


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class DateInput(forms.DateInput):
    input_type = 'date'


class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    signature = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = [ 'frist_name', 'last_name' , 'image', 'marrital_status', 'gender',  'date_of_birth', 'signature', 'company' , 'mobile']
        widgets = {
            "frist_name": forms.TextInput(attrs={"placeholder":"Frist Name"}),
            "last_name": forms.TextInput(attrs={"placeholder":"Last Name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"Mobile Number"}),
            "company": forms.TextInput(attrs={"placeholder":"Company"}),
            'date_of_birth':DateInput
        }