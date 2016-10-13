import requests
import json

from django.http import HttpResponse
from django.shortcuts import render
from shopping.settings import SMS_APPID, SMS_APIKEY, SMS_SENDER
from sample.models import Sample

def send_sms(phone_num, content):
	receivers = [phone_num]
	url = 'https://api.bluehouselab.com/smscenter/v1.0/sendsms'
	params = {
		'sender': SMS_SENDER,
		'receivers': receivers,
		'content': content,
	}
	headers = {'Content-type': 'application/json; charset=utf-8',}
	r = requests.post(url, data=json.dumps(params),
	auth=(SMS_APPID, SMS_APIKEY), headers=headers)
	return r.status_code

def sms_send_form(request):
	if request.method == 'POST':
		phone_num = request.POST['phone_num']
		content = request.POST['content']
		result = send_sms(phone_num, content)
		return HttpResponse(result)
	else:
		phone_num = request.GET['phone_num']
		return render(request, 'message/sms_send_form.html',{'phone_num':phone_num})