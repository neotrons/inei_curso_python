from django.contrib import admin
from .models import Categoria, Item


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'price', 'unidad_medida')
    list_filter = ('unidad_medida', )
    list_editable = ('price', )
