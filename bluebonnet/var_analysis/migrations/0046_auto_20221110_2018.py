# Generated by Django 3.2.15 on 2022-11-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0045_alter_query_running'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='date_str',
        ),
        migrations.AlterField(
            model_name='query',
            name='date_updated',
            field=models.CharField(default=2001, editable=False, max_length=25),
            preserve_default=False,
        ),
    ]
