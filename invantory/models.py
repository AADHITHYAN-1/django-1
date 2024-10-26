# from django.db import models

# class Product (models.Model):
#     product_name=models.CharField(max_length=200,null=False)
#     product_code=models.CharField(max_length=200,null=False)
#     prize=models.FloatField(default=0)
#     gst=models.IntegerField(default=0)
#     food_product=models.BooleanField(default=False)
     
#     def __str__(self):
#        return self.product_name+''+self.product_code

from django.db import models

class buy(models.Model):  # Ensure 'Product' is defined like this
    product_name = models.CharField(max_length=200, null=False)
    product_code = models.CharField(max_length=200, null=False)
    prize = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_product = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name or ''} {self.product_code or ''}".strip()
