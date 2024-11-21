from rest_framework import serializers
from .models import User

class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class OTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp_code = serializers.CharField()

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'name', 'email']