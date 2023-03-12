import django.contrib.auth.views
from django.urls import re_path
from kitshop import settings
from accounts import views
from django.contrib.auth import views as auth

urlpatterns =[
    re_path(r'^register/$', views.register, {'template_name': 'registration/register.html'}, name='register'),
    re_path(r'^my_account/$', views.my_account, {'template_name': 'registration/my_account.html'}, name='my_account'),
    re_path(r'^order_details/(?P<order_id>[-\w]+)/$', views.order_details, {'template_name': 'registration/order_details.html'}, name='order_details'),
    re_path(r'^order_info//$', views.order_info, {'template_name': 'registration/order_info.html'}, name='order_info'),
]

urlpatterns +=[
    re_path(r'^login/$', auth.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    re_path(r'^logout/$', auth.LogoutView.as_view(), {'template_name': 'registration/logged_out.html'}, name='logout'),
    re_path(r'^change_password/$', auth.PasswordChangeView.as_view(), {'template_name': 'registration/login.html'}, name='change_password'),
]