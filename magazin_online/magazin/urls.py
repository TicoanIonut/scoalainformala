from django.urls import path
from magazin import views



urlpatterns = [
	path('', views.magazin, name='magazin'),
	path('cos/', views.cos, name='cos'),
	path('comanda/', views.comanda, name='comanda'),
	path('log/', views.log, name='log'),
	path('searchp/', views.searchp, name='searchp'),
	path('logout/', views.logout, name='logout'),
	path('login/', views.register_request, name='login'),
	path('update_item/', views.updateItem, name='update_Item'),
	path('vezi/<int:pk>', views.vezi, name='vezi'),
	path('chat/', views.chat, name='chat'),
	
	# path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
	
]
