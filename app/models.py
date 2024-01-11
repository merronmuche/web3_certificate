from collections.abc import Iterable
from django.db import models

# Create your models here.

from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date_certified = models.DateField(auto_now_add=True)
    certificate = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # open the certificate image using opencv
        # add the name, course and date to the certificate
        return super().save(*args, **kwargs)

