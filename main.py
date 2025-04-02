############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

from faker import Faker
from db.models import *
from django.contrib.auth.models import User
import random
from model_bakery.recipe import Recipe

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

"""
In case you need to start over. 
Note- this will delete any other tables on the public schema.
Alternatively, you could drop django's tables one-by-one

Login to psql and run these commands in order:

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres, public;

... then migrate again, and re-create your superuser
"""

# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')

fake = Faker()
from faker.providers import address, currency, person, phone_number

JOB_CHOICES = [
    ("RE", "Restocker"),
    ("MA", "Manager"),
    ("CO", "Cook"),
    ("RC", "Receipt Checker"),
    ("CA", "Cashier"),
]

for i in range(40):
    a = Store(address = fake.address())
for i in range(40):
    edate = fake.date()
    b = Employee(employee_name = fake.full_name(), store = fake.random_int(min = 0, max = 40), occupation = random.choice(JOB_CHOICES))
    c = Inventory(store_id = fake.random_int(min = 0, max = 40), stock = fake.random_int(min = 0, max = 15000), cost = fake.random_int(), product_name = fake.random_object_name())
    d = Member(expiration_date = edate, member_name = fake.full_name(), member_address = fake.address())
    e = Order(customer = fake.random_int(min = 0, max = 40), bill = fake.pricetag(), before_date = edate)
    f = Item(order_id = fake.random_int(min = 0, max = 40), store_id = fake.random_int(min = 0, max = 40), item_id = fake.random_int(min = 0, max = 40))
    g = Food_Court(store_id = fake.random_int(min = 0, max = 40), name = fake.random_object_name(), price = fake.random_int())
    