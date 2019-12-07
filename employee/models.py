from django.db import models


# Create your models here.


class Workers(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    Position = (
        ('Работники зала', 'Работники зала'),
        ('Работники кухни', 'Работники кухни'),
        ('Управляющий персонал', 'Управляющий персонал'),
    )
    position = models.CharField(max_length=50,
                                choices=Position)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.surname
