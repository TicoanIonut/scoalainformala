
from rest_framework import viewsets

from aplicatie1.models import Location
from myapi.serializers import LocationSerializers


class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all().order_by('city')
	serializer_class = LocationSerializers
	