

from django import forms
from .models import Invoice, InvoiceSummary, Category_Sales, Master, Sales_Entry

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
# category
class Category_Sales_Form(forms.ModelForm):       
    class Meta:
        model = Category_Sales
        fields = [
          'category'
        ]
class DeleteRecord_CategorySalesForm(forms.ModelForm):
  class Meta :
    model= Category_Sales
    fields=('category',)
    labels={
      'category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_CategorySalesForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['category'].widget.attrs['readonly'] = True
class UpdateRecord_CategorySalesForm(forms.ModelForm):
  class Meta :
    model= Category_Sales
    fields=('category',)
    labels={
      'category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecord_CategorySalesForm,self).__init__(*args,**kwargs)
    self.fields['category'].required=True
# master
class Master_Form(forms.ModelForm):       
    class Meta:
        model = Master
        fields = [ 'itemnumber', 'description','price', 'myimage', ]
class DeleteRecord_MasterForm(forms.ModelForm):
  class Meta :
    model= Master
    fields=('itemnumber','description','myimage')
    labels={
      'itemnumber':'Itemnumber',
      'description':'Description',
      'myimage':'Image'
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_MasterForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['itemnumber'].widget.attrs['readonly'] = True        
      self.fields['description'].widget.attrs['readonly'] = True      
      self.fields['myimage'].widget.attrs['readonly'] = True              
class UpdateRecord_MasterForm(forms.ModelForm):
  class Meta :
    model= Master
    fields=('itemnumber','description','myimage')
    labels={
      'itemnumber':'Itemnumber',
      'description':'Description',
      'myimage': 'Image'
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecord_MasterForm,self).__init__(*args,**kwargs)
    self.fields['itemnumber'].required=True    
    self.fields['description'].required=True    
    self.fields['myimage'].required=True  

# sales entry
class Sales_entry_Form(forms.ModelForm):       
  class Meta:
    model = Sales_Entry
    fields = [ 'itemnumber', 'description','quantity', 'price', ]   
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args,**kwargs)
  #   self.fields['description'].queryset=Master.objects.none()
  #   if 'description' in self.data:
  #     self.fields['description'].queryset=Master.objects.all()
    # elif self.instance:   
    #   self.fields['description'].queryset=Master.objects.all().filter(pk=self.instance.description.pk)


class DeleteRecord_SalesEntryForm(forms.ModelForm):
  class Meta :
    model= Sales_Entry
    fields=('itemnumber','description','quantity','price')
    labels={
      'itemnumber':'Itemnumber',
      'description':'Description',
      'quantity':'Quantity',
      'price':'Price',
    }
  def __init__(self,*args,**kwargs):
    super(DeleteRecord_SalesEntryForm,self).__init__(*args,**kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['itemnumber'].widget.attrs['readonly'] = True        
      self.fields['description'].widget.attrs['readonly'] = True      
      self.fields['quantity'].widget.attrs['readonly'] = True          
      self.fields['price'].widget.attrs['readonly'] = True          