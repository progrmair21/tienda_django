from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'creado_en')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('creado_en',)
    ordering = ('-creado_en',)
    readonly_fields = ('creado_en',)