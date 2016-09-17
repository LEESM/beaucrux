from django.db import models
from order.models import Item

class Sample(models.Model):
	password = models.CharField(max_length=128)
	samples = models.ManyToManyField(Item,blank=True)
	name = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	postcode = models.CharField(max_length=32)
	address1 = models.CharField(max_length=128)
	address2 = models.CharField(max_length=128)
	request_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=128)
	delivery_number = models.CharField(max_length=128)

	def __str__(self):
		return self.name