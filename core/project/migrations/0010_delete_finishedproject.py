# Generated by Django 5.1.1 on 2024-09-19 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_remove_project_pending_project_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FinishedProject',
        ),
    ]
