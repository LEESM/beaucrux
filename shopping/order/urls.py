from django.conf.urls import url, include
from order import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    url(r'^cart_update/', views.cart_update, name='cart_update'),
    url(r'^order_info/', views.order_info, name='order_info'),
    url(r'^order_update/', views.order_update, name='order_update'),
    url(r'^view_orders/', views.view_orders, name='view_orders'),
    url(r'^view_order_detail/', views.view_order_detail, name='view_order_detail'),
    url(r'^pop_item/', views.pop_item),
    url(r'^cart_number_update/', views.cart_number_update, name='cart_number_update'),    
]