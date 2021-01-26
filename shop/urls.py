from django.urls import path
from .views import * 
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('',HomePage, name = 'home-page'), # name ไว้สำหรับเอาไว้เรียกในหน้า ของ html
	
	url(r'^detail/(?P<id>[A-Za-z0-9_.@-]+)/$', views.DetailJewelry, name="account_task"),
]
