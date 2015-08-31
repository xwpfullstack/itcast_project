from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<br />itcast cpp hello world by xingwenpeng!<hr />")
