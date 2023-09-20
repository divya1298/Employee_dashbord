from django.shortcuts import render, get_object_or_404, HttpResponse
from employee.models import employee


# Create your views here.
def employee_details(request, pk):
    employees = get_object_or_404(employee, pk=pk)
    context= {
        'employees': employees,
    }
    return render(request, 'employee_details.html', context)

