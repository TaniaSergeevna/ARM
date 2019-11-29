from django.db import models

# Create your models here.


class HallWorkers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.surname


class KitchenWorkers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.surname


class Administrator(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.surname