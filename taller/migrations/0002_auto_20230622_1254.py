# Generated by Django 3.2.19 on 2023-06-22 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Rut',
            field=models.CharField(max_length=50),
        ),
    ]
