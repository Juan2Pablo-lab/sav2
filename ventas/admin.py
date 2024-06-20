from django.contrib import admin
from ventas.models import Cliente, Producto, Compra, detalleCompra, Categoria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Categoria)
admin.site.register(detalleCompra)