from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    easy_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_easy_name(self):
        return self.easy_name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) 
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    grade = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name   
