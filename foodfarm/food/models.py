from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CITY_CHOICES= (
    ('NBI','Nairobi'),
    ('KSM','Kisumu'),
    ('ELD','Edldoret'),
    ('Nak','Nakuru'),
    ('MBS','Mombasa')
)
CATEGORY_CHOICES=(
    ('FR','Fruits'),
    ('VG','Vegetables'),
    ('DY','Dairy'),
    ('GN','Grains'),
    ('PF','Protein foods')
)

#Categories
class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


#Customer Orders
class Order(models.Model):
   # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    #date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)



    def __str__(self):
        return self.product
    
#All our Products
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price  = models.DecimalField(max_digits=6, default=0, decimal_places=2, null=True)
    discounted_price = models.DateTimeField(null=True)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')





    def __str__(self):
        return self.title
    



class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(choices= CITY_CHOICES, max_length=100)
    mobile = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    



    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
