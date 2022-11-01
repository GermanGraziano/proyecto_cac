from django.contrib import admin
from .models import Categoria, Producto
#from .forms import ContactoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria"]
    list_editable = ["precio"] #para que el campo sea editable desde el admin
    search_fields = ["nombre"]
    list_filter = ["categoria", "precio"] #filtros por marca, nuevo
    #list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Producto) #, ProductoAdmin)
#admin.site.register(ContactoForm)
