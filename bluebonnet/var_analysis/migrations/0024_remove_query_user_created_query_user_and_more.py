# Generated by Django 4.1 on 2022-08-11 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('var_analysis', '0023_alter_query_user_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='user_created',
        ),
        migrations.AddField(
            model_name='query',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='query',
            name='user_updated',
            field=models.CharField(editable=False, max_length=25),
        ),
    ]
