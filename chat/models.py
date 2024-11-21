from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.CharField(max_length=100)  # E.g., username or user ID
    message = models.TextField(blank=True)     # Optional text message
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  # File attachment
    timestamp = models.DateTimeField(auto_now_add=True)  # Message timestamp

    def __str__(self):
        return f"{self.sender} - {self.timestamp}"
