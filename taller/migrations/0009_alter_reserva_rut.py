# Generated by Django 3.2.19 on 2023-06-24 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0008_alter_reserva_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='rut',
            field=models.CharField(max_length=10),
        ),
    ]