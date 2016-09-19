from django.contrib import admin
from .models import Sample, SampleReview

class SampleAdmin(admin.ModelAdmin):
	list_display = ['id','name','get_samples', 'password','phone','postcode','address1','address2','request_date','status','have_review','delivery_number','get_coupon_name',]

class SampleReviewAdmin(admin.ModelAdmin):
	list_display = ['name','score','comment','review_date']


admin.site.register(Sample, SampleAdmin)
admin.site.register(SampleReview, SampleReviewAdmin)
