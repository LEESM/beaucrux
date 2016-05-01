from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	point = models.IntegerField(default=0)
	postcode = models.CharField(max_length=10, default='', null=True, blank=True)
	address = models.CharField(max_length=300, default='', null=True, blank=True)
	address_detail = models.CharField(max_length=300, default='', null=True, blank=True)
	phone = models.CharField(max_length=30, default='', null=True, blank=True)
	ads_agree = models.BooleanField(default = False)

class Texts(models.Model):
	name = models.CharField(max_length=50)
	contents = models.TextField(blank = True)
