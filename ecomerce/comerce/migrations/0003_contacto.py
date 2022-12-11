# Generated by Django 4.1 on 2022-12-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comerce', '0002_productos_baja_ventas_baja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('email', models.EmailField(default=None, max_length=100, null=True, verbose_name='email')),
                ('dni', models.BigIntegerField(verbose_name='dni')),
                ('texto', models.TextField(max_length=100, verbose_name='texto')),
            ],
        ),
    ]
