from distutils.command.upload import upload
from email.headerregistry import Address
from re import M
from django.db import models
from datetime import datetime

# Doctor Tabel.
class Doctor(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d' )
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Address = models.CharField(max_length=60)
    SSN = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()
    #gender
    GENDER_CHOICES = (
          ('M', 'Male'),
          ('F', 'Female'),
    )

    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=M)

    def __str__(self):
        return self.Fname
  
# Nurse Tabel.
class Nurse(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d' )
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Address = models.CharField(max_length=60)
    SSN = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()
    #gender
    GENDER_CHOICES = (
          ('M', 'Male'),
          ('F', 'Female'),
    )

    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=M)

    def __str__(self):
        return self.Fname
  # patient Tabel.
class Patient(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d' )
    Mobil = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=8)
    Address = models.CharField(max_length=60)
    SSN = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()
    Examinations = models.ImageField( upload_to='photos/%Y/%m/%d' )
    Symptoms = models.TextField()
    #gender
    GENDER_CHOICES = (
          ('M', 'Male'),
          ('F', 'Female'),
    )

    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=M)

    def __str__(self):
        return self.Fname
  
