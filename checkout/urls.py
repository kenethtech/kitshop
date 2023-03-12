from django.conf.urls import *
from django.urls import path, re_path
from kitshop import settings
from . import views

urlpatterns =[
    re_path(r'^$', views.show_checkout, {'template_name': 'checkout/checkout.html'}, name='checkout'),
    re_path(r'^receipt/$', views.receipt, {'template_name': 'checkout/receipt.html'}, name='checkout_receipt'),
    re_path(r'^mpesa_checkout/$', views.show_mpesa_checkout, {'template_name': 'checkout/mpesa_checkout.html'}, name='mpesa_checkout')
]