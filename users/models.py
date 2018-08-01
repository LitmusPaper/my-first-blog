from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# Create your models here.
def upload_to(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return '%s/%s/avatar%s'%('users',instance.user.username,file_extension)

class UserProfile(models.Model):
	MALE='1'
	FEMALE='2'
	SEX=((MALE,'Kişi'),(FEMALE,'Qadın'))
	user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
	bio=models.TextField(max_length=200,verbose_name='Haqqında', blank=True, null=True)
	tel=models.CharField(max_length=14, verbose_name='Telefon Nömrəsi', blank=True, null=True)
	tarix=models.DateField(verbose_name='Doğum Tarixi', blank=True, null=True)
	sex=models.CharField(verbose_name='Cins', max_length=1, choices=SEX, blank=True, null=True)
	photo=models.ImageField(verbose_name='Avatar',blank=True, upload_to=upload_to, default='pp_default.jpg', null=True)
	
	class Meta:
		verbose_name='Profil'
		verbose_name_plural='Profillər'
	
	def __str__(self):
		return '%s - %s'%(self.user.username,'Profil')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

