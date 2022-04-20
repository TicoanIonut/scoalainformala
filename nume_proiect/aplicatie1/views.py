from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Location


class Locationsview(LoginRequiredMixin, ListView):
	model = Location
	template_name = 'aplicatie1/locations_index.html'
	
	def get_context_data(self, *args, **kwargs):
		data = super(Locationsview, self).get_context_data(*args, **kwargs)
		data['locations'] = self.model.objects.filter(active=1)
		return data


class CreateLocationView(LoginRequiredMixin, CreateView):
	model = Location
	# fields = '__all__'
	fields = ['city', 'country']
	template_name = 'aplicatie1/location_form.html'
	
	def get_success_url(self):
		return reverse('locations:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
	model = Location
	fields = ['city', 'country']
	template_name = 'aplicatie1/location_form.html'
	
	def get_success_url(self):
		return reverse('locations:lista_locatii')


@login_required
def delete_location(request, pk):
	Location.objects.filter(id=pk).update(active=0)
	return redirect('locations:lista_locatii')


@login_required
def activate_location(request, pk):
	Location.objects.filter(id=pk).update(active=1)
	return redirect('locations:lista_locatii')


class LocationInactiveView(LoginRequiredMixin, ListView):
	model = Location
	template_name = 'aplicatie1/locations_index.html'
	
	def get_context_data(self, *args, **kwargs):
		data = super(LocationInactiveView, self).get_context_data(*args, **kwargs)
		data['locations'] = self.model.objects.filter(active=0)
		return data


class LocationAllView(LoginRequiredMixin, ListView):
	model = Location
	template_name = 'aplicatie1/locations_index.html'
	
	def get_context_data(self, *args, **kwargs):
		data = super(LocationAllView, self).get_context_data(*args, **kwargs)
		data['locations'] = self.model.objects.filter()
		return data
