from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def magazin(request):
	# produse = Produs.objects.all()
	# contain = {'produse': produse}
	p = Paginator(Produs.objects.all().order_by('name'), 6)
	page = request.GET.get('page')
	produse_paginate = p.get_page(page)
	contain2 = {'produse_paginate': produse_paginate}
	return render(request, 'magazin/magazin.html', contain2)


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
		return render(request, 'magazin/searchp.html', {'cauta': cauta}, {'produse': produse})
	else:
		return render(request, 'magazin/searchp.html')

