# Generated by Django 2.0.6 on 2018-06-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0004_detail_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=10),
            preserve_default=False,
        ),
    ]