from rest_framework import serializers
from .models import MyProduct

class MyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct
        fields = '__all__' #Fields to show in API REST, could be '__all__'