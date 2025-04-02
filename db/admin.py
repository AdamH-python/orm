from django.contrib import admin

from .models import User, Reporter, Article, Publication, Store, Employee, Inventory, Member, Order, Item, Food_Court

admin.site.register(User)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Store)
admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Member)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Food_Court)