from django.contrib import admin
from . import models
from .models import Category, Customer, Product, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'selling_price', 'discounted_price']
    search_fields = ['title', 'description']
    list_filter = ['selling_price', 'discounted_price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city','mobile']
    search_fields = ['user', 'locality', 'city']

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)