# Generated by Django 2.1.2 on 2018-11-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0003_voters_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters_profile',
            name='type',
            field=models.CharField(choices=[(0, 'Organiser'), (1, 'Voter')], default=1, max_length=1),
        ),
    ]
