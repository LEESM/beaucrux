from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from item.models import ItemReview

class ItemReviewForm(ModelForm):
	class Meta:
		model = ItemReview
		fields = ['comment',]
		widgets = {
			'comment':SummernoteWidget(),
		}