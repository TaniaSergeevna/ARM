from django.db import models

# Create your models here.


class Workers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    worksNumber = models.IntegerField()

    def __str__(self):
        return self.surname

