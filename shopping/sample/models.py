from django.db import models
from order.models import Item, Coupon

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
	have_review = models.BooleanField(default=False)
	coupon = models.ForeignKey(Coupon, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_samples(self):
		return "\n".join([sample.item_name for sample in self.samples.all()])

	def get_coupon_name(self):
		try:
			return self.coupon.coupon_id
		except:
			return '없음'			

class SampleReview(models.Model):
	name = models.CharField(max_length=128)
	item = models.ForeignKey(Item)
	score = models.IntegerField()
	comment = models.TextField()
	review_date = models.DateTimeField(auto_now_add=True)