# Generated by Django 5.1.3 on 2024-11-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_remove_perfil_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='access_token_mercado_pago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='collector_id_mercado_pago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='expiration_date_access_token_mercado_pago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='expiration_date_refresh_token_mercado_pago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='refresh_token_mercado_pago',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]