# Generated by Django 4.1 on 2022-08-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0019_alter_query_query_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='query',
            name='query_id',
            field=models.PositiveIntegerField(),
        ),
    ]
