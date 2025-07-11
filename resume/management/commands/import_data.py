import csv
from django.core.management.base import BaseCommand
from resume.models import Employee, Project, EmployeeProjectMapping

class Command(BaseCommand):
    help = 'Import employees, projects, and mappings from CSV files'

    def handle(self, *args, **kwargs):
     
        with open('employees.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp, _ = Employee.objects.get_or_create(
                    name=row['name'],
                    designation=row['designation'],
                    summary=row['summary'],
                    technical_skills=row['technical_skills']
                )

        
        with open('projects.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                proj, _ = Project.objects.get_or_create(
                    name=row['name'],
                    technology_used=row['technology_used'],
                    description=row['description'],
                    roles_and_responsibilities=row['roles_and_responsibilities']
                )

      
        with open('mappings.csv', newline='', encoding='utf-8') as csvfile:
           reader = csv.DictReader(csvfile)
           for row in reader:
                try:
                   emp = Employee.objects.get(id=int(row['employee_id']))

                   proj = Project.objects.get(name=row['project_name'])
                   EmployeeProjectMapping.objects.get_or_create(employee=emp, project=proj)
                except Employee.DoesNotExist:
                  self.stdout.write(self.style.WARNING(f"Employee not found: {row['employee_name']}"))
                except Project.DoesNotExist:
                  self.stdout.write(self.style.WARNING(f"Project not found: {row['project_name']}"))

        self.stdout.write(self.style.SUCCESS("CSV import complete!"))
