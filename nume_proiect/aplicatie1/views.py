from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from django.views.generic import ListView, CreateView

from aplicatie1.models import Location


class Locationsview(ListView):
	model = Location
	template_name = 'aplicatie1/locations_index.html'


class CreateLocationView(CreateView):
	model = Location
	# fields = '__all__'
	fields = ['city', 'country']
	template_name = 'aplicatie1/location_form.html'
	
	def get_success_url(self):
		return reverse('locations:lista_locatii')
