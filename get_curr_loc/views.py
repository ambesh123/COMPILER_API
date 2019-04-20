from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def index(request):
	response = requests.get("http://api.open-notify.org/iss-now.json")
	res = "Current Location of <b>International Space Station</b> is as follows : <br>"
	res += "<br>Latitude : "
	res += response.json()['iss_position']['latitude']
	res += " Longitude : " + response.json()['iss_position']['longitude']
	return HttpResponse(res)