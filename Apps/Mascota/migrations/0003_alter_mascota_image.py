# Generated by Django 4.1 on 2022-08-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascota', '0002_mascota_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='image',
            field=models.ImageField(blank=True, upload_to='mascota_image/'),
        ),
    ]
