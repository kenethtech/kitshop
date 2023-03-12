from django.urls import path, re_path
from . import views

urlpatterns =[
    re_path(r'^$', views.show_cart, {'template_name': 'cart/cart.html'}, name='show_cart'),
]