from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password']
		
		widgets = {
			'first_name': TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
			'last_name': TextInput(attrs={'placeholder': 'Lirst name', 'class': 'form-control'}),
			'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
			'username': TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
			'password': TextInput(attrs={'placeholder': 'password', 'class': 'form-control'}),
		}
	

	def clean(self):
		field_data = self.cleaned_data
		email_value = field_data.get('email')
		usename_value = field_data.get('username')
		if User.objects.filter(email=email_value).exists():
			self._errors['email'] = self.error_class(['Emailul exista, adauga un email unic'])
		if User.objects.filter(username=usename_value).exists():
			self._errors['username'] = self.error_class(['Username-ul deja exista!'])
		
		return field_data
