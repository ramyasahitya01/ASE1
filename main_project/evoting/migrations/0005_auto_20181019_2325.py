# Generated by Django 2.1.2 on 2018-10-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0004_auto_20181019_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votersdet',
            name='voterId',
        ),
        migrations.DeleteModel(
            name='VotersDet',
        ),
        migrations.DeleteModel(
            name='Voterslog',
        ),
    ]
