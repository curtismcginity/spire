"""spire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appspire import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.index, name='landing'),
    url(r'^home',v.index, name='home'),
    url(r'^about',v.about, name='about'),
    url(r'^contact',v.contact, name='contact'),
    url(r'^dr',v.about, name='dr'),
    url(r'^testgallery',v.testgallery, name='gallery2'),
    url(r'^gallery',v.gallery, name='gallery'),
]

urlpatterns += staticfiles_urlpatterns()
