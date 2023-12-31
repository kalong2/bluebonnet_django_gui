# Generated by Django 3.2.15 on 2022-10-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('var_analysis', '0033_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='active_sites_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='active_sites_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='active_sites_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='active_sites_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='additional_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='additional_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='additional_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='additional_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='clinvar_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='clinvar_patho_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='clinvar_patho_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='clinvar_patho_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='comp_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='comp_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='comp_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='comp_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dbsnp_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dbsnp_patho_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dbsnp_patho_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dbsnp_patho_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='exac_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='exac_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='exac_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='exac_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='gnomad_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='gnomad_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='gnomad_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='gnomad_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='splice_comment',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='evidence',
            name='splice_evidence_category_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='splice_evidence_category_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='evidence',
            name='splice_evidence_category_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
