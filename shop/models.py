from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username  # return email

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/img",default="")

    def __str__(self):
        return (self.product_name+" :) ")

    @property             # not give error while rendering image
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ProductImgae(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop/img2",default="")
    
    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    data_ordred = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([i.get_total for i in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([i.quantity for i in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        price = self.product.price
        total_price = price * self.quantity
        return total_price


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField(max_length=500, default="")
    
    def __str__(self):
        return self.name      

class Checkout(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    Zipcode=models.CharField(max_length=50)

    def __str__(self):
        return self.name   

class Payment(models.Model):
    Payment =models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Help(models.Model):
    problem = models.TextField(max_length=500)

class Subscribers(models.Model):
    subscribers=models.EmailField(max_length=50)
    def __str__(self):
        return self.subscribers





