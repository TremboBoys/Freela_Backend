# Generated by Django 5.1.1 on 2024-09-10 17:46

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_hability_myhability_myproject_perfil'),
        ('project', '0002_project_crontractor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myhability',
            name='user',
        ),
        migrations.AddField(
            model_name='myhability',
            name='perfil',
            field=models.ForeignKey(default=builtins.print, on_delete=django.db.models.deletion.PROTECT, to='perfil.perfil'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myproject',
            name='perfil',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='perfil.perfil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project'),
        ),
        migrations.AlterField(
            model_name='myproject',
            name='term',
            field=models.DateField(),
        ),
    ]