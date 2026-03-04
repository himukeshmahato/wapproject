from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)

    manager = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.project_name


class Product(models.Model):
    product_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_type


class AssignedTo(models.Model):

    ROLE_CHOICES = [
        ("Project Manager", "Project Manager"),
        ("Database Engineer", "Database Engineer"),
        ("QA Tester", "QA Tester"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role_in_project = models.CharField(max_length=50, choices=ROLE_CHOICES)
    hours_allocated = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employee} -> {self.project}"
    

class ProjectProduct(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project} + {self.product}"