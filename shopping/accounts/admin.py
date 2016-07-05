from django.contrib import admin
from .models import Profile, Texts, PointHistory, Landing
from django_summernote.admin import SummernoteModelAdmin

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user','point','postcode','address','address_detail','phone','ads_agree','level',]

class TextsAdmin(SummernoteModelAdmin):
	list_display = ['name','contents']

class PointHistoryAdmin(SummernoteModelAdmin):
	list_display = ['user','kindof','record','amount','content','time']

class LandingAdmin(SummernoteModelAdmin):
	list_display = ['email']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Texts, TextsAdmin)
admin.site.register(PointHistory, PointHistoryAdmin)
admin.site.register(Landing, LandingAdmin)
