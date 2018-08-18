from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Thing(models.Model):
	
	owner = models.ForeignKey(User,related_name='owner')
	title = models.CharField(max_length=120,verbose_name='Başlıq', blank=False)
	text=models.TextField(verbose_name='Şərh',max_length=1200, null=True, blank=True)
	completed = models.BooleanField(default=False)
	created_to = models.DateTimeField(auto_now_add=True)
	updated_to = models.DateTimeField(auto_now=True)
	updated = models.BooleanField(default=False)
	completed_at = models.DateTimeField(auto_now=True)
	'''def __init__(self, *args, **kwargs):
		super (thing, self).__init__(*args, **kwargs)'''

	class Meta:
		ordering=['-created_to']
	def is_completed(self):
		if self.completed == True:
			return "Tamamlanıb"
		