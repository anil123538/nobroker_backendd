from django.urls import path
from .views import SendOTPView, VerifyOTPView, UserDetailsView

urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('user-details/', UserDetailsView.as_view(), name='user_details'),
]

#get/api/auth/send-otp/
#post/api/auth/verify-otp/
#post/api/auth/user-details/