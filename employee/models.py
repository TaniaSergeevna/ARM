from django.db import models


class Position(models.Model):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Slug', max_length=50)

    def __str__(self):
        return self.name 


class Workers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='workers', blank=True, null=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.surname
