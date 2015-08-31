from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

#def index(request):
	#return HttpResponse("<br />itcast cpp hello world by xingwenpeng!<hr />")
def index(request):
	category_list = Category.objects.all()
	context_dict = {'categories':category_list}
	return render(request, 'rango/index.html', context_dict)


def about(request):
	pengchong_dict = {'pengchong': "How old ary you!"}
	return render(request, 'rango/about.html', pengchong_dict)