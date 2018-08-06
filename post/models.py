from django.db import models
from django import forms
from django.utils.text import slugify
import random
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
#from .models import User


def upload_to(instance, filename):
	return '%s/%s/%s'%('post',instance.slug,filename)


class Category(models.Model):
	name=models.CharField(max_length=50,verbose_name='Kateqoriya')
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name='Kateqoriya'
		verbose_name_plural='Kateqoriyalar'

class Post(models.Model):
	author=models.ForeignKey(User, verbose_name='Müəllif',related_name='author')
	title=models.CharField(max_length=120, blank=False,verbose_name='Başlıq')
	slug=models.SlugField(max_length=120,default='', unique=True, null=False,verbose_name='Slug title', editable=False)
	post=RichTextField(verbose_name='Məqalə')
	img= models.ImageField(blank=True, verbose_name='Post img',upload_to=upload_to)
	draft=models.BooleanField(default=False)
	category=models.ManyToManyField(Category,verbose_name='Kateqoriya')
	created_time=models.DateTimeField(auto_now_add=True)
	updated_time=models.DateTimeField(auto_now=True)
	
	def __str__ (self):
		return self.title
	
	def get_slug(self):
		return self.slug
	
	def unique_slug(self, new_slug, orginal_slug, index):
		if Post.objects.filter(slug=new_slug):
			new_slug='%s-%s' %(orginal_slug,index)
			index +=1
			return self.unique_slug(new_slug=new_slug, orginal_slug=orginal_slug, index=index)
		return new_slug
		
	def save(self,*args, **kwargs):
		if self.slug=='':
			index=1
			new_slug=slugify(self.title)
			self.slug=self.unique_slug(new_slug=new_slug, orginal_slug=new_slug, index=index)
		super(Post,self).save(*args,**kwargs)
		
	
	def get_img_or_default(self):
		if self.img and hasattr(self.img,'url'):
			return self.img.url
		return '/staticfiles/img/default.png'
	
	class Meta:
		verbose_name='Postlar'
		verbose_name_plural='Postlar'
		ordering=['-created_time']
		
		
class Comment(models.Model):
	post=models.ForeignKey(Post, verbose_name='comment',related_name='comment')
	sender=models.ForeignKey(User, verbose_name='sender',related_name='sender')
	text=models.TextField(verbose_name='Şərh',max_length=1200)
	date=models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name='Şərh'
		verbose_name_plural='Şərhlər'
		ordering=['-date']
	'''def save(self,*args, **kwargs):
		text=self.text
		com_list=Comment.objects.filter(sender=self.sender)
		com_list=com_list.filter(text=text)
		if len(com_list) ==0:
			super(Comment,self).save(*args,**kwargs)'''
		
		
	def __str__(self):
		return '%s - %s'%(self.post,self.sender)

class Reply(models.Model):
	comment=models.ForeignKey(Comment,verbose_name='reply', related_name='reply')
	rsender=models.ForeignKey(User,verbose_name='sender',related_name='rsender')
	rtext=models.TextField(verbose_name='Cavab', max_length=1200)
	date=models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name='Cavab'
		verbose_name_plural='Cavablar'
		ordering=['-date']
	def __str__(self):
		return '%s - %s'%(self.rsender, self.comment)
