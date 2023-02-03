from django.contrib import admin
from .models import Product,Image
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','color']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','product','image']
