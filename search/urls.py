from django.urls import path, re_path
from . import views

urlpatterns =[
    re_path(r'^results/$', views.results, {'template_name': 'search/results.html'}, name='search_results'),
]