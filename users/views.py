from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404,Http404
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from post.models import Post,Category

# Create your views here.

def profile(request,pk):
	user=User.objects.get(pk=pk)
	posts_list=Post.objects.filter(author_id=pk)
	return render(request,'users/profile.html', context={'user':user,'post_list':posts_list})

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('post:index'))
	form=RegisterForm(request.POST or None)
	
	if form.is_valid():
		user=form.save(commit=False)
		username=form.cleaned_data['username']
		password=form.cleaned_data['password1']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		login(request,user)
		return HttpResponseRedirect(reverse('post:index'))
	return render(request,'users/register.html', context={'form':form})
	
def user_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('post:index'))
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse('post:index'))
		else:
			error='İstifadəçi adı və ya parol səhvdir'
			return render(request,'users/login.html', context={'form':form,'error':error})
	return render(request,'users/login.html', context={'form':form})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('post:index'))
	
	
	
	
	
	