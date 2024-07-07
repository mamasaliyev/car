from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField

from apps.shared.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    phone = PhoneField(blank=True, help_text='Contact phone number')
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default-user-avatar.jpg")
    birth_date = models.DateField(null=True, blank=True)
