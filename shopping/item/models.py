from django.db import models
from ingredient.models import Ingredient
from django.conf import settings
import os
from django.template.defaultfilters import truncatechars  # or truncatewords

class Category(models.Model):
	category_id = models.CharField(unique=True, max_length=30)
	category_name = models.CharField(max_length=100)
	def __str__(self):
		return self.category_name

class Brand(models.Model):
	brand_id = models.CharField(unique=True, max_length=30)
	brand_name = models.CharField(max_length=100)
	brand_desc = models.TextField()
	brand_active = models.BooleanField(default=True)
	brand_order = models.IntegerField(default=0)
	def __str__(self):
		return self.brand_name

def get_image_path(instance, filename):
	return os.path.join('item_images', str(instance.item_id), filename)

class Item(models.Model):
	item_id = models.CharField(unique=True, max_length=30)
	item_name = models.CharField(max_length=100)
	item_desc = models.CharField(max_length=100,blank=True)
	price = models.IntegerField(default=0)
	custom_price = models.IntegerField(default=0)
	categories = models.ManyToManyField(Category,blank=True)
	brand = models.ForeignKey(Brand,blank=True, null=True,on_delete=models.SET_NULL)
	item_active = models.BooleanField(default=True)
	main1 = models.BooleanField(default=False)
	main2 = models.BooleanField(default=False)
	main3 = models.BooleanField(default=False)
	is_sample = models.BooleanField(default=False)
	order_number = models.IntegerField(default = 0)
	image0 = models.ImageField(blank=True, upload_to=get_image_path)
	image1 = models.ImageField(blank=True, upload_to=get_image_path)
	image2 = models.ImageField(blank=True, upload_to=get_image_path)
	image3 = models.ImageField(blank=True, upload_to=get_image_path)
	image4 = models.ImageField(blank=True, upload_to=get_image_path)
	image5 = models.ImageField(blank=True, upload_to=get_image_path)
	image6 = models.ImageField(blank=True, upload_to=get_image_path)
	image7 = models.ImageField(blank=True, upload_to=get_image_path)
	image8 = models.ImageField(blank=True, upload_to=get_image_path)
	image9 = models.ImageField(blank=True, upload_to=get_image_path)
	delivery = models.TextField(blank=True)
	detail = models.TextField(blank=True)
	ingredients = models.ManyToManyField(Ingredient,blank=True, through='ItemIngredientCombination')
	def __str__(self):
		return self.item_name

	def get_categories(self):
		return "\n".join([cat.category_name for cat in self.categories.all()])

	def get_options(self):
		options=ItemOption.objects.filter(original_item=self)
		return options

	def get_options_name(self):
		options=ItemOption.objects.filter(original_item=self)
		return "\n".join([option.option_name for option in options ])

	@property
	def short_detail(self):
		return truncatechars(self.detail, 30)

	@property
	def short_delivery(self):
		return truncatechars(self.delivery, 30)


class ItemIngredientCombination(models.Model):
	ingredient = models.ForeignKey(Ingredient, blank=True,null=True,on_delete=models.SET_NULL)
	item = models.ForeignKey(Item, blank=True,null=True,on_delete=models.SET_NULL)
	order = models.IntegerField(default=0)

class ItemOption(models.Model):
	option_id = models.CharField(unique=True, max_length=30)
	original_item = models.ForeignKey(Item, blank=True, null=True)
	option_name = models.CharField(max_length=100)
	option_price = models.IntegerField(default=0)
	option_custom_price = models.IntegerField(default=0)
	option_stock = models.IntegerField(default=0)
	def __str__(self):
		return self.option_name

class ItemQna(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	item = models.ForeignKey(Item)
	secret = models.BooleanField(default=True)
	question = models.TextField(blank=True)
	answer = models.TextField(blank=True, default="<p>답변 전 입니다.</p>")
	qna_time = models.DateTimeField(auto_now_add=True)

class ItemReview(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	item = models.ForeignKey(Item)
	score = models.IntegerField(default=10)
	comment = models.TextField(blank=True)
	review_time = models.DateTimeField(auto_now_add=True)