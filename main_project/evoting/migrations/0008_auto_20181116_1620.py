# Generated by Django 2.1.2 on 2018-11-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0007_organizers_database'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters_profile',
            name='activation',
            field=models.CharField(blank=True, default=False, max_length=5),
        ),
    ]
