

from django import forms
from .models import Invoice, InvoiceSummary, Category_Sales,MasterFile

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'customer','itemnumber','description','quantity','price'
        ]
class InvoiceForm2(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'itemnumber','description','quantity','price'
        ]        


class InvoiceSearchForm(forms.ModelForm):       
    class Meta:
        model = Invoice
        fields = [
          'description'
        ]

class Date_Sample1(forms.Form ):
    mydate_field = forms.DateField()

class PrintInvoiceForm(forms.Form):
    model = InvoiceSummary
    fields = [
        'invoice_no'
    ]

class DeleteRecord_CategoryForm(forms.ModelForm):
  class Meta :
    model= Category_Sales
    fields=('user','product_category',)
    labels={
      'user':'User',
      'product_category':'Product Category',
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_CategoryForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['user'].widget.attrs['readonly'] = True
      self.fields['product_category'].widget.attrs['readonly'] = True
     
class UpdateRecord_CategoryForm(forms.ModelForm):
  class Meta :
    model= Category_Sales
    fields=('user','product_category',)
    labels={
      'user':'User',
      'product_category':'Product Category',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecord_CategoryForm,self).__init__(*args,**kwargs)
    
    self.fields['user'].required=True
    self.fields['product_category'].required=True

class DeleteRecord_MasterFileForm(forms.ModelForm):
  class Meta :
    model= MasterFile
    fields=('user','itemnumber','description','category','price','myimage')
    labels={
      'user':'User',
      'itemnumber':'Item Number',
      'description' : 'Description',
      'category':'Category',
      'price':'Price',
      'myimage':'Product Image'

    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_MasterFileForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['user'].widget.attrs['readonly'] = True
      self.fields['itemnumber'].widget.attrs['readonly'] = True
      self.fields['description'].widget.attrs['readonly'] = True
      self.fields['category'].widget.attrs['readonly'] = True
      self.fields['price'].widget.attrs['readonly'] = True

      self.fields['myimage'].widget.attrs['readonly'] = True

class Masterfile_form(forms.ModelForm):
  class Meta:
    model=MasterFile

    fields=["itemnumber","description","category","price", "myimage", ]
    
class UpdateRecord_MasterFileForm(forms.ModelForm):
  class Meta :
    model= MasterFile
    fields=('itemnumber','description','category', 'price', 'myimage')
    labels={
     
      'itemnumber':'Item Number',
      'description':'Description',
      'category':"Category",
      'price' : 'Price',
      'myimage': 'Image'

    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecord_MasterFileForm,self).__init__(*args,**kwargs)
    
  
    self.fields['itemnumber'].required=True
    self.fields['description'].required=True
    self.fields['category'].required=True
    self.fields['price'].required=True
    self.fields['myimage'].required=True

class DeleteRecord_SalesEntryForm(forms.ModelForm):
  class Meta :
    model= Invoice
    fields=('user','itemnumber','description','quantity','price',)
    labels={
      'user':'User',
      'itemnumber':'Item Number',
      'description' : 'Description',
      'quantity':'Quantity',
      'price':'Price',
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_SalesEntryForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['user'].widget.attrs['readonly'] = True
      self.fields['itemnumber'].widget.attrs['readonly'] = True
      self.fields['description'].widget.attrs['readonly'] = True
      self.fields['quantity'].widget.attrs['readonly'] = True
      self.fields['price'].widget.attrs['readonly'] = True

 