# yourappname/models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.email
    
    