from django.contrib import admin

# Register your models here.
from .models import MyProduct

admin.site.register(MyProduct)