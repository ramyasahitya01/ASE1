# Generated by Django 2.1.2 on 2018-12-12 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0011_report_data_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
