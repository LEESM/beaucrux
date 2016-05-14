from django.db import models
from django.conf import settings
from item.models import Item, ItemOption

class Cart(models.Model):
	cart_id = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,on_delete=models.SET_NULL)
	item = models.ForeignKey(Item,null=True, blank=True,on_delete=models.SET_NULL)
	item_option = models.ForeignKey(ItemOption,null=True, blank=True,on_delete=models.SET_NULL)
	quantity = models.IntegerField(default=0)
	order_flag = models.BooleanField(default=False)
	cart_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.cart_id
	def item_plus_option_price(self):
		result = self.item.price + self.item_option.option_price
		return result
	def sub_total_price(self):
		result = (self.item.price + self.item_option.option_price)*self.quantity
		return result

class Order(models.Model):
	order_id = models.CharField(max_length=50, unique=True)
	cart_id = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,on_delete=models.SET_NULL)
	item_price = models.IntegerField(default=0)
	delivery_price = models.IntegerField(default=0)
	total_price = models.IntegerField(default=0)
	pay_price = models.IntegerField(default=0)
	point_price = models.IntegerField(default=0)
	point_made = models.IntegerField(default=0)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	postcode = models.CharField(max_length=10, default='', null=True, blank=True)
	address = models.CharField(max_length=300, default='', null=True, blank=True)
	address_detail = models.CharField(max_length=300, default='', null=True, blank=True)
	phone = models.CharField(max_length=30)
	postscript = models.CharField(max_length=300)
	status = models.CharField(max_length=30)
	delivery_company = models.CharField(max_length=50, null=True, blank=True)
	delivery_tracking_number = models.CharField(max_length=50, null=True, blank=True)
	order_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.order_id
