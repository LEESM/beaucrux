from django.contrib import admin
from board.models import Notice, Event, Sample, After28, Labs
from django_summernote.admin import SummernoteModelAdmin

class NoticeAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class EventAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class SampleAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class After28Admin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

class LabsAdmin(SummernoteModelAdmin):
	list_display = ['user','title','content','pub_time','hits','parentId','secret']

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(After28, After28Admin)
admin.site.register(Labs, LabsAdmin)
