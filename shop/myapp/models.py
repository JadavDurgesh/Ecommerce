from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField(default=1234)
        
    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class main_category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class Add_product(models.Model):
    main_id = models.ForeignKey(main_category,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    o_price = models.IntegerField()
    que = models.IntegerField()
    IMG = models.ImageField(upload_to = 'img')


    def __str__(self):
        return self.name

class Add_to_cart(models.Model):
    product_id = models.ForeignKey(Add_product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    IMG = models.ImageField(upload_to='img')
    que = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.user_id






