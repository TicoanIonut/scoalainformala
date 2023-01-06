
from rest_framework import viewsets

from aplicatie1.models import Location
from myapi.serializers import LocationSerializers
from myapi.serializers import CompaniesSerializers
from aplicatie2.models import Companies


class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all().order_by('city')
	serializer_class = LocationSerializers
	
	
class CompaniesViewSet(viewsets.ModelViewSet):
	queryset = Companies.objects.all().order_by('name')
	serializer_class = CompaniesSerializers
	