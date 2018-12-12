# Generated by Django 2.0.5 on 2018-12-12 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('candidate_name', models.CharField(max_length=50)),
                ('candidate_fname', models.CharField(max_length=50)),
                ('candidate_party', models.CharField(choices=[('BJP', 'Bhartiya Janta Party'), ('CPI', 'Communist Party of India'), ('INC', 'Indian National Congress'), ('AAP', 'Aam Aadmi Party'), ('TDP', 'Telugu Desam Party'), ('SS', 'Shiv Sena'), ('TRS', 'Telangana Rashtra Samithi'), ('JD', 'Janata Dal'), ('SP', 'Samajwadi Party'), ('RJD', 'Rashtriya Janata Dal')], default='Bhartiya Janta Party', max_length=10)),
                ('candidate_region', models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], default='AndhraPradesh', max_length=10)),
                ('candidate_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='Male', max_length=1)),
                ('candidate_email', models.EmailField(max_length=254, unique=True)),
                ('candidate_dob', models.DateField()),
                ('candidate_aadhar', models.BigIntegerField(unique=True)),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate_election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_type', models.CharField(choices=[('A', 'Assembly'), ('P', 'Parliamentary')], default='Parliamentary', max_length=1)),
                ('election_id', models.AutoField(primary_key=True, serialize=False)),
                ('election_year', models.CharField(choices=[('2018', '2018'), ('2019 ', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028')], default=2018, max_length=6)),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('status', models.CharField(choices=[('0', 'not started'), ('1', 'on going'), ('2', 'end')], default='0', max_length=2)),
                ('candidates', models.ManyToManyField(to='organiser_app.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Election_region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Election')),
            ],
        ),
        migrations.CreateModel(
            name='Vote_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Election')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('voter_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('voter_name', models.CharField(max_length=50)),
                ('voter_email', models.EmailField(max_length=254, unique=True)),
                ('voter_dob', models.DateField()),
                ('voter_age', models.IntegerField()),
                ('voter_aadhar', models.BigIntegerField(unique=True)),
                ('voter_phone', models.BigIntegerField(unique=True)),
                ('isalive', models.BooleanField(default=True)),
                ('voter_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10)),
                ('voter_region', models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='vote_count',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Voter'),
        ),
        migrations.AddField(
            model_name='candidate_election',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organiser_app.Election'),
        ),
    ]
