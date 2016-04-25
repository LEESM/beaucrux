from django.contrib import admin
from .models import Cart, Order

class CartAdmin(admin.ModelAdmin):
	list_display = ['cart_id','user','item','item_option','quantity']


class OrderAdmin(admin.ModelAdmin):
	list_display = ['order_id','cart_id','item_price','delivery_price','total_price','pay_price','point_price','name','city','address','phone','postscript','status']

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)