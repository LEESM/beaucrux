from django.shortcuts import render, redirect
from accounts.forms import SignupForm, MypageForm
from accounts.models import Profile, Texts, PointHistory
from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.views import login as default_login_view
from django.contrib.auth.decorators import login_required

def login(request):
	return default_login_view(request, template_name="accounts/login.html")

def login_after(request):
	before_sixmonth = datetime.today() - timedelta(days=180)
	pointhistory = PointHistory.objects.filter(user=request.user, time__gte=before_sixmonth)
	total_amount = 0
	for item in pointhistory:
		total_amount += item.record
	new_profile=request.user.profile
	if total_amount>=300000:
		new_profile.level = 3
	elif total_amount>=50000:
		new_profile.level = 2
	else:
		new_profile.level = 1
	new_profile.save()
	return redirect("index")
'''return render(request,"accounts/login_after.html",{
		'pointhistory':pointhistory,
		'total_amount':total_amount,
		'before_sixmonth':before_sixmonth,
		})
'''

def logout(request):
	logout_user(request)
	return redirect("index")

@login_required
def mypage(request):
	message=None
	if request.method == "POST":
		mypageform=MypageForm(request.POST)
		if mypageform.is_valid():
			profile = Profile.objects.get(user=request.user)
			profile.phone = mypageform.cleaned_data['phone']
			profile.postcode=request.POST.get('postcode')
			profile.address=request.POST.get('address')
			profile.address_detail=request.POST.get('address_detail')
			check = request.POST.get('ads_agree')
			if check == None :
				profile.ads_agree=False
			else:
				profile.ads_agree=True
			profile.save()
			user=request.user
			user.first_name = mypageform.cleaned_data['first_name']
			user.save()
			message = '정보가 업데이트 되었습니다.'
		else:
			message = mypageform.errors
	user=User.objects.get(id=request.user.id)
	#프로필 있는지 확인 없으면생성
	try:
		profile=Profile.objects.get(user=request.user)
	except:
		new_profile=Profile(user=request.user)
		new_profile.save()
	mypageform = MypageForm({'first_name':request.user.first_name, 'phone':user.profile.phone})
	context={'message':message,'mypageform':mypageform, 'user':user}
	return render(request,"accounts/mypage.html", context)

def signup(request):
	regist_terms=Texts.objects.get(name="regist_terms")
	privacy_info_terms=Texts.objects.get(name="privacy_info_terms")
	if request.method=="POST":
		userform = SignupForm(request.POST)
		if userform.is_valid():
			user = userform.save(commit=False)
			user.username = userform.cleaned_data['username']
			user.email = userform.cleaned_data['email']
			user.save()
			profile = Profile(user=user)
			profile.ads_agree = request.POST.get('ads_agree')
			if profile.ads_agree==None:
				profile.ads_agree=False
			else:
				profile.ads_agree=True
			profile.save()
			return HttpResponseRedirect(reverse("signup_ok"))	
		return render(request, "accounts/signup.html", {
			'userform': userform,
			'message':'입력정보를 정확히 확인해주세요.',
			'regist_terms':regist_terms.contents,
			'privacy_info_terms':privacy_info_terms.contents,
		})
	elif request.method=="GET":
		userform = SignupForm()
		return render(request, "accounts/signup.html", {
			'userform':userform,
			'message':'첫 화면',
			'regist_terms':regist_terms.contents,
			'privacy_info_terms':privacy_info_terms.contents,
		})