from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/', views.login_view),
	url(r'^logout/', views.logout_view),
	url(r'^$', views.login_redirect, name='login_redirect')
]