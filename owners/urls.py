from django.urls import path
from .views import (
    CityListCreateView, CityDetailView,
    PropertyTypeListCreateView, PropertyTypeDetailView,
    PropertyOptionListCreateView, PropertyOptionDetailView,
    PropertyListCreateView, PropertyDetailView
)

urlpatterns = [
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    
    path('property-types/', PropertyTypeListCreateView.as_view(), name='property-type-list-create'),
    path('property-types/<int:pk>/', PropertyTypeDetailView.as_view(), name='property-type-detail'),
    
    path('property-options/', PropertyOptionListCreateView.as_view(), name='property-option-list-create'),
    path('property-options/<int:pk>/', PropertyOptionDetailView.as_view(), name='property-option-detail'),
    
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]

# API's for testing

# List Cities (GET): http://127.0.0.1:8000/api/owners/cities/
# List Cities (GET): http://127.0.0.1:8000/api/owners/cities/1/

# List Property Types (GET):http://127.0.0.1:8000/api/owners/property-types/
# List Property Types (GET):http://127.0.0.1:8000/api/owners/property-types/1/

# List Property Options: http://127.0.0.1:8000/api/owners/property-options/
# List Property Options: http://127.0.0.1:8000/api/owners/property-options/1/


# List Properties: http://127.0.0.1:8000/api/owners/properties/
# List Properties: http://127.0.0.1:8000/api/owners/properties/1/


# city5 = City.objects.create(name="Gurgaon")
# city6 = City.objects.create(name="Ghaziabad")
# city7 = City.objects.create(name="Greater Noida")
# city8 = City.objects.create(name="Hyderabad")
# city9 = City.objects.create(name="Chennai")
# city10 = City.objects.create(name="Faridabad")
# city11 = City.objects.create(name="Noida")