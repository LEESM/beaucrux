from django.shortcuts import render, redirect
from order.models import Cart, Order, Coupon
from item.models import Item, ItemOption
from accounts.models import PointHistory
from order.forms import OrderInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.decorators import login_required
import urllib.request
import urllib.parse
from shopping.settings import IMP_KEY, IMP_SECRET
import json
from django.views.decorators.csrf import csrf_exempt
from item.views import get_brands

def cart(request):
	if request.user.is_authenticated():
		cart_items = Cart.objects.filter(user=request.user, order_flag=False)
	else:
		cart_items = Cart.objects.filter(cart_id=request.session.session_key, order_flag=False)
	total_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		total_price += tmp
	return render(request, "order/cart.html", {
		'cart_items':cart_items,
		'total_price':total_price,
		'brands':get_brands(),
	})

def cart_update(request):
	if request.method=="POST":
		#POST 값 받아오기
		item_id_list = request.POST.getlist('item_id')
		option_id_list = request.POST.getlist('option_id')
		quantity_list = request.POST.getlist('quantity')
		buy_now_text = request.POST.get('buy_now')
		#있는거 번호 체크
		num_list = []
		for i, item in enumerate(quantity_list):
			if item != '0':
				num_list.append(i)
		#로그인여부 체크
		if not request.user.is_authenticated():
			#세션 키 이름으로 카트 존재하는지 확인
			if not request.session.session_key:
				request.session.create()
			cart_exist_check = Cart.objects.filter(cart_id=request.session.session_key).order_by('cart_id')
			if(cart_exist_check):
				#있으면 거기다 추가
				new_cart_id = cart_exist_check[0].cart_id
			else :			
				#익명유저다 그러면
				new_cart_id = request.session.session_key
			for i in num_list:
				new_cart = Cart(
					cart_id = new_cart_id, 
					item = Item.objects.get(item_id = item_id_list[i]),
					item_option = ItemOption.objects.get(option_id = option_id_list[i]), 
					quantity=quantity_list[i],
					)
				new_cart.save()
		else:
			#카트 있는지 체크
			cart_exist_check = Cart.objects.filter(user = request.user, order_flag=False).order_by('cart_id')
			if(cart_exist_check):
				#카트 있으면 있는거에 집어넣기
				new_cart_id = cart_exist_check[0].cart_id
			else:
				#카트 없으면 카트 아이디 만들고 집어넣기
				new_cart_id = 'cart'+datetime.datetime.now().strftime ("%Y%m%d%H%M%S")+str(request.user)
			for i in num_list:
				new_cart = Cart(
					cart_id = new_cart_id, 
					user = request.user, 
					item = Item.objects.get(item_id = item_id_list[i]),
					item_option = ItemOption.objects.get(option_id = option_id_list[i]), 
					quantity=quantity_list[i],
					)
				new_cart.save()
		if buy_now_text == 'buy_now':
			return redirect('order_info')
	return HttpResponseRedirect(reverse("cart"))	

def cart_number_update(request):
	if request.method == 'POST':
		update_target_id_list = request.POST.getlist('id')
		update_quantity = request.POST.getlist('quantity')
		for i, update_target_id in enumerate(update_target_id_list):
			update_cart = Cart.objects.get(id=update_target_id)
			update_cart.quantity = update_quantity[i]
			update_cart.save()
		return HttpResponseRedirect(reverse("cart"))	
	else:
		return HttpResponseRedirect(reverse("index"))	

def pop_item(request):
	remove_cart_id = request.GET.get('id')
	remove_cart = Cart.objects.get(id=remove_cart_id)
	remove_cart.delete()
	return HttpResponseRedirect(reverse("cart"))	

def order_info(request):
	if request.user.is_authenticated():
		cart_items = Cart.objects.filter(user=request.user, order_flag=False)
		anonymous=False
	else:
		cart_items = Cart.objects.filter(cart_id=request.session.session_key)
		anonymous=True
	item_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		item_price += tmp
	orderinfoform = OrderInfoForm()
	cart_id = cart_item.cart_id
	#쿠폰처리
	coupons = []
	if request.user.is_authenticated():
		coupons = Coupon.objects.filter(user=request.user, used=False)
	#50000원이상 무료배송
	if(item_price>50000):
		delivery_price=0
	else:
		delivery_price=2500
	total_price = item_price+delivery_price
	#포인트 5%
	point_made = int(item_price*0.05)
	#pg 용 이름 짓기 ~외 *종
	pg_product_name = cart_items[0].item.item_name
	if(cart_items.count()>1):
		pg_product_name = pg_product_name + ' 외' + str(cart_items.count()-1) + '종'
	return render(request, "order/order_info.html", {
		'anonymous':anonymous,
		'orderinfoform':orderinfoform,
		'cart_id':cart_id,
		'cart_items':cart_items,
		'item_price':item_price,
		'delivery_price':delivery_price,
		'total_price':total_price,
		'point_made':point_made,
		'pg_product_name':pg_product_name,
		'coupons':coupons,
		'brands':get_brands(),
	})

def order_update(request):
	order_id=request.POST.get('order_id')
	cart_id=request.POST.get('cart_id')
	cart_items=Cart.objects.filter(cart_id=cart_id)
	for item in cart_items:
		item.order_flag=True
		item.save()
	item_price=request.POST.get('item_price')
	delivery_price=request.POST.get('delivery_price')
	total_price=request.POST.get('total_price')
	pay_price=request.POST.get('pay_price')
	point_price=request.POST.get('point_price')
	coupon_price=request.POST.get('coupon_price')
	selected_coupon_id=request.POST.get('selected_coupon_id')
	point_made=request.POST.get('point_made')
	name=request.POST.get('name')
	email=request.POST.get('email')
	postcode=request.POST.get('postcode')
	address=request.POST.get('address')
	address_detail=request.POST.get('address_detail')
	phone=request.POST.get('phone')
	postscript=request.POST.get('postscript')
	mypage_check=request.POST.get('mypage_check',False)
	status='결제'
	message='주문이 완료되었습니다. 주문번호는'+order_id+'입니다.'
	if request.user.is_authenticated():
		new_order = Order(
			order_id=order_id,
			cart_id=cart_id,
			user=request.user,
			item_price=item_price,
			delivery_price=delivery_price,
			total_price=total_price,
			pay_price=pay_price,
			point_price=point_price,
			coupon_price=coupon_price,
			point_made=point_made,
			name=name,
			email=email,
			postcode=postcode,
			address=address,
			address_detail=address_detail,
			phone=phone,
			postscript=postscript,
			status=status,
			)
		user=request.user
		#포인트 처리
		changed_point = int(user.profile.point)-int(point_price)+int(point_made)
		user.profile.point = str(changed_point)
		point_history = PointHistory(
			user = user,
			kindof = '구매',
			record = int(total_price),
			amount = int(point_made),
			content = '주문번호 ' + order_id + ' 구매로 발생',
			)
		point_history.save()
		#쿠폰처리
		if not (selected_coupon_id == 'nocoupon' ):
			renew_coupon = Coupon.objects.get(coupon_id=selected_coupon_id)
			renew_coupon.used = True
			renew_coupon.save()
		if(mypage_check):
			user.first_name=name
			user.save()
			user.email=email
			user.profile.postcode=postcode
			user.profile.address=address
			user.profile.address_detail=address_detail
			user.profile.phone=phone
		user.profile.save()
	else:
		new_order = Order(
			order_id=order_id,
			cart_id=cart_id,
			item_price=item_price,
			delivery_price=delivery_price,
			total_price=total_price,
			pay_price=pay_price,
			point_price=point_price,
			coupon_price=coupon_price,
			name=name,
			email=email,
			postcode=postcode,
			address=address,
			address_detail=address_detail,
			phone=phone,
			postscript=postscript,
			status=status,
			)
	new_order.save()
	return render(request, "order/order_complete.html", {
		'order_id':order_id,
		'new_order':new_order,
		'cart_items':cart_items,
		'brands':get_brands(),
	})

def test(request):
	order_id=request.GET.get('order_id')
	cart_id=request.GET.get('cart_id')
	cart_items=Cart.objects.filter(cart_id=cart_id)
	for item in cart_items:
		item.order_flag=True
		item.save()
	new_order = Order.objects.get(order_id=order_id)
	return render(request, "order/order_complete.html", {
		'order_id':order_id,
		'new_order':new_order,
		'cart_items':cart_items,
	})

def view_orders(request):
	if request.user.is_authenticated():
		orders=Order.objects.filter(user=request.user).order_by('-order_date')
		return render(request, "order/view_orders.html", {
			'orders':orders,
			})
	else:
		main_post="주문서 번호를 입력해주세요."
		if(request.method=="POST"):
			order_id=request.POST.get('order_id')
			try : 
				order=Order.objects.get(order_id=order_id)
				return redirect('/order/view_order_detail/?order_id='+request.POST.get('order_id'))
			except :
				main_post="주문서 번호를 정확하게 입력해주세요."
		return render(request, "order/anonymous_order.html",{'main_post':main_post, 'brands':get_brands(),})

def view_order_detail(request):
	order_id=request.GET.get('order_id')
	order=Order.objects.get(order_id=order_id)
	cart_items=Cart.objects.filter(cart_id=order.cart_id)
	return render(request, "order/view_order_detail.html", {
		'order':order,
		'cart_items':cart_items,
		'brands':get_brands(),
	})

def order_mobile_redirect(request):
	order_id=request.GET.get('order_id')
	cart_id=request.GET.get('cart_id')
	cart_items=Cart.objects.filter(cart_id=cart_id)
	for item in cart_items:
		item.order_flag=True
		item.save()
	item_price=request.GET.get('item_price')
	delivery_price=request.GET.get('delivery_price')
	total_price=request.GET.get('total_price')
	pay_price=request.GET.get('pay_price')
	point_price=request.GET.get('point_price')
	coupon_price=request.GET.get('coupon_price')
	point_made=request.GET.get('point_made')
	name=request.GET.get('name')
	email=request.GET.get('email')
	postcode=request.GET.get('postcode')
	address=request.GET.get('address')
	address_detail=request.GET.get('address_detail')
	phone=request.GET.get('phone')
	postscript=request.GET.get('postscript')
	mypage_check=request.GET.get('mypage_check')
	username=request.GET.get('username')
	#아임포트 정보 가져오기
	imp_uid=request.GET.get('imp_uid')
	imp_success=request.GET.get('imp_success')

	#토큰 얻기
	data = urllib.parse.urlencode({"imp_key":IMP_KEY,"imp_secret":IMP_SECRET})
	data = data.encode('UTF-8')
	f = urllib.request.urlopen('https://api.iamport.kr/users/getToken/',data)
	result = f.read().decode('UTF-8')
	result_json=json.loads(result)
	access_token=result_json['response']['access_token']

	#imp_uid로 요청
	url = 'https://api.iamport.kr/payments/'+imp_uid
	request2 = urllib.request.Request(url)
	request2.add_header("X-ImpTokenHeader",access_token)
	response = urllib.request.urlopen(request2)
	result2 = response.read().decode('UTF-8')
	result2_json=json.loads(result2)
	#결과 받기
	pay_amount = result2_json['response']['amount']#int로 들어옴
	pay_status = result2_json['response']['status']
	pay_method = result2_json['response']['pay_method']

	if pay_status == 'paid' and str(pay_amount) == pay_price:
		message='주문이 완료되었습니다. 주문번호는'+order_id+'입니다.'
	elif pay_status == 'ready' and pay_method == 'vbank':
		message='주문이 완료되었습니다. 주문번호는'+order_id+'입니다.'
	else:
		message='주문이 실패하였습니다. 주문번호 : '+order_id
		return render(request, "order/order_complete.html", {
			'order_id':order_id,
			'brands':get_brands(),
		})
	status='결제'
#회원, 비회원 구분
	try:
		user = User.objects.get(username=username)
		new_order = Order(
			order_id=order_id,
			cart_id=cart_id,
			user=user,
			item_price=item_price,
			delivery_price=delivery_price,
			total_price=total_price,
			pay_price=pay_price,
			point_price=point_price,
			coupon_price=coupon_price,
			point_made=point_made,
			name=name,
			email=email,
			postcode=postcode,
			address=address,
			address_detail=address_detail,
			phone=phone,
			postscript=postscript,
			status=status,
			)
		#포인트처리
		changed_point = int(user.profile.point)-int(point_price)+int(point_made)
		user.profile.point = str(changed_point)
		point_history = PointHistory(
			user = user,
			kindof = '구매',
			record = int(total_price),
			amount = int(point_made),
			content = '주문번호 ' + order_id + ' 구매로 발생',
			)
		point_history.save()
		#쿠폰처리
		if not (selected_coupon_id == 'nocoupon' ):
			renew_coupon = Coupon.objects.get(coupon_id=selected_coupon_id)
			renew_coupon.used = True
			renew_coupon.save()
		if(mypage_check):
			user.first_name=name
			user.save()
			user.email=email
			user.profile.postcode=postcode
			user.profile.address=address
			user.profile.address_detail=address_detail
			user.profile.phone=phone
		user.profile.save()
	except:
		new_order = Order(
			order_id=order_id,
			cart_id=cart_id,
			item_price=item_price,
			delivery_price=delivery_price,
			total_price=total_price,
			pay_price=pay_price,
			point_price=point_price,
			coupon_price=coupon_price,
			name=name,
			email=email,
			postcode=postcode,
			address=address,
			address_detail=address_detail,
			phone=phone,
			postscript=postscript,
			status=status,
			)
	new_order.save()
	return render(request, "order/order_complete.html", {
		'order_id':order_id,
		'brands':get_brands(),
	})

@csrf_exempt
def order_complete(request):
	#토큰 얻기
	data = urllib.parse.urlencode({"imp_key":IMP_KEY,"imp_secret":IMP_SECRET})
	data = data.encode('UTF-8')
	f = urllib.request.urlopen('https://api.iamport.kr/users/getToken/',data)
	result = f.read().decode('UTF-8')
	imp_uid = request.POST.get('imp_uid')
	paid_amount = request.POST.get('paid_amount')
	result_json=json.loads(result)
	access_token=result_json['response']['access_token']
	#imp_uid로 요청
	url = 'https://api.iamport.kr/payments/'+imp_uid
	request = urllib.request.Request(url)
	request.add_header("X-ImpTokenHeader",access_token)
	response = urllib.request.urlopen(request)
	result2 = response.read().decode('UTF-8')
	result2_json=json.loads(result2)
	#결과 받기
	pay_amount = result2_json['response']['amount']#int로 들어옴
	pay_status = result2_json['response']['status']
	pay_method = result2_json['response']['pay_method']
	if pay_status == 'paid' and str(pay_amount) == paid_amount:
		return HttpResponse('{"check":true}')
	elif pay_status == 'ready' and pay_method == 'vbank':
		return HttpResponse('{"check":true}')
	else:
		return HttpResponse('{"check":false,"pay_status":'+pay_status+'}')

@csrf_exempt
def coupon_check(request):
	username = request.POST.get('username')
	coupon_id = request.POST.get('coupon_id')
	if Coupon.objects.filter(coupon_id = coupon_id, user = None, used = False ).exists():
		check = True
		update = Coupon.objects.get(coupon_id=coupon_id)
		user = User.objects.get(username = username)
		update.user = user
		update.save()
	else :
		check = False
	return HttpResponse('{"check":"'+str(check)+'", "coupon_id":"'+coupon_id+'"}')

@csrf_exempt
def ajax_test(request):
	return render(request,"order/ajax_test.html")

