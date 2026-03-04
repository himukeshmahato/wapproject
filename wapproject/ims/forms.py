from django import forms
from .models import Department, Employee, Customer, Project, Product, AssignedTo, ProjectProduct


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class AssignedToForm(forms.ModelForm):
    class Meta:
        model = AssignedTo
        fields = "__all__"


class ProjectProductForm(forms.ModelForm):
    class Meta:
        model = ProjectProduct
        fields = "__all__"