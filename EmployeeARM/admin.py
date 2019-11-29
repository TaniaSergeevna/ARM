from django.contrib import admin
from .models import HallWorkers, KitchenWorkers, Administrator

# Register your models here.
admin.site.register(HallWorkers)
admin.site.register(KitchenWorkers)
admin.site.register(Administrator)