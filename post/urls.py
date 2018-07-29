from django.conf.urls import url
from .views import post_list, post_create, post_update, post_delete, post_detail, form_test, test, comment_delete

urlpatterns =[
	url(r'^$', post_list, name='index'),
	url(r'^create/$', post_create, name='create'),
	url(r'^update/(?P<slug>[\w\-]+)/$', post_update, name='update'),
	url(r'^delete/(?P<slug>[\w\-]+)$', post_delete, name='delete'),
	url(r'^comment/delete/(?P<pk>[0-9]+)$', comment_delete, name='comment_delete'),
	url(r'^detail/(?P<slug>[\w\-]+)/$', post_detail,name='detail'),
	url(r'^form/$', form_test),
	url(r'^test/$', test)

]