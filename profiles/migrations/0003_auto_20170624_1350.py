# Generated by Django 2.0.dev20170607153035 on 2017-06-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170613_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requester',
            name='department',
            field=models.CharField(max_length=200),
        ),
    ]
