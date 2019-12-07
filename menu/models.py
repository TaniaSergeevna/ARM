from django.db import models


class Menu(models.Model):
    MENU_SECTION = (('Закуски', 'Закуски'),
                    ('Салаты', 'Салаты'),
                    ('Гарниры', 'Гарниры'),
                    ('Мясо', 'Мясо'),
                    ('Десерты', 'Десерты'),
                    ('Напитки', 'Напитки'),
                    ('Алкоголь', 'Алкоголь'),
                    )
    name = models.CharField(max_length=100)
    menu_section = models.CharField(max_length=100, choices=MENU_SECTION)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
