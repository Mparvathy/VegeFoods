from django.db import models
from django.contrib.auth.models import User
from  django.contrib.auth.models import AbstractUser
from django.conf import settings

class customuser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    def has_admin_permission(self):
        return self.is_admin

       
class Product(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='app/cover',null=True,blank=True)
    description =models.CharField(max_length=400)
    price=models.IntegerField()
    sold=models.IntegerField()
    def __str__(self): 
        return self.name 

       
class Veg(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='app/cover',null=True,blank=True)
    description =models.CharField(max_length=400)
    price=models.IntegerField()
    sold=models.IntegerField()
    def __str__(self): 
        return self.name 

class Fruit(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='app/cover',null=True,blank=True)
    description =models.CharField(max_length=400)
    price=models.IntegerField()
    sold=models.IntegerField()
    def __str__(self): 
        return self.name 

class Juice(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField(upload_to='app/cover',null=True,blank=True)
    description =models.CharField(max_length=400)
    price=models.IntegerField()
    sold=models.IntegerField()
    def __str__(self): 
        return self.name 
    

class Cart(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    veg = models.ForeignKey(Veg, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    fruit = models.ForeignKey(Fruit, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    juice = models.ForeignKey(Juice, null=True, blank=True, on_delete=models.CASCADE, related_name='carts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def subtotal(self):
        if self.product:
            return self.quantity * self.product.price
        elif self.veg:
            return self.quantity * self.veg.price
        elif self.fruit:
            return self.quantity * self.fruit.price
        elif self.juice:
            return self.quantity * self.juice.price
        return 0
    def __str__(self):
        if self.product:
            return f"{self.user.username}'s cart item: {self.product.name}"
        elif self.veg:
            return f"{self.user.username}'s cart item: {self.veg.name}"
        elif self.fruit:
            return f"{self.user.username}'s cart item: {self.fruit.name}"
        elif self.juice:
            return f"{self.user.username}'s cart item: {self.juice.name}"
        return "Unknown cart item"




class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def get_total_price(self):
        return self.quantity * self.price
    def __str__(self):
        return f"{self.product_name} ({self.quantity})"



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    veg = models.ForeignKey(Veg, on_delete=models.SET_NULL, null=True, blank=True)
    fruit = models.ForeignKey(Fruit, on_delete=models.SET_NULL, null=True, blank=True)
    juice= models.ForeignKey(Juice, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Ad
    def __str__(self):
        return f"{self.product_name} ({self.quantity})"


# models.py
from django.db import models
from django.contrib.auth.models import User


  
class Account(models.Model):
    account_number = models.CharField(max_length=20, blank=True, null=True)
    acctype=models.CharField(max_length=30)
    amount=models.IntegerField()
    def __str__(self):
        return self.account_number  
 
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    veg = models.ForeignKey(Veg, null=True, blank=True, on_delete=models.CASCADE)
    fruit= models.ForeignKey(Fruit, null=True, blank=True, on_delete=models.CASCADE)
    juice= models.ForeignKey(Juice, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.user.username} - {self.product or self.veg or self.fruit or self.juice}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} ({self.email})"    