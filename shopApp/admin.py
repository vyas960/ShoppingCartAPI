from django.contrib import admin
from shopApp.models import Product, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display=['id','item_name','item_detail','item_price']


class CustomerAdmin(admin.ModelAdmin):
	list_display=['id','c_name','c_age','c_address']


admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
