from django.db import models
from django.db.models import CASCADE

from apps.users.models import User


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="contacts")

    def __str__(self):
        return self.name
