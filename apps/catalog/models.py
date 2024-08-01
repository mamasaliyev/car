from django.db import models

from apps.shared.models import AbstractBaseModel
from django.db.models import SET_NULL


class Logo(AbstractBaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='logos/')
    object = models.Manager

    def __str__(self):
        return self.title


class Car(AbstractBaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    km = models.IntegerField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=20)
    color = models.CharField(max_length=50)
    order = models.IntegerField()
    image = models.ImageField(upload_to='cars/')
    logo = models.ForeignKey(Logo, on_delete=SET_NULL, null=True)
    objects = models.Manager

    def __str__(self):
        return self.title


class Contract(AbstractBaseModel):
     month = models.FloatField()
     year = models.FloatField()




