from django.db import models

# Create your models here.



class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'
    LAND_PLOT = 'Land/Plot'
    
    PROPERTY_TYPE_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
        (LAND_PLOT, 'Land/Plot'),
    ]
    
    name = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class PropertyOption(models.Model):
    RENT = 'Rent'
    RESALE = 'Resale'
    PG_HOSTEL = 'PG/Hostel'
    FLATMATES = 'Flatmates'
    SALE = 'Sale'

    RESIDENTIAL_OPTIONS = [(RENT, 'Rent'), (RESALE, 'Resale'), (PG_HOSTEL, 'PG/Hostel'), (FLATMATES, 'Flatmates')]
    COMMERCIAL_OPTIONS = [(RENT, 'Rent'), (SALE, 'Sale')]
    LAND_PLOT_OPTIONS = [(RESALE, 'Resale')]

    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.property_type} - {self.option}"

class Property(models.Model):
    owner = models.CharField(max_length=100)  # Replace with ForeignKey to Owner model if needed
    city = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.property_type} in {self.city}, {self.address} by {self.owner}"

class PropertyDetails(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='details')
    apartment_type = models.CharField(max_length=50, blank=True, null=True)
    apartment_name = models.CharField(max_length=100, blank=True, null=True)
    bhk_type = models.CharField(max_length=10, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    total_floor = models.IntegerField(blank=True, null=True)
    property_age = models.CharField(max_length=20, blank=True, null=True)
    facing = models.CharField(max_length=20, blank=True, null=True)
    built_up_area = models.FloatField(blank=True, null=True)

class LocalityDetails(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='locality')
    locality = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)

class RentalDetails(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='rental')
    rental_type = models.CharField(max_length=10, choices=[('Rent', 'Only Rent'), ('Lease', 'Only Lease')])
    expected_rent = models.FloatField(blank=True, null=True)
    expected_lease_amount = models.FloatField(blank=True, null=True)
    expected_deposit = models.FloatField(blank=True, null=True)
    monthly_maintenance = models.CharField(max_length=20, blank=True, null=True)
    available_from = models.DateField(blank=True, null=True)
    preferred_tenants = models.CharField(max_length=50, blank=True, null=True)
    furnishing = models.CharField(max_length=20, blank=True, null=True)
    parking = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Amenities(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='amenities')
    bathrooms = models.IntegerField(blank=True, null=True)
    balcony = models.BooleanField(default=False)
    water_supply = models.CharField(max_length=20, blank=True, null=True)
    gym = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    gated_security = models.BooleanField(default=False)
    show_property_by = models.CharField(max_length=50, blank=True, null=True)
    secondary_number = models.CharField(max_length=15, blank=True, null=True)
    similar_units_available = models.BooleanField(default=False)
    directions_tip = models.TextField(blank=True, null=True)

class Gallery(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='gallery')
    gallery_images = models.JSONField(blank=True, null=True)

