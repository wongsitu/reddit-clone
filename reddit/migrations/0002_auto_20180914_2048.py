# Generated by Django 2.0.5 on 2018-09-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote_total',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='site_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote_total',
            field=models.SmallIntegerField(blank=True),
        ),
    ]