# Generated by Django 3.2.22 on 2023-10-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0012_agenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cod', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=100)),
                ('Costo', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Agenda',
        ),
    ]
