# Generated by Django 5.1.1 on 2024-10-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ads_ads_category_ads_target_audience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Potas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arroz', models.CharField(max_length=255)),
            ],
        ),
    ]