from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


# class Permisos(models.Model):
#    nombre_permiso = models.CharField(
#        max_length=100, verbose_name='Nombre_Permiso')
#    descripcion_categoria = models.CharField(
#        max_length=200, verbose_name='Descripcion_Permisos')


# class Usuarios(models.Model):
#    nombre = models.CharField(max_length=100, verbose_name='Nombre_Usuario')
#    apellido = models.CharField(
#        max_length = 100, verbose_name = 'Apellido_Usuario')
#    mail = models.CharField(max_length=100, verbose_name='Mail')
#    contrasena = models.CharField(max_length=100, verbose_name='Contrasena')
#    permiso = models.ManyToManyField(Permisos)

class Categorias(models.Model):
    nombre_categoria = models.CharField(
        max_length=100, verbose_name='Nombre_Categoria')
    descripcion_categoria = models.CharField(
        max_length=200, verbose_name='Descripcion_Categoria')


class Productos(models.Model):
    nombre_producto = models.CharField(
        max_length=200, verbose_name='Nombre_Producto')
    precio = models.FloatField(verbose_name='Precio')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='Stock', default=0)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)


class Ventas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name='Fecha')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        verbose_name='Cantidad',  blank=False, null=False)
    monto = models.FloatField(verbose_name='Monto',
                              blank=False, null=False)

    def set_amount(self):
        if self.producto.stock > self.cantidad:
            self.monto = self.producto.precio * self.cantidad

    def sell(self):
        self.producto.stock -= self.cantidad
