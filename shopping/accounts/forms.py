from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	username = forms.RegexField(label="Username", max_length=30,
	regex=r'^[\w.@+-]+$',
	help_text="Required! 30 characters or fewer. Letters, digits and "
	"@/./+/-/_ only.",
	error_messages={
		'invalid': "아이디는 영어, 숫자, @ . + - _ 만 사용하실 수 있습니다.",
	},
	widget=forms.TextInput(attrs={
	'class': 'form-control',
	'required': 'true',
	}))
	password1 = forms.CharField(label="Password",
	widget=forms.PasswordInput(attrs={
	'class': 'form-control',
	'required': 'true',
	}))
	password2 = forms.CharField(label="Password confirmation",
	widget=forms.PasswordInput(attrs={
	'class': 'form-control',
	'required': 'true',
	}),
	error_messages={
		'password_mismatch': "비밀번호가 일치하지 않습니다.",
	},
	)
	email = forms.EmailField(
	widget=forms.EmailInput(attrs={
	'class': 'form-control',
	'required': 'true',
	}))

	class Meta:
		model = User
		fields = ("username", "password1", "password2",)

class LoginForm(AuthenticationForm):
	username = forms.CharField(
		max_length=254,
		widget=forms.TextInput(
		attrs={
		'class': 'form-control',
		'placeholder': 'Username',
		'required': 'True',
	}))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		'class': 'form-control',
		'placeholder': 'Password',
		'required': 'True',
	}))

class MypageForm(forms.Form):
	first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))
	phone = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
	}))