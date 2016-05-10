from django.db import models

class Ingredient(models.Model):
	kcia_no = models.IntegerField(unique=True)
	ko_name = models.CharField(max_length=2000, null=True, blank=True)
	en_name = models.CharField(max_length=2000, null=True, blank=True)
	purpose = models.TextField(null=True, blank=True)
	ewg_high_grade = models.IntegerField(default=-1)
	ewg_low_grade = models.IntegerField(default=-1)
	caution20 = models.IntegerField(default=0)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ko_name