# Generated by Django 4.1 on 2022-08-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Refugio', '0007_alter_refugio_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugio',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='refugio',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]