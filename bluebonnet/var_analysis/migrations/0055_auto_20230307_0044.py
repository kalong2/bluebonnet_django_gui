# Generated by Django 3.2.15 on 2023-03-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0054_auto_20230127_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='exac',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='exac_comment',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='exac_evidence_category_1',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='exac_evidence_category_2',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='exac_evidence_category_3',
        ),
    ]
