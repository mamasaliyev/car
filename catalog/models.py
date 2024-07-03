from django.db import models


class Logo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    km = models.IntegerField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=20)
    color = models.CharField(max_length=50)
    order = models.IntegerField()
    image = models.ImageField(upload_to='image/')
    logo = models.ImageField(upload_to='logos/')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contract(models.Model):
     month = models.FloatField()
     year = models.FloatField()
     create = models.DateTimeField(auto_now=True)
     update = models.DateTimeField(auto_now=True)



