# Generated by Django 5.1.3 on 2024-11-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_contractservice_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractservice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]