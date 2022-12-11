from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Categorias(models.Model):
    nombre_categoria = models.CharField(
        max_length=100, verbose_name='Nombre_Categoria')
    descripcion_categoria = models.CharField(
        max_length=200, verbose_name='Descripcion_Categoria')

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    apellido = models.CharField(max_length=100, verbose_name='apellido')
    email = models.EmailField(max_length=100, verbose_name='email', null=True, default=None)
    dni = models.BigIntegerField(verbose_name='dni')
    texto = models.TextField(max_length=100, verbose_name='texto')

class Productos(models.Model):
    nombre_producto = models.CharField(
        max_length=200, verbose_name='Nombre_Producto')
    precio = models.FloatField(verbose_name='Precio')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='Stock', default=0)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    baja = models.BooleanField(verbose_name='Baja',
                               blank=False, null=False, default=False)


class Ventas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name='Fecha')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        verbose_name='Cantidad',  blank=False, null=False)
    monto = models.FloatField(verbose_name='Monto',
                              blank=False, null=False)
    baja = models.BooleanField(verbose_name='Baja',
                               blank=False, null=False, default=False)

    def set_amount(self):
        if self.producto.stock > self.cantidad:
            self.monto = self.producto.precio * self.cantidad

    def sell(self):
        if self.producto.stock >= self.cantidad:
            print("Stock antes: ", self.producto.stock)
            self.producto.stock -= self.cantidad
            self.producto.save()
            print("Stock después: ", self.producto.stock)
            return True
        return False
