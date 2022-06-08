from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
	utilizator = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	parola = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.name
	
	
class Produs(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField()
	imagine = models.ImageField(null=True, blank=True)
	
	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.imagine.url
		except:
			url = ''
		return url


class Comanda(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
	data_comenzii = models.DateTimeField(auto_now_add=True)
	complet = models.BooleanField(default=False)
	id_tranzactie = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return str(self.id)
	
	@property
	def livrare(self):
		livrare = False
		comandaitems = self.comandaprodus_set.all()
		for i in comandaitems:
			if i.produs.digital == False:
				livrare = True
		return livrare
	
	@property
	def get_cart_total(self):
		comandaitems = self.comandaprodus_set.all()
		total = sum([produs.get_total for produs in comandaitems])
		return total

	@property
	def get_cart_items(self):
		comandaitems = self.comandaprodus_set.all()
		total = sum([produs.cantitate for produs in comandaitems])
		return total

	
class ComandaProdus(models.Model):
	produs = models.ForeignKey(Produs, on_delete=models.SET_NULL, blank=True, null=True)
	comanda = models.ForeignKey(Comanda, on_delete=models.SET_NULL, blank=True, null=True)
	cantitate = models.IntegerField(default=0, null=True, blank=True)
	data_adaugarii = models.DateTimeField(auto_now_add=True)
	
	@property
	def get_total(self):
		total = self.produs.price * self.cantitate
		return total

	
class AdresaComanda(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
	comanda = models.ForeignKey(Comanda, on_delete=models.SET_NULL, blank=True, null=True)
	adresa = models.CharField(max_length=200, null=True)
	oras = models.CharField(max_length=200, null=True)
	judet = models.CharField(max_length=200, null=True)
	cod_postal = models.CharField(max_length=200, null=True)
	data_adaugarii = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.adresa
