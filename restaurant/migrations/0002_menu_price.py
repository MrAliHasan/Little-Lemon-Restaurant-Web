# Generated by Django 4.1.7 on 2023-03-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
