from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from .models import CustomUser, Department, Role, Program

# Register your models here.

class CustomUserAdmin(UserAdmin):
  fieldsets = UserAdmin.fieldsets + (
    (None, {'fields':('department', 'role', 'address')}),
  )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Role)

# filter out users To ensure that only program chair users are assigned to a program
class ProgramAdmin(admin.ModelAdmin):
  list_display = ['name', 'department','program_chair']
  list_filter = ['department']
  search_fields = ['name']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == "program_chair":
      kwargs["queryset"] = CustomUser.objects.filter(role=2)
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  

admin.site.register(Program, ProgramAdmin)