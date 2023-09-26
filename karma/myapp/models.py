from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/images')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

 
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    def product_total(self):
        return (self.product.price * self.quantity)

class CustomeraddressModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

step = (('Pending','Pending'),('Accepted','Accepted'),('Packing','Packing'),
        ('Shipping','Shipping'),('Deliverd','Deliverd'))


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomeraddressModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices = step, max_length=50, default='Pending')




