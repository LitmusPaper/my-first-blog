from django import forms
from .models import Thing


class FastCreateForm(forms.ModelForm):
	title = forms.CharField(max_length=120,label="Başlıq", widget=forms.TextInput(attrs={"class":"form-control"}))
	text = forms.CharField(max_length=1200, label="Haqqında", widget=forms.Textarea(attrs={"required":"False", "class":"form-control"}))

	class Meta:
		model = Thing
		fields = ['title','text']

	'''def __init__(self, *args, **kwargs):
		super(CreateThingForm, self).__init__(*args, **kwargs)
		self.fields['text'].widget.attrs['class']='form-control'
		'''