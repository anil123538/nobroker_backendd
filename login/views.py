from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_otp.oath import TOTP
from django_otp.util import random_hex
from .models import User
from .serializers import PhoneSerializer, OTPSerializer, UserDetailsSerializer

# Mock function to send OTP (replace with actual SMS service)
def send_otp(phone_number, otp_code):
    # Replace this with your SMS API integration
    print(f"Sending OTP {otp_code} to {phone_number}")

class SendOTPView(APIView):
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp_code = random_hex(3)  # Generate a 6-digit OTP
            user, created = User.objects.get_or_create(phone_number=phone_number)
            user.otp_code = otp_code
            user.is_verified = False
            user.save()
            send_otp(phone_number, otp_code)
            return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp_code = serializer.validated_data['otp_code']
            try:
                user = User.objects.get(phone_number=phone_number)
                if user.otp_code == otp_code:
                    user.is_verified = True
                    user.save()
                    return Response({"message": "OTP verified successfully."}, status=status.HTTP_200_OK)
                return Response({"message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsView(APIView):
    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            try:
                user = User.objects.get(phone_number=phone_number, is_verified=True)
                user.name = serializer.validated_data['name']
                user.email = serializer.validated_data['email']
                user.save()
                return Response({"message": "User details saved successfully."}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"message": "User not verified."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)