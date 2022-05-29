from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView
from magazin.forms import NewAccountForm


def magazin(request):
	p = Paginator(Produs.objects.all().order_by('name'), 6)
	page = request.GET.get('page')
	produse_paginate = p.get_page(page)
	contain = {'produse_paginate': produse_paginate}
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

