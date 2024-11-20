from django import forms 

from app_notary.models import Notarized_Documents, Notary_Category
from app_import.models import Phil_City,Phil_Province_Towns

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class Date_filter(forms.Form ):
  from_date = forms.DateField(
    widget = forms.DateInput(
      attrs={
        'class':'form-control', 'type': 'date'
      }
    )
  )
  to_date = forms.DateField(
    widget = forms.DateInput(
      attrs={
        'class':'form-control', 'type': 'date'
      }
    )
  )
  

class Sampleform(forms.Form):
  name = forms.CharField(max_length=50)
  age = forms.IntegerField(max_value=100)
  date_input = forms.DateField(widget=AdminDateWidget())
  time_input = forms.DateField(widget=AdminTimeWidget())
  date_time_input = forms.DateField(widget=AdminSplitDateTime())
  

class CreateRecordNotaryForm(forms.ModelForm):
  myfile =forms.ImageField(
    label='myfile photo',
    widget=forms.ClearableFileInput(attrs={'class':'form-control'})                       
    )
  class Meta :
    model= Notarized_Documents
    fields=('category','firstname','lastname','myfile','myimage','address','bookno','pageno', 'recordno','amount', 'or_number')

    labels={
      'category':'Category',
      'firstname':'First Name',
      'lastname':'Last Name',
      'address':'Address',

      'myimage': 'Image',
      'myfile':'Attached document',
      'bookno' :'Book No.',
      'pageno':'Page No.',
      'recordno':'Record No.',
      'amount': 'Amount',
      'or_number':'Official Receipt Number',
    }
  def  clean_firstname(self):
    firstname= self.cleaned_data.get('firstname')
    if (len( firstname ) < 4):
      raise forms.ValidationError('firstname must be more than 3 chars')
    return firstname
  
  def __init__(self,*args,**kwargs):
    super(CreateRecordNotaryForm,self).__init__(*args,**kwargs)
    self.fields['firstname'].required=True
    self.fields['lastname'].required=True
    self.fields['category'].required=True
    self.fields['bookno'].required=True    
    self.fields['pageno'].required=True    
    self.fields['recordno'].required=True
    self.fields['amount'].required=True
    self.fields['or_number'].required=True

  # def save(self, *args, **kwargs):
  #       kwargs['commit'] = False
  #       my_model = super().save(*args, **kwargs)
  #       Notarized_Documents.objects.update_or_create(
  #           total_tax_amount=self.cleaned_data['amount'] * 2,
            
          
  #       )
    

  
class UpdateRecordNotaryForm(forms.ModelForm):
  class Meta :
    model= Notarized_Documents
    fields=('category','firstname','lastname','myfile','myimage','address','bookno','pageno', 'recordno','amount','or_number')

    labels={
      'category':'Category',
      'firstname':'First Name',
      'lastname':'Last Name',
      'address':'Address',
      'myimage': 'Image',
      'myfile':'Attached document',
      'bookno' :'Book No.',
      'pageno':'Page No.',
      'recordno':'Record No.',
      'amount': 'Amount Paid',
      'or_number': 'Official Receipt Number'
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecordNotaryForm,self).__init__(*args,**kwargs)
    self.fields['firstname'].required=True
    self.fields['lastname'].required=True
    self.fields['category'].required=True
    self.fields['bookno'].required=True    
    self.fields['pageno'].required=True    
    self.fields['recordno'].required=True
    self.fields['amount'].required=True
    self.fields['or_number'].required=True



''' Category'''    

class CreateRecordCategoryForm(forms.ModelForm):
  class Meta :
    model=Notary_Category
    fields=('doc_category',)

    labels={
      'doc_category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(CreateRecordCategoryForm,self).__init__(*args,**kwargs)
    self.fields['doc_category'].required=True

class UpdateRecordCategoryForm(forms.ModelForm):
  class Meta :
    model=Notary_Category
    fields=('doc_category',)

    labels={
      'doc_category':'Category',
    }
  def __init__(self,*args,**kwargs):
    super(UpdateRecordCategoryForm,self).__init__(*args,**kwargs)
    self.fields['doc_category'].required=True
    
''' province / Town'''    
# class CreateRecord_ProvTownForm(forms.ModelForm):
#   class Meta :
#     model=Phil_Province_Towns
#     fields=('doc_category',)

#     labels={
#       'doc_category':'Category',
#     }
#   def __init__(self,*args,**kwargs):
#     super(CreateRecordCategoryForm,self).__init__(*args,**kwargs)
#     self.fields['doc_category'].required=True


  