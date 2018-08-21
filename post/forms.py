from django import forms
from .models import Post, Comment, Reply



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
	
	def __init__(self,*args,**kwargs):
		super(CommentForm,self).__init__(*args, **kwargs)
		self.fields['text'].widget.attrs['class']='form-control'

class ReplyForm(forms.ModelForm):
	class Meta:
		model=Reply
		fields=['rtext']
		error_messages = {
            'rtext': {
                'max_length': ("Bu cavab çox uzundur. Maksimim 1200 simvol"),
            },
        }
	
	def __init__(self,*args,**kwargs):
		super(ReplyForm,self).__init__(*args, **kwargs)
		self.fields['rtext'].widget.attrs['class']='form-control'
		self.fields['rtext'].widget.attrs['rows']='5'
		#self.fields['rtext'].widget.attrs['column']='1'		