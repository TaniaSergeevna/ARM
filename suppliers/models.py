from django.db import models


# Create your models here.
class Supply(models.Model):
    name = models.CharField(max_length=50)
    type_supply = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
