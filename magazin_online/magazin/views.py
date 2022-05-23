from django.contrib.auth import login as lgin, authenticate, logout as lgout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


def magazin(request):
	p = Paginator(Produs.objects.all().order_by('name'), 6)
	page = request.GET.get('page')
	produse_paginate = p.get_page(page)
	contain = {'produse_paginate': produse_paginate}
	return render(request, 'magazin/magazin.html', contain)


def cos(request):
	# if request.user.is_authenticated:
	# 	client = request.user.client
	# 	comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
	# 	items = comanda.comadaitem_set.all()
	# else:
	# 	items = []
	# 	comanda = {'cos_total': 0, 'cos_items': 0}
	# contain = {'items': items, 'comanda': comanda}
	contain = {'comanda': comanda}
	return render(request, 'magazin/cos.html', contain)


def comanda(request):
	# if request.user.is_authenticated:
	# 	client = request.user.client
	# 	comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
	# 	items = comanda.comadaitem_set.all()
	# else:
	# 	items = []
	# 	comanda = {'cos_total': 0, 'cos_items': 0}
	# contain = {'items': items, 'comanda': comanda}
	contain = {'comanda': comanda}
	return render(request, 'magazin/comanda.html', contain)


def chat(request):
	return render(request, 'magazin/chat.html')
	
	
def login(request):
	return render(request, 'magazin/login.html')


def log(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				lgin(request, user)
				messages.info(request, f"Esti logat ca si {username}.")
				return redirect("magazin")
			else:
				messages.error(request, "Numele de utilizator sau parola sunt incorecte.")
		else:
			messages.error(request, "Numele de utilizator sau parola sunt incorecte.")
	return render(request, "magazin/log.html")


def logout(request):
	lgout(request)
	messages.info(request, "Ai iesit din cont.")
	return redirect("magazin")


def searchp(request):
	if request.method == 'POST':
		cauta = request.POST['cauta']
		produse = Produs.objects.filter(name__contains=cauta)
		contain = {'cauta': cauta, 'produse': produse}
		return render(request, 'magazin/searchp.html', contain)
	else:
		return render(request, 'magazin/searchp.html')



