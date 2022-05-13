from django.shortcuts import render
from .models import *


def magazin(request):
	produse = Produs.objects.all()
	contain = {'produse': produse}
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


