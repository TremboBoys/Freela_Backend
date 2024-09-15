# Generated by Django 5.1.1 on 2024-09-15 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_integrationtype_remove_project_area_and_more'),
        ('user', '0009_rename_confirmation_token_user_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contractor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='user.user'),
            preserve_default=False,
        ),
    ]