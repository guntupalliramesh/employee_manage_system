# Generated by Django 2.2.4 on 2019-08-07 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20190808_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]