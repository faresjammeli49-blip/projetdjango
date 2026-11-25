from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
class Speciality(models.Model):
    name = models.CharField(max_length=100)
class Doctor(models.Model):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    specialities = models.ManyToManyField('Speciality', related_name='doctors')
class Patient(models.Model):
    national_id = models.CharField(max_length=8,unique=True,validators=[RegexValidator(regex=r"^\d{8}$",
     message="Le numéro d'identité national doit contenir 8 chiffres.",
        )],
    )
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(
            regex=r"^\d{8}$",
            message="Le téléphone doit contenir 8 chiffres.",
        )],
    )
    birth_date = models.DateField()