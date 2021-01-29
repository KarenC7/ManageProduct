import decimal
from django.contrib import admin


# Register your models here.
from .models import MyProduct
from .models import Administrator
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

#Function to send the mails to Admins when admins modifies a product
def send_email(mail,prod):
    context = {prod}
    template = get_template('email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Product Notification',
        'Other admin modified a product',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    
    email.attach_alternative(content, 'text/html')

#Check if the request on products is POST to send notifications
def products(self,request):
    if request.method == 'POST':
        mail = MyAdministrator.get_queryset
        prod = self.name
        send_email(mail)
    return render(request, 'admin/products')

#Add to wish list action, can you see at history of the products who user wished
def wishProducts(self,request, queryset):
    for myproduct in queryset:
        myproduct.wished = myproduct.wished + 1
        myproduct.save()
    self.message_user(request, "Added at your wished list.")
wishProducts.short_description = 'I wished this'

class MyProductAdmin(admin.ModelAdmin):
    actions = [wishProducts, ]  # <-- Add one extra list action function here to do a disccount
    list_display = ['name', 'prize']
    
#Register our classes in admin
admin.site.register(MyProduct,MyProductAdmin)
  
   

