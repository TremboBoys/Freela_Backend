# Generated by Django 5.1.3 on 2024-11-06 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='uploader.image'),
        ),
    ]
