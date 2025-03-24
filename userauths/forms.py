from django import forms
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.forms import ImageField, FileInput, DateInput


from .models import User 


class UserRegisterForm(UserCreationForm):
    frist_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Frist Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Phone"}))
    date_of_birth = forms.DateTimeField(widget=forms.DateInput(attrs={"type": "date", "placeholder": "Date of Birth"}))
    company = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Company"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['frist_name', 'last_name', 'username', 'email', 'phone', 'date_of_birth', 'company', 'password1', 'password2']



class DateInput(forms.DateInput):
    input_type = 'date'


# class KYCForm(forms.ModelForm):
#     image = ImageField(widget=FileInput)

#     class Meta:
#         model = KYC
#         fields = [ 'frist_name', 'last_name' , 'image', 'marrital_status', 'gender',  'date_of_birth', 'company' , 'mobile']
#         widgets = {
#             "frist_name": forms.TextInput(attrs={"placeholder":"Frist Name"}),
#             "last_name": forms.TextInput(attrs={"placeholder":"Last Name"}),
#             "mobile": forms.TextInput(attrs={"placeholder":"Mobile Number"}),
#             "company": forms.TextInput(attrs={"placeholder":"Company"}),
#             'date_of_birth':DateInput
#         }


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'