# Generated by Django 3.2.15 on 2022-10-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0030_evidence_active_sites_evidence_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='active_sites',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='additional_info',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]