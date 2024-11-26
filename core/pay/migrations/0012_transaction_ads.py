# Generated by Django 5.1.3 on 2024-11-26 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ads_is_paid'),
        ('pay', '0011_transaction_method_transaction_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='ads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ads'),
        ),
    ]
