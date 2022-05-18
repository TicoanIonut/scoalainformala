from django.urls import path
from utilizatori import views

app_name = 'utilizatori'

urlpatterns = [
	path('new_account/', views.CreateNewAccount.as_view(), name='utilizator_nou')
]