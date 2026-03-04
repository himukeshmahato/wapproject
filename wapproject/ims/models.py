from django.db import models

# Employee model creation
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dept_id = models.ForeignKey('Department', on_delete=models.CASCADE) # this is many to one relationship between employee and department

    def __str__(self):
        return self.emp_name

# department models creation
class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dept_name