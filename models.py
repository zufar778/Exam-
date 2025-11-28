from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    picture = models.ImageField(upload_to="rasm/", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class POSTS(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    description = models.TextField()
    datetime = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name    

   
    
    
    
    

