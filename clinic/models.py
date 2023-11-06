from django.db import models
from django.contrib import admin
from django.conf import settings

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.street} {self.city}'

class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='branch')

    def __str__(self) -> str:
        return self.name
class Package(models.Model):
    PACKAGE_A = 'A'
    PACKAGE_B = 'B'
    PACKAGE_C = 'C'
    PACKAGE_CHOICES = [
        (PACKAGE_A, 'Standard'),
        (PACKAGE_B, 'Premium'),
        (PACKAGE_C, 'Delux'),
    ]
    title = models.CharField(max_length=255)
    package_type = models.CharField(max_length=1, choices=PACKAGE_CHOICES, default=PACKAGE_A)
    price= models.DecimalField(max_digits=10, decimal_places=2)

    # Change the rendered package title in the admin
    def __str__(self) -> str:
        return self.title
    
class Patient(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='patients')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='patients', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='patients')

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name



class Dentist(models.Model):
    GENERAL_DENTIST = 'GD'
    PEDIATRIC_DENTIST = 'PD'
    ORTHODENTIST = 'OD'
    GUM_SPECIALIST = 'GS'
    ROOT_CANAL_SPECIALIST = 'RCS'
    ORAL_SURGEON = 'OS'
    PROSTHODONTIST = 'PTD'
    DENTIST_ROLE_CHOICES = [
        (GENERAL_DENTIST, "General Dentist"),
        (PEDIATRIC_DENTIST, ' Pediatric Dentist'),
        (ORTHODENTIST, 'Orthodentist'),
        (GUM_SPECIALIST, 'Gum Specialist'),
        (ROOT_CANAL_SPECIALIST, 'Root Canal Specialist'),
        (ORAL_SURGEON, 'Oral Surgeon'),
        (PROSTHODONTIST, 'Prothodontist'),
    ]
    phone = models.CharField(max_length=255)
    role = models.CharField(max_length=5, choices=DENTIST_ROLE_CHOICES, default=GENERAL_DENTIST)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        permissions = [
            ('cancel_appointment', 'Can cancel appointment')
        ]
