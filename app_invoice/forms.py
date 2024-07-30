

from django import forms
from .models import Invoice, InvoiceSummary, Category_Sales

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
