from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.
class Thing(models.Model):
	
	owner = models.ForeignKey(User,related_name='owner')
	title = models.CharField(max_length=120,verbose_name='Başlıq',blank=False)
	text = RichTextField(max_length=500,verbose_name='text',blank=True)
	completed = models.BooleanField(default=False)
	created_to = models.DateTimeField(auto_now_add=True)
	updated_to = models.DateTimeField(auto_now=True)
	'''def __init__(self, *args, **kwargs):
		super (thing, self).__init__(*args, **kwargs)'''

	class Meta:
		ordering=['-created_to']
	def is_completed(self):
		if self.completed == True:
			return "Tamamlanıb"
		