from django.db import models
# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    reg_emp_id = models.CharField(max_length=50)  # Assuming 'reg_emp_id' is a string
    type = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.name
        
class StudentDetails(models.Model):
    reg_emp_id = models.CharField(max_length=100)  # Registration or employee ID
    first_name = models.CharField(max_length=100)  # First Name
    last_name = models.CharField(max_length=100)   # Last Name
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=10)  # Gender (e.g., "Male", "Female")
    blood_group = models.CharField(max_length=5)  # Blood group (e.g., "O+", "A-")
    contact_no = models.CharField(max_length=15)  # Contact number
    address = models.TextField()  # Address (long text)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"   #This is an f-string, a convenient way to format strings in Python. pip install djangorestframeworkIt combines the first and last names into a single string.

class SubjectDetails(models.Model):
    reg_emp_id = models.CharField(max_length=50,)  # Assuming reg_emp_id is a unique identifier
    subject = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.subject} {self.faculty_name}"
