
from rest_framework import serializers
from .models import City, PropertyType, PropertyOption, Property

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name']

class PropertyOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyOption
        fields = ['id', 'property_type', 'option']

class PropertySerializer(serializers.ModelSerializer):
    city = CitySerializer()
    property_type = PropertyTypeSerializer()
    option = PropertyOptionSerializer()

    class Meta:
        model = Property
        fields = ['id', 'owner','address', 'city', 'property_type', 'option', 'description']
