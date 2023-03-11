from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
 
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    # image = models.ImageField(upload_to = "",default = "")
    image=models.FileField(upload_to="images/")

    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default= 'PENDING')
     
    # def __str__(self):
    #     return self.name

class Checkout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    payment = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return self.address

        