from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']
    list_per_page = 10
    list_select_related = ['branch']

    def branch(self, address):
        return address.branch.name
    
@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10
    search_fields = ['branch__istartswith']

@admin.register(models.Dentist)
class DentistAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user_id', 'first_name', 'last_name', 'phone', 'role']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    list_select_related = ['user']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ['balance']
    autocomplete_fields = ['branch', 'package', 'user']
    list_display = ['user_id', 'first_name', 'last_name', 'phone', 'branch_name', 'package_type', 'balance']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    list_select_related = ['branch', 'package', 'user']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    def branch_name(self, patient):
        return patient.branch.name
    
    def package_type(self, patient):
        if patient.package:
            return patient.package.title
        return None

@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    actions = ['price_50k']
    list_display = ['title', 'package_type', 'price']
    list_per_page = 10 # simple pagination
    search_fields = ['title__istartswith']
