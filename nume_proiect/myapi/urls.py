from django.urls import path, include
from rest_framework import routers
from myapi import views

router = routers.DefaultRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
	path('', include(router.urls))
	
]
