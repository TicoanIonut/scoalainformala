from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
	path('', views.Locationsview.as_view(), name='lista_locatii'),
	path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
]
