from rest_framework import serializers

from aplicatie1.models import Location


class LocationSerializers(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Location
		fields = ['city', 'country']
		
		