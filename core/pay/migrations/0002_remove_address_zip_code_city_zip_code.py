# Generated by Django 5.1.3 on 2024-11-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='city',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
