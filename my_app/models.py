from django.db import models
from django.utils import timezone


STATUS = (
    (0,"pending"),
    (1,"processing"),
    (2,"shipped"),
    (3,"delivered")

)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    cat_image = models.ImageField()

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    post = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    shipping_address = models.CharField(max_length=2000, blank=True)
    customer_number = models.CharField(max_length=2000)
    message = models.TextField()
    quantity = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.customer_name


    