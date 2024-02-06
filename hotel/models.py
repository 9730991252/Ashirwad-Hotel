from django.db import models

# Create your models here.


class Admin (models.Model):
    admin_name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    admin_mobile=models.IntegerField(default=True,unique=True)
    pin = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)





class Dish_category(models.Model):
    category_name = models.CharField(max_length=100)
    added_by = models.ForeignKey(Admin,on_delete=models.PROTECT,default=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)


class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    dish_category = models.ForeignKey(Dish_category,on_delete=models.PROTECT,default=True)
    price=models.FloatField(default=0)
    added_by = models.ForeignKey(Admin,on_delete=models.PROTECT,default=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)



class OrderDetail(models.Model):
    added_by = models.ForeignKey(Admin,on_delete=models.PROTECT,default=True)
    dish=models.ForeignKey(Dish,on_delete=models.PROTECT,null=True)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    qty = models.IntegerField(default=1)
    price=models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    
