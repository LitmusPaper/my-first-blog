
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .models import UserProfile

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
		self.fields['email'].widget.attrs['required'] = 'required'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['class']='form-control'
	
	def clean_email(self):
		email=self.cleaned_data['email'].lower()
		username=self.cleaned_data['username'].lower()
		if email!='' and email!=username:
			mail_list=User.objects.filter(email=email)
			if len(mail_list)==0:
				return email
			else:
				raise forms.ValidationError('Bu email istifade olunub')
		else:
			raise forms.ValidationError('Email düzgün yazılmalıdır')

class LoginForm(forms.Form):
	username=forms.CharField(max_length=150, label='İstifadəçi adı/email',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	password=forms.CharField(required=True, label='Parol', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	
	def clean_username(self):
		username=self.cleaned_data['username']
		mail_list=User.objects.filter(email=username.lower())
		if len(mail_list) ==1:
			user=mail_list.first()
			return user.username
		elif len(mail_list)==0:
			return username
		else:
			return username


class ProfileForm(forms.ModelForm):
	tarix = forms.DateField(label='Doğum Tarixi',help_text='Belə yazın: 31-12-0000',input_formats=['%d-%m-%Y'],widget=forms.DateInput())
	class Meta:
		model=UserProfile
		type='test'
		fields=('bio','tel','tarix','sex','photo')
	
	
	def __init__(self, *args, **kwargs):
		super(ProfileForm,self).__init__(*args, **kwargs)
		#self.fields['tarix'].widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime":False})
		self.fields['bio'].widget.attrs['class']='form-control'
		self.fields['tel'].widget.attrs['class']='form-control'
		self.fields['tarix'].widget.attrs['class']='form-control'
		self.fields['sex'].widget.attrs['class']='form-control'
		self.fields['photo'].widget.attrs['class']='form-control'

class UserForm(forms.ModelForm):
	class Meta:
		model= User
		fields = ('username','first_name','last_name','email')
		
	def __init__(self, *args, **kwargs):
		super(UserForm,self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['first_name'].widget.attrs['class']='form-control'
		self.fields['last_name'].widget.attrs['class']='form-control'
		self.fields['email'].widget.attrs['class']='form-control'
		
class CustomPasswordForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(CustomPasswordForm,self).__init__(*args,**kwargs)
		self.fields['old_password'].widget.attrs['class']='form-control'
		self.fields['new_password1'].widget.attrs['class']='form-control'
		self.fields['new_password2'].widget.attrs['class']='form-control'