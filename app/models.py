from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    # pub_date = models.DateTimeField("date published")
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.name