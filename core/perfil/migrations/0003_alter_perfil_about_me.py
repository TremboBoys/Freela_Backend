# Generated by Django 5.1.3 on 2024-11-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='about_me',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
