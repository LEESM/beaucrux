from django.conf.urls import url, include
from aboutus import views

urlpatterns = [
    url(r'^$', views.aboutus, name='aboutus'),
]