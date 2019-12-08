from django.contrib import admin

# Register your models here.
from menu.models import Menu, Sections

admin.site.register(Menu)


@admin.register(Sections)
class Section_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
