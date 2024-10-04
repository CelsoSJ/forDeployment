from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# role and department models creation
class Department(models.Model):
  name = models.CharField(max_length=4)

  def __str__(self):
    return self.name
  

class Role(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name
  






# extending the user model fields
# first add to the top: from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

  address = models.CharField(max_length=100)
  role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)




class Program(models.Model):
  name = models.CharField(max_length=4, null=True)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  program_chair = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name 