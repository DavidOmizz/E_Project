from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category','price','created_at')
    search_fields = ['subject', 'body']


admin.site.register(Category)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','post','quantity','shipping_address')
    search_fields = ['subject', 'body']

