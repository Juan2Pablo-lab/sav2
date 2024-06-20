from django.forms import EmailInput, ModelForm, TextInput
from ventas.models import Producto, Categoria, Compra, Cliente, detalleCompra

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoFormEdit(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'precio', 'categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'cantidad']
        widgets = {
            'cliente': TextInput(attrs={'type': 'number'})
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'dni': TextInput(attrs={'type': 'number'}),
            'correo': EmailInput(attrs={'type': 'email'})
        }

class detalleVentaForm(ModelForm):
    class Meta:
        model = detalleCompra
        fields = ['compra', 'descripcion']