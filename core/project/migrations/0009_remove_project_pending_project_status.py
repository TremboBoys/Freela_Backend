# Generated by Django 5.1.1 on 2024-09-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_remove_project_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pending',
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, "It project isn't started"), (2, 'It project is pending'), (3, 'It project is pending')], default=1, verbose_name='Status of the project'),
        ),
    ]
