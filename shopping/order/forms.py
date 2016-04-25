from django import forms
from datetime import datetime

class OrderInfoForm(forms.Form):
	order_id = forms.CharField()
	cart_id = forms.CharField()
	item_price = forms.IntegerField()
	delivery_price = forms.IntegerField()
	total_price = forms.IntegerField()
	pay_price = forms.IntegerField()
	point_price = forms.IntegerField()
	point_made = forms.IntegerField()
	name = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))
	address = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))
	phone = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))
	postscript = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))