from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    summary = models.TextField()
    technical_skills = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.designation}"

class Project(models.Model):
    name = models.CharField(max_length=200)
    technology_used = models.CharField(max_length=200)
    description = models.TextField()
    roles_and_responsibilities = models.TextField()

    def __str__(self):
        return self.name

class EmployeeProjectMapping(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name} -> {self.project.name}"
