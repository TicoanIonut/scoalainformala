from rest_framework import serializers

from aplicatie1.models import Location
from aplicatie2.models import Companies


class LocationSerializers(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Location
		fields = ['city', 'country']
		
		
class CompaniesSerializers(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Companies
		fields = ['name', 'company_type', 'website', 'active']
		
		