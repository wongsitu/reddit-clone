# Generated by Django 2.0.5 on 2018-09-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0011_auto_20180916_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote_total',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote_total',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
