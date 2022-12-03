from django.db import models 

# from django import forms

Type=(('hospital','HOSPITAL'),
    ('pharmacy','PHARMACY'),
    ('insurance company','INSURANCE COMPANY' ),)
UType=(('Adhaar','ADHAAR'),
    ('Driving license','DRIVING LICENSE'),
    ('Voterid','VOTERID' ),)




# Create your models here.
#patient, hospital, pharmacy, professional

class Patient(models.Model):
    Name=models.CharField(max_length=150, blank=True, null=True)
    # id=models.CharField(max_length=10).primary_key=True
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=150,primary_key=True)
    Password=models.CharField(max_length=120)
    ConfirmPassword=models.CharField(max_length=120)
    Phone=models.CharField(max_length=10)
    City=models.CharField(max_length=120)
    PatientidType=models.CharField(max_length=20,choices=UType,default='Aadhar',null=True)
    Patientid=models.FileField()
    Verified=models.BooleanField(default="False")
    def __str__(self):
        return str(self.Name)

class Professional(models.Model):
    Name=models.CharField(max_length=120, null=True)
    Address=models.CharField(max_length=200)
    # Username=models.CharField(max_length=200,primary_key=True)
    Email=models.EmailField(max_length=150,primary_key=True)
    Password=models.CharField(max_length=120)
    ConfirmPassword=models.CharField(max_length=120)
    Phone=models.CharField(max_length=10, null=True)
    Role=models.CharField(max_length=120)
    Hospital_Name=models.CharField(max_length=120)
    City=models.CharField(max_length=120)
    Professionalid=models.ImageField()
    Verified=models.BooleanField(default="False")

class Organisation(models.Model):
    Name=models.CharField(max_length=120)
    # Username=models.CharField(max_length=200,primary_key=True)
    Address=models.CharField(max_length=150)
    Email=models.EmailField(max_length=150,primary_key=True)
    Phone=models.CharField(max_length=10, null=True)
    Password=models.CharField(max_length=120)
    ConfirmPassword=models.CharField(max_length=120)
    Organisationlisence=models.ImageField()
    OrganisationType=models.CharField(max_length=20,choices=Type,default='hospital')
    City=models.CharField(max_length=120)
    Verified=models.BooleanField(default="False")

class Docsrequest(models.Model): #pharmacy
    Name=models.CharField(max_length=120)
    OrganisationName=models.CharField(max_length=120)
    Hospitalname=models.CharField(max_length=120)
    OrganisationType=models.CharField(max_length=20,choices=Type,default='hospital')
    DocsType=models.CharField(max_length=15)
    Docs=models.FileField()
    
patient=models.ForeignKey(Patient,on_delete=models.CASCADE, null=True)

class Patientpharm(models.model):
    Yourname=models.CharField(max_length=120)
    Youremail=models.CharField(max_length=100)
    Pharmacyemail=models.CharField(max_length=120)
    Reporttitle=models.CharField(max_length=120)
    Document=models.FileField()

class Pharmpatient(models.Model):
    Pharmacyname=models.CharField(max_length=120)
    Patientemail=models.CharField(max_length=120)
    Bill=models.CharField()
    Slip=models.FileField()






