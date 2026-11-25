from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
class Speciality(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    specialities = models.ManyToManyField('Speciality', related_name='doctors')
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    def __str__(self):
        return f"Dr. {self.last_name or self.username}"
def validate_past_date(value):
    if value >= date.today():
        raise ValidationError("La date de naissance doit être dans le passé.")

class Patient(User):
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
    birth_date = models.DateField(validators=[validate_past_date]
)
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
