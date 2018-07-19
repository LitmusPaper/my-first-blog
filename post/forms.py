from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','post','category','img','draft']

class TestForm(forms.Form):
	mesaj=forms.CharField(label='Mesaj', max_length='20',widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	name=forms.CharField(label='Ad', max_length='20',widget=forms.TextInput(attrs={'class': 'form-control'}))
	mesaj_css_class='form-control'
		
	