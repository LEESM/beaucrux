from django.shortcuts import render, redirect
from board.models import Notice, Event, Sample, After28, Labs
from board.forms import BoardWriteForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def board_view(request):
	board_name = request.GET.get('board_name')
	item_id = request.GET.get('item_id')
	if board_name == 'Notice' :
		item = Notice.objects.get(id=item_id)
	elif board_name == 'Event' :
		item = Event.objects.get(id=item_id)
	elif board_name == 'Sample' :
		item = Sample.objects.get(id=item_id)
	elif board_name == 'Labs' :
		item = Labs.objects.get(id=item_id)
	elif board_name == 'After28' :
		item = After28.objects.get(id=item_id)
	else:
		return redirect('index')
	if item.secret:
		if not item.user == request.user:
			if not request.user.is_superuser:
				return redirect('index')
	item.hits+=1
	item.save()
	return render(request, "board/board_view.html", {
		'item':item,
	})

def board_list(request):
	board_name = request.GET.get('board_name')
	if board_name == 'Notice' :
		board_title = '공지사항'
		write_btn = False
		board_list=Notice.objects.all().order_by('-pub_time')
	elif board_name == 'Event' :
		board_title = '이벤트'
		write_btn = True
		board_list=Event.objects.all().order_by('-pub_time')
	elif board_name == 'Sample' :
		board_title = '샘플신청'
		write_btn = True
		board_list=Sample.objects.all().order_by('-pub_time')
	elif board_name == 'Labs' :
		board_title = '탐방기'
		write_btn = False
		board_list=Labs.objects.all().order_by('-pub_time')
	elif board_name == 'After28' :
		board_title = '28일후...'
		write_btn = False
		board_list=After28.objects.all().order_by('-pub_time')
	else:
		return redirect('index')
	paginator = Paginator(board_list, 20) 
	page = request.GET.get('page')
	try:
		board_list = paginator.page(page)
	except PageNotAnInteger:
		board_list = paginator.page(1)
	except EmptyPage:
		board_list = paginator.page(paginator.num_pages)
	return render(request, "board/board_list.html", {
		'write_btn':write_btn,
		'board_name':board_name,
		'board_title':board_title,
		'board_list':board_list,
	})

@login_required
def board_write(request):
	if request.method == "POST" :
		board_name=request.POST.get('board_name')
		title=request.POST.get('title')
		content=request.POST.get('content')
		raw_secret = request.POST.get('secret')
		if raw_secret:
			secret = True
		else:
			secret = False
		#보드네임 확인
		if board_name == 'Notice' :
			newboarditem=Notice(
				user = request.user,
				title = title,
				content = content,
				secret = secret,
				)
		elif board_name == 'Event' :
			newboarditem=Event(
				user = request.user,
				title = title,
				content = content,
				secret = secret,
				)
		elif board_name == 'Sample' :
			newboarditem=Sample(
				user = request.user,
				title = title,
				content = content,
				secret = secret,
				)
		else:
			return redirect('index')
		newboarditem.save()
		return redirect('index')		 
	else:
		board_name = request.GET.get('board_name')
		boardwriteform = BoardWriteForm()
		return render(request, "board/board_write.html", {
			'boardwriteform':boardwriteform,
			'board_name':board_name,
		})
