# Generated by Django 4.1.7 on 2023-03-14 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]