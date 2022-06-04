from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput

from magazin import models
from magazin.models import Client


class NewAccountForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['utilizator', 'name', 'email', 'parola']
		
		widgets = {
			'utilizator': TextInput(attrs={'placeholder': 'utilizator', 'class': 'form-control'}),
			'name': TextInput(attrs={'placeholder': 'nume', 'class': 'form-control'}),
			
			'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
			'parola': TextInput(attrs={'placeholder': 'parola', 'class': 'form-control'}),
		}
	
	def clean(self):
		field_data = self.cleaned_data
		email_value = field_data.get('email')
		usename_value = field_data.get('username')
		if Client.objects.filter(email=email_value).exists():
			self._errors['email'] = self.error_class(['Emailul exista, adauga un email unic'])
		if Client.objects.filter(utilizator=usename_value).exists():
			self._errors['username'] = self.error_class(['Username-ul deja exista!'])
		return field_data
	
	
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
