# Generated by Django 2.0.5 on 2018-09-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0002_auto_20180914_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote_total',
            field=models.SmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote_total',
            field=models.SmallIntegerField(blank=True, default=1),
        ),
    ]
