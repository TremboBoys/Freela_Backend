# Generated by Django 5.1.3 on 2024-11-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ads_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='image',
        ),
    ]