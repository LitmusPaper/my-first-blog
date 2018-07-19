from django.db import models
from django import forms
from django.utils.text import slugify
import random

class Category(models.Model):
	name=models.CharField(max_length=50,verbose_name='Kateqoriya')
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name='Kateqoriya'
		verbose_name_plural='Kateqoriyalar'

class Post(models.Model):
	title=models.CharField(max_length=120, blank=False,verbose_name='Başlıq')
	slug=models.SlugField(max_length=120,default='', unique=True, null=False,verbose_name='Slug title', editable=False)
	post=models.TextField(verbose_name='Məqalə')
	img= models.ImageField(blank=True, verbose_name='Post img')
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
		return '/static/img/default.png'
	
	class Meta:
		verbose_name='Postlar'
		verbose_name_plural='Postlar'

