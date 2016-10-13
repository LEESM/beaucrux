"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from item.views import index, landing
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^item/', include('item.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^sample/', include('sample.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )