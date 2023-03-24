from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=20)
    def __str__(self):
        return (self.category)

class Product(models.Model):
    product_name=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.FloatField()
    date_added=models.DateTimeField(auto_now=True,editable=False)


    def __str__(self):
        return (self.name)
