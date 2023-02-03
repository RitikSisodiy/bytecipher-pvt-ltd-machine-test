# from django.db import models
from djongo import models
class Product(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    def __str__(self) -> str:
        return str(self.product)
