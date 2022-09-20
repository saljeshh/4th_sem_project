from django.db import models
from django.contrib.auth.models import User

# Choices

STATE_CHOICE = (
    ('Province No. 1','Province No. 1'),
    ('Madhesh Province','Madhesh Province'),
    ('Bagmati Province','Bagmati Province'),
    ('Gandaki Province','Gandaki Province'),
    ('Lumbini Province','Lumbini Province'),
    ('Karnali Province','Karnali Province'),
    ('Sudurpashchim Province','Sudurpashchim Province'),
)

CATEGORY_CHOICES = (
    ('Banknotes', 'Banknotes'),
    ('Coins', 'Coins'),
)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled'),
)

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    product_image = models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES, default = 'Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price