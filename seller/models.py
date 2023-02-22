from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    product_no =models.BigIntegerField()
    product_des = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    

    class Meta:
        db_table ='product_tb'

