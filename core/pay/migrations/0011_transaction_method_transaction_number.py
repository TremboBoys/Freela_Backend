# Generated by Django 5.1.3 on 2024-11-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0010_address_cpf_transaction_accept_proposal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='number',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
