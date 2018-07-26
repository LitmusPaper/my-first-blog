from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		#fields=['first_name','last_name','username','email','password1','password2']
	def __init__(self, *args, **kwargs):
		super(RegisterForm,self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class']='form-control'
		self.fields['last_name'].widget.attrs['class']='form-control'
		self.fields['email'].widget.attrs['class']='form-control'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['class']='form-control'

class LoginForm(forms.Form):
	username=forms.CharField(max_length=150, label='İstifadəçi adı',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(required=True, label='Parol', widget=forms.PasswordInput(attrs={'class':'form-control'}))