from django.contrib import admin
from .models import Sample

class SampleAdmin(admin.ModelAdmin):
	list_display = ['name','password','phone','postcode','address1','address2','request_date','status','delivery_number',]

admin.site.register(Sample, SampleAdmin)
