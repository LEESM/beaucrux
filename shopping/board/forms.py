from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from board.models import Notice, Event, Sample

class BoardWriteForm(forms.Form):
	title = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'제목',
		}))
	content = forms.CharField(widget=SummernoteWidget())