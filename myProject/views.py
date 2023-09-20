from django.http import HttpResponse
from django.shortcuts import render
from employee.models import employee

def home(request):
    employees = employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request, 'home.html', context)