# Generated by Django 2.0.2 on 2018-11-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='old_url',
            field=models.CharField(max_length=2000, unique=True),
        ),
    ]
