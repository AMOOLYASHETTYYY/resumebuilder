from django.contrib import admin
from .models import Employee, Project, EmployeeProjectMapping

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation')  

admin.site.register(Project)
admin.site.register(EmployeeProjectMapping)
