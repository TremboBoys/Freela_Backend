from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_delete_finishedproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, "It project isn't started"), (2, 'It project is pending'), (3, 'It project is finished')], default=1, verbose_name='Status of the project'),
        ),
    ]
