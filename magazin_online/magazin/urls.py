from django.urls import path
from magazin import views

urlpatterns = [
	path('', views.magazin, name='magazin'),
	path('cos/', views.cos, name='cos'),
	path('comanda/', views.comanda, name='comanda'),
	path('chat/', views.chat, name='chat'),
	path('log/', views.log, name='log'),
	path('searchp/', views.searchp, name='searchp'),
	path('logout/', views.logout, name='logout'),
	path('login/', views.register_request, name='login')
]
