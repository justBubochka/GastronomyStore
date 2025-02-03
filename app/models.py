from django.db import models
from django.utils import timezone

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    pub_date = models.DateTimeField(null=True, blank=True, default=None) # null=True 
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.name