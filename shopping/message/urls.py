from django.conf.urls import url, include
from message import views

urlpatterns = [
	url(r'^sms_send_form/', views.sms_send_form, name='sms_send_form'),
]
