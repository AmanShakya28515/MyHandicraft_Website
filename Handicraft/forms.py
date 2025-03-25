from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import ProductCategory,Product_Buddha,Utencils,Product_Tara,Product_Ganesh,Product_Sarsoti_Laxmi,Profile

class RegistrationForm(UserCreationForm):
    #usercreationform we have taken from user mdoel soo here class inherits the usercerationform hence helps to connect to the user model 
    email=forms.EmailField(required=True)
    username=forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['email','username','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UsereUpdateForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

class Buddha_Form(forms.ModelForm):
    class Meta:
        model = Product_Buddha
        fields = ['name','price','description','image']

class Tara_Form(forms.ModelForm):
    class Meta:
        model = Product_Tara
        fields = ['name','price','description','image']

class Ganesh_Form(forms.ModelForm):
    class Meta:
        model = Product_Ganesh
        fields = ['name','price','description','image']

class laxmi_Sarsoti_Form(forms.ModelForm):
    class Meta:
        model = Product_Sarsoti_Laxmi
        fields = ['name','price','description','image']

class Utensils_Form(forms.ModelForm):
    class Meta:
        model = Utencils
        fields = ['name','price','description','image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name','image','history']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile  # Ensure this matches your Profile model name
        fields = ['user','profile_picture']  # Adjust fields as per your model

