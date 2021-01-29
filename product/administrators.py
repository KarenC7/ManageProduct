from django.db import models
from django.contrib.auth.models import User

#Class to get administrators from Users
class MyAdministrator(User):
    def get_queryset(self):
        #Filter administrators users 
        return super(MyAdministrator, self).get_queryset.filter(superuserestate=True)
    
    
    
