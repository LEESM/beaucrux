from django.contrib import admin
from board.models import Notice, Event, Sample
from django_summernote.admin import SummernoteModelAdmin

class NoticeAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class EventAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class SampleAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sample, SampleAdmin)
