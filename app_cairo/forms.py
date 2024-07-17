from django import forms 

from app_cairo.models import Product

class ProductForm(forms.ModelForm):
  class Meta :
    model=Product
    fields=('name','dateadded','productcode','price','quantity','category_type')