from django.shortcuts import render
from .forms import SampleForm
from item.models import Item
from .models import Sample
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
			for sample_id in sample_list:
				sample = Item.objects.get(item_id=sample_id)
				new_sample.samples.add(sample)
			return render(request,"sample/sample_complete.html",{'new_sample':new_sample})
	else:
		sample_form = SampleForm()
	samples = Item.objects.filter(is_sample=True)
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
	if request.method == 'POST':
		sample = Sample.objects.get(pk=sample_id)
		original_password = sample.password
		applied_password = request.POST['password']
		if(original_password==applied_password):
			return render(request, "sample/sample_detail.html", {'sample':sample})
		else:
			return render(request, "sample/sample_detail_password.html", {'message':'비밀번호가 일치하지 않습니다. 정확하게 입력해주세요.'})
	else:
		return render(request, "sample/sample_detail_password.html", {'sample_id':sample_id})













