# Generated by Django 5.1.3 on 2024-11-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_perfil_is_pro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='photo',
        ),
    ]
