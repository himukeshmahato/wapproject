from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, "dashboard.html")

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})
