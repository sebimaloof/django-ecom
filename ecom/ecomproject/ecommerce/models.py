from django.db import models


# superusername      : ecom
# superuser password : ecom

# Create your models here.




class ProductCode(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class AllProducts(models.Model):
    product_code = models.ForeignKey(ProductCode, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)

    pro_discr1 = models.CharField(max_length=200) # max length 45 othervise seemore button will go out of the div
    pro_discr2 = models.CharField(max_length=200, null=True, blank=True)
    pro_discr3 = models.CharField(max_length=200, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    quantity = models.CharField(max_length=50)

    weekly_product = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)

    old_price = models.CharField(max_length=10)
    current_price = models.CharField(max_length=10)
    product_image = models.ImageField(upload_to='Products/')

    def __str__(self):
        return self.product_name
 
# 

from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    adress=models.TextField(max_length=500,blank=True)
    location=models.CharField(max_length=30,blank=True)
    mobile_number=models.CharField(max_length=10,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
    # make migrations and migrate 
    


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(AllProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"

