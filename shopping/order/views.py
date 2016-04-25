from django.shortcuts import render
from order.models import Cart, Order
from item.models import Item, ItemOption
from order.forms import OrderInfoForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
	cart_items = Cart.objects.filter(user=request.user)
	total_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		total_price += tmp
	return render(request, "order/cart.html", {
		'cart_items':cart_items,
		'total_price':total_price,
		'message':'카트 상세보기',
	})

@login_required
def cart_update(request):
	if request.method=="POST":
		#POST 값 받아오기
		item_id_list = request.POST.getlist('item_id')
		option_id_list = request.POST.getlist('option_id')
		quantity_list = request.POST.getlist('quantity')
		#있는거 번호 체크
		num_list = []
		for i, item in enumerate(quantity_list):
			if item != '0':
				num_list.append(i)
		#카트 있는지 체크
		cart_exist_check = Cart.objects.filter(user = request.user).order_by('cart_id')
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
	return HttpResponseRedirect(reverse("cart"))	

@login_required
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

@login_required
def pop_item(request):
	remove_cart_id = request.GET.get('id')
	remove_cart = Cart.objects.get(id=remove_cart_id)
	remove_cart.delete()
	return HttpResponseRedirect(reverse("cart"))	

@login_required
def order_info(request):
	cart_items = Cart.objects.filter(user=request.user)
	item_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		item_price += tmp
	orderinfoform = OrderInfoForm()
	cart_id = cart_item.cart_id
	delivery_price=2500
	total_price = item_price+delivery_price
	point_made = int(item_price*0.05)
	return render(request, "order/order_info.html", {
		'orderinfoform':orderinfoform,
		'cart_id':cart_id,
		'cart_items':cart_items,
		'item_price':item_price,
		'delivery_price':delivery_price,
		'total_price':total_price,
		'point_made':point_made,
		'message':'주문 정보 입력',
	})
