# Generated by Django 4.1.3 on 2022-12-02 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=200, verbose_name='Nombre_Producto')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comerce.categorias')),
            ],
        ),
    ]