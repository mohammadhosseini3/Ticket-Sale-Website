from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import profileModel

class ProfileRegisterationForm(forms.ModelForm):
    # django user elements
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    # profile elements
    class Meta:
        model = profileModel
        fields = ['credit',"profile_img","gender"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields = ['profile_img','credit','gender']

# changing djnago user
class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name','last_name','email']
    