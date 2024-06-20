from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    identificador = models.CharField(max_length=50, default='ANOTHER')
    descripcion = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, unique=True, max_length=8)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre}'

class Compra(models.Model):
    numero_compra = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    cantidad = models.IntegerField(default=1)
    def __str__(self):
        return f'Compra {self.numero_compra}: {self.cliente}'


class detalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=6, default=1)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return f'Detalle {self.id}'