from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404
from .models import Post,Category
from .forms import PostForm,TestForm
from django.contrib import messages
from django.db.models import Q
import django
import jquery

def form_test(request):
	form= TestForm()
	mesaj=None
	if request.method=='POST':
		form=TestForm(request.POST)
		if form.is_valid:
			mesaj=form.data
	return render(request, 'post/form_test.html', context={'form': form,'mesaj':mesaj})
	

def index(request):
	ver= django.get_version()
	return HttpResponse(ver)

def post_create(request):
	post_form=PostForm()
	if request.method == "POST":
		post_form=PostForm(request.POST, files=request.FILES or None)
		if post_form.is_valid:
			crepost=post_form.save(commit=True)
			messages.success(request,'Post Yaradıldı')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':crepost.slug}))
	return render(request,'post/post_create.html',context={'form':post_form})

def post_update(request,slug):
	post=get_object_or_404(Post,slug=slug)
	form=PostForm(data=request.POST or None, instance=post, files=request.FILES or None)
	if request.method == 'POST':
		if form.is_valid:
			form.save(commit='True')
			messages.success(request,'Post redaktə olundu!')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':form.instance.slug}))
	return render(request, 'post/update.html', context={'form':form})
	
def post_delete(request,slug):
	post = get_object_or_404(Post,slug=slug)
	post.delete()
	messages.success(request,'Post silindi!',extra_tags='danger')
	return HttpResponseRedirect(reverse('post:index'))
	
def post_list(request):
	posts_list= Post.objects.order_by('-created_time')
	posts_list_len= len(posts_list)
	return render(request,'post/post_list.html', context={'post_list':posts_list,'post_list_len':posts_list_len})

def post_filter(request):
	if request.POST:
		if 'catfilter' in request.POST.keys():
			filter_value = request.POST['catfilter']
			posts_list= Post.objects.filter(Q(category=filter_value))
			posts_list_len= len(posts_list)
			cat_name=Category.objects.filter(id=filter_value)
			return render(request,'post/post_list.html', context={'post_list':posts_list,'post_list_len':posts_list_len ,'cat_name':cat_name})
		elif 'key' in request.POST.keys():
			filter_value= request.POST['key']
			posts_list=Post.objects.filter(title__contains=filter_value)
			posts_list_len= len(posts_list)
			return render(request,'post/post_list.html', context={'post_list':posts_list,'post_list_len':posts_list_len})
		else:
			pass
	return HttpResponseRedirect(reverse('post:index'))

def post_detail(request,slug):
	#post=Post.objects.get(pk=pk)  # Ən sadə üsul
	post=get_object_or_404(Post, slug=slug)
	return render(request,'post/detail.html', context={'post':post})
	
def test(request):
	return render(request, 'base.html')
	
	
	
	
	
