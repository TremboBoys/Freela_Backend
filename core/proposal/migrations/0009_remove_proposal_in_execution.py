# Generated by Django 5.1.1 on 2024-09-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0008_alter_acceptproposal_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='in_execution',
        ),
    ]