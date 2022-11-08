# Generated by Django 4.1.3 on 2022-11-08 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100, verbose_name='Nombre_Categoria')),
                ('descripcion_categoria', models.CharField(max_length=200, verbose_name='Descripcion_Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_permiso', models.CharField(max_length=100, verbose_name='Nombre_Permiso')),
                ('descripcion_categoria', models.CharField(max_length=200, verbose_name='Descripcion_Permisos')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100, verbose_name='Nombre_Producto')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comerce.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre_Usuario')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido_Usuario')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('contrasena', models.CharField(max_length=100, verbose_name='Contrasena')),
                ('permiso', models.ManyToManyField(to='comerce.permisos')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('monto', models.FloatField(verbose_name='Monto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comerce.productos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comerce.usuarios')),
            ],
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
