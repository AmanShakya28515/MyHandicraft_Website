from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product_Buddha(models.Model):
    name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    category = models.CharField(max_length=100, default='buddha')

    def __str__(self):
        return self.name

class Product_Tara(models.Model):
    name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    category = models.CharField(max_length=100, default='tara')

    def __str__(self):
        return self.name
    
class Product_Ganesh(models.Model):
    name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    category = models.CharField(max_length=100, default='ganesh')

    def __str__(self):
        return self.name
    
class Product_Sarsoti_Laxmi(models.Model):
    name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    category = models.CharField(max_length=100, default='sarsoti_laxmi')

    def __str__(self):
        return self.name
    
class Utencils(models.Model):
    name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')
    category = models.CharField(max_length=100, default='utencils')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/')
    history = models.TextField(default="History not available")


    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    product_image = models.ImageField(upload_to='static/', null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} in cart of {self.user.username}"

    def get_total_price(self):
        return self.product_price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    