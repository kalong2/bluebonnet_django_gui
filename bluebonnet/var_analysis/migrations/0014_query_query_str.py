# Generated by Django 4.1 on 2022-08-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0013_query_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='query_str',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
