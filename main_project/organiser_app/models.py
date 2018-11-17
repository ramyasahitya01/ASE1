from django.db import models

# Create your models here.

election_options=(
    ('P','Parliamentary'),
    ('A','Assembly')

)

statuses=(

    (0,'not started'),
    (1,'on going'),
    (2,'end')

)


Gender_options = (

    ('M','Male'),
    ('F','Female'),
    ('O','Others')
)

party_options={

    ('BJP','Bhartiya Janta Party'),
    ('CPI','Communist Party of India'),
    ('INC','Indian National Congress'),
    ('AAP','Aam Aadmi Party') ,
    ('TDP','Telugu Desam Party'),
    ('SS','Shiv Sena') ,
    ('TRS','Telangana Rashtra Samithi'),
    ('JD','Janata Dal') ,
    ('SP','Samajwadi Party') ,
   ('RJD', 'Rashtriya Janata Dal')

}

region_options=(

 ('0','AndhraPradesh') ,
 ('1','Bihar') ,
 ('2','karnataka'),
 ('3','Tamilnadu' ),
 ('4','Kerela') ,
 ('5','UttarPradesh'),
 ('6','WestBengal') ,
 ('7','MadhyaPradesh') ,
 ('8','Haryana') ,
 ('9','Assam')

)



class Election(models.Model):
    election_type=models.CharField(choices=election_options,null=False,max_length=1)
    election_id=models.CharField(unique=True,max_length=10,primary_key=True,null=False)
    election_year=models.IntegerField(null=False)
    date_of_start=models.DateField(null=False)
    date_of_end=models.DateField(null=False)
    status=models.CharField(choices=statuses,max_length=1)


class Voter(models.Model):
    voter_id=models.CharField(max_length=10,unique=True,primary_key=True,null=False)
    voter_name=models.CharField(max_length=50,null=False)
    voter_email=models.EmailField(unique=True,null=False)
    voter_dob=models.DateField(null=False)
    voter_age=models.IntegerField(null=False)
    voter_aadhar=models.BigIntegerField(unique=True,null=False)
    voter_phone=models.BigIntegerField(unique=True,null=False)
    isalive=models.BooleanField(default=True,null=False)
    voter_gender=models.CharField(choices=Gender_options,null=False,max_length=10)
    voter_region=models.CharField(choices=region_options,null=False,max_length=10)


class Candidate(models.Model):
    candidate_id=models.CharField(max_length=10,unique=True,primary_key=True,null=False)
    candidate_name=models.CharField(max_length=50,null=False)
    candidate_fname=models.CharField(max_length=50,null=False)
    candidate_party=models.CharField(choices=party_options,null=False,max_length=10)
    candidate_region=models.CharField(choices=region_options,null=False,max_length=10)
    candidate_gender=models.CharField(choices=Gender_options,null=False,max_length=1)
    candidate_email=models.EmailField(unique=True,null=False)
    candidate_dob=models.DateField(null=False)
    candidate_aadhar=models.BigIntegerField(unique=True,null=False)

class Candidate_election(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    election=models.ForeignKey(Election,on_delete=models.CASCADE)

class Election_region(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    region=models.CharField(choices=region_options,null=False,max_length=10)


class Vote_count(models.Model):
    voter=models.ForeignKey(Voter,on_delete=models.CASCADE)
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
