from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name
