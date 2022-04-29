from django.contrib import admin
from .models import Laptops , Monitors , Printers, Headphones,Customer,Cart,OrderPlaced

admin.site.register(Laptops)
admin.site.register(Monitors)
admin.site.register(Printers)
admin.site.register(Headphones)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name',
    'Contact_No','locality','city','zipcode','state']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_id','category','quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product_id', 'category',
    'quantity','ordered_date','status']
