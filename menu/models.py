from django.db import models

# class Sections(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100)
#
#     def __str__(self):
#         return self.name

class Menu(models.Model):
    MENU_SECTION = (('Закуски', 'Закуски'),
                    ('Салаты', 'Салаты'),
                    ('Гарниры', 'Гарниры'),
                    ('Мясо', 'Мясо'),
                    ('Десерты', 'Десерты'),
                    ('Напитки', 'Напитки'),
                    ('Алкоголь', 'Алкоголь'),
                    )
    # sections = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='menus', blank=True,
    #                             null=True)
    name = models.CharField(max_length=100)
    menu_section = models.CharField(max_length=100, choices=MENU_SECTION)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

