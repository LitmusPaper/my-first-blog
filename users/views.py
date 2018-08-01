from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404,Http404
from django.contrib import messages
from .forms import RegisterForm,LoginForm,ProfileForm,UserForm
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from post.models import Post,Category
from .models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.

def profile(request,pk):
	user_list=User.objects.all()
	user=user_list.get(pk=pk)
	posts_list=Post.objects.filter(author_id=pk)
	return render(request,'users/profile.html', context={'user':user,'post_list':posts_list,'user_list':user_list})

@login_required(login_url='/users/user_login/')
def update(request,pk):
	user=User.objects.get(pk=pk)
	if user != request.user:
		return HttpResponseRedirect(reverse('users:update', kwargs={'pk':request.user.pk}))
	profile=UserProfile.objects.filter(user_id=pk)
	user=User.objects.filter(pk=pk).first()
	profile_form=ProfileForm(data=request.POST or None, instance=profile)
	user_form=UserForm(data=request.POST or None, instance=user)
	if user_form.is_valid() and profile_form.is_valid():
		user_form.save(commit='True')
		profile_form.save(commit='True')
		
		messages.success(request,'Profil redaktə olundu!')
		return HttpResponseRedirect(reverse('users:profile', kwargs={'pk':pk}))
	return render(request,'users/update.html', context={'profile_form':profile_form,'user_form':user_form,'user':user})


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
	next=request.GET.get('next', '')
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('post:index'))
	form=LoginForm(request.POST or None)
	if form.is_valid():
		next=request.POST.get('next', '')
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			if next != '':
				return HttpResponseRedirect(next)
			return HttpResponseRedirect(reverse('post:index'))
		else:
			error='İstifadəçi adı/email və ya parol səhvdir'
			return render(request,'users/login.html', context={'form':form,'error':error})
	return render(request,'users/login.html', context={'form':form,'next':next})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('post:index'))
	
	
	
	
	
	
