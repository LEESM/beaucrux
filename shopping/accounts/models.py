from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	point = models.IntegerField(default=0)
	city = models.CharField(max_length=30, default='')
	address = models.CharField(max_length=300, default='')
	phone = models.CharField(max_length=30, default='')
	ads_agree = models.BooleanField(default = False)

class Texts(models.Model):
	name = models.CharField(max_length=50)
	contents = models.TextField(blank = True)
