from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Employee, Customer, Project, Product, AssignedTo, ProjectProduct
from .forms import (
    DepartmentForm, EmployeeForm, CustomerForm, ProjectForm,
    ProductForm, AssignedToForm, ProjectProductForm
)


def dashboard(request):
    return render(request, "dashboard.html")


# -------------------- DEPARTMENT --------------------

def department_list(request):
    data = Department.objects.select_related('manager').all()
    return render(request, "list.html", {"data": data, "title": "Departments", "key": "department", "count": data.count()})


def department_add(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("department_list")
    return render(request, "form.html", {"form": form, "title": "Add Department", "key": "department"})


def department_edit(request, id):
    obj = get_object_or_404(Department, id=id)
    form = DepartmentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("department_list")
    return render(request, "form.html", {"form": form, "title": "Edit Department", "key": "department"})


def department_delete(request, id):
    obj = get_object_or_404(Department, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("department_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Department", "key": "department"})


# -------------------- EMPLOYEE --------------------

def employee_list(request):
    data = Employee.objects.select_related('dept').all()
    return render(request, "list.html", {"data": data, "title": "Employees", "key": "employee", "count": data.count()})


def employee_add(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "form.html", {"form": form, "title": "Add Employee", "key": "employee"})


def employee_edit(request, id):
    obj = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "form.html", {"form": form, "title": "Edit Employee", "key": "employee"})


def employee_delete(request, id):
    obj = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("employee_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Employee", "key": "employee"})


# -------------------- CUSTOMER --------------------

def customer_list(request):
    data = Customer.objects.all()
    return render(request, "list.html", {"data": data, "title": "Customers", "key": "customer", "count": data.count()})


def customer_add(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("customer_list")
    return render(request, "form.html", {"form": form, "title": "Add Customer", "key": "customer"})


def customer_edit(request, id):
    obj = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("customer_list")
    return render(request, "form.html", {"form": form, "title": "Edit Customer", "key": "customer"})


def customer_delete(request, id):
    obj = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("customer_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Customer", "key": "customer"})


# -------------------- PROJECT --------------------

def project_list(request):
    data = Project.objects.select_related('customer', 'project_manager').all()
    return render(request, "list.html", {"data": data, "title": "Projects", "key": "project", "count": data.count()})


def project_add(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("project_list")
    return render(request, "form.html", {"form": form, "title": "Add Project", "key": "project"})


def project_edit(request, id):
    obj = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("project_list")
    return render(request, "form.html", {"form": form, "title": "Edit Project", "key": "project"})


def project_delete(request, id):
    obj = get_object_or_404(Project, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("project_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Project", "key": "project"})


# -------------------- PRODUCT --------------------

def product_list(request):
    data = Product.objects.all()
    return render(request, "list.html", {"data": data, "title": "Products", "key": "product", "count": data.count()})


def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "form.html", {"form": form, "title": "Add Product", "key": "product"})


def product_edit(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "form.html", {"form": form, "title": "Edit Product", "key": "product"})


def product_delete(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("product_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Product", "key": "product"})


# -------------------- ASSIGNED TO --------------------

def assignedto_list(request):
    data = AssignedTo.objects.select_related('employee', 'project').all()
    return render(request, "list.html", {"data": data, "title": "Assignments", "key": "assignedto", "count": data.count()})


def assignedto_add(request):
    form = AssignedToForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("assignedto_list")
    return render(request, "form.html", {"form": form, "title": "Add Assignment", "key": "assignedto"})


def assignedto_edit(request, id):
    obj = get_object_or_404(AssignedTo, id=id)
    form = AssignedToForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("assignedto_list")
    return render(request, "form.html", {"form": form, "title": "Edit Assignment", "key": "assignedto"})


def assignedto_delete(request, id):
    obj = get_object_or_404(AssignedTo, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("assignedto_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Assignment", "key": "assignedto"})


# -------------------- PROJECT PRODUCT --------------------

def projectproduct_list(request):
    data = ProjectProduct.objects.select_related('project', 'product').all()
    return render(request, "list.html", {"data": data, "title": "Project Products", "key": "projectproduct", "count": data.count()})


def projectproduct_add(request):
    form = ProjectProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("projectproduct_list")
    return render(request, "form.html", {"form": form, "title": "Add Project Product", "key": "projectproduct"})


def projectproduct_edit(request, id):
    obj = get_object_or_404(ProjectProduct, id=id)
    form = ProjectProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("projectproduct_list")
    return render(request, "form.html", {"form": form, "title": "Edit Project Product", "key": "projectproduct"})


def projectproduct_delete(request, id):
    obj = get_object_or_404(ProjectProduct, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("projectproduct_list")
    return render(request, "delete.html", {"obj": obj, "title": "Delete Project Product", "key": "projectproduct"})