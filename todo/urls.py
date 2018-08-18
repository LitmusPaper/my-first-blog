from django.conf.urls import url
from .views import index, complete, delete

urlpatterns =[
	url(r'^$', index, name='index'),
	url(r'^complete/(?P<pk>[0-9]+)$', complete, name='complete'),
	url(r'^delete/(?P<pk>[0-9]+)$', delete, name='delete'),
]