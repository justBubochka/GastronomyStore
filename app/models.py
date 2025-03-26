from django.db import models
from django.utils import timezone

# Create your models here.



class Product(models.Model):
    '''Product model that represents a product in the store'''

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    rate = models.IntegerField(default=0) 
    create_date = models.DateTimeField(null=True, blank=True, default=None)  # null=True
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    '''Category model that represents a category in the store'''

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name


