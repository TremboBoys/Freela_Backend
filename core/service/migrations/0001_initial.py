# Generated by Django 5.1.1 on 2024-10-05 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.IntegerField(choices=[(1, 'Free'), (2, 'Month'), (3, 'Year')], default=1, verbose_name='Services')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.perfil')),
            ],
        ),
    ]
