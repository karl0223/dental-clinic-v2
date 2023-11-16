from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']
    list_per_page = 10
    search_fields = ['street__istartswith', 'city__istartswith']

    def branch(self, address):
        return address.branch.name
    
@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    autocomplete_fields = ['address']
    list_display = ['name', 'address']
    ordering = ['name', 'address']
    list_per_page = 10
    search_fields = ['branch__istartswith']
    list_select_related = ['address']

@admin.register(models.Dentist)
class DentistAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'address']
    list_display = ['user_id', 'first_name', 'last_name', 'phone', 'role']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    list_select_related = ['user']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ['balance']
    autocomplete_fields = ['branch', 'package', 'user', 'address']
    list_display = ['user_id', 'first_name', 'last_name', 'phone', 'balance', 'gender', 'branch']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    list_select_related = ['package', 'user']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    # def branch_name(self, patient):
    #     return patient.branch.name
    
    # def package_type(self, patient):
    #     if patient.package:
    #         return patient.package.title
    #     return None

@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    actions = ['price_50k']
    list_display = ['title', 'package_type', 'price']
    list_per_page = 10 # simple pagination
    search_fields = ['title__istartswith']


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['patient', 'dentist']
    list_display = ['patient', 'dentist', 'start_time', 'end_time']
    list_select_related = ['patient', 'dentist']
    list_per_page = 10

@admin.register(models.DentalHistory)
class DentalHistoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['patient']
    list_display = ['patient', 'last_dental_visit', 'reason_for_visit', 'previous_treatment']
    list_select_related = ['patient']

@admin.register(models.TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    autocomplete_fields = ['patient']
    list_display = ['patient', 'proposed_treatment', 'priority_of_treatment', 'estimated_cost', 'alternative_treatment_options']
    list_select_related = ['patient']