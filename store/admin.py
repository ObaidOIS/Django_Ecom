from django.contrib import admin
from .models import *
# Register your models here.
# username = obaid
# email = obaidch00@gmail.com
# password = admin123

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


