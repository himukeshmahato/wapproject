from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # Department
    path("departments/", views.department_list, name="department_list"),
    path("departments/add/", views.department_add, name="department_add"),
    path("departments/<int:id>/edit/", views.department_edit, name="department_edit"),
    path("departments/<int:id>/delete/", views.department_delete, name="department_delete"),

    # Employee
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_add, name="employee_add"),
    path("employees/<int:id>/edit/", views.employee_edit, name="employee_edit"),
    path("employees/<int:id>/delete/", views.employee_delete, name="employee_delete"),

    # Customer
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.customer_add, name="customer_add"),
    path("customers/<int:id>/edit/", views.customer_edit, name="customer_edit"),
    path("customers/<int:id>/delete/", views.customer_delete, name="customer_delete"),

    # Project
    path("projects/", views.project_list, name="project_list"),
    path("projects/add/", views.project_add, name="project_add"),
    path("projects/<int:id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:id>/delete/", views.project_delete, name="project_delete"),

    # Product
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/<int:id>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:id>/delete/", views.product_delete, name="product_delete"),

    # AssignedTo
    path("assignments/", views.assignedto_list, name="assignedto_list"),
    path("assignments/add/", views.assignedto_add, name="assignedto_add"),
    path("assignments/<int:id>/edit/", views.assignedto_edit, name="assignedto_edit"),
    path("assignments/<int:id>/delete/", views.assignedto_delete, name="assignedto_delete"),

    # ProjectProduct
    path("project-products/", views.projectproduct_list, name="projectproduct_list"),
    path("project-products/add/", views.projectproduct_add, name="projectproduct_add"),
    path("project-products/<int:id>/edit/", views.projectproduct_edit, name="projectproduct_edit"),
    path("project-products/<int:id>/delete/", views.projectproduct_delete, name="projectproduct_delete"),
]