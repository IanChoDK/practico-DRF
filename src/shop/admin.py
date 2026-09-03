from django.contrib import admin
from .models import Ropa, Categoria, Color, Proveedor, Talle

# Register your models here.
admin.site.register(Ropa)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Proveedor)
admin.site.register(Talle)