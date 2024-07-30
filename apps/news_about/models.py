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

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class About(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
