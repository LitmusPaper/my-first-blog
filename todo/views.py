from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, get_object_or_404, Http404
from .forms import FastCreateForm
from .models import Thing
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse

@login_required(login_url='/users/user_login/')
def index(request):
	object_list = Thing.objects.filter(owner=request.user)
	page = request.GET.get('page', 1)
	form = FastCreateForm()
	com = request.GET.get('list', 'uncompleted')
	if com == 'uncompleted':
		object_list = object_list.filter(completed=False)
	elif com == 'completed':
		object_list = object_list.filter(completed=True)
	paginator = Paginator(object_list, 10)
	try:
		object_list = paginator.page(page)
	except PageNotAnInteger:
		object_list = paginator.page(1)
	except EmptyPage:
		object_list = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = FastCreateForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.owner = request.user
			data.save()
			form = FastCreateForm()
			json = {'success':'true', 'pk':data.pk, 'title':data.title,"created":data.created_to,"completed":data.completed}
			return JsonResponse(data=json)
	return render(request,'todo/index.html', context={'object_list':object_list,'form':form})

@login_required(login_url='/users/user_login/')
def complete(request, pk):
	thing = get_object_or_404(Thing, pk=pk)
	if thing.owner != request.user:
		return HttpResponse('400')
	if thing.completed == True:
		data={'success':False}
	else:
		thing.completed = True
		thing.save()
		data={'success':True}
	return JsonResponse(data=data)