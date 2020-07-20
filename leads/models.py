from django.core.validators import EmailValidator
from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, validators=[EmailValidator], blank=False)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.name, self.phone_number, self.email, self.message)

