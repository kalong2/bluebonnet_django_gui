# Generated by Django 4.1 on 2022-08-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0005_alter_query_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
