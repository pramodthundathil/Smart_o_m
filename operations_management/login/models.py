from django.db import models
from django.db.models.fields import EmailField, IntegerField

# Create your models here.

# users database------------------------------------------------------------------

class employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# employes database------------------------------------------------------------------

class staff(models.Model):
    
    staff_name = models.CharField(max_length=100)
    emp_id = models.AutoField(primary_key=True)
    emp_title = models.CharField(max_length=100)
    department_id = models.CharField(max_length=50)
    DOB = models.DateField()
    date_of_join = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)

# leave Datebase----------------------------------------------------------------------   

class leave(models.Model):

    staff_name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
    employee_title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    leave_start = models.DateField(auto_now_add=False)
    leave_end = models.DateField(auto_now_add=False)
    total_leave = models.CharField(max_length=50)
    approve_status = models.BooleanField(default=False)

# messages for dashboard--------------------------------------------------------------

class dashboard(models.Model):

    msg_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    time = models.DateField(auto_now_add=True)
    
  
