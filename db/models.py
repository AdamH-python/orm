import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

JOB_CHOICES = [
    ("RE", "Restocker"),
    ("MA", "Manager"),
    ("CO", "Cook"),
    ("RC", "Receipt Checker"),
    ("CA", "Cashier"),
]

# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]

##########################################
### Converting from postgresql into Django
##########################################

class Store(models.Model):
    #store_id = models.BigAutoField(primary_key=True)
    store_address = models.CharField(max_length=100)

class Employee(models.Model):
    #employee_id = models.BigAutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=2, choices=JOB_CHOICES)

class Inventory(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    #item_id = models.BigAutoField()
    stock = models.IntegerField()
    cost = models.DecimalField(max_digits = 6, decimal_places = 2)
    product_name = models.CharField(max_length=30)

class Member(models.Model):
    expiration_date = models.DateField()
    member_name = models.CharField(max_length=100)
    member_address = models.CharField(max_length=70)
    
class Order(models.Model):
    #store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Member, on_delete=models.CASCADE)
    bill = models.DecimalField(max_digits = 7, decimal_places = 2)
    before_date = models.ForeignKey(Store, on_delete=models.CASCADE)
    
class Item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    
class Food_Court(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    
