# Generated by Django 4.1 on 2022-08-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0011_remove_query_date_query_date_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
