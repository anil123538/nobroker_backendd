from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import City, PropertyType, PropertyOption, Property
from .serializers import CitySerializer, PropertyTypeSerializer, PropertyOptionSerializer, PropertySerializer


# City Views
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Property Type Views
class PropertyTypeListCreateView(generics.ListCreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

class PropertyTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

# Property Option Views
class PropertyOptionListCreateView(generics.ListCreateAPIView):
    queryset = PropertyOption.objects.all()
    serializer_class = PropertyOptionSerializer

class PropertyOptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyOption.objects.all()
    serializer_class = PropertyOptionSerializer

# Property Views
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
