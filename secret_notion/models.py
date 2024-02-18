from django.db import models

# Create your models here.
class SecretNotion(models.Model):
    message = models.CharField(max_length=300)
    salt = models.CharField(max_length=30)
    hashed_message = models.TextField()