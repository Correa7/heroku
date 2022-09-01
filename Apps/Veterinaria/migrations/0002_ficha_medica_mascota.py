# Generated by Django 4.1 on 2022-08-20 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mascota', '0003_alter_mascota_image'),
        ('Veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_medica',
            name='mascota',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='veterinaria', to='Mascota.mascota'),
        ),
    ]
