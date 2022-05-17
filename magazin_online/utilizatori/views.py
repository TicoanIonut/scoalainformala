
import random
import string


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView

from utilizatori.forms import NewAccountForm


punctuation = '!$%?#@'


class CreateNewAccount(LoginRequiredMixin, CreateView):
	model = User
	template_name = 'magazin/login.html'
	form_class = NewAccountForm
	
	def form_valid(self, form):
		if form.is_valid() and form.errors is False:
			form.save(commit=False)
		return super(CreateNewAccount, self).form_valid(form)
	
	def form_invalid(self, form):
		print(form.errors)
		return super(CreateNewAccount, self).form_invalid(form)
	
	def get_success_url(self):
		psw = ''.join(
			random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation)
			for _ in range(8))
		if User.objects.filter(id=self.object.id).exists():
			user_instance = User.objects.get(id=self.object.id)
			user_instance.set_password(psw)
			user_instance.save()
			content = f'Datele de autentificare sunt: \n username: {user_instance.username} \n password: {psw}'
			msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
			email = EmailMultiAlternatives(subject='Invitatie utilizator',
			                               body=content, from_email='contact@test.ro', to=[user_instance.email])
			email.attach_alternative(msg_html, 'text/html')
			email.send()
		return reverse('magazin')
	