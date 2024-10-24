# Generated by Django 5.1.1 on 2024-10-09 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ads_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ads.adscategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='target_audience',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]