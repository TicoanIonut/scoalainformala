from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
	path('', views.Locationsview.as_view(), name='lista_locatii'),
	path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
	path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modifica'),
	path('<int:pk>/delete/', views.delete_location, name='sterge'),
	path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),
	path('locatii_inactive', views.LocationInactiveView.as_view(), name='locatii_inactive'),
	path('locatii_toate', views.LocationAllView.as_view(), name='locatii_toate'),

]
