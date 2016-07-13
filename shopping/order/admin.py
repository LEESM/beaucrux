from django.contrib import admin
from .models import Cart, Order, Coupon

class CartAdmin(admin.ModelAdmin):
	list_display = ['cart_id','user','item','item_option','quantity']

class OrderAdmin(admin.ModelAdmin):
	list_display = [
		'order_date',
		'user',
		'item_price',
		'delivery_price',
		'total_price',
		'pay_price',
		'point_price',
		'point_made',
		'name',
		'email',
		'postcode',
		'address',
		'address_detail',
		'phone',
		'postscript',
		'status',
		'delivery_company',
		'delivery_tracking_number',
		'order_id',
		'cart_id',
		]
	list_filter = ('status',)

class CouponAdmin(admin.ModelAdmin):
	list_display = ['coupon_id','subject','subject','user','kind_of','quantity','used','pub_date']

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)