# Generated by Django 2.0.dev20170607153035 on 2017-06-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requester',
            name='field',
            field=models.CharField(max_length=200),
        ),
    ]