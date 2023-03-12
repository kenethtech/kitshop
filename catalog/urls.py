from django.urls import path, re_path
from . import views


urlpatterns =[
   re_path(r'^$', views.index, {'template_name':'catalog/index.html'}, name='catalog_home'),
   re_path(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, {'template_name': 'catalog/category.html'}, name='catalog_category'),
   re_path(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, {'template_name': 'catalog/product.html'}, name='catalog_product'),
   re_path(r'^all_products/$', views.all_products, {'template_name': 'catalog/all_products.html'}, name='all_products'),


]