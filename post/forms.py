from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','post','category','img','draft']
		
	
	def __init__(self, *args, **kwargs):
		super(PostForm,self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['class']='form-control'
		self.fields['post'].widget.attrs['class']='form-control'
		self.fields['category'].widget.attrs['class']='form-control'
		self.fields['img'].widget.attrs['class']='form-control'
		

class PostFilterForm(forms.Form):
	elements = (('all','All'),('draft', 'Only Drafts'),('nodraft', 'Not Drafts'))
	list=forms.CharField(widget=forms.Select(choices=elements, attrs={'class':'form-control','style':'width:auto;'}))
	
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['text']
		error_messages = {
            'text': {
                'max_length': ("Bu şərh çox uzundur. Maksimim 1200 simvol"),
            },
        }
	'''
	def clean_text(self):
		text=self.cleaned_data['text']
		com_list=Comment.objects.filter(sender=user)
		com_list=Comment.objects.filter(text=text)
		if len(com_list) >0:
			raise forms.ValidationError('Spam!')
		return text'''
	def __init__(self,*args,**kwargs):
		super(CommentForm,self).__init__(*args, **kwargs)
		self.fields['text'].widget.attrs['class']='form-control'
	"""
	def clean_name(self):
		name=self.cleaned_data['name']
		if not name.isalpha():
			raise forms.ValidationError('Sadəcə hərf yazın')
		return name
		
		"""
	