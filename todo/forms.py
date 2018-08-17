from django import forms
from .models import Thing
from ckeditor.fields import RichTextField

class FastCreateForm(forms.ModelForm):
	title = forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class":"form-control"}))
	#text = RichTextField(max_length=500)

	class Meta:
		model = Thing
		fields = ['title']

	'''def __init__(self, *args, **kwargs):
		super(CreateThingForm, self).__init__(*args, **kwargs)
		self.fields['text'].widget.attrs['class']='form-control'
		'''