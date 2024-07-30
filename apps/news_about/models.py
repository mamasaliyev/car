from django.db import models

from apps.shared.models import AbstractBaseModel
from phone_field import PhoneField


class News(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.title


class About(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title
