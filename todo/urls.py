from django.conf.urls import url
from .views import index, complete

urlpatterns =[
	url(r'^$', index, name='index'),
	url(r'^complete/(?P<pk>[0-9]+)$', complete, name='complete')
]