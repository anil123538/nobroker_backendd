from django.urls import path
from .views import ChatView

urlpatterns = [
    path('api/chat/', ChatView.as_view(), name='chat'),
]

#GET request to /api/chat/ to fetch all messages.
#POST request to /api/chat/ with message, sender, and optional file to send a new message.

