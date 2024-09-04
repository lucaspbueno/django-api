from django.contrib import admin
from .models import Equipment
# Register your models here.


@admin.register(Equipment)
class EquipmentAmin(admin.ModelAdmin):
    ...