from django.db import models

# Create your models here.
class Product(models.Model):
  FILLOW = 1
  FOOD = 2
  TOYS = 3
  PRODUCT_TYPES=(
    (FILLOW,'Pillow'),
    (FOOD,'Food'),
    (TOYS,'Toys'),


  )

  name = models.CharField(max_length=50)
  dateadded = models.DateField(blank=True, null=True)
  productcode = models.CharField(max_length=30, blank =True)
  price=models.DecimalField(max_digits=7,decimal_places=2)
  quantity = models.IntegerField(blank=True, null=True)
  category_type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPES, blank=True, null=True)
  class Meta:
    db_table = "myapp_product"
