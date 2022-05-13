from django.urls import path
from magazin import views

urlpatterns = [
	path('', views.magazin, name='magazin'),
	path('cos/', views.cos, name='cos'),
	path('comanda/', views.comanda, name='comanda'),
	path('chat/', views.chat, name='chat'),
	path('login/', views.cos, name='login'),
]
