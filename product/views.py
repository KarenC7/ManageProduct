from django.shortcuts import render
from rest_framework import viewsets
from .models import MyProduct
from .serializers import MyProductSerializer
# Create your views here.

class MyProductViewSet(viewsets.ModelViewSet):
    serializer_class = MyProductSerializer
    queryset = MyProduct.objects.all()
