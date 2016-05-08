from django.db import models
from django.conf import settings

class Notice(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	pub_time = models.DateTimeField(auto_now_add=True)
	hits = models.IntegerField(default=0)
	parentId = models.ForeignKey("self", null=True, blank=True)
	secret = models.BooleanField(default=True)

class Event(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	pub_time = models.DateTimeField(auto_now_add=True)
	hits = models.IntegerField(default=0)
	parentId = models.ForeignKey("self", null=True, blank=True)
	secret = models.BooleanField(default=True)

class Sample(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	pub_time = models.DateTimeField(auto_now_add=True)
	hits = models.IntegerField(default=0)
	parentId = models.ForeignKey("self", null=True, blank=True)
	secret = models.BooleanField(default=True)
