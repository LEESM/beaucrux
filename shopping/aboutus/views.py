from django.shortcuts import render
from item.views import get_brands

def aboutus(request):
	return render(request,"aboutus/aboutus.html", 	{'brands':get_brands()})