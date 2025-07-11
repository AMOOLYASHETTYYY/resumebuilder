from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee, EmployeeProjectMapping
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO



def search_employee(request):
    query = request.GET.get('query')
    employees = []

    if query:
        if query.isdigit():
            employees = Employee.objects.filter(id=int(query))
        else:
            employees = Employee.objects.filter(name__icontains=query)

    return render(request, 'resume/search.html', {'employees': employees})



def generate_resume(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    projects = EmployeeProjectMapping.objects.filter(employee=employee).select_related('project')

    html = render_to_string('resume/resume.html', {
        'employee': employee,
        'projects': [ep.project for ep in projects]
    })

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error generating PDF', status=500)

