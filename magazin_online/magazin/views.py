from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def magazin(request):
	p = Paginator(Produs.objects.all().order_by('name'), 6)
	page = request.GET.get('page')
	produse_paginate = p.get_page(page)
	contain = {'produse_paginate': produse_paginate}
	return render(request, 'magazin/magazin.html', contain)


def cos(request):
	contain = {}
	return render(request, 'magazin/cos.html', contain)


def comanda(request):
	contain = {}
	return render(request, 'magazin/comanda.html', contain)


def chat(request):
	return render(request, 'magazin/chat.html')
	
	
# def login(request):
# 	return render(request, 'magazin/login.html')

def searchp(request):
	if request.method == 'POST':
		cauta = request.POST['cauta']
		produse = Produs.objects.filter(name__contains=cauta)
		contain = {'cauta': cauta, 'produse': produse}
		return render(request, 'magazin/searchp.html', contain)
	else:
		return render(request, 'magazin/searchp.html')

# def searchp(request):
# 	if 'q' in request.GET:
# 		q = request.GET['q']
# 		data = Produs.objects.filter(name__contains=q)
# 	else:
# 		data = Produs.objects.all()
# 	contain = {'data': data}
# 	return  render(request, 'magazin/searchp.html', contain)


