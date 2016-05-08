from django.conf.urls import url, include
from board import views

urlpatterns = [
	url(r'^view/', views.board_view, name='board_view'),
	url(r'^list/', views.board_list, name='board_list'),
	url(r'^write/', views.board_write, name='board_write'),
]