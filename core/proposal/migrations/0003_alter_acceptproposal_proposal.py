# Generated by Django 5.1.1 on 2024-09-17 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_acceptproposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptproposal',
            name='proposal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposal.proposal'),
        ),
    ]