from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404,Http404
from .models import Post,Category
from .forms import PostForm,PostFilterForm, CommentForm
from django.contrib import messages
from django.db.models import Q
import django
import jquery
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

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
	if not request.user.is_authenticated():
		raise Http404
	post_form=PostForm()
	if request.method == "POST":
		post_form=PostForm(request.POST, files=request.FILES or None)
		if post_form.is_valid:
			crepost=post_form.save(commit=False)
			crepost.author=request.user
			crepost.save()
			messages.success(request,'Post Yaradıldı')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':crepost.slug}))
	return render(request,'post/post_create.html',context={'form':post_form})

def post_update(request,slug):
	if not request.user.is_authenticated():
		raise Http404
	post=get_object_or_404(Post,slug=slug)
	form=PostForm(data=request.POST or None, instance=post, files=request.FILES or None)
	if request.method == 'POST':
		if form.is_valid:
			form.save(commit='True')
			messages.success(request,'Post redaktə olundu!')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':form.instance.slug}))
	return render(request, 'post/update.html', context={'form':form})
	
def post_delete(request,slug):
	if not request.user.is_authenticated():
		raise Http404
	post = get_object_or_404(Post,slug=slug)
	post.delete()
	messages.success(request,'Post silindi!',extra_tags='danger')
	return HttpResponseRedirect(reverse('post:index'))
	
def post_list(request):
	filter_form=PostFilterForm(request.GET or None)
	posts_list= Post.objects.order_by('-created_time')
	page = request.GET.get('page', 1)
	cat_name=''
	cat_id = request.GET.get('cat_id','')
	author_id = request.GET.get('author_id','')
	key= request.GET.get('key','')
	if cat_id is not "":
		posts_list= Post.objects.filter(Q(category=cat_id))
		cat_name=Category.objects.filter(id=cat_id)
	if key is not "":		
		posts_list=posts_list.filter(title__icontains=key)
	if author_id is not '':
		posts_list=posts_list.filter(author=author_id)
			
	if filter_form.is_valid():
		list=request.GET.get('list', 'all')
		#filter_form.cleaned_data['list']
		if list == 'draft':
			posts_list=posts_list.filter(draft=True)
		elif list == 'nodraft':
			posts_list=posts_list.filter(draft=False)
		else:
			pass
	paginator = Paginator(posts_list, 3)
	try:
		posts_list = paginator.page(page)
	except PageNotAnInteger:
		posts_list = paginator.page(1)
	except EmptyPage:
		posts_list = paginator.page(paginator.num_pages)
	return render(request,'post/post_list.html', context={'post_list':posts_list,'filter_form':filter_form,'cat_name':cat_name,'key':key})


def post_detail(request,slug):
	#post=Post.objects.get(pk=pk)  # Ən sadə üsul
	post=get_object_or_404(Post, slug=slug)
	comment_form=CommentForm(request.POST or None)
	if comment_form.is_valid():
		comment=comment_form.save(commit=False)
		comment.post=post
		comment.save()
		comment_form=CommentForm()
		return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':post.slug}))
	return render(request,'post/detail.html', context={'post':post,'form':comment_form})
	
def test(request):
	return render(request, 'base.html')
	
	
	
	
	
