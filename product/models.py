from django.db import models

# Create your models here.

class MyProduct(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    prize = models.FloatField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdateDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    