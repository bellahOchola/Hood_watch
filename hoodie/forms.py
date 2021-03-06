from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post,Business
from pyuploadcare.dj.forms import ImageField



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200,help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class UploadProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'location')

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email', 'description')

