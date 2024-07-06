from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
