from django.conf.urls import url, include
from accounts import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup_ok/', TemplateView.as_view(template_name='accounts/signup_ok.html'), name='signup_ok'),
    url(r'^mypage/', views.mypage, name='mypage'),
]