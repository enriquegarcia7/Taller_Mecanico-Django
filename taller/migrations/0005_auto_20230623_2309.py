# Generated by Django 3.2.19 on 2023-06-24 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0004_trabajo_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajo',
            name='email_cliente',
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='nombre_cliente',
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='telefono_cliente',
        ),
    ]
