from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_employee, name='search_employee'),
    path('resume/<int:employee_id>/', views.generate_resume, name='generate_resume'),
]
