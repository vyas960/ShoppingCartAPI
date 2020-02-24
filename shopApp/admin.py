from django.contrib import admin
from shopApp.models import Product,Cart,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display=['id','item_name','item_detail','item_price']



admin.site.register(Product,ProductAdmin)
