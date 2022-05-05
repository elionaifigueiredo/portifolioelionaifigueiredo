from django.contrib import admin

# Register your models here.

from app01.models import Carro


@admin.register(Carro)
class AdminCarro(admin.ModelAdmin):
    list_display = ['nome']
