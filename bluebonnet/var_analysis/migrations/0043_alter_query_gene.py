# Generated by Django 3.2.15 on 2022-11-08 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0042_gene_condition_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='var_analysis.gene'),
        ),
    ]
