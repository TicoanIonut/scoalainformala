from datetime import datetime

from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from magazin.forms import NewAccountForm
from django.http import JsonResponse
import json


def magazin(request):
	if request.user.is_authenticated:
		client = request.user.client
		comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
		produse = comanda.comandaprodus_set.all()
		cosProduse = comanda.get_cart_items
	else:
		produse=[]
		comanda = {'get_cart_total': 0, 'get_cart_items': 0}
		cosProduse = comanda['get_cart_items']
		
	p = Paginator(Produs.objects.all().order_by('name'), 6)
	page = request.GET.get('page')
	produse_paginate = p.get_page(page)
	
	contain = {'produse_paginate': produse_paginate, 'cosProduse': cosProduse}
	return render(request, 'magazin/magazin.html', contain)

def searchp(request):
	if request.method == 'POST':
		cauta = request.POST['cauta']
		p = Paginator(Produs.objects.filter(name__contains=cauta).order_by('name'), 6)
		produse_paginate = p.get_page('cauta')
		contain = {'cauta': cauta, 'produse_paginate': produse_paginate}
		return render(request, 'magazin/searchp.html', contain)
	else:
		return render(request, 'magazin/searchp.html')


def cos(request):
	if request.user.is_authenticated:
		client = request.user.client
		comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
		items = comanda.comandaprodus_set.all()
		cosProduse = comanda.get_cart_items
	else:
		items = []
		comanda = {'get_cart_total': 0, 'get_cart_items': 0}
		cosProduse = comanda['get_cart_items']

	contain = {'items': items, 'comanda': comanda, 'cosProduse': cosProduse}
	return render(request, 'magazin/cos.html', contain)


def comanda(request):
	if request.user.is_authenticated:
		client = request.user.client
		comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
		items = comanda.comandaprodus_set.all()
		cosProduse = comanda.get_cart_items
	else:
		items = []
		comanda = {'get_cart_total': 0, 'get_cart_items': 0}
		cosProduse = comanda['get_cart_items']
	
	contain = {'items': items, 'comanda': comanda, 'cosProduse': cosProduse}
	return render(request, 'magazin/comanda.html', contain)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)
	client = request.user.client
	produs = Produs.objects.get(id=productId)
	comanda, created = Comanda.objects.get_or_create(client=client, complet=False)
	comandaItem, created = ComandaProdus.objects.get_or_create(comanda=comanda, produs=produs)
	if action == 'add':
		comandaItem.cantitate = (comandaItem.cantitate + 1)
	elif action == 'remove':
		comandaItem.cantitate = (comandaItem.cantitate - 1)
	comandaItem.save()
	if comandaItem.cantitate <= 0:
		comandaItem.delete()
	return JsonResponse('Produs adaugat', safe=False)


def register_request(request):
	if request.method == "POST":
		form = NewAccountForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Inregistrarea a avut loc cu succes." )
			return redirect("magazin")
		messages.error(request, "Inregistrarea nu a aputut fi efectuata .")
	form = NewAccountForm()
	return render(request=request, template_name="magazin/login.html", context={"form": form})


def log(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("magazin")
			else:
				messages.error(request, "Numele de utilizator sau parola sunt incorecte.")
		else:
			messages.error(request, "Numele de utilizator sau parola sunt incorecte.")
	form = AuthenticationForm()
	return render(request=request, template_name="magazin/log.html", context={'form': form})


def logout(request):
	lgout(request)
	messages.info(request, "Ai iesit din cont.")
	return redirect("magazin")


def vezi(request):
	vez = Produs.objects.order_by('name')
	# pk = Produs.objects.filter(3)
	contain = {'vez': vez, 'pk': 3}
	return render(request, 'magazin/vezi.html', contain)


def chat(request):
	return render(request, 'magazin/chat.html')


