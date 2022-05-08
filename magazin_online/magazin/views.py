from django.shortcuts import render


def magazin(request):
	contain = {}
	return render(request, 'magazin/magazin.html', contain)


def cos(request):
	contain = {}
	return render(request, 'magazin/cos.html', contain)


def comanda(request):
	contain = {}
	return render(request, 'magazin/comanda.html', contain)


def chat(request):
	return render(request, 'magazin/chat.html')