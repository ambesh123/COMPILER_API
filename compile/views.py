from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.

def index(request):
	return render(request , 'index.html')

def run(request):
	source = request.GET.get('source_code')
	lang = request.GET.get('lang')
	CLIENT_SECRET = "898e4fb3034c56a5e32de55248841f5249fec76d026c9461c01fa15184282369"
	CLIENT_ID = "311b351f54b26b1b004944f37f8c2c53"
	STDIN = request.GET.get('input')
	data = {
		'script' : source,
		'language' : lang,
		'versionIndex' : "0",
		'clientId' : CLIENT_ID,
		'clientSecret' : CLIENT_SECRET,
		'stdin' : STDIN,
	}
	headers = {'content-type': 'application/json'}
	url = 'https://api.jdoodle.com/v1/execute'

	r = requests.post(url , data = json.dumps(data) , headers = headers)
	r = r.json()
	if r['statusCode'] == 200 :
		return HttpResponse(r['output'])
	else :
		return HttpResponse('some error occured : ' + str(r['statusCode']))