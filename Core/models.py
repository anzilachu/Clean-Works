from django.db import models
from U_Auth.models import User


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Status = models.IntegerField(default=1)
    number = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
