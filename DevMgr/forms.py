from django import forms
from django.contrib.auth.models import User
from DevMgr.models import UserOtherInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserOtherInfoForm(forms.ModelForm):
    class Meta():
        model = UserOtherInfo
        fields = ('name', 'zipcode', 'address', 'telephone', 'admin')
