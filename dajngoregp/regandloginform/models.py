from django.db import models
class registration(models.Model):
    User=models.CharField(max_length=20)
    Pwd=models.CharField(max_length=20)
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    Dob=models.DateField()
    phone=models.IntegerField()


# Create your models here.
