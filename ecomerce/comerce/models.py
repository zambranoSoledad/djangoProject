from django.db import models

# Create your models here.

class Venta(models.Model):
    usuario = models.CharField(max_length=100, verbose_name='Usuario')
    fecha = models.DateField(verbose_name='Fecha')
    producto = models.CharField(max_length=100, verbose_name='Usuario')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    monto = models.FloatField(verbose_name='Monto')