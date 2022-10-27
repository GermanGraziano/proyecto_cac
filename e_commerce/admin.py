from django.contrib import admin
'''
from .models import Marca, Producto
from .form import ContactoForm
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"] #para que el campo sea editable desde el admin
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo", "precio"] #filtros por marca, nuevo
    list_per_page = 5

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.sit.register(ContactoForm)
'''
