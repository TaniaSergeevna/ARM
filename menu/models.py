from django.db import models


class Menu1(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu2(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu3(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu4(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu5(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu6(models.Model):
    name = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu7(models.Model):
    name = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name