from django.contrib import admin
from .models import Workers, Position

# Register your models here.
admin.site.register(Workers)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}