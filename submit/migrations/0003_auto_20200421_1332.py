# Generated by Django 3.0.4 on 2020-04-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0002_rides_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='driSmokes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rides',
            name='riderLugg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rides',
            name='riderPets',
            field=models.BooleanField(default=False),
        ),
    ]
