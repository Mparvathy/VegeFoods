from django.contrib import admin
from app.models import customuser,Product,Veg,Cart,CartItem,Order,OrderItem,Account,Fruit,Juice,ContactMessage
admin.site.register(customuser)
admin.site.register(Product)
admin.site.register(Veg)
admin.site.register(Fruit)
admin.site.register(Juice)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Account)
admin.site.register(ContactMessage)