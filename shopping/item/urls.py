from django.conf.urls import url, include
from item import views

urlpatterns = [
	url(r'^detail/', views.detail, name='detail'),
	url(r'^qna_update/', views.qna_update, name='qna_update'),
	url(r'^review_write/', views.review_write, name='review_write'),
	url(r'^review_update/', views.review_update, name='review_update'),
]