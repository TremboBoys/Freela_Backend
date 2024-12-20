# Generated by Django 5.1.3 on 2024-11-19 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0004_perfil_number_projects_in_execution'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=255)),
                ('complemement', models.CharField(blank=True, max_length=255, null=True)),
                ('neighborhood_name', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.perfil')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.city')),
            ],
        ),
    ]
