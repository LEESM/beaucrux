from django.contrib import admin
from .models import Profile, Texts
from django_summernote.admin import SummernoteModelAdmin

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user','point','city','address','phone',]

class TextsAdmin(SummernoteModelAdmin):
	list_display = ['name','contents']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Texts, TextsAdmin)