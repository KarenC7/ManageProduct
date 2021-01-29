from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .administrators import MyAdministrator

#Model of my product
class MyProduct(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    prize = models.FloatField()
    wished = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdateDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
#Create a proxy model, It allows us to access to Users models
class Administrator(User):
    objects = MyAdministrator()
    class Meta:
        proxy = True
    def __str__(self):
        return self.email_address

   
    


   
  