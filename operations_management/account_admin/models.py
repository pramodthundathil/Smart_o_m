from django.db import models


class Conveyane(models.Model):
    conveyance_amount = models.FloatField()
    username = models.CharField(max_length=255,null=True,blank=True)
    Reason = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False) 
    
class Works(models.Model):
    workname = models.CharField(max_length=255)
    WorkDiscription = models.TextField(max_length=1000)
    status = models.CharField(max_length=255,choices=(
        ("Started","Started"),
        ("Partialy Completed","Partialy Completed"),
        ("Taken Over","Taken Over"),
        ("pending","pending")
    ))
    manager  = models.CharField(max_length=255,null=True,blank=True)
    employee = models.CharField(max_length=255,null=True,blank=True)
    CompletionStatus = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
