from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class values(models.Model):
    name = models.CharField(max_length=100)
    dis = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = True)
    img = models.ImageField(upload_to = 'pic')
