# Generated by Django 2.0.5 on 2018-09-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_auto_20180916_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
