from django.shortcuts import get_object_or_404, render, redirect
from ventas.forms import CompraForm, ProductoForm, CategoriaForm, ProductoFormEdit, ClienteForm, detalleVentaForm
from ventas.models import Cliente, Compra, Producto, Categoria, detalleCompra
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required
def verProductos(request):
    buscar = request.GET.get('buscar')
    resultados = Producto.objects.all()
    if buscar:
        resultados = Producto.objects.filter(nombre__contains=buscar)
        return render(request, 'productos/ver.html', {'resultados': resultados})
    else:
        return render(request, 'productos/ver.html', {'resultados': resultados})

@login_required
def verProductoscategoria(request, id):
    productos = Producto.objects.filter(categoria_id = id)
    categoria = get_object_or_404(Categoria, pk=id)
    return render(request, 'productos/ver_por_categoria.html', {'productos': productos, 'categoria': categoria})

@login_required
def verProductosCodigo(request):
    buscar = request.GET.get('buscar_codigo')
    resultados = Producto.objects.all()
    if buscar:
        resultados = Producto.objects.filter(codigo__contains=buscar)
        return render(request, 'productos/ver.html', {'resultados': resultados})
    else:
        return render(request, 'productos/ver.html', {'resultados': resultados})

@login_required
def agregarProducto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar.html', {'form': form, 'categorias': categorias})

@login_required
def editarProducto(request,id):
    producto = get_object_or_404(Producto, pk=id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProductoFormEdit(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoFormEdit(instance=producto)
    return render(request, 'productos/editar.html', {'form': form, 'producto': producto, 'categorias':categorias})

@login_required
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if producto:
        producto.delete()
        return redirect('productos')

@login_required
def verCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/ver.html', {'categorias': categorias})

@login_required
def agregarCategoria(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/agregar.html', {'form': form, 'categorias': categorias})

@login_required
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar.html', {'form': form, 'categoria': categoria})

@login_required
def eliminarCategoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if categoria:
        categoria.delete()
        return redirect('categorias')

@login_required
def venta(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.cliente = cliente
            nuevo.total = '0.00'
            nuevo.save()
            return redirect('categorias')
    else:
        form = CompraForm()
    return render(request, 'ventas/nuevo.html', {'form': form, 'cliente': cliente})

@login_required
def buscarCliente(request):
    clientes = Cliente.objects.all()
    buscar = request.GET.get('buscar')
    if buscar:
        clientes = Cliente.objects.filter(dni=buscar)
        return render(request, 'ventas/venta.html', {'clientes': clientes})
    else:
        return render(request, 'ventas/venta.html', {'clientes': clientes})

@login_required
def nuevoCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form = ClienteForm()
    return render(request, 'ventas/venta.html', {'form': 'form'})



@login_required
def detalleVenta(request, id):
    producto = get_object_or_404(Producto, pk=id)
    compras = Compra.objects.all()
    if request.method == 'POST':
        form = detalleVentaForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.producto = producto
            nuevo.subtotal = producto.precio
            nuevo.save()
            return redirect('categorias')
    else:
        form = detalleVentaForm()
    return render(request, 'ventas/detalle_venta.html', {'form': form, 'producto': producto, 'compras': compras})

@login_required
def verHistorialCompras(request):
    compras = Compra.objects.all()
    return render(request, 'ventas/ver.html', {'compras': compras})

def verHistoriaDetalle(request, id):
    detalles = detalleCompra.objects.filter(compra=id)
    return render(request, 'ventas/ver_detalle.html', {'detalles': detalles})
