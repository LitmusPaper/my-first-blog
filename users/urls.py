from django.conf.urls import url

from .views import register,user_login, user_logout,profile,update
 
urlpatterns =[
	url(r'^register/$', register, name='register'),
	url(r'^user_login/$', user_login, name='user_login'),
	url(r'^user_logout/$', user_logout, name='user_logout'),
	url(r'^profile/(?P<pk>[0-9]+)/$', profile, name='profile'),
	url(r'^update/(?P<pk>[0-9]+)/$', update, name='update'),

	
	
	
	]