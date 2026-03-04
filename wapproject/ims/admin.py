from django.contrib import admin
from .models import Department, Employee, Customer, Project, Product, AssignedTo, ProjectProduct

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Product)
admin.site.register(AssignedTo)
admin.site.register(ProjectProduct)