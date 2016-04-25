from django.db import models
from django.conf import settings
from item.models import Item, ItemOption

class Cart(models.Model):
	cart_id = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	item = models.ForeignKey(Item)
	item_option = models.ForeignKey(ItemOption)
	quantity = models.IntegerField(default=0)
	def __str__(self):
		return self.cart_id
	def item_plus_option_price(self):
		result = self.item.price + self.item_option.option_price
		return result
	def sub_total_price(self):
		result = (self.item.price + self.item_option.option_price)*self.quantity
		return result

class Order(models.Model):
	order_id = models.CharField(max_length=50)
	cart_id = models.CharField(max_length=50)
	item_price = models.IntegerField(default=0)
	delivery_price = models.IntegerField(default=0)
	total_price = models.IntegerField(default=0)
	pay_price = models.IntegerField(default=0)
	point_price = models.IntegerField(default=0)
	point_made = models.IntegerField(default=0)
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=300)
	phone = models.CharField(max_length=30)
	postscript = models.CharField(max_length=300)
	status = models.CharField(max_length=30)
	def __str__(self):
		return self.order_id
