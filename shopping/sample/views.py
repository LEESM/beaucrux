from django.shortcuts import render, redirect, HttpResponse
from .forms import SampleForm
from item.models import Item
from order.models import Coupon
from .models import Sample, SampleReview
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def sample_request(request):
	if request.method == 'POST':
		sample_form = SampleForm(request.POST)
		if sample_form.is_valid():
			sample_list = request.POST.getlist('sample_list')
			name = request.POST['name']
			password = request.POST['password']
			phone = request.POST['phone']
			postcode = request.POST['postcode']
			address1 = request.POST['address1']
			address2 = request.POST['address2']
			new_sample = Sample(
				password = password,
				name = name,
				phone = phone,
				postcode = postcode,
				address1 = address1,
				address2 = address2,
				status = '접수',
				delivery_number='미입력',
				)
			new_sample.save()
			new_coupon = make_coupon(new_sample.id, name)
			new_sample.coupon = new_coupon
			new_sample.save()
			for sample_id in sample_list:
				sample = Item.objects.get(item_id=sample_id)
				new_sample.samples.add(sample)
			return render(request,"sample/sample_complete.html",{'new_sample':new_sample})
	else:
		sample_form = SampleForm()
	samples = Item.objects.filter(is_sample=True).order_by('order_number')
	return render(request, 'sample/sample_request.html', {'sample_form':sample_form, 'samples':samples})

def sample_list(request):
	sample_list = Sample.objects.all().order_by('-request_date')
	paginator = Paginator(sample_list,20)
	page = request.GET.get('page')
	try:
		sample_list = paginator.page(page)
	except PageNotAnInteger:
		sample_list = paginator.page(1)
	except EmptyPage:
		sample_list = paginator.page(paginator.num_pages)
	return render(request, "sample/sample_list.html", {'sample_list':sample_list,})

def sample_detail(request,sample_id):
	sample = Sample.objects.get(pk=sample_id)
	if request.method == 'POST':
		original_password = sample.password
		applied_password = request.POST['password']
		if(original_password==applied_password):
			return render(request, "sample/sample_detail.html", {'sample':sample})
		else:
			return render(request, "sample/sample_detail_password.html", {'title':sample.name + '님 신청내역', 'message':'비밀번호가 일치하지 않습니다. 정확하게 입력해주세요.'})
	else:
		return render(request, "sample/sample_detail_password.html", {'title':sample.name + '님 신청내역'})

def sample_review(request, sample_id):
	sample = Sample.objects.get(pk=sample_id)
	if sample.have_review:
		return render(request,"sample/sample_message.html", {
			'title' : '평가가 이미 있네요?' ,
			'content' : sample.name + '님의 평가는 이미 저장되었습니다. 감사합니다^^',
			})
	if request.method == 'POST':
		original_password = sample.password
		applied_password = request.POST['password']
		if(original_password==applied_password):
			return render(request, "sample/sample_review.html", {'sample':sample,})
		else:
			return render(request, "sample/sample_detail_password.html", {'title':sample.name + '님의 평가는?', 'message':'비밀번호가 일치하지 않습니다. 정확하게 입력해주세요.'})		
	else:
		return render(request, "sample/sample_detail_password.html", {'title':sample.name + '님의 평가는?'})

def sample_review_update(request,sample_id):
	if request.method == 'POST':
		sample = Sample.objects.get(pk=sample_id)
		if not sample.have_review:
			for item in sample.samples.all():
				new_sample_review = SampleReview(
					name = sample.name,
					item = item,
					score = request.POST['rating'+str(item.id)],
					comment = request.POST['comment'+str(item.id)],
				)
				new_sample_review.save()
			sample.have_review = True
			sample.save()
			#정상 처리 감사하다는 메시지 쓰기
			return render(request,"sample/sample_message.html", {
				'title' : '평가 완료' ,
				'content' : sample.name + '님의 평가가 저장되었습니다. 감사합니다^^',
				})
		else:
			return render(request,"sample/sample_message.html", {
				'title' : '평가가 이미 있네요?' ,
				'content' : sample.name + '님의 평가는 이미 저장되었습니다. 감사합니다^^',
				})
	else:
		return redirect('index')

def make_coupon(sample_id, name):
	coupon_id = '0901♥'+name
	if Coupon.objects.filter(coupon_id = coupon_id).exists():
		coupon_id = '0901♥' + name + '(' + str(sample_id) +')'
	subject = name+'님께 화장품연구공원에서 샘플과 쿠폰을 함께 선물로 드립니다^^'
	condition = 0
	kind_of = 'flat'
	quantity = 3000
	new_coupon = Coupon(
			coupon_id=coupon_id,
			subject=subject,
			condition=condition,
			kind_of=kind_of,
			quantity=quantity,
		)
	new_coupon.save()
	return new_coupon
