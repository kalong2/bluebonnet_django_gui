# Generated by Django 3.2.15 on 2023-03-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0055_auto_20230307_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='rsid',
            field=models.CharField(default='tmp', editable=False, max_length=50),
            preserve_default=False,
        ),
    ]