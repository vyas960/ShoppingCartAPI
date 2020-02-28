from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	c_name=models.CharField(max_length=250)
	c_age=models.FloatField()
	c_address=models.CharField(max_length=250)



class Product(models.Model):
	item_name=models.CharField(max_length=250)
	item_detail=models.CharField(max_length=250)
	item_price=models.FloatField()
	item_image=models.ImageField(blank=True, null=True)
	owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE,blank=True, null=True)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE,blank=True, null=True)

	def __str__(self):
		return self.item_name
