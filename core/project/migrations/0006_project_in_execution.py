# Generated by Django 5.1.1 on 2024-09-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_contractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='in_execution',
            field=models.BooleanField(default=False),
        ),
    ]
