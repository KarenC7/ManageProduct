from django.shortcuts import render
from rest_framework import viewsets
from .models import MyProduct
from .serializers import MyProductSerializer

# Create view to Product Set (API REST)
class MyProductViewSet(viewsets.ModelViewSet):
    serializer_class = MyProductSerializer
    queryset = MyProduct.objects.all()
   
