from django.urls import path
from magazin import views

urlpatterns = [
	path('', views.magazin, name='magazin'),
	path('cos/', views.cos, name='cos'),
	path('comanda/', views.comanda, name='comanda'),
]