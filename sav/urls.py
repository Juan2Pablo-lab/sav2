"""
URL configuration for sav project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido, Registro, IniciarSesion, CerrarSesion
from ventas.views import verProductos, agregarProducto, verProductosCodigo, verCategoria, agregarCategoria, editarCategoria, verProductoscategoria, editarProducto, eliminarProducto, eliminarCategoria, venta, nuevoCliente, detalleVenta, buscarCliente, verHistorialCompras, verHistoriaDetalle

urlpatterns = [
    path("admin/", admin.site.urls),
    path("categorias/", verCategoria, name='categorias'),
    path("categorias/<int:id>", editarCategoria, name='editar_categoria'),
    path("categorias/<int:id>/ver_productos/", verProductoscategoria, name='ver_productos'),
    path("categorias/<int:id>/eliminar/", eliminarCategoria, name='eliminar_categoria'),
    path("nueva_categoria/", agregarCategoria, name='nueva_categoria'),
    path("productos/", verProductos, name='productos'),
    path("productos/<id>", editarProducto, name='editar_producto'),
    path("productos/<id>/eliminar/", eliminarProducto, name='eliminar_producto'),
    path("buscarCodigo/", verProductosCodigo, name='buscar_codigo'),
    path("nuevo_producto/", agregarProducto, name='nuevo_producto'),
    path("ver_historial/", verHistorialCompras, name='ver_historial'),
    path("ver_historial/<int:id>", verHistoriaDetalle, name='ver_historial_detalle'),
    path("detalle_venta/<id>", detalleVenta, name='detalle_venta'),
    path("cliente/", nuevoCliente, name='cliente'),
    path("buscar_cliente/", buscarCliente, name='buscar_cliente'),
    path("cliente/<int:id>", venta, name='venta'),
    path("", IniciarSesion, name='iniciar_sesion'),
    path("cerrar_sesion/", CerrarSesion, name='cerrar_sesion'),
    path("registrarse/", Registro, name='registro'),
]
