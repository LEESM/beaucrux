from django.conf.urls import url, include
from sample import views

urlpatterns = [
	url(r'^request/', views.sample_request, name='sample_request'),
	url(r'^list/', views.sample_list, name='sample_list'),
	url(r'^detail/(?P<sample_id>[0-9]+)/$', views.sample_detail, name='sample_detail'),
	url(r'^(?P<sample_id>[0-9]+)/$', views.sample_review, name='sample_review'),
	url(r'^review_update/(?P<sample_id>[0-9]+)/$', views.sample_review_update, name='sample_review_update'),
]
