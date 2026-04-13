from django.contrib import admin
from .models import Ingrediente, Plato, Receta, Venta

# Esto permite editar la receta dentro de la página del Plato
class RecetaInline(admin.TabularInline):
    model = Receta
    extra = 1 # Te muestra una fila vacía para añadir un ingrediente nuevo

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_venta', 'categoria')
    inlines = [RecetaInline]

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad_de_medida', 'precio_costo_unitario')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('plato', 'cantidad_vendida', 'fecha_venta')
    list_filter = ('fecha_venta', 'plato') # Filtros laterales útiles