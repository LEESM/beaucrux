from django import forms

class SampleForm(forms.Form):
	name = forms.CharField(label="성함", max_length=128, widget=forms.TextInput(attrs={'class':'form-control',}))
	password = forms.CharField(label="비밀번호", max_length=128, widget=forms.PasswordInput(attrs={'class':'form-control',}))
	phone = forms.CharField(label="연락처", max_length=128, widget=forms.TextInput(attrs={'class':'form-control',}))
	postcode = forms.CharField(label="우편번호", max_length=32, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'우편번호','style':'width:100px;display:inline-block;',}))
	address1 = forms.CharField(label="기본주소", max_length=128, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'기본주소'}))
	address2 = forms.CharField(label="상세주소", max_length=128, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'상세주소'}))