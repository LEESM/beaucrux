from django.shortcuts import render, redirect
from item.models import Category, Brand, Item, ItemOption, ItemQna, ItemReview
from accounts.models import PointHistory, Landing, Texts
from item.forms import ItemReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

#url조정
def landing(request):
	message = ''
	if request.method == "POST":
		get_email = request.POST.get('email')
		new_landing = Landing(email = get_email)
		new_landing.save()
		message = get_email + " 접수되었습니다. 감사합니다^^"
	context = {"message": message}
	return render(request,"landing.html", context)

def index(request):
	items1 = Item.objects.all().exclude(item_active=False).order_by('-item_id')
	try:
		head1 = Texts.objects.get(name='head1').contents
	except:
		head1 = '내용이 입력되지 않았습니다. 관리필요.'
	context={'items1':items1,'head1':head1}
	return render(request,"item/index.html", context)

def brand(request):
	try:
		brand_name = request.GET.get('brand_name')
	except:
		redirect('index')
	brand = Brand.objects.get(brand_id=brand_name)
	items = Item.objects.filter(brand=brand).exclude(item_active=False).order_by('-item_id')
	return render(request,"item/brand.html",{
		'brand':brand,
		'items':items,
		})

def detail(request):
	item_id=request.GET.get('item_id')
	item=Item.objects.get(item_id=item_id)
	images = []
	images.append(item.image0)
	if(item.image1!=''):
		images.append(item.image1)
	if(item.image2!=''):
		images.append(item.image2)
	if(item.image3!=''):
		images.append(item.image3)
	if(item.image4!=''):
		images.append(item.image4)
	if(item.image5!=''):
		images.append(item.image5)
	if(item.image6!=''):
		images.append(item.image6)
	if(item.image7!=''):
		images.append(item.image7)
	if(item.image8!=''):
		images.append(item.image8)
	if(item.image9!=''):
		images.append(item.image9)
	ingredients=item.ingredients.all().order_by('itemingredientcombination__order')
	item_qnas = ItemQna.objects.filter(item=item).order_by('-qna_time')
	review_write = ItemReviewForm()
	item_reviews = ItemReview.objects.filter(item=item).order_by('-review_time')
	context={
		'item':item, 
		'images':images, 
		'ingredients':ingredients,
		'item_qnas':item_qnas, 
		'review_write':review_write, 
		'item_reviews':item_reviews,
		}
	return render(request,"item/detail.html", context)

@login_required
def qna_update(request):
	raw = request.POST.get('question')
	lines = raw.split('\n')
	question = '<p>'+'</p><p>'.join(lines)+'</p>'
	raw_secret = request.POST.get('secret')
	if raw_secret:
		secret = True
	else:
		secret = False
	newqna=ItemQna(
		user=request.user, 
		secret=secret,
		item=Item.objects.get(item_id=request.POST.get('item_id')), 
		question=question,
		)
	newqna.save()
	return redirect('/item/detail/?item_id='+newqna.item.item_id)

@login_required
def review_write(request):
	item_id=request.GET.get('item_id')
	try:
		item = Item.objects.get(item_id=item_id)
	except:
		return redirect('index')
	itemreviewform = ItemReviewForm()
	context={'item':item,'itemreviewform':itemreviewform}
	return render(request,"item/review_write.html", context)

@login_required
def review_update(request):
	itemreviewform = ItemReviewForm(request.POST)
	newreview = ItemReview(
		user=request.user,
		item=Item.objects.get(item_id=request.POST.get('item_id')), 
		score=request.POST.get('score'),
		comment=request.POST.get('comment')
		)
	newreview.save()
	user=request.user
	user.profile.point += 1000
	user.profile.save()
	point_history = PointHistory(
		user = user,
		kindof = '후기',
		amount = 1000,
		content = '후기 작성으로 발생',
		)
	point_history.save()
	return redirect('/item/detail/?item_id='+newreview.item.item_id)




















