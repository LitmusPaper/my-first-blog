from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404,Http404
from .models import Post,Category, Comment, Reply, Like
from .forms import PostForm,PostFilterForm, CommentForm, ReplyForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import django
import jquery
from time import sleep
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse

def form_test(request):
	form= TestForm()
	mesaj=None
	if request.method=='POST':
		form=TestForm(request.POST)
		if form.is_valid:
			mesaj=form.data
	return render(request, 'post/form_test.html', context={'form': form,'mesaj':mesaj})
	

def index(request):
	return HttpResponseRedirect(reverse('post:index'))

@login_required(login_url='/users/user_login/')
def post_create(request):
	
	post_form=PostForm()
	if request.method == "POST":
		post_form=PostForm(request.POST, files=request.FILES or None)
		if post_form.is_valid():
			crepost=post_form.save(commit=False)
			crepost.author=request.user
			crepost.save()
			#post_form=PostForm()
			messages.success(request,'Post Yaradıldı',extra_tags='addpost')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':crepost.slug}))
		else:
			HttpResponseRedirect(reverse('post:index'))
	return render(request,'post/post_create.html',context={'form':post_form})

@login_required(login_url='/users/user_login/')
def post_update(request,slug):
	post=get_object_or_404(Post,slug=slug)
	if post.author!=request.user:
		return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':slug}))
	form=PostForm(data=request.POST or None, instance=post, files=request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save(commit='True')
			messages.success(request,'Post redaktə olundu!', extra_tags='postupdate')
			return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':form.instance.slug}))
	return render(request, 'post/update.html', context={'form':form})

@login_required(login_url='/users/user_login/')
def post_delete(request,slug):
	post = get_object_or_404(Post,slug=slug)
	if post.author!=request.user:
		return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':slug}))
	post.delete()
	messages.success(request,'Post silindi!',extra_tags='postdelete')
	return HttpResponseRedirect(reverse('post:index'))

@login_required(login_url='/users/user_login/')
def comment_delete(request,pk):
	comment = get_object_or_404(Comment,pk=pk)
	if request.user != comment.sender:
		return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':comment.post.slug}))
	comment.delete()
	messages.success(request,'Şərh silindi!',extra_tags='commentdelete')
	#return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':comment.post.slug}))
	return JsonResponse(data={'success':'true'})
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
	paginator = Paginator(posts_list, 4)
	try:
		posts_list = paginator.page(page)
	except PageNotAnInteger:
		posts_list = paginator.page(1)
	except EmptyPage:
		posts_list = paginator.page(paginator.num_pages)
	return render(request,'post/post_list.html', context={'post_list':posts_list,'filter_form':filter_form,'cat_name':cat_name,'key':key})

#@login_required(login_url='/users/user_login/')
def post_detail(request,slug):
	#post=Post.objects.get(pk=pk)  # Ən sadə üsul
	post=get_object_or_404(Post, slug=slug)
	post.read += 1
	post.save()
	comment_form=CommentForm()
	reply_form=ReplyForm()
	like=Like.objects.filter(sender=request.user,post=post).exists()
	if request.method == "POST":
		comment_form=CommentForm(request.POST)
		if comment_form.is_valid():
			comment=comment_form.save(commit=False)
			comment.post=post
			comment.sender=request.user
			comment.save()
			comment_form=CommentForm()
			#return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':post.slug}))
			return HttpResponseRedirect('#comment')
		else:
			return HttpResponseRedirect('#comment')
	return render(request,'post/detail.html', context={'post':post,'form':comment_form,'reply_form':reply_form,'like':like})

@login_required(login_url='/users/user_login/')
def reply_view(request,pk):
	comment=get_object_or_404(Comment, pk=pk)
	reply_form=ReplyForm(request.POST)
	if reply_form.is_valid():
		reply=reply_form.save(commit=False)
		reply.comment=comment
		reply.rsender=request.user
		reply.save()
		reply_form=ReplyForm()
		#return HttpResponseRedirect(reverse('post:detail', kwargs={'slug':comment.post.slug}))
		#return HttpResponseRedirect('/post/detail/'+comment.post.slug+'#comment')
		return JsonResponse(data={'success':'submit','pk':pk,'sender':reply.rsender.username,'text':reply.rtext,'date':reply.date})
	else:
		return HttpResponse('444')

@login_required(login_url='/users/user_login/')
def like(request,pk):
	post=get_object_or_404(Post, pk=pk)
	user=request.user
	like, created = Like.objects.get_or_create(sender=user, post=post)
	
	data={'success':None}
	if created:
		data['success']='like'
	else:
		like.delete()
		data['success']='unlike'
	dat = list(Like.objects.filter(post=post).values('sender'))
	userlist=[]
	for element in dat:
		pk=element['sender']
		username = User.objects.get(pk=pk).username
		userlist.append(username)
	data['names']=userlist
	return JsonResponse(data=data)
		
		
def test(request):
	return render(request, 'base.html')


	
	
	
