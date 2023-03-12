"""kitshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.views.static
from django.contrib import admin
from django.urls import path, include, re_path

admin.autodiscover()

urlpatterns = [
    path('',
         include('catalog.urls')),
    re_path(r'^cart/', include('cart.urls')),
    re_path(r'^checkout/', include('checkout.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'search/', include('search.urls')),
    path('admin/', admin.site.urls),
]
handler404 = 'views.file_not_found_404'
admin.site.site_header = "Kitshop Admin"
admin.site.site_title = "Kitshop admin site"
admin.site.index_title = "Kitshop Admin"
