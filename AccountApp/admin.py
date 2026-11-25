from django.contrib import admin
from django.contrib import admin
from .models import User, Doctor, Patient, Speciality
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Speciality)
