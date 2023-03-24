from django.contrib import admin
from .models import Product,Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product_name','category','amount','date_added')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display=('id','category')
