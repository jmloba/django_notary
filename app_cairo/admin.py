
from django.contrib import admin
from .models import Product
# Register your models here.



class Product_Admin(admin.ModelAdmin):
  list_display=('name','category_type','productcode','price','quantity','dateadded')
  ordering=('category_type','name')
  list_editable =('quantity',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()



admin.site.register(Product, Product_Admin)
